# Scale Ref Image and VAE Encode 🎭🅐🅓②
## Documentation
- Class name: ADE_UpscaleAndVAEEncode
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The ADE_UpscaleAndVAENDEncode node is designed to process images by first magnifying them to a higher resolution and then encoding them as potential expressions using the VAE. This node is part of the AnimatéDiff package and is dedicated to enhancing image quality before applying further generation or conversion processes.

## Input types
### Required
- image
    - represents the parameters of the input image to be magnified and coded. It plays a key role in determining the quality and resolution of the ultimate potential expression.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - Specifies the variable-based encoder model that you use to encode the magnified image as a potential expression. It affects the coding efficiency and the quality of the potential space that you generate.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- latent_size
    - is the size of the potential expression that you want to generate. It determines the dimension of the potential space to be exported.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- scale_method
    - Defines the method used to magnify the image. It affects the mass of the magnified image.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- crop
    - Specifies the cropping method to be applied after magnification to influence the construction of the final image.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- latent
    - Comfy dtype: LATENT
    - Output is the potential expression of the input image, which is coded by VAE after magnification. It captures the basic features of the image in compressed form and is suitable for further tasks.
    - Python dtype: Dict[str, torch.Tensor]

## Usage tips
- Infra type: GPU
- Common nodes: unknown

## Source code
```python
class UpscaleAndVaeEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "vae": ("VAE",),
                "latent_size": ("LATENT",),
                "scale_method": (ScaleMethods._LIST_IMAGE,),
                "crop": (CropMethods._LIST, {"default": CropMethods.CENTER},),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "preprocess_images"

    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V"

    def preprocess_images(self, image: torch.Tensor, vae: VAE, latent_size: torch.Tensor, scale_method: str, crop: str):
        b, c, h, w = latent_size["samples"].size()
        image = image.movedim(-1,1)
        image = comfy.utils.common_upscale(samples=image, width=w*8, height=h*8, upscale_method=scale_method, crop=crop)
        image = image.movedim(1,-1)
        # now that images are the expected size, VAEEncode them
        try:  # account for old ComfyUI versions (TODO: remove this when other changes require ComfyUI update)
            if not hasattr(vae, "vae_encode_crop_pixels"):
                image = VAEEncode.vae_encode_crop_pixels(image)
        except Exception:
            pass
        return ({"samples": vae.encode(image[:,:,:,:3])},)