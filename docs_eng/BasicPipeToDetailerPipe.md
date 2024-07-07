# Documentation
- Class name: BasicPipeToDetailerPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The BasicPipeToDetailer Pipe node is designed to transform the basic plumbing structure into a more detailed pipeline and to enhance the processing capacity of the follow-on tasks. It works together to refine input data for more complex analysis by integrating various components, such as bbox_detector, wildcards and optional models.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is essential because it provides the basic data structure necessary for node operations. It is a prerequisite for the node-driven conversion process.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
- bbox_detector
    - The bbox_detector is a key component in identifying and locating areas of interest in the data.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: Any
- wildcard
    - The wildcard parameter introduces flexibility in the treatment of nodes by allowing dynamic replacement of placeholders during execution. This feature increases the adaptability of nodes to various data scenarios.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- Select to add LoRA
    - The LoRA selection parameters provide optional enhancements to node functions, allowing for additional abstract layers or complexity to be incorporated into processing pipes.
    - Comfy dtype: COMBO[Select the LoRA to add to the text]
    - Python dtype: Union[str, None]
- Select to add Wildcard
    - This optional parameter allows users to introduce additional wildcards into the processing process, which can be used for more dynamic and diversified data operations.
    - Comfy dtype: COMBO[Select the Wildcard to add to the text]
    - Python dtype: Union[str, None]
- sam_model_opt
    - Optional sam_model_opt parameters enable nodes to use advanced models for more complex analysis in case default processing is inadequate.
    - Comfy dtype: SAM_MODEL
    - Python dtype: Union[Any, None]
- segm_detector_opt
    - When segm_detector_opt parameters are provided, allowing for more finer partition measurements in node operations may improve the accuracy of the results.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: Union[Any, None]
- detailer_hook
    - Detailer_hook is an optional parameter that can be used to customize or extend the function of a node and allows custom processing for specific cases.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Union[Any, None]

# Output types
- detailer_pipe
    - The detailer_pipe output represents an enhanced pipeline that is processed by nodes. It is a detailed structure to be used for further analysis or downstream tasks.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class BasicPipeToDetailerPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'bbox_detector': ('BBOX_DETECTOR',), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],)}, 'optional': {'sam_model_opt': ('SAM_MODEL',), 'segm_detector_opt': ('SEGM_DETECTOR',), 'detailer_hook': ('DETAILER_HOOK',)}}
    RETURN_TYPES = ('DETAILER_PIPE',)
    RETURN_NAMES = ('detailer_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, *args, **kwargs):
        basic_pipe = kwargs['basic_pipe']
        bbox_detector = kwargs['bbox_detector']
        wildcard = kwargs['wildcard']
        sam_model_opt = kwargs.get('sam_model_opt', None)
        segm_detector_opt = kwargs.get('segm_detector_opt', None)
        detailer_hook = kwargs.get('detailer_hook', None)
        (model, clip, vae, positive, negative) = basic_pipe
        pipe = (model, clip, vae, positive, negative, wildcard, bbox_detector, segm_detector_opt, sam_model_opt, detailer_hook, None, None, None, None)
        return (pipe,)
```