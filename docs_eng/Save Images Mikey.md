# Documentation
- Class name: SaveImagesMikeyML
- Category: Mikey/Image
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

The SaveImagesmikeML node is responsible for saving images to the specified directory with customable naming options. It allows for various metadata elements, such as time stampes, counter values and additional text. The node ensures that the filename is purified and adheres to predefined length limits.

# Input types
## Required
- images
    - The parameters are vital because it defines the actual image data to be saved. It influences the execution of nodes by determining what is to be written into the output file.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- sub_directory
    - Sub_directory parameters specify a subdirectories in the output directory, and the image will be saved in this subdirectorate. This is important for organizing the saved files into a particular category or group.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_text_1
    - The filename_text_1 parameter allows users to define a text that will be contained in the file name that saves the image. It helps customize the filename.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_text_2
    - Similar to filename_text_1, this parameter adds another customable text element to the filename. It enhances the flexibility of the naming agreement.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_text_3
    - This is the third custom-made text parameter for the filename and provides users with more options to include specific information in the saved image filename.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_separator
    - The filename_separator parameter determines the character or string that is used to separate the different text elements in the filename. It is essential to define the structure of the filename.
    - Comfy dtype: STRING
    - Python dtype: str
- timestamp
    - The timestamp parameter indicates whether to include a time stamp in the filename. It plays a role in managing and tracking the time of image preservation in the version.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str
- counter_type
    - The method used to specify an increment counter in the filename is based on the folder structure or file name mode. It is important to ensure the uniqueness of the filename.
    - Comfy dtype: COMBO['none', 'folder', 'filename']
    - Python dtype: str
- filename_text_1_pos
    - The filename_text_1_pos parameter sets the position of the first text element in the filename. It is important to control the order of elements in the filename.
    - Comfy dtype: INT
    - Python dtype: int
- filename_text_2_pos
    - This parameter determines the position of the second text element in the filename and allows users to align text elements according to their preferences.
    - Comfy dtype: INT
    - Python dtype: int
- filename_text_3_pos
    - The filename_text_3_pos parameter is used to set the position of the third text element in the filename, which helps the whole organizational filename.
    - Comfy dtype: INT
    - Python dtype: int
- timestamp_pos
    - The timestamp_pos parameter defines the position of the time stamp in the filename. It affects the overall order of the filename components.
    - Comfy dtype: INT
    - Python dtype: int
- timestamp_type
    - The timestamp_type parameter specifies the source of the time stamp used in the filename, which can be based on the start of the operation or the time of preservation of the image.
    - Comfy dtype: COMBO['job', 'save_time']
    - Python dtype: str
- counter_pos
    - The clock_pos parameter specifies the location where the counter appears in the filename. It is essential to maintain the order in which the files are saved.
    - Comfy dtype: INT
    - Python dtype: int
- extra_metadata
    - Extra_metadata parameters allow for additional metadata to be included in PNG information for saved images. It provides a way to store additional information next to image data.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - The prompt parameter is used to inject context information into the process of creating a filename. It can influence how the filename is constructed depending on the content provided.
    - Comfy dtype: PROMPT
    - Python dtype: Dict[str, Any]
- extra_pnginfo
    - Extra_pnginfo parameters allow the inclusion of additional information from PNG metadata in file names. This is useful for additional details that can be retrieved when embedded.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- ui
    - The ui parameter is used as an interface to present results to users. It usually contains a dictionary list, each of which represents a saved image with its filename and subfolder information.
    - Comfy dtype: COMBO[Dict[str, List[Dict[str, str]]]]
    - Python dtype: Dict[str, List[Dict[str, str]]]
- images
    - The iages parameter in ui output contains detailed information about each saved image, including the filename and the subdirectories that save it.
    - Comfy dtype: COMBO[List[Dict[str, str]]]
    - Python dtype: List[Dict[str, str]]

# Usage tips
- Infra type: CPU

