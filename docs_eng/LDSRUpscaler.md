# Documentation
- Class name: LDSRUpscaler
- Category: Flowty LDSR
- Output node: False
- Repo Ref: https://github.com/flowtyone/ComfyUI-Flowty-LDSR.git

The LDSR Uppscaler node 'upscale' method is designed to use pre-training models to enhance the resolution of the input image. It uses the ability of the LDSR algorithm to perform ultra-resolution, i.e. to increase the spatial resolution of the image while maintaining or improving the quality of the image. This method is particularly suitable for magnifying images with high detail, such as photographs or digital art works.

# Input types
## Required
- model
    - The `model' parameter is the path of the pre-training model for magnification. It is essential for the function of the node, as it determines the specific model weight and structure that will be applied to the input image for ultra-resolution.
    - Comfy dtype: STRING
    - Python dtype: str
- images
    - The `images' parameter is the set of images that the node will process to magnify. This input is essential because it represents data that will be converted from node to achieve a higher resolution.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
- steps
    - The'steps' parameter defines the number of proliferation steps to be used in the ultra-resolution process. It affects the quality and calculation time of the magnifying image. More steps usually lead to better results, but they also extend processing time.
    - Comfy dtype: INT
    - Python dtype: int
- pre_downscale
    - The 'pre_downscale' parameter specifies whether and what proportion of the image should be reduced before the hyper-resolution process. This is an optional setup that can be used to control the initial resolution of the input image.
    - Comfy dtype: STRING
    - Python dtype: str
- post_downscale
    - The 'post_downscale' parameter determines whether and how to narrow the image after the hyper-resolution process. It allows control over the final resolution of the output image.
    - Comfy dtype: STRING
    - Python dtype: str
- downsample_method
    - The `downsample_method' parameter selects the reduction algorithm to be used in adjusting the image for a larger time. It may affect the quality of the image, usually including `Nearest' or `Lanczos'.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- images
    - The `images' output parameters contain magnified images from ultra-resolution processes. These are the main results of node execution and represent conversion data with an increased resolution.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LDSRUpscaler:

    @classmethod
    def INPUT_TYPES(s):
        model_list = get_filename_list('upscale_models')
        candidates = [name for name in model_list if 'last.ckpt' in name]
        if len(candidates) > 0:
            default_path = candidates[0]
        else:
            default_path = 'last.ckpt'
        return {'required': {'model': (model_list, {'default': default_path}), 'images': ('IMAGE',), 'steps': (['25', '50', '100', '250', '500', '1000'], {'default': '100'}), 'pre_downscale': (['None', '1/2', '1/4'], {'default': 'None'}), 'post_downscale': (['None', 'Original Size', '1/2', '1/4'], {'default': 'None'}), 'downsample_method': (['Nearest', 'Lanczos'], {'default': 'Lanczos'})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'upscale'
    CATEGORY = 'Flowty LDSR'

    def upscale(self, model, images, steps, pre_downscale='None', post_downscale='None', downsample_method='Lanczos'):
        model_path = get_full_path('upscale_models', model)
        pbar = ProgressBar(int(steps))
        p = {'prev': 0}

        def prog(i):
            i = i + 1
            if i < p['prev']:
                p['prev'] = 0
            pbar.update(i - p['prev'])
            p['prev'] = i
        ldsr = LDSR(modelPath=model_path, torchdevice=get_torch_device(), on_progress=prog)
        outputs = []
        for image in images:
            outputs.append(ldsr.superResolution(image, int(steps), pre_downscale, post_downscale, downsample_method))
        return (torch.stack(outputs),)
```