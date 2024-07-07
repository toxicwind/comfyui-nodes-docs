# Documentation
- Class name: SavePromptToFile
- Category: OneButtonPrompt
- Output node: True
- Repo Ref: https://github.com/AIrjen/OneButtonPrompt

The node facilitates the storage of tips in documents to ensure that information is stored in an orderly and easily accessible manner. It enhances workflows by automating file naming and storage processes, which are essential for maintaining a clear reminder record and its associated data.

# Input types
## Required
- filename_prefix
    - The prefix of the filename is essential for generating the only identifiable filename, helping to organize and quote the saved tips efficiently.
    - Comfy dtype: STRING
    - Python dtype: str
- positive_prompt
    - A positive hint is a key input that sets the tone and content for saving the hint, affecting the overall context and usefulness of saving the data.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - The opposite side of the negative hint as a positive tip provides a comparative perspective and is of great value in understanding the nuances of the hint.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prompt_g
    - Additional tips can provide additional information or context, enrich the data saved and provide a more comprehensive range of indications.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_l
    - Longer hints may provide details or examples of extensions, which may enhance the depth and applicability of retention tips.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- status
    - Status output confirms the successful execution of the saving operation and ensures that the reminder is correctly saved and stored.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SavePromptToFile:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.prefix_append = ''

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'filename_prefix': ('STRING', {'default': 'Prompt'}), 'positive_prompt': ('STRING', {'multiline': True}), 'negative_prompt': ('STRING', {'multiline': True})}, 'optional': {'prompt_g': ('STRING', {'multiline': True}), 'prompt_l': ('STRING', {'multiline': True})}}
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'saveprompttofile'
    CATEGORY = 'OneButtonPrompt'

    def saveprompttofile(self, positive_prompt, prompt_g, prompt_l, negative_prompt, filename_prefix):
        filename_prefix += self.prefix_append
        pattern = '%date:([^\\%]+)%'
        match = re.search(pattern, filename_prefix)
        if match:
            date_format = match.group(1)
            current_date = datetime.now()
            date_format = date_format.replace('M', 'X')
            date_format = date_format.replace('m', 'Z')
            if platform.system() == 'Windows':
                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%#y')
                date_format = date_format.replace('X', '%#m')
                date_format = date_format.replace('d', '%#d')
                date_format = date_format.replace('h', '%#H')
                date_format = date_format.replace('Z', '%#M')
                date_format = date_format.replace('s', '%#S')
            else:
                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%-y')
                date_format = date_format.replace('X', '%-m')
                date_format = date_format.replace('d', '%-d')
                date_format = date_format.replace('h', '%-H')
                date_format = date_format.replace('Z', '%-M')
                date_format = date_format.replace('s', '%-S')
            formatted_date = current_date.strftime(date_format)
            filename_prefix = re.sub(pattern, formatted_date, filename_prefix)
        (full_output_folder, filename_short, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        if positive_prompt.find('of a ') != -1:
            start_index = positive_prompt.find('of a ') + len('of a ')
            end_index = positive_prompt.find(',', start_index)
            if end_index == -1:
                end_index = len(positive_prompt)
        else:
            start_index = 0
            end_index = 128
        filename = positive_prompt[start_index:end_index]
        filename = filename.replace('"', '')
        filename = filename.replace('[', '')
        filename = filename.replace('|', '')
        filename = filename.replace(']', '')
        filename = filename.replace('<', '')
        filename = filename.replace('>', '')
        filename = filename.replace(':', '_')
        filename = filename.replace('.', '')
        filename = re.sub('[0-9]+', '', filename)
        safe_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
        filename = re.sub('[^{}]+'.format(re.escape(''.join(safe_characters))), '', filename)
        if filename == '':
            filename = str(uuid.uuid4())
        if filename_prefix == '':
            now = datetime.now()
            filenamecomplete = now.strftime('%Y%m%d%H%M%S') + '_' + filename.replace(' ', '_').strip() + '.txt'
        else:
            formatted_counter = str(counter + 1).zfill(5)
            filenamecomplete = filename_short + '_' + formatted_counter + '_' + filename.replace(' ', '_').strip() + '.txt'
        directoryandfilename = os.path.abspath(os.path.join(full_output_folder, filenamecomplete))
        with open(directoryandfilename, 'w', encoding='utf-8') as file:
            file.write('prompt: ' + positive_prompt + '\n')
            if len(prompt_g) > 0:
                file.write('prompt_g: ' + prompt_g + '\n')
            if len(prompt_l) > 0:
                file.write('prompt_l: ' + prompt_l + '\n')
            file.write('negative prompt: ' + negative_prompt + '\n')
        return 'done'
```