# Documentation
- Class name: ToDetailerPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ToDetailer Pipe node is designed to convert the input data into a more detailed and structured format. It refines and enhances the level of detail of the data by integrating various components, such as models, clips and detectors. This node plays a key role in preparing the data for further analysis or visualization, ensuring that the data meets the required quality and detail standards.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the main algorithmic framework for data conversion. They directly affect the ability of nodes to process and refine input data, ensuring that the output meets the expected detail requirements.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Cut parameters are a key component in the data conversion process, which assists in data conversion by providing context information and constraints. It ensures that conversion follows specific guidelines, thereby preserving the integrity and consistency of the output data.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- vae
    - VAE (distribution from encoder) is an important element in the node structure and is responsible for coding and decoding data as a potential spatial expression. It plays an important role in the process of detail enhancement, enabling nodes to generate detailed and rich output from input data.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive
    - Positive parameters, as guidance for node operations, provide positive examples or conditions that should be followed for output. This is essential to ensure that node output is consistent with desired quality and detail standards.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[str]
- negative
    - Negative parameters add positive parameters by providing examples or conditions that the output should avoid. It is important for guiding nodes to produce outputs that meet the required criteria and do not contain unwanted features.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[str]
- bbox_detector
    - The bbox_detector parameter is essential for identifying and locating the interest areas in the input data. It helps nodes to focus on specific areas and enhances the details and accuracy of the output.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: Callable
- wildcard
    - The wildcard parameters allow dynamic and flexible data processing, enabling nodes to adapt to input scenarios. It is important to ensure that nodes are able to process data types and formats, thereby enhancing their multifunctionality and usefulness.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- Select to add LoRA
    - The LoRA selection parameters provide the flexibility to integrate a particular low-adaptation (Low-Rank Applications) into the node processing process. This enhances the function of the node by allowing the node to adjust its operation to a particular case or need.
    - Comfy dtype: COMBO['Select the LoRA to add to the text', folder_paths.get_filename_list('loras')]
    - Python dtype: Union[str, None]
- Select to add Wildcard
    - Additional wildcard parameters provide the option to include more dynamic elements in node operations. They can be used to introduce variability and to adjust node behaviour to different data input or processing needs.
    - Comfy dtype: COMBO['Select the Wildcard to add to the text']
    - Python dtype: Union[str, None]

# Output types
- detailer_pipe
    - The detailer_pipe output represents the results of node processing and contains detailed and refined data. It marks the successful implementation of the node and provides a structured format for downstream applications.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class ToDetailerPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'bbox_detector': ('BBOX_DETECTOR',), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],)}, 'optional': {'sam_model_opt': ('SAM_MODEL',), 'segm_detector_opt': ('SEGM_DETECTOR',), 'detailer_hook': ('DETAILER_HOOK',)}}
    RETURN_TYPES = ('DETAILER_PIPE',)
    RETURN_NAMES = ('detailer_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, *args, **kwargs):
        pipe = (kwargs['model'], kwargs['clip'], kwargs['vae'], kwargs['positive'], kwargs['negative'], kwargs['wildcard'], kwargs['bbox_detector'], kwargs.get('segm_detector_opt', None), kwargs.get('sam_model_opt', None), kwargs.get('detailer_hook', None), kwargs.get('refiner_model', None), kwargs.get('refiner_clip', None), kwargs.get('refiner_positive', None), kwargs.get('refiner_negative', None))
        return (pipe,)
```