# Source code
```
class SaveImagesMikeyML:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'sub_directory': ('STRING', {'default': ''}), 'filename_text_1': ('STRING', {'default': 'Filename Text 1'}), 'filename_text_2': ('STRING', {'default': 'Filename Text 2'}), 'filename_text_3': ('STRING', {'default': 'Filename Text 3'}), 'filename_separator': ('STRING', {'default': '_'}), 'timestamp': (['true', 'false'], {'default': 'true'}), 'counter_type': (['none', 'folder', 'filename'], {'default': 'folder'}), 'filename_text_1_pos': ('INT', {'default': 0}), 'filename_text_2_pos': ('INT', {'default': 2}), 'filename_text_3_pos': ('INT', {'default': 4}), 'timestamp_pos': ('INT', {'default': 1}), 'timestamp_type': (['job', 'save_time'], {'default': 'save_time'}), 'counter_pos': ('INT', {'default': 3}), 'extra_metadata': ('STRING', {'default': 'Extra Metadata'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_images'
    OUTPUT_NODE = True
    CATEGORY = 'Mikey/Image'

    def _prepare_filename_texts(self, filename_text_1, filename_text_2, filename_text_3, extra_pnginfo, prompt):
        filename_texts = [filename_text_1, filename_text_2, filename_text_3]
        default_texts = ['Filename Text 1', 'Filename Text 2', 'Filename Text 3']
        for (i, text) in enumerate(filename_texts):
            if text == default_texts[i]:
                filename_texts[i] = ''
            filename_texts[i] = search_and_replace(text, extra_pnginfo, prompt)
            filename_texts[i] = re.sub('[<>:"/\\\\|?*]', '', filename_texts[i])
            filename_texts[i] = filename_texts[i].encode('ascii', 'ignore').decode('ascii')
        total_length = len(filename_texts[0]) + len(filename_texts[1]) + len(filename_texts[2]) + 5 + 5 + 12
        if total_length > 120:
            longest_text = max(filename_texts, key=len)
            longest_text_idx = filename_texts.index(longest_text)
            text_length_without_longest = total_length - len(longest_text)
            filename_texts[longest_text_idx] = longest_text[0:120 - text_length_without_longest]
        return filename_texts

    def _get_initial_counter(self, files, full_output_folder, counter_type, filename_separator, counter_pos, filename_texts):
        counter = 1
        if counter_type == 'folder':
            if files:
                for f in files:
                    if filename_separator in f:
                        try:
                            counter = max(counter, int(f.split(filename_separator)[counter_pos]) + 1)
                        except:
                            counter = 1
                            break
            else:
                counter = 1
        elif counter_type == 'filename':
            for f in files:
                f_split = f.split(filename_separator)
                f_split = [x.replace('.png', '') for x in f_split]
                matched_texts = all((filename_texts[i] == f_split[i] for i in range(3) if filename_texts[i]))
                if matched_texts:
                    counter += 1
        return counter

    def _get_next_counter(self, full_output_folder, filename_base, counter):
        """Checks for the next available counter value."""
        while True:
            current_filename = filename_base.format(counter=f'{counter:05}')
            if not os.path.exists(os.path.join(full_output_folder, f'{current_filename}.png')):
                return counter
            counter += 1

    def save_images(self, images, sub_directory, filename_text_1, filename_text_2, filename_text_3, filename_separator, timestamp, counter_type, filename_text_1_pos, filename_text_2_pos, filename_text_3_pos, timestamp_pos, timestamp_type, counter_pos, extra_metadata, prompt=None, extra_pnginfo=None):
        positions = [filename_text_1_pos, filename_text_2_pos, filename_text_3_pos, timestamp_pos, counter_pos]
        if len(positions) != len(set(positions)):
            raise ValueError('Duplicate position numbers detected. Please ensure all position numbers are unique.')
        sub_directory = search_and_replace(sub_directory, extra_pnginfo, prompt)
        sub_directory = re.sub('[<>:"|?*]', '', sub_directory)
        sub_directory = sub_directory.encode('ascii', 'ignore').decode('ascii')
        full_output_folder = os.path.join(self.output_dir, sub_directory)
        os.makedirs(full_output_folder, exist_ok=True)
        filename_texts = self._prepare_filename_texts(filename_text_1, filename_text_2, filename_text_3, extra_pnginfo, prompt)
        if timestamp == 'true':
            ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        else:
            ts = ''
        elements = {filename_text_1_pos: filename_texts[0], filename_text_2_pos: filename_texts[1], filename_text_3_pos: filename_texts[2], timestamp_pos: ts, counter_pos: 'counter' if counter_type != 'none' else None}
        sorted_elements = [elem for (_, elem) in sorted(elements.items()) if elem]
        filename_base = filename_separator.join(sorted_elements).replace('counter', '{counter}')
        files = os.listdir(full_output_folder)
        if counter_type != 'none':
            counter = self._get_initial_counter(files, full_output_folder, counter_type, filename_separator, counter_pos, filename_texts)
        else:
            counter = 0
        results = list()
        for (ix, image) in enumerate(images):
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text('prompt', json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    if x == 'parameters':
                        text = extra_pnginfo[x].encode('utf-8').decode('utf-8')
                        metadata.add_text(x, text)
                    elif x == 'workflow':
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))
                    elif x == 'prompt':
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))
                    else:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x], ensure_ascii=False))
            if extra_metadata:
                metadata.add_text('extra_metadata', extra_metadata)
            if counter_type != 'none':
                counter = self._get_next_counter(full_output_folder, filename_base, counter)
                current_filename = filename_base.format(counter=f'{counter:05}')
            else:
                current_filename = filename_base
            if timestamp_type == 'save_time' and timestamp == 'true':
                current_timestamp = datetime.datetime.now().strftime('%y%m%d%H%M%S')
                current_filename = current_filename.replace(ts, current_timestamp)
                ts = current_timestamp
            if ix > 0 and counter_type == 'none':
                current_filename = current_filename.replace(ts, ts + f'_{ix:02}')
            img.save(os.path.join(full_output_folder, f'{current_filename}.png'), pnginfo=metadata, compress_level=4)
            results.append({'filename': f'{current_filename}.png', 'subfolder': sub_directory, 'type': self.type})
            if counter_type != 'none':
                counter += 1
        return {'ui': {'images': results}}
```