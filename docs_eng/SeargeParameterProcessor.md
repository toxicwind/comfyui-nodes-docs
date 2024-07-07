# Documentation
- Class name: SeargeParameterProcessor
- Category: Searge/_deprecated_/UI
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is intended to process and optimize the input parameters of the image generation task and to ensure that the parameters are properly configured to achieve the desired output quality and style.

# Input types
## Required
- inputs
    - The input parameter is essential because it provides the initial set of parameters that the node will process and optimize. It directly influences the operation and final output of the node.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The output parameter represents the set of parameters that have been processed and optimized and can now be prepared for use in the subsequent stages of the image generation process.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeParameterProcessor:
    REFINER_INTENSITY = ['hard', 'soft']
    HRF_SEED_OFFSET = ['same', 'distinct']
    STATES = ['disabled', 'enabled']
    OPERATION_MODE = ['text to image', 'image to image', 'inpainting']
    PROMPT_STYLE = ['simple', '3 prompts G+L-N', 'subject focus', 'style focus', 'weighted', 'overlay', 'subject - style', 'style - subject', 'style only', 'weighted - overlay', 'overlay - weighted']
    STYLE_TEMPLATE = ['none', 'from preprocessor', 'test']
    SAVE_TO = ['output folder', 'input folder']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'inputs': ('PARAMETER_INPUTS',)}}
    RETURN_TYPES = ('PARAMETERS',)
    RETURN_NAMES = ('parameters',)
    FUNCTION = 'process'
    CATEGORY = 'Searge/_deprecated_/UI'

    def process(self, inputs):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        if parameters['denoise'] is None:
            parameters['denoise'] = 1.0
        saturation = parameters['refiner_intensity']
        if saturation is not None:
            if saturation == SeargeParameterProcessor.REFINER_INTENSITY[1]:
                parameters['noise_offset'] = 1
            else:
                parameters['noise_offset'] = 0
        hires_fix = parameters['hires_fix']
        if hires_fix is not None and hires_fix == SeargeParameterProcessor.STATES[0]:
            parameters['hrf_steps'] = 0
        hrf_saturation = parameters['hrf_intensity']
        if hrf_saturation is not None:
            if hrf_saturation == SeargeParameterProcessor.REFINER_INTENSITY[1]:
                parameters['hrf_noise_offset'] = 1
            else:
                parameters['hrf_noise_offset'] = 0
        seed_offset = parameters['hrf_seed_offset']
        if seed_offset is not None:
            seed = parameters['seed'] if parameters['seed'] is not None else 0
            if seed_offset == SeargeParameterProcessor.HRF_SEED_OFFSET[1]:
                parameters['hrf_seed'] = seed + 3
            else:
                parameters['hrf_seed'] = seed
        style_template = parameters['style_template']
        if style_template is not None:
            if style_template == SeargeParameterProcessor.STYLE_TEMPLATE[1]:
                pass
            if style_template == SeargeParameterProcessor.STYLE_TEMPLATE[2]:
                if parameters['noise_offset'] is not None:
                    parameters['noise_offset'] = 1 - parameters['hrf_noise_offset']
                if parameters['hrf_noise_offset'] is not None:
                    parameters['hrf_noise_offset'] = 1 - parameters['hrf_noise_offset']
            else:
                pass
        operation_mode = parameters['operation_mode']
        if operation_mode is not None:
            if operation_mode == SeargeParameterProcessor.OPERATION_MODE[1]:
                parameters['operation_selector'] = 1
            elif operation_mode == SeargeParameterProcessor.OPERATION_MODE[2]:
                parameters['operation_selector'] = 2
            else:
                parameters['operation_selector'] = 0
                parameters['denoise'] = 1.0
        prompt_style = parameters['prompt_style']
        if prompt_style is not None:
            if prompt_style == SeargeParameterProcessor.PROMPT_STYLE[0]:
                parameters['prompt_style_selector'] = 0
                parameters['prompt_style_group'] = 0
                main_prompt = parameters['main_prompt']
                parameters['secondary_prompt'] = main_prompt
                parameters['style_prompt'] = ''
                parameters['negative_style'] = ''
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[2]:
                parameters['prompt_style_selector'] = 1
                parameters['prompt_style_group'] = 0
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[3]:
                parameters['prompt_style_selector'] = 2
                parameters['prompt_style_group'] = 0
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[4]:
                parameters['prompt_style_selector'] = 3
                parameters['prompt_style_group'] = 0
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[5]:
                parameters['prompt_style_selector'] = 4
                parameters['prompt_style_group'] = 0
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[6]:
                parameters['prompt_style_selector'] = 0
                parameters['prompt_style_group'] = 1
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[7]:
                parameters['prompt_style_selector'] = 1
                parameters['prompt_style_group'] = 1
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[8]:
                parameters['prompt_style_selector'] = 2
                parameters['prompt_style_group'] = 1
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[9]:
                parameters['prompt_style_selector'] = 3
                parameters['prompt_style_group'] = 1
            elif prompt_style == SeargeParameterProcessor.PROMPT_STYLE[10]:
                parameters['prompt_style_selector'] = 4
                parameters['prompt_style_group'] = 1
            else:
                parameters['prompt_style_selector'] = 0
                parameters['prompt_style_group'] = 0
                parameters['style_prompt'] = ''
                parameters['negative_style'] = ''
        save_image = parameters['save_image']
        if save_image is not None:
            if save_image == SeargeParameterProcessor.STATES[0]:
                parameters['save_upscaled_image'] = SeargeParameterProcessor.STATES[0]
                parameters['hires_fix'] = SeargeParameterProcessor.STATES[0]
            elif parameters['save_directory'] == SeargeParameterProcessor.SAVE_TO[1]:
                parameters['hires_fix'] = SeargeParameterProcessor.STATES[1]
        return (parameters,)
```