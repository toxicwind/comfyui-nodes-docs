# Documentation
- Class name: LoadCheckPointDragNUWA
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

This node class covers the functions of loading and operating the DragNUWA model, enabling users to condition the model through various input (e.g. tracking point or light flow data) to produce a high-realistic video frame. It simplifys the process of creating complex visual effects through the complexity of the abstract bottom model and provides a simple interface for video frame generation.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential because it identifies the specific DragNUWA model that you want to load. It affects the quality and properties of the resulting video frame and ensures that the correct model configuration is used for the task at hand.
    - Comfy dtype: COMBO
    - Python dtype: str
- dimension
    - The size parameter determines the resolution of the video frame that the model will generate. It is essential to ensure the format and quality standards required for output matching, which is critical for downstream processing and display.
    - Comfy dtype: COMBO
    - Python dtype: str
- model_length
    - Model length parameters are important because they set the time dimensions of the model and determine the number of frames that the model can handle. It affects the extent of the video generation and the ability of the model to capture motion and detail over time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - The output model is the core component of the follow-up video frame generation. It encapsifies the learning patterns and characteristics needed to produce high-quality visual content. The output of the model plays a key role in achieving the desired visual effects and meeting creative goals.
    - Comfy dtype: DragNUWA
    - Python dtype: Drag

# Usage tips
- Infra type: GPU

# Source code
```
class LoadCheckPointDragNUWA:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'ckpt_name': (['dragnuwa-svd-pruned.fp16.safetensors'], {'default': 'dragnuwa-svd-pruned.fp16.safetensors'}), 'dimension': (['576x320', '512x512', '320x576'], {'default': '576x320'}), 'model_length': ('INT', {'default': 14})}}
    RETURN_TYPES = ('DragNUWA',)
    RETURN_NAMES = ('model',)
    FUNCTION = 'load_dragnuwa'
    CATEGORY = 'DragNUWA'

    def load_dragnuwa(self, ckpt_name, dimension, model_length):
        width = int(dimension.split('x')[0])
        height = int(dimension.split('x')[1])
        comfy_path = os.path.dirname(folder_paths.__file__)
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        current_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.append(current_path)
        DragNUWA_net = Drag('cuda:0', ckpt_path, f'{comfy_path}/custom_nodes/ComfyUI-DragNUWA/DragNUWA_net.py', height, width, model_length)
        return (DragNUWA_net,)
```