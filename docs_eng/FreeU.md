# Documentation
- Class name: FreeU
- Category: model_patches
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

FreeU node is designed to modify the behaviour of the given model by applying patches to its output blocks. It adjusts the size and deviation parameters indicated in the middle of the model and enhances the performance of the model on a given task.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basic model that FreeU nodes will apply to their patches. This is the main input for node operations to achieve the required modifications.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- b1
    - The b1 parameter is a zoom factor that affects the first half of the model channel. It plays a key role in the ability of nodes to adjust model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2
    - The b2 parameter is another scaling factor that affects the second quarter of the model channel. It helps to fine-tune the behaviour of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s1
    - The s1 parameter defines the deviation that should be applied to the first half of the model channel after scaling. It is a core part of the node modification model output function.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s2
    - The s2 parameter specifies the deviation of the second quarter of the model channel and further customizes the output of the model to meet specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - Modified_model output is the result of the application of a patch from the FreeU node to the input model. It represents an enhanced model with adjustment parameters.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class FreeU:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'b1': ('FLOAT', {'default': 1.1, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'b2': ('FLOAT', {'default': 1.2, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 's1': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 's2': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'model_patches'

    def patch(self, model, b1, b2, s1, s2):
        model_channels = model.model.model_config.unet_config['model_channels']
        scale_dict = {model_channels * 4: (b1, s1), model_channels * 2: (b2, s2)}
        on_cpu_devices = {}

        def output_block_patch(h, hsp, transformer_options):
            scale = scale_dict.get(h.shape[1], None)
            if scale is not None:
                h[:, :h.shape[1] // 2] = h[:, :h.shape[1] // 2] * scale[0]
                if hsp.device not in on_cpu_devices:
                    try:
                        hsp = Fourier_filter(hsp, threshold=1, scale=scale[1])
                    except:
                        logging.warning('Device {} does not support the torch.fft functions used in the FreeU node, switching to CPU.'.format(hsp.device))
                        on_cpu_devices[hsp.device] = True
                        hsp = Fourier_filter(hsp.cpu(), threshold=1, scale=scale[1]).to(hsp.device)
                else:
                    hsp = Fourier_filter(hsp.cpu(), threshold=1, scale=scale[1]).to(hsp.device)
            return (h, hsp)
        m = model.clone()
        m.set_model_output_block_patch(output_block_patch)
        return (m,)
```