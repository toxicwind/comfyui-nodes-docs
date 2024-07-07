# Documentation
- Class name: CinematicLook
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The CinematicLook node is designed to enhance the visual appeal of images by applying various styled adjustments, imitating high-quality appearances that are common in cinematography and professional photography. The node converts ordinary images into movie quality images using colour hierarchies and other visual effects and applies to a wide range of uses from professional collections to social media posts.

# Input types
## Required
- image
    - The image parameter is the source material for node processing. It is vital because it serves as the basis for all subsequent conversions and enhancements. The quality and properties of the input image directly influence the final output, affecting the aesthetic and visual impact of the whole.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- look
    - Appearance parameters determine the style of image conversion. It is essential to determine the final visual tone and mood of the post-processed image. Different appearances meet different creative visions and applications, allowing for customized results consistent with desired aesthetics.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- result_img
    - Reult_img output is a converted image that applies the image of the film. It represents the result of node processing and contains style enhancements and adjustments to input images. This is the final product of the creative workflow that is intended to be used or further processed.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class CinematicLook:

    @classmethod
    def INPUT_TYPES(s):
        s.haldclut_files = read_cluts()
        s.file_names = [os.path.basename(f) for f in s.haldclut_files]
        return {'required': {'image': ('IMAGE', {'default': None}), 'look': (['modern', 'retro', 'clipped', 'broadcast', 'black and white', 'black and white - warm'],)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('result_img',)
    FUNCTION = 'cinematic_look'
    CATEGORY = 'Mikey/Image'

    def apply_haldclut(self, image, hald_clut, gamma_correction):
        hald_img = Image.open(self.haldclut_files[self.file_names.index(hald_clut)])
        img = tensor2pil(image)
        if gamma_correction == 'True':
            corrected_img = gamma_correction_pil(img, 1.0 / 2.2)
        else:
            corrected_img = img
        filtered_image = apply_hald_clut(hald_img, corrected_img).convert('RGB')
        return filtered_image

    @apply_to_batch
    def cinematic_look(self, image, look):
        if look == 'modern':
            image = self.apply_haldclut(image, 'modern.png', 'False')
        elif look == 'retro':
            image = self.apply_haldclut(image, 'retro.png', 'False')
        elif look == 'clipped':
            image = self.apply_haldclut(image, 'clipped.png', 'False')
        elif look == 'broadcast':
            image = self.apply_haldclut(image, 'broadcast.png', 'False')
        elif look == 'black and white':
            image = self.apply_haldclut(image, 'bw.png', 'False')
        elif look == 'black and white - warm':
            image = self.apply_haldclut(image, 'bw_warm.png', 'False')
        p = os.path.dirname(os.path.realpath(__file__))
        if look in ['black and white']:
            noise_img = os.path.join(p, 'noise_bw.png')
        else:
            noise_img = os.path.join(p, 'noise.png')
        noise = Image.open(noise_img)
        IO = ImageOverlay()
        image = pil2tensor(image)
        noise = pil2tensor(noise)
        if look == 'modern':
            image = IO.overlay(image, noise, 0.3)[0]
        if look == 'retro':
            image = IO.overlay(image, noise, 0.4)[0]
        if look == 'clipped':
            image = IO.overlay(image, noise, 0.25)[0]
        if look == 'broadcast':
            image = IO.overlay(image, noise, 0.3)[0]
        if look == 'black and white':
            image = IO.overlay(image, noise, 0.25)[0]
        if look == 'black and white - warm':
            image = IO.overlay(image, noise, 0.25)[0]
        return image
```