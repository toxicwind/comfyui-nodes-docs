# Documentation
- Class name: LDSRUpscale
- Category: Flowty LDSR
- Output node: False
- Repo Ref: https://github.com/flowtyone/ComfyUI-Flowty-LDSR.git

The node class covers advanced features that perform ultra-resolution on the image, using the LDSR model to improve the resolution of the image and thereby enhance its quality. It aims to enhance visual authenticity and detail without compromising the basic content of the image.

# Input types
## Required
- upscale_model
    - The upscale_model parameter is essential because it defines the bottom model that the node will be used to perform ultra-resolution tasks. This is essential for the correct function of the node and for producing accurate results.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: str
- images
    - The Images parameter is the main input for node operations, representing the image that needs to be magnified. Its role is critical because the quality and type of input directly influences the effectiveness of the output appearance and hyperresolution process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- steps
    - The steps parameters affect the number of overlaps that are implemented during the magnification process. It is a balancing factor between the quality of the output and the computational resources required. More steps usually yield better results, but the calculation costs are higher.
    - Comfy dtype: COMBO[25, 50, 100, 250, 500, 1000]
    - Python dtype: int
- pre_downscale
    - Pre_downscale parameters determine the size of the reduction applied to input images prior to the hyper-resolution process. This is particularly useful for managing loads and memory, especially for very high-resolution images.
    - Comfy dtype: COMBO[None, 1/2, 1/4]
    - Python dtype: str
- post_downscale
    - Post_downscale parameters determine the operation to be scaled down after applying the super-resolution. It helps to control the size of the final output and can be used to optimize the output according to different cases or requirements.
    - Comfy dtype: COMBO[None, Original Size, 1/2, 1/4]
    - Python dtype: str
- downsample_method
    - The downsample_method parameter specifies the lower sampling technique that will be used to reduce the image hours before or after the ultra-resolution process. It affects the image quality after resizing, and Lanczos usually provides better results, but the calculation costs are higher.
    - Comfy dtype: COMBO[Nearest, Lanczos]
    - Python dtype: str

# Output types
- images
    - The output images are the result of an ultra-resolution process that shows the enhanced detail and improved visual authenticity. They are the main output of the nodes and directly reflect the validity of the magnifying models and the parameters used.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LDSRUpscale:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upscale_model': ('UPSCALE_MODEL',), 'images': ('IMAGE',), 'steps': (['25', '50', '100', '250', '500', '1000'], {'default': '100'}), 'pre_downscale': (['None', '1/2', '1/4'], {'default': 'None'}), 'post_downscale': (['None', 'Original Size', '1/2', '1/4'], {'default': 'None'}), 'downsample_method': (['Nearest', 'Lanczos'], {'default': 'Lanczos'})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'upscale'
    CATEGORY = 'Flowty LDSR'

    def upscale(self, upscale_model, images, steps, pre_downscale='None', post_downscale='None', downsample_method='Lanczos'):
        pbar = ProgressBar(int(steps))
        p = {'prev': 0}

        def prog(i):
            i = i + 1
            if i < p['prev']:
                p['prev'] = 0
            pbar.update(i - p['prev'])
            p['prev'] = i
        ldsr = LDSR(model=upscale_model, on_progress=prog)
        outputs = []
        for image in images:
            outputs.append(ldsr.superResolution(image, int(steps), pre_downscale, post_downscale, downsample_method))
        return (torch.stack(outputs),)
```