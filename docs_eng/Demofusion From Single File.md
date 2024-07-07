# Documentation
- Class name: DemofusionFromSingleFile
- Category: tests
- Output node: False
- Repo Ref: https://github.com/deroberon/demofusion-comfyui

The node facilitates the implementation of diffusion models for image generation, using pre-trained checkpoints to synthesize new visual content based on text tips. It emphasizes the role of nodes in creative AI applications, focusing on the generation process rather than on detailed implementation details.

# Input types
## Required
- ckpt_name
    - The check point name parameter is essential for the pre-training model specified for image generation. It guides node positioning and loading appropriate model weights and configurations, which are essential for the subsequent generation process.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positive parameter, as a texttip, guides the image generation process. Its importance is to set the theme direction for the output, affecting the overall style and content of the synthetic image.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - A negative parameter is used as an exclusionary filter for image generation to keep the output away from certain elements or themes. It refines the direction of creation by specifying the aspects that should be avoided in the end result.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The width parameters determine the horizontal resolution of the image, affecting the details and quality of the whole. They play a key role in determining the proportion and size of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical resolution of the image to determine the size of the canvas of the production process with width. It is part of the final size of the output.
    - Comfy dtype: INT
    - Python dtype: int
- inference_steps
    - The logical step parameter controls the number of turns used in the diffusion process, directly affecting the complexity and precision of the images generated. It is a key factor in achieving the desired level of detail.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the model to fine-tune the generation process to achieve a specific visual effect. It affects the style output and consistency of the content generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters ensure the replicability of results by using a fixed value initialization random number generator. It is essential for consistent experiments and results comparisons in different operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output image is the peak of the node function and contains visual content generated from the texttips and model configurations provided. It is the main result of the creation process and demonstrates the ability of the node to synthesize new images.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class DemofusionFromSingleFile:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),), 'positive': ('STRING', {'multiline': True, 'default': ''}), 'negative': ('STRING', {'multiline': True, 'default': ''}), 'width': ('INT', {'default': 2048, 'min': 2048, 'max': 4096, 'step': 64, 'display': 'number'}), 'height': ('INT', {'default': 2048, 'min': 2048, 'max': 4096, 'step': 64, 'display': 'number'}), 'inference_steps': ('INT', {'default': 40, 'min': 1, 'max': 100, 'step': 1, 'display': 'number'}), 'cfg': ('FLOAT', {'default': 7.5, 'min': 1.0, 'max': 20.0, 'step': 0.5, 'round': 0.001, 'display': 'number'}), 'seed': ('INT', {'default': 522, 'display': 'number'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'execute'
    CATEGORY = 'tests'

    def execute(self, ckpt_name, positive, negative, width, height, inference_steps, cfg, seed):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        pipe = DemoFusionSDXLStableDiffusionPipeline.from_single_file(ckpt_path, torch_dtype=torch.float16, use_safetensors=True)
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