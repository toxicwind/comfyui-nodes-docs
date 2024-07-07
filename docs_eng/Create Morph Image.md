# Documentation
- Class name: WAS_Image_Morph_GIF
- Category: WAS Suite/Animation
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Morph_GIF node is designed to create an animation between two images. It smooths the transition from one image to another on one specified frame number, allowing custom transition properties such as frame delay and loop settings. This node is particularly suitable for generating animation sequences such as GIF or APNG, which can be used in various multimedia presentations or applications.

# Input types
## Required
- image_a
    - The first image used for deformation animations. It sets the starting point for transition and is essential for the final output appearance.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- image_b
    - Animated deformation of the second image. This image defines the end state of the transition and contributes to the overall effect of the deformation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- transition_frames
    - The number of frames used for the transition between two images. The larger the number, the smoother the transition, the longer the animation takes.
    - Comfy dtype: INT
    - Python dtype: int
- still_image_delay_ms
    - The delay time (in milliseconds) for each static frame before the deformation transition begins.
    - Comfy dtype: FLOAT
    - Python dtype: float
- duration_ms
    - The duration of each frame during the deformation transition (in milliseconds).
    - Comfy dtype: FLOAT
    - Python dtype: float
- loops
    - Animation should be repeated several times. Value 0 means animation will be recycled indefinitely.
    - Comfy dtype: INT
    - Python dtype: int
- max_size
    - The maximum size of the output image (in pixels) may be adjusted to suit the limit while maintaining the vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- output_path
    - Saves the path to the output GIF file. If not specified, the default is './ComfyUI/output'.
    - Comfy dtype: STRING
    - Python dtype: str
- filename
    - Outputs the expected name of the GIF file. If not provided, the default is'morph'.
    - Comfy dtype: STRING
    - Python dtype: str
- filetype
    - Output animated file format. Supports 'GIF' or 'APNG'.
    - Comfy dtype: COMBO['GIF', 'APNG']
    - Python dtype: str

# Output types
- image_a_pass
    - The first input image, unaltered, is included in the output to maintain consistency.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- image_b_pass
    - The second input image, unchanged, is included in the output to maintain consistency.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- filepath_text
    - The full path to the created GIF file.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- filename_text
    - Creates a file name for the GIF.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Morph_GIF:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'transition_frames': ('INT', {'default': 30, 'min': 2, 'max': 60, 'step': 1}), 'still_image_delay_ms': ('FLOAT', {'default': 2500.0, 'min': 0.1, 'max': 60000.0, 'step': 0.1}), 'duration_ms': ('FLOAT', {'default': 0.1, 'min': 0.1, 'max': 60000.0, 'step': 0.1}), 'loops': ('INT', {'default': 0, 'min': 0, 'max': 100, 'step': 1}), 'max_size': ('INT', {'default': 512, 'min': 128, 'max': 1280, 'step': 1}), 'output_path': ('STRING', {'default': './ComfyUI/output', 'multiline': False}), 'filename': ('STRING', {'default': 'morph', 'multiline': False}), 'filetype': (['GIF', 'APNG'],)}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
    RETURN_TYPES = ('IMAGE', 'IMAGE', TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ('image_a_pass', 'image_b_pass', 'filepath_text', 'filename_text')
    FUNCTION = 'create_morph_gif'
    CATEGORY = 'WAS Suite/Animation'

    def create_morph_gif(self, image_a, image_b, transition_frames=10, still_image_delay_ms=10, duration_ms=0.1, loops=0, max_size=512, output_path='./ComfyUI/output', filename='morph', filetype='GIF'):
        tokens = TextTokens()
        WTools = WAS_Tools_Class()
        if 'imageio' not in packages():
            install_package('imageio')
        if filetype not in ['APNG', 'GIF']:
            filetype = 'GIF'
        if output_path.strip() in [None, '', '.']:
            output_path = './ComfyUI/output'
        output_path = tokens.parseTokens(os.path.join(*output_path.split('/')))
        if not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)
        if image_a == None:
            image_a = pil2tensor(Image.new('RGB', (512, 512), (0, 0, 0)))
        if image_b == None:
            image_b = pil2tensor(Image.new('RGB', (512, 512), (255, 255, 255)))
        if transition_frames < 2:
            transition_frames = 2
        elif transition_frames > 60:
            transition_frames = 60
        if duration_ms < 0.1:
            duration_ms = 0.1
        elif duration_ms > 60000.0:
            duration_ms = 60000.0
        output_file = WTools.morph_images([tensor2pil(image_a), tensor2pil(image_b)], steps=int(transition_frames), max_size=int(max_size), loop=int(loops), still_duration=int(still_image_delay_ms), duration=int(duration_ms), output_path=output_path, filename=tokens.parseTokens(filename), filetype=filetype)
        return (image_a, image_b, output_file)
```