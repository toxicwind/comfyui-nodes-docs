# Documentation
- Class name: NewLayer
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

NewLayer nodes are designed to operate and group image layers according to specific locations and zoom properties. It allows for the creation of a layered structure in which each layer can be positioned separately and scaled according to the parameters provided. The function of the nodes is concentrated on enhancing visual displays by precisely controlling their appearance and sequencing, thus enabling the stacking of multiple images.

# Input types
## Required
- x
    - The parameter 'x' specifies the horizontal position of the inner layer of the canvas. It is vital because it determines the exact location of the layer from the left side of the canvas and affects the overall structure.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The parameter 'y' defines the vertical position of the inner layer of the canvas. It is the key factor that determines how the layer is aligned from the top of the canvas and influences the final visual effect.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The parameter 'width' sets the width of the layer. It plays an important role in the scaling of the layer, allowing the horizontal dimensions of the visual content to be controlled.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The parameter 'height' determines the vertical dimensions of the layer. It is essential for the scale of the control layer on the vertical axis, and it affects the visibility of the layer.
    - Comfy dtype: INT
    - Python dtype: int
- z_index
    - Parameter'z_index' establishes the stacking order of the layer relative to the other layer. The higher the value, the higher the layer will be placed in front of the other layer, which is critical to the visibility and depth of management.
    - Comfy dtype: INT
    - Python dtype: int
- scale_option
    - The parameter'scale_option' determines how to zoom the layer. It is important to keep the horizontal ratio or evenly adjust the size of the layer, which can significantly change the visual output.
    - Comfy dtype: COMBO['width', 'height', 'overall']
    - Python dtype: str
- image
    - The parameter 'image' is the source of visual content of the layer. It is basic because it provides the actual pixels that will be operated and displayed in the canvas.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- mask
    - The optional parameter'mask' can be used to define a particular area of the image that should be visible or modified. It adds complexity to the image operation process and allows creative control of the final output.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- layers
    - The optional parameter 'layers' allows additional existing layers to be included in a combination. This is very useful for constructing or integrating multiple visual elements on existing visual structures.
    - Comfy dtype: LAYER
    - Python dtype: List[Dict[str, Union[int, str, torch.Tensor, PIL.Image.Image]]]
- canvas
    - The optional parameter 'canvas' provides a base image where the layer will be placed. It is important for setting the initial visual environment where the new layer will be integrated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Output types
- layers
    - The output 'layers' is a collection of layers of objects that represent the final combination of visual elements. It encapsulates the results of node operations and details the structure and appearance of the stratification images.
    - Comfy dtype: LAYER
    - Python dtype: Tuple[List[Dict[str, Union[int, str, torch.Tensor, PIL.Image.Image]]], ...]

# Usage tips
- Infra type: CPU

# Source code
```
class NewLayer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'x': ('INT', {'default': 0, 'min': -1024, 'max': 8192, 'step': 1, 'display': 'number'}), 'y': ('INT', {'default': 0, 'min': -1024, 'max': 8192, 'step': 1, 'display': 'number'}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'z_index': ('INT', {'default': 0, 'min': 0, 'max': 100, 'step': 1, 'display': 'number'}), 'scale_option': (['width', 'height', 'overall'],), 'image': ('IMAGE',)}, 'optional': {'mask': ('MASK', {'default': None}), 'layers': ('LAYER', {'default': None}), 'canvas': ('IMAGE', {'default': None})}}
    RETURN_TYPES = ('LAYER',)
    RETURN_NAMES = ('layers',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, x, y, width, height, z_index, scale_option, image, mask=None, layers=None, canvas=None):
        if mask == None:
            im = tensor2pil(image[0])
            mask = im.convert('L')
            mask = pil2tensor(mask)
        else:
            mask = mask[0]
        layer_n = [{'x': x[0], 'y': y[0], 'width': width[0], 'height': height[0], 'z_index': z_index[0], 'scale_option': scale_option[0], 'image': image[0], 'mask': mask}]
        if layers != None:
            layer_n = layer_n + layers
        return (layer_n,)
```