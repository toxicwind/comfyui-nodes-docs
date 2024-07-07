# Documentation
- Class name: WAS_Image_Morph_GIF_Writer
- Category: WAS Suite/Animation/Writer
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Morph_GIF_Writer is designed to create an animated GIF from a range of images or frames. It provides the function of managing the transition between frames, controlling the delay between them and setting up the GIF cycle behaviour. This node is particularly suitable for creating animations in a seamless and efficient manner and applies to applications such as visual effects, presentations or web content.

# Input types
## Required
- image
    - Enter an image or an image series for the creation of animated GIF frames. This parameter is essential because it directly affects the visual content of the animated drawings generated.
    - Comfy dtype: IMAGE
    - Python type: List [torch. Tensor] or torch. Tensor
## Optional
- transition_frames
    - Generates the number of frames to be converted from one image to the next. This parameter influences the smoothness of the animation by controlling the speed at which each frame moves to the next frame.
    - Comfy dtype: INT
    - Python dtype: int
- image_delay_ms
    - The delay before each frame transition begins is in milliseconds. This parameter is important for controlling the timing of the animation and can be adjusted as necessary to create the desired effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- duration_ms
    - The total length of the GIF animation is in milliseconds. This parameter sets the overall length of the animation from beginning to end.
    - Comfy dtype: FLOAT
    - Python dtype: float
- loops
    - The number of cycles of the GIF. Value 0 means that the GIF will loop indefinitely.
    - Comfy dtype: INT
    - Python dtype: int
- max_size
    - The maximum size of the output GIF is in pixels. This parameter is used to narrow the animation to suit specific display requirements or limitations.
    - Comfy dtype: INT
    - Python dtype: int
- output_path
    - Saves the path of the output GIF file. This parameter determines where the final animation is stored in the filesystem.
    - Comfy dtype: STRING
    - Python dtype: str
- filename
    - Outputs the name of the GIF file. This parameter allows the user to specify the required name for the animation file.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image_pass
    - A processed image or image series used to create GIF. This output reflects the visual content of the node process.
    - Comfy dtype: IMAGE
    - Python type: List [torch. Tensor] or torch. Tensor
- filepath_text
    - Creates the full file path for the GIF animation. This output applies to the reference or further processing of the animation file.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- filename_text
    - The name of the created GIF file. This output provides a specific name for the animated file.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Morph_GIF_Writer:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'transition_frames': ('INT', {'default': 30, 'min': 2, 'max': 60, 'step': 1}), 'image_delay_ms': ('FLOAT', {'default': 2500.0, 'min': 0.1, 'max': 60000.0, 'step': 0.1}), 'duration_ms': ('FLOAT', {'default': 0.1, 'min': 0.1, 'max': 60000.0, 'step': 0.1}), 'loops': ('INT', {'default': 0, 'min': 0, 'max': 100, 'step': 1}), 'max_size': ('INT', {'default': 512, 'min': 128, 'max': 1280, 'step': 1}), 'output_path': ('STRING', {'default': comfy_paths.output_directory, 'multiline': False}), 'filename': ('STRING', {'default': 'morph_writer', 'multiline': False})}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
    RETURN_TYPES = ('IMAGE', TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ('image_pass', 'filepath_text', 'filename_text')
    FUNCTION = 'write_to_morph_gif'
    CATEGORY = 'WAS Suite/Animation/Writer'

    def write_to_morph_gif(self, image, transition_frames=10, image_delay_ms=10, duration_ms=0.1, loops=0, max_size=512, output_path='./ComfyUI/output', filename='morph'):
        if 'imageio' not in packages():
            install_package('imageio')
        if output_path.strip() in [None, '', '.']:
            output_path = './ComfyUI/output'
        if image is None:
            image = pil2tensor(Image.new('RGB', (512, 512), (0, 0, 0))).unsqueeze(0)
        if transition_frames < 2:
            transition_frames = 2
        elif transition_frames > 60:
            transition_frames = 60
        if duration_ms < 0.1:
            duration_ms = 0.1
        elif duration_ms > 60000.0:
            duration_ms = 60000.0
        tokens = TextTokens()
        output_path = os.path.abspath(os.path.join(*tokens.parseTokens(output_path).split('/')))
        output_file = os.path.join(output_path, tokens.parseTokens(filename) + '.gif')
        if not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)
        WTools = WAS_Tools_Class()
        GifMorph = WTools.GifMorphWriter(int(transition_frames), int(duration_ms), int(image_delay_ms))
        for img in image:
            pil_img = tensor2pil(img)
            GifMorph.write(pil_img, output_file)
        return (image, output_file, filename)
```