# Documentation
- Class name: EditDetailerPipeSDXL
- Category: text_processing
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

EditDetailer PipeSDXL is a node to enhance the specificity and detail of text output by integrating additional elements such as LoRA and wildcards. It plays a key role in text generation, allowing for more nuanced and detailed content to be created.

# Input types
## Required
- detailer_pipe
    - The detailer_pipe parameter is essential to define the basic text-processing conduit that the node will operate. It sets the basis for text enhancement and is essential to the function of the node.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: str
- wildcard
    - The wildcard parameter allows users to enter dynamic text segments that can be replaced or operated during text generation. It plays a key role in custom output to meet specific requirements.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- Select to add LoRA
    - The LoRA selection parameter allows for the addition of a layer of detail to the text, which enhances the ability of the model to produce detailed and informative content. This is an optional feature that significantly enhances the ability of nodes.
    - Comfy dtype: COMBO[loras]
    - Python dtype: str
- Select to add Wildcard
    - This parameter provides a mechanism for introducing wildcards into text generation, providing flexibility and adaptability to output. It is an optional feature that can be customized according to different examples.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- model
    - The model parameter is used to specify the machine learning model that the node will be used for text processing. This is an optional input that enhances the performance of the node by selecting the right model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Output types
- refined_text
    - The output of refined_text is the result of the node operation, which provides a detailed and enhanced version of the input text. It represents the result of the node text processing capacity.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class EditDetailerPipeSDXL(EditDetailerPipe):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],)}, 'optional': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'refiner_model': ('MODEL',), 'refiner_clip': ('CLIP',), 'refiner_positive': ('CONDITIONING',), 'refiner_negative': ('CONDITIONING',), 'bbox_detector': ('BBOX_DETECTOR',), 'sam_model': ('SAM_MODEL',), 'segm_detector': ('SEGM_DETECTOR',), 'detailer_hook': ('DETAILER_HOOK',)}}
```