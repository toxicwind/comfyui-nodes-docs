# Documentation
- Class name: Segformer_B2_Clothes
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

To create a mask of face, hair, arms, legs, and costumes for people, mainly for dispersing clothing. Model division code from StartHua, thanks to the original author. This node has super-high edge details compared to the cofyui_segformer_b2_clothes nodes. (Note: The creation of pictures with edges above 2K sizes will take up a lot of memory using the VITMatte method.)

* Download all files from https://huggingface.co/matmdjaga/segformer_b2_clothes to ComfyUI/models/segformer_b2_clothes folders.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- face
    - Face.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- hair
    - Hair.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- hat
    - Hat.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- sunglass
    - Sunglasses.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- left_arm
    - Left arm.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- right_arm
    - Right arm.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- left_leg
    - Left leg.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- right_leg
    - Right leg.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- upper_clothes
    - The top.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- skirt
    - The dress.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- pants
    - Pants.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- dress
    - Clothes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- belt
    - The belt.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- shoe
    - Shoes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- bag
    - Bag.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- scarf
    - The scarf.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- detail_method
    - . Provides VITMatte, VITMatte (local), PyMatting, GuideedFilter. If the post-VITMatte model has been downloaded for the first time, then the VITMatte (local) can be used.
    - Comfy dtype: ['VITMatte', 'VITMatte(local)', 'PyMatting', 'GuidedFilter']
    - Python dtype: str

- detail_erode
    - The greater the value, the greater the range of internal restoration.
    - Comfy dtype: INT
    - Python dtype: int

- detail_dilate
    - The edge of the mask expands out. The greater the value, the greater the range of restoration.
    - Comfy dtype: INT
    - Python dtype: int

- black_point
    - Marginal black sampling threshold value.
    - Comfy dtype: FLOAT
    - Python dtype: float

- white_point
    - Marginal white sampling thresholds.
    - Comfy dtype: FLOAT
    - Python dtype: float

- process_detail
    - Set here as False will skip the edge treatment to save running time.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class Segformer_B2_Clothes:

    def __init__(self):
        pass

    # Labels: 0: "Background", 1: "Hat", 2: "Hair", 3: "Sunglasses", 4: "Upper-clothes", 5: "Skirt",
    # 6: "Pants", 7: "Dress", 8: "Belt", 9: "Left-shoe", 10: "Right-shoe", 11: "Face",
    # 12: "Left-leg", 13: "Right-leg", 14: "Left-arm", 15: "Right-arm", 16: "Bag", 17: "Scarf"

    @classmethod
    def INPUT_TYPES(cls):
        method_list = ['VITMatte', 'VITMatte(local)', 'PyMatting', 'GuidedFilter', ]
        return {"required":
                {
                "image":("IMAGE",),
                "face": ("BOOLEAN", {"default": False}),
                "hair": ("BOOLEAN", {"default": False}),
                "hat": ("BOOLEAN", {"default": False}),
                "sunglass": ("BOOLEAN", {"default": False}),
                "left_arm": ("BOOLEAN", {"default": False}),
                "right_arm": ("BOOLEAN", {"default": False}),
                "left_leg": ("BOOLEAN", {"default": False}),
                "right_leg": ("BOOLEAN", {"default": False}),
                "upper_clothes": ("BOOLEAN", {"default": False}),
                "skirt": ("BOOLEAN", {"default": False}),
                "pants": ("BOOLEAN", {"default": False}),
                "dress": ("BOOLEAN", {"default": False}),
                "belt": ("BOOLEAN", {"default": False}),
                "shoe": ("BOOLEAN", {"default": False}),
                "bag": ("BOOLEAN", {"default": False}),
                "scarf": ("BOOLEAN", {"default": False}),
                "detail_method": (method_list,),
                "detail_erode": ("INT", {"default": 12, "min": 1, "max": 255, "step": 1}),
                "detail_dilate": ("INT", {"default": 6, "min": 1, "max": 255, "step": 1}),
                "black_point": ("FLOAT", {"default": 0.01, "min": 0.01, "max": 0.98, "step": 0.01, "display": "slider"}),
                "white_point": ("FLOAT", {"default": 0.99, "min": 0.02, "max": 0.99, "step": 0.01, "display": "slider"}),
                "process_detail": ("BOOLEAN", {"default": True}),
                }
        }

    RETURN_TYPES = ("IMAGE", "MASK", )
    RETURN_NAMES = ("image", "mask", )
    FUNCTION = "segformer_ultra"
    CATEGORY = '😺dzNodes/LayerMask'

    def segformer_ultra(self, image,
                        face, hat, hair, sunglass, upper_clothes, skirt, pants, dress, belt, shoe,
                        left_leg, right_leg, left_arm, right_arm, bag, scarf, detail_method,
                        detail_erode, detail_dilate, black_point, white_point, process_detail
                        ):

        ret_images = []
        ret_masks = []

        if detail_method == 'VITMatte(local)':
            local_files_only = True
        else:
            local_files_only = False

        for i in image:
            pred_seg, cloth = get_segmentation(i)
            i = torch.unsqueeze(i, 0)
            i = pil2tensor(tensor2pil(i).convert('RGB'))
            orig_image = tensor2pil(i).convert('RGB')

            labels_to_keep = [0]
            if not hat:
                labels_to_keep.append(1)
            if not hair:
                labels_to_keep.append(2)
            if not sunglass:
                labels_to_keep.append(3)
            if not upper_clothes:
                labels_to_keep.append(4)
            if not skirt:
                labels_to_keep.append(5)
            if not pants:
                labels_to_keep.append(6)
            if not dress:
                labels_to_keep.append(7)
            if not belt:
                labels_to_keep.append(8)
            if not shoe:
                labels_to_keep.append(9)
                labels_to_keep.append(10)
            if not face:
                labels_to_keep.append(11)
            if not left_leg:
                labels_to_keep.append(12)
            if not right_leg:
                labels_to_keep.append(13)
            if not left_arm:
                labels_to_keep.append(14)
            if not right_arm:
                labels_to_keep.append(15)
            if not bag:
                labels_to_keep.append(16)
            if not scarf:
                labels_to_keep.append(17)

            mask = np.isin(pred_seg, labels_to_keep).astype(np.uint8)

            # Create angnostic-mask images
            mask_image = Image.fromarray((1 - mask) * 255)
            mask_image = mask_image.convert("L")
            _mask = pil2tensor(mask_image)

            detail_range = detail_erode + detail_dilate
            if process_detail:
                if detail_method == 'GuidedFilter':
                    _mask = guided_filter_alpha(i, _mask, detail_range // 6 + 1)
                    _mask = tensor2pil(histogram_remap(_mask, black_point, white_point))
                elif detail_method == 'PyMatting':
                    _mask = tensor2pil(mask_edge_detail(i, _mask, detail_range // 8 + 1, black_point, white_point))
                else:
                    _trimap = generate_VITMatte_trimap(_mask, detail_erode, detail_dilate)
                    _mask = generate_VITMatte(orig_image, _trimap, local_files_only=local_files_only)
                    _mask = tensor2pil(histogram_remap(pil2tensor(_mask), black_point, white_point))
            else:
                _mask = mask2image(_mask)

            ret_image = RGB2RGBA(orig_image, _mask.convert('L'))
            ret_images.append(pil2tensor(ret_image))
            ret_masks.append(image2mask(_mask))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), torch.cat(ret_masks, dim=0),)
```