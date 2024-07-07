# Documentation
- Class name: smZ_CLIPTextEncode
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/shiimizu/ComfyUI_smZNodes.git

The smZ_CLIPTextEncode node is designed to process text input and convert it into a structured expression that can be used for further computing tasks. It uses the power of the CLIP model to understand and generate text embedding, which is essential for various AI-driven applications. The node abstractes the complexity of text encoding and allows users to focus on the broader objectives of the project rather than on the details of text processing.

# Input types
## Required
- text
    - Text parameters are essential because they provide raw text data processed by nodes. They provide the basis for the entire encoded operation, the content of which directly affects the quality and relevance of the embedded generation.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The clip parameter represents the CLIP model that the node uses to encode the text. This is a key element because the capabilities and training of the model directly influence the coding process and the subsequent use of embedded.
    - Comfy dtype: CLIP
    - Python dtype: comfy.sd.CLIP
- parser
    - The parser parameter is essential to determine how the text will be interpreted and processed by nodes. It affects the particle size and structure indicated by the text, which is essential for the accuracy and validity of the code.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- CONDITIONING
    - The output of the smZ_CLIPTextEncode node is a set of reconciliation data derived from coded text. These data are important because they can be used to guide and refine subsequent AI models or tasks by providing them with the necessary context and structure.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: GPU

# Source code
```
class smZ_CLIPTextEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'parser': (['comfy', 'comfy++', 'A1111', 'full', 'compel', 'fixed attention'], {'default': 'comfy'}), 'mean_normalization': (BOOLEAN, {'default': True}), 'multi_conditioning': (BOOLEAN, {'default': True}), 'use_old_emphasis_implementation': (BOOLEAN, {'default': False}), 'with_SDXL': (BOOLEAN, {'default': False}), 'ascore': ('FLOAT', {'default': 6.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}), 'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'text_g': ('STRING', {'multiline': True, 'placeholder': 'CLIP_G'}), 'text_l': ('STRING', {'multiline': True, 'placeholder': 'CLIP_L'})}, 'optional': {'smZ_steps': ('INT', {'default': 1, 'min': 1, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning'

    def encode(self, clip: comfy.sd.CLIP, text, parser, mean_normalization, multi_conditioning, use_old_emphasis_implementation, with_SDXL, ascore, width, height, crop_w, crop_h, target_width, target_height, text_g, text_l, smZ_steps=1):
        params = locals()
        params['steps'] = params.pop('smZ_steps', smZ_steps)
        from .modules.shared import opts_default as opts
        should_use_fp16_signature = inspect.signature(comfy.model_management.should_use_fp16)
        _p = should_use_fp16_signature.parameters
        devices.device = shared.device = clip.patcher.load_device if hasattr(clip.patcher, 'load_device') else clip.device
        if 'device' in _p and 'prioritize_performance' in _p:
            should_use_fp16 = partial(comfy.model_management.should_use_fp16, device=devices.device, prioritize_performance=False)
        elif 'device' in should_use_fp16_signature.parameters:
            should_use_fp16 = partial(comfy.model_management.should_use_fp16, device=devices.device)
        else:
            should_use_fp16 = comfy.model_management.should_use_fp16
        dtype = torch.float16 if should_use_fp16() else torch.float32
        dtype_unet = dtype
        devices.dtype = dtype
        if devices.dtype_unet == torch.float16:
            devices.dtype_unet = dtype_unet
        devices.unet_needs_upcast = opts.upcast_sampling and devices.dtype == torch.float16 and (devices.dtype_unet == torch.float16)
        devices.dtype_vae = comfy.model_management.vae_dtype() if hasattr(comfy.model_management, 'vae_dtype') else torch.float32
        params.pop('self', None)
        result = run(**params)
        result[0][0][1]['params'] = {}
        result[0][0][1]['params'].update(params)
        if opts.pad_cond_uncond:
            text = params['text']
            with_SDXL = params['with_SDXL']
            params['text'] = ''
            params['with_SDXL'] = False
            empty = run(**params)[0]
            params['text'] = text
            params['with_SDXL'] = with_SDXL
            shared.sd_model.cond_stage_model_empty_prompt = empty[0][0]
        return result
```