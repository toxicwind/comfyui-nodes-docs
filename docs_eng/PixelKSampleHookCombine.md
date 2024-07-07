# Documentation
- Class name: PixelKSampleHookCombine
- Category: image_processing
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Pixel KSampleHookCombine is a node designed to apply two separate hook sequences to a series of image processing operations. It coordinates hook pre-processing, decoding, magnification and encoded pixel data in a particular order to ensure a coordinated workflow for image operations.

# Input types
## Required
- hook1
    - The first hook to be used in sequence. It plays a crucial role in the initial phase of image processing and lays the foundation for subsequent operations.
    - Comfy dtype: PixelKSampleHook
    - Python dtype: PixelKSampleHook
- hook2
    - The second one to be applied in sequence is the hook, which further refines the image treatment flow line after the first hook has been applied and improves the overall output quality.
    - Comfy dtype: PixelKSampleHook
    - Python dtype: PixelKSampleHook

# Output types
- processed_pixels
    - The output of the Pixel KSampleHookCombine node is the result of using two hooks to enter pixel data. It represents the final state of the image after all processing steps have been completed.
    - Comfy dtype: COMBO[str, torch.Tensor]
    - Python dtype: Union[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class PixelKSampleHookCombine(PixelKSampleHook):
    hook1 = None
    hook2 = None

    def __init__(self, hook1, hook2):
        super().__init__()
        self.hook1 = hook1
        self.hook2 = hook2

    def set_steps(self, info):
        self.hook1.set_steps(info)
        self.hook2.set_steps(info)

    def pre_decode(self, samples):
        return self.hook2.pre_decode(self.hook1.pre_decode(samples))

    def post_decode(self, pixels):
        return self.hook2.post_decode(self.hook1.post_decode(pixels))

    def post_upscale(self, pixels):
        return self.hook2.post_upscale(self.hook1.post_upscale(pixels))

    def post_encode(self, samples):
        return self.hook2.post_encode(self.hook1.post_encode(samples))

    def post_crop_region(self, w, h, item_bbox, crop_region):
        crop_region = self.hook1.post_crop_region(w, h, item_bbox, crop_region)
        return self.hook2.post_crop_region(w, h, item_bbox, crop_region)

    def touch_scaled_size(self, w, h):
        (w, h) = self.hook1.touch_scaled_size(w, h)
        return self.hook2.touch_scaled_size(w, h)

    def pre_ksample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, upscaled_latent, denoise):
        (model, seed, steps, cfg, sampler_name, scheduler, positive, negative, upscaled_latent, denoise) = self.hook1.pre_ksample(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, upscaled_latent, denoise)
        return self.hook2.pre_ksample(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, upscaled_latent, denoise)
```