# Documentation
- Class name: IPAdapterModelHelper
- Category: InspirePack/models
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The IPAdapterModelHelper node is a key component in the InspirePack package, which promotes models and preset seamless integration and applications. It skilfully manages the complexity of model loads and ensures compatibility so that users can use the powerful functions of different models with minimal friction. The node is designed to simplify the use of models and provide a uniform interface to access the diversity function.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the core technology models to be used. They significantly influence the performance of nodes and the quality of the results produced, making them an essential aspect of the node function.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter plays an important role in the function of the node by providing the context required for image processing. It is essential for the node to generate accurate and relevant outputs based on input data.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- preset
    - Preset parameters allow the user to select the predefined settings and to adjust the behaviour of the node to a specific case. It is a key element that you customize the node to your user's needs.
    - Comfy dtype: COMBO[list(model_preset.keys())]
    - Python dtype: str
- lora_strength_model
    - The lora_strength_model parameter adjusts the impact of the LoRA model on node output. It is an important adjustment factor that can significantly influence the end result and allow fine particle size control of node behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_strength_clip
    - The lora_strength_clip parameter fine-tunes the impact of the CLIP model on node processing. It is a key parameter for users who need to control the balance between the impact of the CLIP model and other factors.
    - Comfy dtype: FLOAT
    - Python dtype: float
- insightface_provider
    - The insightface_provider parameter is assigned to the backend of the InsightFace model, which is essential for facial recognition tasks. This is an important option that affects the performance of nodes and their compatibility with user systems.
    - Comfy dtype: COMBO[['CPU', 'CUDA', 'ROCM']]
    - Python dtype: str
- cache_mode
    - Cache_mode parameters determine node cache strategies that can improve performance by reducing redundancy. This is an important consideration for optimizing node efficiency.
    - Comfy dtype: COMBO[['insightface only', 'clip_vision only', 'all', 'none']]
    - Python dtype: str
- unique_id
    - The unique_id parameter is used to track and identify nodes in the system, which is particularly useful for several examples of debugging and managing nodes.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- IPADAPTER_PIPE
    - The IPADAPTER_PIPE output is a composite structure that covers processed data and models and provides a comprehensive flow line for further analysis or use.
    - Comfy dtype: IPADAPTER_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.Tensor, torch.Tensor, Any, Callable[[torch.nn.Module], torch.nn.Module]]
- IPADAPTER
    - The IPADAPTER output represents the installed IPAdapter model, which can be used for applications in follow-up image processing tasks.
    - Comfy dtype: IPADAPTER
    - Python dtype: torch.nn.Module
- CLIP_VISION
    - The CLIP_VISION output provided the loaded CLIP model, which is essential for embedding from the context of image generation.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.Tensor
- INSIGHTFACE
    - The INSIGHTFACE output provided the InsightFace model, which is dedicated to facial recognition and analysis in node operations.
    - Comfy dtype: INSIGHTFACE
    - Python dtype: Any
- MODEL
    - MODEL output refers to the main model that has been enhanced or modified by nodes for further processing or direct application.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - CLIP output represents processed CLIP data that can be used for various downstream tasks involving the interaction of images and text.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- insightface_cache_key
    - The output of insightface_cache_key is the only identifier used to cache the InsightFace model, which optimizes the performance of nodes when reused.
    - Comfy dtype: STRING
    - Python dtype: str
