# Documentation
- Class name: Demofusion
- Category: tests
- Output node: False
- Repo Ref: https://github.com/deroberon/demofusion-comfyui

The node uses pre-trained diffusion models for image generation, guides the creation process in conjunction with texttips and generates high-resolution output.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential for selecting a pre-training model for image generation. It guides node access to the specified model structure and weights.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - A positive hint is used as a guide text that enhances the desired features in the creation of the image and directs the output to a specific visual element.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative hints help to remove unwanted elements from the images generated, making the output more in line with the intended creative vision.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The width determines the horizontal resolution of the generation of the image and affects the overall detail and quality of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altitude determines the vertical resolution of the image generation, affecting the size and width ratio of the end product.
    - Comfy dtype: INT
    - Python dtype: int
- inference_steps
    - The reasoning step defines the number of overlaps in model implementation to refine the image, directly affecting the details and clarity level of the final result.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters (or cfg) to adjust the guiding scale of the model and control the intensity of the impact of texttips on image generation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seeds provide a value for random number generation to ensure the replicability of results when using the same seeds in different operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output is a high-resolution image that contains the creative direction provided by the texttips and represents the peak of the ability to generate diffusion models.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class Demofusion:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': ('STRING', {'multiline': False, 'default': 'stabilityai/stable-diffusion-xl-base-1.0'}), 'positive': ('STRING', {'multiline': True, 'default': ''}), 'negative': ('STRING', {'multiline': True, 'default': ''}), 'width': ('INT', {'default': 2048, 'min': 2048, 'max': 4096, 'step': 64, 'display': 'number'}), 'height': ('INT', {'default': 2048, 'min': 2048, 'max': 4096, 'step': 64, 'display': 'number'}), 'inference_steps': ('INT', {'default': 40, 'min': 1, 'max': 100, 'step': 1, 'display': 'number'}), 'cfg': ('FLOAT', {'default': 7.5, 'min': 1.0, 'max': 20.0, 'step': 0.5, 'round': 0.001, 'display': 'number'}), 'seed': ('INT', {'default': 522, 'display': 'number'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'execute'
    CATEGORY = 'tests'

    def execute(self, ckpt_name, positive, negative, width, height, inference_steps, cfg, seed):
        pipe = DemoFusionSDXLStableDiffusionPipeline.from_pretrained(ckpt_name, torch_dtype=torch.float16)
        pipe = pipe.to('cuda')
        generator = torch.Generator(device='cuda')
        generator = generator.manual_seed(seed)
        images = pipe(str(positive), negative_prompt=str(negative), height=height, width=width, view_batch_size=4, stride=64, num_inference_steps=inference_steps, guidance_scale=cfg, cosine_scale_1=3, cosine_scale_2=1, cosine_scale_3=1, sigma=0.8, multi_decoder=True, show_image=False)
        image = images[len(images) - 1]
        image = image.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image,)
```