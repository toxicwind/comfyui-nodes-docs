# Documentation
- Class name: SeargeControlnetModels
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node coordinates the retrieval and integration of control network models for image processing tasks and facilitates customizing visual output to different model check points.

# Input types
## Required
- clip_vision
    - Clip_vision parameters are essential for the selection of model check points that influence the visual style and content of the images generated.
    - Comfy dtype: COMBO[UI.CLIP_VISION_WITH_NONE()]
    - Python dtype: Union[str, None]
- canny_checkpoint
    - This parameter is essential for the detection of the edges in the image so that nodes can fine-tune the structural elements of the output according to the selected checkpoint.
    - Comfy dtype: COMBO[UI.CONTROLNETS_WITH_NONE()]
    - Python dtype: Union[str, None]
- depth_checkpoint
    - The depth_checkpoint parameter is essential to control depth perception in the generation of images and enhances the 3-D presentation.
    - Comfy dtype: COMBO[UI.CONTROLNETS_WITH_NONE()]
    - Python dtype: Union[str, None]
- recolor_checkpoint
    - This parameter is essential for adjusting the colour panels of the image and allows for extensive style changes in the final visual products.
    - Comfy dtype: COMBO[UI.CONTROLNETS_WITH_NONE()]
    - Python dtype: Union[str, None]
- sketch_checkpoint
    - The sketch_checkpoint parameters play an important role in rendering images in sketch style, providing a unique artistic interpretation.
    - Comfy dtype: COMBO[UI.CONTROLNETS_WITH_NONE()]
    - Python dtype: Union[str, None]
- custom_checkpoint
    - This parameter allows the implementation of a custom control network model that expands the function of the node to meet specific user definition requirements.
    - Comfy dtype: COMBO[UI.CONTROLNETS_WITH_NONE()]
    - Python dtype: Union[str, None]

# Output types
- data
    - Data output is a structured dictionary that contains selected control network models and provides the basis for further image processing operations.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeControlnetModels:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'clip_vision': (UI.CLIP_VISION_WITH_NONE(),), 'canny_checkpoint': (UI.CONTROLNETS_WITH_NONE(),), 'depth_checkpoint': (UI.CONTROLNETS_WITH_NONE(),), 'recolor_checkpoint': (UI.CONTROLNETS_WITH_NONE(),), 'sketch_checkpoint': (UI.CONTROLNETS_WITH_NONE(),), 'custom_checkpoint': (UI.CONTROLNETS_WITH_NONE(),)}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(clip_vision, canny_checkpoint, depth_checkpoint, recolor_checkpoint, sketch_checkpoint, custom_checkpoint):
        return {UI.F_CLIP_VISION_CHECKPOINT: clip_vision, UI.F_CANNY_CHECKPOINT: canny_checkpoint, UI.F_DEPTH_CHECKPOINT: depth_checkpoint, UI.F_RECOLOR_CHECKPOINT: recolor_checkpoint, UI.F_SKETCH_CHECKPOINT: sketch_checkpoint, UI.F_CUSTOM_CHECKPOINT: custom_checkpoint}

    def get(self, clip_vision, canny_checkpoint, depth_checkpoint, recolor_checkpoint, sketch_checkpoint, custom_checkpoint, data=None):
        if data is None:
            data = {}
        data[UI.S_CONTROLNET_MODELS] = self.create_dict(clip_vision, canny_checkpoint, depth_checkpoint, recolor_checkpoint, sketch_checkpoint, custom_checkpoint)
        return (data,)
```