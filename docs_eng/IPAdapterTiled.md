# Documentation
- Class name: IPAdapterTiled
- Category: ipadapter/tiled
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdaptTiled node is designed to process images through a lay-up mechanism, which is particularly useful in dealing with large images that may not be suitable for storage as a whole. It uses a series of changes and adjustments to the image sheet to generate embedding using the capabilities of the IPAdapter and CLIPVISION models, which can be used for further processing or model training.

# Input types
## Required
- model
    - Model parameters are necessary because they represent an in-depth learning model that will be used to process image data. It is the core component of the node function and determines how the image sheet is eventually analysed and converted.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter assigns the adapter model, which will be used in conjunction with the main model with appropriate image features. It plays a key role in the ability of nodes to modify and enhance image data to enhance model performance.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]
- image
    - Image input is the primary data source for the node. It is the original image data, which will be levelled and processed by the node. The quality and format of the image data directly influences the output and subsequent analysis of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- weight
    - The weight parameter allows you to adjust the impact of the image levelling on model output. It can fine-tune the contribution of each sheet to achieve the desired effect or balance in the final result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - The output model represents the treatment model after application of tiling and image-processing techniques. It encapsifies the features and conversions that have already been applied to input image-laying.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tiles
    - Tiled output contains a processed image sheeting. Each sheet undergos a node conversion process and can be used for further use or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- masks
    - The mask output provides a cover of concern that is used during the treatment of the image profile. These masks may be useful for the particular area of the focus image or for excluding certain areas from the analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterTiled:

    def __init__(self):
        self.unfold_batch = False

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'sharpening': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
    RETURN_TYPES = ('MODEL', 'IMAGE', 'MASK')
    RETURN_NAMES = ('MODEL', 'tiles', 'masks')
    FUNCTION = 'apply_tiled'
    CATEGORY = 'ipadapter/tiled'

    def apply_tiled(self, model, ipadapter, image, weight, weight_type, start_at, end_at, sharpening, combine_embeds='concat', image_negative=None, attn_mask=None, clip_vision=None, embeds_scaling='V only'):
        if 'ipadapter' in ipadapter:
            ipadapter_model = ipadapter['ipadapter']['model']
            clip_vision = clip_vision if clip_vision is not None else ipadapter['clipvision']['model']
        else:
            ipadapter_model = ipadapter
            clip_vision = clip_vision
        if clip_vision is None:
            raise Exception('Missing CLIPVision model.')
        del ipadapter
        tile_size = 256
        (_, oh, ow, _) = image.shape
        if attn_mask is None:
            attn_mask = torch.ones([1, oh, ow], dtype=image.dtype, device=image.device)
        image = image.permute([0, 3, 1, 2])
        attn_mask = attn_mask.unsqueeze(1)
        attn_mask = T.Resize((oh, ow), interpolation=T.InterpolationMode.BICUBIC, antialias=True)(attn_mask)
        if oh / ow > 0.75 and oh / ow < 1.33:
            image = T.CenterCrop(min(oh, ow))(image)
            resize = (tile_size * 2, tile_size * 2)
            attn_mask = T.CenterCrop(min(oh, ow))(attn_mask)
        else:
            resize = (int(tile_size * ow / oh), tile_size) if oh < ow else (tile_size, int(tile_size * oh / ow))
        imgs = []
        for img in image:
            img = T.ToPILImage()(img)
            img = img.resize(resize, resample=Image.Resampling['LANCZOS'])
            imgs.append(T.ToTensor()(img))
        image = torch.stack(imgs)
        del imgs, img
        attn_mask = T.Resize(resize[::-1], interpolation=T.InterpolationMode.BICUBIC, antialias=True)(attn_mask)
        if oh / ow > 4 or oh / ow < 0.25:
            crop = (tile_size, tile_size * 4) if oh < ow else (tile_size * 4, tile_size)
            image = T.CenterCrop(crop)(image)
            attn_mask = T.CenterCrop(crop)(attn_mask)
        attn_mask = attn_mask.squeeze(1)
        if sharpening > 0:
            image = contrast_adaptive_sharpening(image, sharpening)
        image = image.permute([0, 2, 3, 1])
        (_, oh, ow, _) = image.shape
        tiles_x = math.ceil(ow / tile_size)
        tiles_y = math.ceil(oh / tile_size)
        overlap_x = max(0, (tiles_x * tile_size - ow) / (tiles_x - 1 if tiles_x > 1 else 1))
        overlap_y = max(0, (tiles_y * tile_size - oh) / (tiles_y - 1 if tiles_y > 1 else 1))
        base_mask = torch.zeros([attn_mask.shape[0], oh, ow], dtype=image.dtype, device=image.device)
        tiles = []
        masks = []
        for y in range(tiles_y):
            for x in range(tiles_x):
                start_x = int(x * (tile_size - overlap_x))
                start_y = int(y * (tile_size - overlap_y))
                tiles.append(image[:, start_y:start_y + tile_size, start_x:start_x + tile_size, :])
                mask = base_mask.clone()
                mask[:, start_y:start_y + tile_size, start_x:start_x + tile_size] = attn_mask[:, start_y:start_y + tile_size, start_x:start_x + tile_size]
                masks.append(mask)
        del mask
        model = model.clone()
        for i in range(len(tiles)):
            ipa_args = {'image': tiles[i], 'image_negative': image_negative, 'weight': weight, 'weight_type': weight_type, 'combine_embeds': combine_embeds, 'start_at': start_at, 'end_at': end_at, 'attn_mask': masks[i], 'unfold_batch': self.unfold_batch, 'embeds_scaling': embeds_scaling}
            model = ipadapter_execute(model, ipadapter_model, clip_vision, **ipa_args)
        return (model, torch.cat(tiles), torch.cat(masks))
```