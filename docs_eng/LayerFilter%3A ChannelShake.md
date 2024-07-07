# Documentation
- Class name: ChannelShake
- Category: 😺dzNodes/LayerFilter
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Channel is mispositioned. It's like a shivering logo effect.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- distance
    - The passage's at the wrong distance.
    - Comfy dtype: INT
    - Python dtype: int
    - Value range: 1-999

- angle
    - The angle of the passage is wrong.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Value range: -360-360

- mode
    - The channel is mispositioned in a pattern.
    - Comfy dtype: ENUM
    - Python dtype: str
    - Optional value: RGB, RBG, BGR, BRG, GBR, GRB

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ChannelShake:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        channel_mode = ['RGB', 'RBG', 'BGR', 'BRG', 'GBR', 'GRB']
        return {
            "required": {
                "image": ("IMAGE", ),  #
                "distance": ("INT", {default" 20, "min" : 1, "max" :999, "step" ), # distance
                "angle": ("FLOAT", {default" 40, "min" --360, "max" :360, "step" ): # Angle
                "mode": (channel_mode, # mode)
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'channel_shake'
    CATEGORY = '😺dzNodes/LayerFilter'

    def channel_shake(self, image, distance, angle, mode, ):

        ret_images = []

        for i in image:
            i = torch.unsqueeze(i, 0)
            _canvas = tensor2pil(i).convert('RGB')
            R, G, B = _canvas.split()
            x = int(math.cos(angle) * distance)
            y = int(math.sin(angle) * distance)
            if mode.startswith('R'):
                R = shift_image(R.convert('RGB'), -x, -y).convert('L')
            if mode.startswith('G'):
                G = shift_image(G.convert('RGB'), -x, -y).convert('L')
            if mode.startswith('B'):
                B = shift_image(B.convert('RGB'), -x, -y).convert('L')
            if mode.endswith('R'):
                R = shift_image(R.convert('RGB'), x, y).convert('L')
            if mode.endswith('G'):
                G = shift_image(G.convert('RGB'), x, y).convert('L')
            if mode.endswith('B'):
                B = shift_image(B.convert('RGB'), x, y).convert('L')

            ret_image = Image.merge('RGB', [R, G, B])
            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```