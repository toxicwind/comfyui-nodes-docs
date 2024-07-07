# Documentation
- Class name: AnimateDiffModuleLoader
- Category: Animate Diff
- Output node: False
- Repo Ref: https://github.com/ArtVentureX/comfyui-animatediff.git

The node is designed to manage and operate campaign modules within the animated framework, focusing on the integration and application of advanced sports techniques to enhance animation dynamics and fluidity.

# Input types
## Required
- model_name
    - The model name is essential for identifying specific motion modules to be loaded and operated. It determines the origin of animation assets and provides the basis for follow-up operations.
    - Comfy dtype: string
    - Python dtype: str
## Optional
- lora_stack
    - The Lora stack is an optional parameter that allows fine-tuning of the motion module by layer. It enhances animation adaptation and customization to meet specific requirements.
    - Comfy dtype: list
    - Python dtype: List[Tuple[Dict[str, torch.Tensor], float]]

# Output types
- motion_module
    - The output sports module is the result of node processing, representing animated modules that are finalized and optimized for use in the animation process.
    - Comfy dtype: object
    - Python dtype: MotionWrapper

# Usage tips
- Infra type: CPU

# Source code
```
class AnimateDiffModuleLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model_name': (get_available_models(),)}, 'optional': {'lora_stack': ('MOTION_LORA_STACK',)}}
    RETURN_TYPES = ('MOTION_MODULE',)
    CATEGORY = 'Animate Diff'
    FUNCTION = 'load_motion_module'

    def inject_loras(self, motion_module: MotionWrapper, lora_stack: List[Tuple[Dict[str, Tensor], float]]):
        for lora in lora_stack:
            (state_dict, alpha) = lora
            for key in state_dict:
                layer_infos = key.split('.')
                curr_layer = motion_module
                while len(layer_infos) > 0:
                    temp_name = layer_infos.pop(0)
                    curr_layer = curr_layer.__getattr__(temp_name)
                curr_layer.weight.data += alpha * state_dict[key].to(curr_layer.weight.data.device)

    def eject_loras(self, motion_module: MotionWrapper, lora_stack: List[Tuple[float, Dict[str, Tensor]]]):
        lora_stack.reverse()
        for lora in lora_stack:
            (state_dict, alpha) = lora
            for key in state_dict:
                layer_infos = key.split('.')
                curr_layer = motion_module
                while len(layer_infos) > 0:
                    temp_name = layer_infos.pop(0)
                    curr_layer = curr_layer.__getattr__(temp_name)
                curr_layer.weight.data -= alpha * state_dict[key].to(curr_layer.weight.data.device)

    def load_motion_module(self, model_name: str, lora_stack: List=None):
        motion_module = load_motion_module(model_name)
        if motion_module.is_v2:
            if hasattr(motion_module, 'lora_stack') and isinstance(motion_module.lora_stack, list):
                self.eject_loras(motion_module, motion_module.lora_stack)
                delattr(motion_module, 'lora_stack')
            if isinstance(lora_stack, list):
                self.inject_loras(motion_module, lora_stack)
                setattr(motion_module, 'lora_stack', lora_stack)
        elif isinstance(lora_stack, list):
            logger.warning('LoRA is provided but only motion module v2 is supported.')
        return (motion_module,)
```