- clip_vision_cache_key
    - The clip_vision_cache_key output provides the CLIP Vision model with the only identifier for the cache, which helps to increase the efficiency of nodes in duplicate tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterModelHelper:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'preset': (list(model_preset.keys()),), 'lora_strength_model': ('FLOAT', {'default': 1.0, 'min': -20.0, 'max': 20.0, 'step': 0.01}), 'lora_strength_clip': ('FLOAT', {'default': 1.0, 'min': -20.0, 'max': 20.0, 'step': 0.01}), 'insightface_provider': (['CPU', 'CUDA', 'ROCM'],), 'cache_mode': (['insightface only', 'clip_vision only', 'all', 'none'], {'default': 'insightface only'})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('IPADAPTER_PIPE', 'IPADAPTER', 'CLIP_VISION', 'INSIGHTFACE', 'MODEL', 'CLIP', 'STRING', 'STRING')
    RETURN_NAMES = ('IPADAPTER_PIPE', 'IPADAPTER', 'CLIP_VISION', 'INSIGHTFACE', 'MODEL', 'CLIP', 'insightface_cache_key', 'clip_vision_cache_key')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/models'

    def doit(self, model, clip, preset, lora_strength_model, lora_strength_clip, insightface_provider, cache_mode='none', unique_id=None):
        if 'IPAdapterApply' not in nodes.NODE_CLASS_MAPPINGS:
            utils.try_install_custom_node('https://github.com/cubiq/ComfyUI_IPAdapter_plus', "To use 'IPAdapterModelHelper' node, 'ComfyUI IPAdapter Plus' extension is required.")
            raise Exception(f"[ERROR] To use IPAdapterModelHelper, you need to install 'ComfyUI IPAdapter Plus'")
        is_sdxl_preset = 'SDXL' in preset
        is_sdxl_model = isinstance(clip.tokenizer, sdxl_clip.SDXLTokenizer)
        if is_sdxl_preset != is_sdxl_model:
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 1, 'label': 'IPADAPTER (fail)'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 2, 'label': 'CLIP_VISION (fail)'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 3, 'label': 'INSIGHTFACE (fail)'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 4, 'label': 'MODEL (fail)'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 5, 'label': 'CLIP (fail)'})
            print(f'[ERROR] IPAdapterModelHelper: You cannot mix SDXL and SD1.5 in the checkpoint and IPAdapter.')
            raise Exception('[ERROR] You cannot mix SDXL and SD1.5 in the checkpoint and IPAdapter.')
        (ipadapter, clipvision, lora, is_insightface) = model_preset[preset]
        (ipadapter, ok1) = lookup_model('ipadapter', ipadapter)
        (clipvision, ok2) = lookup_model('clip_vision', clipvision)
        (lora, ok3) = lookup_model('loras', lora)
        if ok1 == 'OK':
            ok1 = 'IPADAPTER'
        else:
            ok1 = f'IPADAPTER ({ok1})'
        if ok2 == 'OK':
            ok2 = 'CLIP_VISION'
        else:
            ok2 = f'CLIP_VISION ({ok2})'
        server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 1, 'label': ok1})
        server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 2, 'label': ok2})
        if ok3 == 'FAIL':
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 4, 'label': 'MODEL (fail)'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 5, 'label': 'CLIP (fail)'})
        else:
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 4, 'label': 'MODEL'})
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 5, 'label': 'CLIP'})
        if ok1 == 'FAIL' or ok2 == 'FAIL' or ok3 == 'FAIL':
            raise Exception('ERROR: Failed to load several models in IPAdapterModelHelper.')
        if ipadapter is not None:
            ipadapter = nodes.NODE_CLASS_MAPPINGS['IPAdapterModelLoader']().load_ipadapter_model(ipadapter_file=ipadapter)[0]
        ccache_key = ''
        if clipvision is not None:
            if cache_mode in ['clip_vision only', 'all']:
                ccache_key = clipvision
                if ccache_key not in backend_support.cache:
                    backend_support.cache[ccache_key] = (False, nodes.CLIPVisionLoader().load_clip(clip_name=clipvision)[0])
                clipvision = backend_support.cache[ccache_key][1]
            else:
                clipvision = nodes.CLIPVisionLoader().load_clip(clip_name=clipvision)[0]
        if lora is not None:
            (model, clip) = nodes.LoraLoader().load_lora(model=model, clip=clip, lora_name=lora, strength_model=lora_strength_model, strength_clip=lora_strength_clip)

            def f(x):
                return nodes.LoraLoader().load_lora(model=x, clip=clip, lora_name=lora, strength_model=lora_strength_model, strength_clip=lora_strength_clip)
            lora_loader = f
        else:

            def f(x):
                return x
            lora_loader = f
        icache_key = ''
        if is_insightface:
            if cache_mode in ['insightface only', 'all']:
                icache_key = 'insightface-' + insightface_provider
                if icache_key not in backend_support.cache:
                    backend_support.cache[icache_key] = (False, nodes.NODE_CLASS_MAPPINGS['InsightFaceLoader']().load_insight_face(insightface_provider)[0])
                insightface = backend_support.cache[icache_key][1]
            else:
                insightface = nodes.NODE_CLASS_MAPPINGS['InsightFaceLoader']().load_insight_face(insightface_provider)[0]
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 3, 'label': 'INSIGHTFACE'})
        else:
            insightface = None
            server.PromptServer.instance.send_sync('inspire-node-output-label', {'node_id': unique_id, 'output_idx': 3, 'label': 'INSIGHTFACE (N/A)'})
        pipe = (ipadapter, model, clipvision, insightface, lora_loader)
        return (pipe, ipadapter, clipvision, insightface, model, clip, icache_key, ccache_key)
```