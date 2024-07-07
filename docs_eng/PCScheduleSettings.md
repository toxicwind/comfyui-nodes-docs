# Documentation
- Class name: PCScheduleSettings
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The node is designed to manage and adjust the parameters of the indicative schedule, which is essential to control the process of generation of the AI model. It ensures that the output of the model is fine-tuned according to the specified settings, thereby optimizing the quality and relevance of the results.

# Input types
## Optional
- steps
    - The step parameter is essential to define progress in the AI model output over a certain number of years. It affects the ability of the model to fine-tune its response and reach the desired level of detail and consistency.
    - Comfy dtype: INT
    - Python dtype: int
- mask_width
    - The mask width parameter plays an important role in shaping the spatial dimensions of model output. It helps to control the breadth of the content generated and to ensure that it is consistent with the intended scope and structure.
    - Comfy dtype: INT
    - Python dtype: int
- mask_height
    - The mask height parameter is essential to define the vertical structure of the model output. It works with the mask width to create an overall spatial configuration, which is essential to maintaining the integrity of the content.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_width
    - The SDXL width parameter is important for setting the horizontal scale of model output. It influences how the model distributes information in width to ensure that it is appropriately detailed and balanced.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_height
    - The SDXL height parameter is essential for building vertical proportions of model output. It works with SDXL width to create a harmonious balance and to ensure that the structure of the content is coherent and proportional.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_target_w
    - The SDXL target width parameter is essential for setting the desired width of the output. It guides the model to reach the target size, which is essential for maintaining the visual and structural integrity of the content generated.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_target_h
    - The SDXL target height parameter is essential to define the desired height of output. It works with the SDXL target width to ensure that model output is scalded appropriately and adapted to the desired dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_crop_w
    - SDXL cropwidth parameters are important for specifying the area width to be cut from model output. They help refine the final output, focus on the most relevant parts, and improve the accuracy and relevance of the content.
    - Comfy dtype: INT
    - Python dtype: int
- sdxl_crop_h
    - SDXL crop height parameters are essential to define the height of the area that is being cut from model output. It works with SDXL crop width to ensure that the content of the crop is focused and consistent with the expected output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- settings
    - Setout output provides a comprehensive summary of the application time frame parameters, which is essential for monitoring and adjusting the AI model's behaviour. It ensures that the model operates within the desired parameters and thus obtains optimal and targeted results.
    - Comfy dtype: SCHEDULE_SETTINGS
    - Python dtype: Tuple[int, int, int, int, int, int, int, int, int]

# Usage tips
- Infra type: CPU

# Source code
```
class PCScheduleSettings:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'steps': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'mask_width': ('INT', {'default': 512, 'min': 64, 'max': 4096 * 4}), 'mask_height': ('INT', {'default': 512, 'min': 64, 'max': 4096 * 4}), 'sdxl_width': ('INT', {'default': 1024, 'min': 0, 'max': 4096 * 4}), 'sdxl_height': ('INT', {'default': 1024, 'min': 0, 'max': 4096 * 4}), 'sdxl_target_w': ('INT', {'default': 1024, 'min': 0, 'max': 4096 * 4}), 'sdxl_target_h': ('INT', {'default': 1024, 'min': 0, 'max': 4096 * 4}), 'sdxl_crop_w': ('INT', {'default': 0, 'min': 0, 'max': 4096 * 4}), 'sdxl_crop_h': ('INT', {'default': 0, 'min': 0, 'max': 4096 * 4})}}
    RETURN_TYPES = ('SCHEDULE_SETTINGS',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, steps=0, mask_width=512, mask_height=512, sdxl_width=1024, sdxl_height=1024, sdxl_target_w=1024, sdxl_target_h=1024, sdxl_crop_w=0, sdxl_crop_h=0):
        settings = {'steps': steps, 'mask_width': mask_width, 'mask_height': mask_height, 'sdxl_width': sdxl_width, 'sdxl_height': sdxl_height, 'sdxl_twidth': sdxl_target_w, 'sdxl_theight': sdxl_target_h, 'sdxl_cwidth': sdxl_crop_w, 'sdxl_cheight': sdxl_crop_h}
        return (settings,)
```