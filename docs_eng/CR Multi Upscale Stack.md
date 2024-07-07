# Documentation
- Class name: CR_MultiUpscaleStack
- Category: Comfyroll/Upscale
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_MultiUpscaleStack is a node that aims to improve image quality and resolution through a series of sampling models. It allows users to switch and select different sampling models, apply specific re-scaling factors and combine their effects to achieve better results. This node is essential for tasks requiring high resolution output, such as printing or displaying them on high DPI screens.

# Input types
## Required
- switch_1
    - Switch parameters determine whether the first sample model is activated in a warehouse. It is essential because it controls the contents of the model during the sampling process, thus affecting the quality of the final output.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- upscale_model_1
    - Select the first model to be used in the sample. The selection of the model has a significant impact on the sample results, as different models may be optimized for different types of images or quality requirements.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- rescale_factor_1
    - Defines the scaling factor for the first sampling model. This parameter is critical because it determines the extent of the sampling and directly affects the resolution and clarity of the result image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_2
    - The switch parameters for the second model in the warehouse. It plays a similar role to the switch_1 and allows conditional application of the second model according to the user's choice.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- upscale_model_2
    - Specifies the second model to be considered during the sampling process. The selection changes the overall effects of the stock, especially when used in conjunction with other models.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- rescale_factor_2
    - Sets the scaling factor for the second sampling model. It works with the model selection to fine-tune the sampling process according to the user's needs.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_3
    - Controls whether the third sampling model is contained in a warehouse. This decision can be strategic, as it allows selective improvement of image quality.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- upscale_model_3
    - Identification of the third sample model to be applied in the warehouse. The effectiveness of the model may vary depending on its compatibility with the image and the expected results.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- rescale_factor_3
    - Adjusting the scaling factors of the third upper sample model to allow accurate control of the strength of the third layer of the store.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- upscale_stack
    - An optional parameter allows the user to enter a pre-existing up-sampling module and its factors. This can simplify the sampling process by building on previous configurations.
    - Comfy dtype: UPSCALE_STACK
    - Python dtype: List[Tuple[str, float]]

# Output types
- UPSCALE_STACK
    - The output is a structured list that contains the upscaling models that are activated and combined by nodes and their corresponding re-scaling factors. This output is important because it represents the final configuration of the sampler.
    - Comfy dtype: UPSCALE_STACK
    - Python dtype: List[Tuple[str, float]]
- show_help
    - Provides a URL link to the document to further assist and guide the effective use of the node. This is particularly useful when new users or additional information is needed.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_MultiUpscaleStack:

    @classmethod
    def INPUT_TYPES(s):
        mix_methods = ['Combine', 'Average', 'Concatenate']
        up_models = ['None'] + folder_paths.get_filename_list('upscale_models')
        return {'required': {'switch_1': (['On', 'Off'],), 'upscale_model_1': (up_models,), 'rescale_factor_1': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 16.0, 'step': 0.01}), 'switch_2': (['On', 'Off'],), 'upscale_model_2': (up_models,), 'rescale_factor_2': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 16.0, 'step': 0.01}), 'switch_3': (['On', 'Off'],), 'upscale_model_3': (up_models,), 'rescale_factor_3': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 16.0, 'step': 0.01})}, 'optional': {'upscale_stack': ('UPSCALE_STACK',)}}
    RETURN_TYPES = ('UPSCALE_STACK', 'STRING')
    RETURN_NAMES = ('UPSCALE_STACK', 'show_help')
    FUNCTION = 'stack'
    CATEGORY = icons.get('Comfyroll/Upscale')

    def stack(self, switch_1, upscale_model_1, rescale_factor_1, switch_2, upscale_model_2, rescale_factor_2, switch_3, upscale_model_3, rescale_factor_3, upscale_stack=None):
        upscale_list = list()
        if upscale_stack is not None:
            upscale_list.extend([l for l in upscale_stack if l[0] != 'None'])
        if upscale_model_1 != 'None' and switch_1 == 'On':
            (upscale_list.extend([(upscale_model_1, rescale_factor_1)]),)
        if upscale_model_2 != 'None' and switch_2 == 'On':
            (upscale_list.extend([(upscale_model_2, rescale_factor_2)]),)
        if upscale_model_3 != 'None' and switch_3 == 'On':
            (upscale_list.extend([(upscale_model_3, rescale_factor_3)]),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Upscale-Nodes#cr-multi-upscale-stack'
        return (upscale_list, show_help)
```