# Documentation
- Class name: LaMa
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Remove the object from the image mask. This node is an encapsulation of [IOPaint] (https://www.iopay.com/) supported by the SOTA AI model, thanking the original author.
Provision of Lama, [LDM] (https://github.com/CompVis/latet-discussion), [ZITS] (https://github.com/DQiaole/ZITS_inputing), [MAT] (https://github.com/fenglinglwb/MAT), [FcF] (https://github.com/SHI-Labs/FcF-Inputing), [Manga] (https://github.com/msxie92/MangaInputing) models and SPREAD methods of elimination.
Please download model files (https://pan.baidu.com/s/1LllR9TJHP1G9uEwWT3Mvkg?pwd=tvzv) or [lama models (Google Drive)] (https://drive.google.com/drive/folders/1Aq0a4sybb3SRxi7j1_ZbBRjaWDDP9e?usp=sharing)

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- lama_model
    - The Lama model.
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str
    - Options:
        - lama
        - ldm
        - zits
        - mat
        - fcf
        - manga
        - spread

- device
    - With the correct installation of the Toch and Nvidia CUDA drivers, the use of cuda will significantly increase the speed of operation.
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str
    - Options:
        - cuda
        - cpu

- invert_mask
    - Reverse masked version.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- mask_grow
    - Mask expansion. Positive value is outward expansion, negative value is internal contraction.
    - Comfy dtype: INT
    - Python dtype: int

- mask_blur
    - The mask's fuzzy.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- image
    - The post-repair picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class LaMa:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        model_list = ['lama', 'ldm', 'zits', 'mat', 'fcf', 'manga', 'spread']
        device_list = ['cuda', 'cpu']
        return {
            "required": {
                "image": ("IMAGE", ),  #
                "mask": ("MASK",),  #
                "lama_model": (model_list,),
                "device": (device_list,),
                "invert_mask": ("BOOLEAN", {"default": False}), # Invert mask
                "mask_grow": ("INT", {"default": 25, "min": -255, "max": 255, "step": 1}),
                "mask_blur": ("INT", {"default": 8, "min": -255, "max": 255, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'lama'
    CATEGORY = '😺dzNodes/LayerUtility'

    def lama(self, image, mask, lama_model, device, invert_mask, mask_grow, mask_blur):

        l_images = []
        l_masks = []
        ret_images = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
        if mask is not None:
            if mask.dim() == 2:
                layer_mask = torch.unsqueeze(mask, 0)
            l_masks = []
            for m in mask:
                if invert_mask:
                    m = 1 - m
                l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))
        if len(l_masks) == 0:
            log(f"Error: {NODE_NAME} skipped, because the available mask is not found.", message_type='error')
            return (image,)

        max_batch = max(len(l_images), len(l_masks))

        for i in range(max_batch):
            _image = l_images[i] if i < len(l_images) else l_images[-1]
            _mask = l_masks[i] if i < len(l_masks) else l_masks[-1]
            if mask_grow or mask_blur:
                _mask = tensor2pil(expand_mask(image2mask(_mask), mask_grow, mask_blur))

            if lama_model == 'spread':
                ret_image = pixel_spread(tensor2pil(_image).convert('RGB'), ImageChops.invert(_mask.convert('RGB')))
            else:
                temp_dir = os.path.join(folder_paths.get_temp_directory(), generate_random_name('_lama_', '_temp', 16))
                if os.path.isdir(temp_dir):
                    shutil.rmtree(temp_dir)
                image_dir = os.path.join(temp_dir, 'image')
                mask_dir = os.path.join(temp_dir, 'mask')
                result_dir = os.path.join(temp_dir, 'result')
                try:
                    os.makedirs(image_dir)
                    os.makedirs(mask_dir)
                    os.makedirs(result_dir)
                except Exception as e:
                    print(e)
                    log(f"Error: {NODE_NAME} skipped, because unable to create temporary folder.", message_type='error')
                    return (image, )
                file_name = os.path.join(generate_random_name('lama_', '_temp', 16) + '.png')
                try:
                    tensor2pil(_image).save(os.path.join(image_dir, file_name))
                    _mask.save(os.path.join(mask_dir, file_name))
                except IOError as e:
                    print(e)
                    log(f"Error: {NODE_NAME} skipped, because unable to create temporary file.", message_type='error')
                    return (image, )
                # process
                from iopaint import cli
                cli.run(model=lama_model, device=device, image=Path(image_dir), mask=Path(mask_dir), output=Path(result_dir))
                ret_image = check_image_file(os.path.join(result_dir, file_name), 500)
                shutil.rmtree(temp_dir)
            ret_images.append(pil2tensor(ret_image))


        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```