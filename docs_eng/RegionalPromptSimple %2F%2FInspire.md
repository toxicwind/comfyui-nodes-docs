# Documentation
- Class name: RegionalPromptSimple
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalPromptSimple node is designed to enhance the image synthesis process by regionalization. It uses a mask to focus on a particular area of the image, allowing detailed control of the sampling process. The node improves the overall image quality and leads to more fine and targeted output by ensuring that the area is given appropriate attention.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is essential for the regional reminder process, and it provides the basic elements needed to synthesize images. It includes models, clips, wae, and other necessary components. These elements have a direct impact on the quality and accuracy of the final output.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple
- mask
    - The mask parameter is essential to define the area of interest within the image. It serves as a guide for nodes, guiding their focus and ensuring that the specified area is enhanced with greater detail and clarity. The mask's effectiveness is directly related to the enhanced accuracy of the image required.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- cfg
    - The cfg parameter is a floating point value that adjusts the configuration settings of the node to affect the overall behaviour of the regional reminder process. It plays an important role in determining the balance between detail and efficiency, ensuring that the node functions optimally as the desired result.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter determines the sampling strategy to be used, which is essential for the quality of the composite image. By selecting the right sampler, the node can adjust its output to meet the specific requirements of the task at hand, thereby achieving more accurate and targeted enhancements.
    - Comfy dtype: SAMPLERS
    - Python dtype: str
- scheduler
    - Scheduler parameters play an important role in managing the overlap of nodes, ensuring that the area alerts are implemented in a controlled and efficient manner. They help to optimize the sampling process, avoid unnecessary costing, and focus on the most influential steps.
    - Comfy dtype: SCHEDULERS
    - Python dtype: str
## Optional
- wildcard_prompt
    - The wildcard_prompt parameter allows dynamic text input, which can be used as a hint for custom nodes. This feature increases the flexibility of nodes to adapt to various image synthesis scenarios and produces more customized results.
    - Comfy dtype: STRING
    - Python dtype: str
- controlnet_in_pipe
    - The controlnet_in_pipe parameter determines whether to maintain or overwrite the current control settings in the pipe. This allows fine-tuning of node behaviour to ensure that the regional tips are consistent with the desired creative direction.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- sigma_factor
    - The sigma_factor parameter adjusts the level of noise reduction applied during image synthesis. By adjusting this value, nodes can be balanced between preserving details and reducing unwanted noises, resulting in cleaner and more refined image output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- regional_prompts
    - Regional_prompts output is a series of tips that are tailored to a specific area of the image. These tips are designed to enhance the image synthesis process by focusing on the interest area, thus allowing for more detailed and accurate desired results.
    - Comfy dtype: REGIONAL_PROMPTS
    - Python dtype: List[Dict[str, Any]]

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalPromptSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'mask': ('MASK',), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'wildcard_prompt': ('STRING', {'multiline': True, 'dynamicPrompts': False, 'placeholder': 'wildcard prompt'}), 'controlnet_in_pipe': ('BOOLEAN', {'default': False, 'label_on': 'Keep', 'label_off': 'Override'}), 'sigma_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('REGIONAL_PROMPTS',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, basic_pipe, mask, cfg, sampler_name, scheduler, wildcard_prompt, controlnet_in_pipe=False, sigma_factor=1.0):
        if 'RegionalPrompt' not in nodes.NODE_CLASS_MAPPINGS:
            utils.try_install_custom_node('https://github.com/ltdrdata/ComfyUI-Impact-Pack', "To use 'RegionalPromptSimple' node, 'Impact Pack' extension is required.")
            raise Exception(f"[ERROR] To use RegionalPromptSimple, you need to install 'ComfyUI-Impact-Pack'")
        (model, clip, vae, positive, negative) = basic_pipe
        iwe = nodes.NODE_CLASS_MAPPINGS['ImpactWildcardEncode']()
        kap = nodes.NODE_CLASS_MAPPINGS['KSamplerAdvancedProvider']()
        rp = nodes.NODE_CLASS_MAPPINGS['RegionalPrompt']()
        if wildcard_prompt != '':
            (model, clip, new_positive, _) = iwe.doit(model=model, clip=clip, populated_text=wildcard_prompt)
            if controlnet_in_pipe:
                prev_cnet = None
                for t in positive:
                    if 'control' in t[1] and 'control_apply_to_uncond' in t[1]:
                        prev_cnet = (t[1]['control'], t[1]['control_apply_to_uncond'])
                        break
                if prev_cnet is not None:
                    for t in new_positive:
                        t[1]['control'] = prev_cnet[0]
                        t[1]['control_apply_to_uncond'] = prev_cnet[1]
        else:
            new_positive = positive
        basic_pipe = (model, clip, vae, new_positive, negative)
        sampler = kap.doit(cfg, sampler_name, scheduler, basic_pipe, sigma_factor=sigma_factor)[0]
        regional_prompts = rp.doit(mask, sampler)[0]
        return (regional_prompts,)
```