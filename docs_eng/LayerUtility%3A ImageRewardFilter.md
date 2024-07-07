# Documentation
- Class name: ImageRewardFilter
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

This node uses [ImageReward] (https://github.com/THUMM/ImageReward) as a photo rating, thanking the original author.

# Input types

## Required

- images
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- prompt
    - Selectable input. Enter prompt here as the basis for determining its compatibility with the picture.
    - Comfy dtype: STRING
    - Python dtype: str

- output_num
    - . This value should be less than a lot of pictures.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- images
    - A batch of pictures, in order of rating, from high to low output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- obsolete_images
    - A picture of the phase-out. Similarly, the output is from high to low, in order of rating.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class ImageRewardFilter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "images": ("IMAGE", ),
                "prompt": ("STRING", {"multiline": False}),
                "output_num": ("INT", {"default": 3, "min": 1, "max": 999999, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE", "IMAGE",)
    RETURN_NAMES = ("images", 'obsolete_images',)
    FUNCTION = 'image_reward_filter'
    CATEGORY = '😺dzNodes/LayerUtility'

    def image_reward_filter(self, images, prompt, output_num,):
        log(f"len(images)= {len(images)}, output_num={output_num}")
        if output_num > len(images):
            log(f"Error: {NODE_NAME} skipped, because 'output_num' is greater then input images.", message_type='error')
            return (images,)

        scores = []
        ret_images = []
        obsolete_images = []

        if not torch.cuda.is_available() :
            device = "cpu"
        else:
            device = "cuda"

        import ImageReward as RM
        reward_model = RM.load("ImageReward-v1.0")
        reward_model = reward_model.to(device=device)

        with torch.no_grad():
            for i in range(len(images)):
                score = reward_model.score(prompt, tensor2pil(images[i]))
                scores.append(
                    {
                        "score":score,
                        "image_index":i
                    }
                )
        scores = sorted(scores, key=lambda s: s['score'], reverse=True)

        for i in range(len(images)):
            if i < output_num:
                log(f"{NODE_NAME} append image #{i}: {scores[i]['image_index']}, score = {scores[i]['score']}.")
                ret_images.append(images[scores[i]['image_index']])
            else:
                log(f"{NODE_NAME} obsolete image #{i}: {scores[i]['image_index']}, score = {scores[i]['score']}.")
                obsolete_images.append(images[scores[i]['image_index']])

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')

        return (ret_images, obsolete_images,)
```