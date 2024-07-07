# Documentation
- Class name: PromptExtractor
- Category: InspirePack/Prompt
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

PromptExtractor nodes are designed to analyse image files and extract relevant tip messages that can be used to generate creative tips or guide workflows. It processes image metadata to recognize the input and output required and to construct text expressions for the reminder structure.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input for node execution analysis. The image file is expected to be in the input directory and has a valid format.
    - Comfy dtype: COMBO[sorted_files]
    - Python dtype: str
- positive_id
    - The positionive_id parameter is essential for identifying the positive aspects of the hint. It helps filter the relevant information from the extracted tip data and contributes to the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_id
    - The negative_id parameter is used to specify the negative aspects of the hint. It plays a role in excluding certain information from the final output and ensuring the relevance and accuracy of the extracted data.
    - Comfy dtype: STRING
    - Python dtype: str
- info
    - The information parameter contains metadata about the image, which is essential for the context and structure of the node to understand the hint. It is essential for the accurate extraction and indication of the hint information.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- unique_id
    - The unique_id parameter is the identifier for node operations, which helps track and manage node implementation in the workflow.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- positive
    - Positive output represents extraction of information consistent with the positionive_id parameters, contributing to the creative process by providing constructive aspects of the reminder.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative output captures extracting information consistent with the negative_id parameters, which helps to refine the creative process by excluding non-necessary aspects of the hint.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptExtractor:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': (sorted(files), {'image_upload': True}), 'positive_id': ('STRING', {}), 'negative_id': ('STRING', {}), 'info': ('STRING', {'multiline': True})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    CATEGORY = 'InspirePack/Prompt'
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative')
    FUNCTION = 'doit'
    OUTPUT_NODE = True

    def doit(self, image, positive_id, negative_id, info, unique_id):
        image_path = folder_paths.get_annotated_filepath(image)
        info = Image.open(image_path).info
        positive = ''
        negative = ''
        text = ''
        prompt_dicts = {}
        node_inputs = {}

        def get_node_inputs(x):
            if x in node_inputs:
                return node_inputs[x]
            else:
                node_inputs[x] = None
                obj = nodes.NODE_CLASS_MAPPINGS.get(x, None)
                if obj is not None:
                    input_types = obj.INPUT_TYPES()
                    node_inputs[x] = input_types
                    return input_types
                else:
                    return None
        if isinstance(info, dict) and 'workflow' in info:
            prompt = json.loads(info['prompt'])
            for (k, v) in prompt.items():
                input_types = get_node_inputs(v['class_type'])
                if input_types is not None:
                    inputs = input_types['required'].copy()
                    if 'optional' in input_types:
                        inputs.update(input_types['optional'])
                    for (name, value) in inputs.items():
                        if name in prompt_blacklist:
                            continue
                        if value[0] == 'STRING' and name in v['inputs']:
                            prompt_dicts[f'{k}.{name.strip()}'] = (v['class_type'], v['inputs'][name])
            for (k, v) in prompt_dicts.items():
                text += f'{k} [{v[0]}] ==> {v[1]}\n'
            positive = prompt_dicts.get(positive_id.strip(), '')
            negative = prompt_dicts.get(negative_id.strip(), '')
        else:
            text = 'There is no prompt information within the image.'
        PromptServer.instance.send_sync('inspire-node-feedback', {'node_id': unique_id, 'widget_name': 'info', 'type': 'text', 'data': text})
        return (positive, negative)
```