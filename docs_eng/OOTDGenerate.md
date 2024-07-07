# Documentation
- Class name: OOTDGenerate
- Category: OOTD
- Output node: False
- Repo Ref: https://github.com/AuroBit/ComfyUI-OOTDiffusion.git

The node is designed to create creative fashions using diffusion models based on imported images and type of clothing. It is designed to provide users with diverse, contextually relevant and consistent clothing options.

# Input types
## Required
- pipe
    - The pipe parameter is essential, and it encapsifies the diffusion model used to generate clothing. It is the backbone of node functions and determines the quality and type of clothing produced.
    - Comfy dtype: MODEL
    - Python dtype: OOTDiffusion
- cloth_image
    - The column_image parameter is the basis on which the clothing is generated. It is essential for nodes to understand the context and synthesize clothing that is visually consistent with the image provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- model_image
    - The model_image parameter is used to provide a template for the image of a person in a dress. This is important to preserve the structural integrity of the dress and its true proportion to the human body.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- seed
    - Seed parameters introduce randomity in the formation of clothing, allowing multiple outcomes. This is critical for users seeking unique and non-repeated fashion options.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameter determines the number of turns to be used in the diffusion process. It affects the details and fineness of the clothing that will eventually be generated, and more steps will lead to more subtle results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the proportion of the image used during the generation, which affects the resolution and clarity of the apparel. It is a key factor in achieving high-quality visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- category
    - Category parameters specify the type of clothing to be generated, and guide nodes to generate clothing that corresponds to the selected fashion category. It is essential to ensure the relevance and appropriateness of the content generated.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Output types
- image
    - The Image output shows the finally generated clothing and the creative synthesis of the input-based fashion elements. It is the main result of node operations and represents the realization of the clothing concept.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_masked
    - The Image_masked output provides a clothing generation version that applies a specific fashion element mask. This output is important for users who need to have detailed control over the generation of content and allows further customization and operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class OOTDGenerate:
    display_name = 'OOTDiffusion Generate'

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('MODEL',), 'cloth_image': ('IMAGE',), 'model_image': ('IMAGE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 2.0, 'min': 0.0, 'max': 14.0, 'step': 0.1, 'round': 0.01}), 'category': (list(_category_readable.keys()),)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE')
    RETURN_NAMES = ('image', 'image_masked')
    FUNCTION = 'generate'
    CATEGORY = 'OOTD'

    def generate(self, pipe: OOTDiffusion, cloth_image, model_image, category, seed, steps, cfg):
        category = _category_readable[category]
        if pipe.model_type == 'hd' and category != 'upperbody':
            raise ValueError('Half body (hd) model type can only be used with upperbody category')
        model_image = model_image.squeeze(0)
        model_image = model_image.permute((2, 0, 1))
        model_image = to_pil_image(model_image)
        if model_image.size != (768, 1024):
            print(f'Inconsistent model_image size {model_image.size} != (768, 1024)')
        model_image = model_image.resize((768, 1024))
        cloth_image = cloth_image.squeeze(0)
        cloth_image = cloth_image.permute((2, 0, 1))
        cloth_image = to_pil_image(cloth_image)
        if cloth_image.size != (768, 1024):
            print(f'Inconsistent cloth_image size {cloth_image.size} != (768, 1024)')
        cloth_image = cloth_image.resize((768, 1024))
        (model_parse, _) = pipe.parsing_model(model_image.resize((384, 512)))
        keypoints = pipe.openpose_model(model_image.resize((384, 512)))
        (mask, mask_gray) = get_mask_location(pipe.model_type, _category_get_mask_input[category], model_parse, keypoints, width=384, height=512)
        mask = mask.resize((768, 1024), Image.NEAREST)
        mask_gray = mask_gray.resize((768, 1024), Image.NEAREST)
        masked_vton_img = Image.composite(mask_gray, model_image, mask)
        images = pipe(category=category, image_garm=cloth_image, image_vton=masked_vton_img, mask=mask, image_ori=model_image, num_samples=1, num_steps=steps, image_scale=cfg, seed=seed)
        output_image = to_tensor(images[0])
        output_image = output_image.permute((1, 2, 0)).unsqueeze(0)
        masked_vton_img = masked_vton_img.convert('RGB')
        masked_vton_img = to_tensor(masked_vton_img)
        masked_vton_img = masked_vton_img.permute((1, 2, 0)).unsqueeze(0)
        return (output_image, masked_vton_img)
```