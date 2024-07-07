# Documentation
- Class name: DetailerHookCombine
- Category: PixelKSampleHookCombine
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Detailer HookCombine node acts as the coordinator of two separate hooks during pixel-level sampling. It ensures that each hook is applied in turn to potential spaces, to split and paste images, thereby enhancing the detail and consistency of the output generated.

# Input types
## Required
- latent
    - The " latent " parameter indicates the potential spatial vector that is being processed. It is a key component because it carries the coded information required for the detail enhancement process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- segs
    - The " segs " parameter is a split sheet list used to fine-tune image details. Each sheet in the list corresponds to different parts of the image.
    - Comfy dtype: List[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- image
    - The "image" parameter represents the amount of pasted images that will be further processed to enhance its visual detail.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- cycled_latent
    - The “cycled_latet” output is the result of the application of two hooks to input potential vectors, with the aim of raising the level of detail in potential indications.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- refined_segs
    - The "refined_segs" output consists of splits processed by two hooks in order to achieve a more detailed and accurate partition of the image.
    - Comfy dtype: List[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- processed_image
    - The "processed_image" output is the final load of images after two hooks have been enhanced, resulting in images with improved visual quality and detail.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class DetailerHookCombine(PixelKSampleHookCombine):

    def cycle_latent(self, latent):
        latent = self.hook1.cycle_latent(latent)
        latent = self.hook2.cycle_latent(latent)
        return latent

    def post_detection(self, segs):
        segs = self.hook1.post_detection(segs)
        segs = self.hook2.post_detection(segs)
        return segs

    def post_paste(self, image):
        image = self.hook1.post_paste(image)
        image = self.hook2.post_paste(image)
        return image
```