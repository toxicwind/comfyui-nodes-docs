# Documentation
- Class name: FreeU_V2
- Category: model_patches
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

FreeU_V2 node is intended to enhance the function of the given model by applying a patch that changes the output block of the model. This is achieved by scaling and filtering the hidden state of the model in a manner sensitive to the channel dimensions, which may improve the performance or output properties of the model.

# Input types
## Required
- model
    - Model parameters are necessary because they represent the basic model that FreeU_V2 node will be modified. Node functions around changing the behavior of the model, making this parameter key to node execution.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- b1
    - b1 parameter is the zoom factor applied to certain hidden states in the model. It plays an important role in determining the degree of modification of node applications and influences the final output of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2
    - The b2 parameter is another zoom factor applied to different hidden statesets. It helps the overall modification process and is important for fine-tuning model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s1
    - The s1 parameter defines the zoom factor for the furiet filtering process applied to the model's hidden state. It is important for controlling the frequency fractions retained in model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s2
    - The s2 parameter is another zoom factor used in conjunction with the Fourier filtering process for different subsets of hidden states. It is important for adjusting the influence of nodes on model output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output of FreeU_V2 node is a modified model, which now contains applied patches. The modified model is expected to produce different outputs from the original model and may provide improved performance or characteristics.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class FreeU_V2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'b1': ('FLOAT', {'default': 1.3, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'b2': ('FLOAT', {'default': 1.4, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 's1': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 's2': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
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
                hidden_mean = h.mean(1).unsqueeze(1)
                B = hidden_mean.shape[0]
                (hidden_max, _) = torch.max(hidden_mean.view(B, -1), dim=-1, keepdim=True)
                (hidden_min, _) = torch.min(hidden_mean.view(B, -1), dim=-1, keepdim=True)
                hidden_mean = (hidden_mean - hidden_min.unsqueeze(2).unsqueeze(3)) / (hidden_max - hidden_min).unsqueeze(2).unsqueeze(3)
                h[:, :h.shape[1] // 2] = h[:, :h.shape[1] // 2] * ((scale[0] - 1) * hidden_mean + 1)
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