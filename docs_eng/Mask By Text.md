# Documentation
- Class name: ClipSegNode
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The ClipSegNode class is designed to automatically generate a mask from the input image based on the text tips provided. It uses a pre-training model to understand text descriptions and apply them to visual content, creating a segment mask that separates the theme in the image.

# Input types
## Required
- image
    - Enter the image as the main data source for node operations. It is the visual content that will generate the mask. The quality and resolution of the image directly affect the accuracy of the mask generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- prompt
    - Texttips are descriptive inputs that guide nodes in the image to identify the theme for the mask. It is essential for the model to understand the concerns during the partitioning process.
    - Comfy dtype: STRING
    - Python dtype: str
- precision
    - Precision parameters determine the threshold for mask generation. It is a floating point value that determines how strict the node should be when deciding which pixels are masked.
    - Comfy dtype: FLOAT
    - Python dtype: float
- normalize
    - Normalize parameters indicate whether the result mask should be standardized to a range of 0 to 1. Standardization may be useful in some applications that require consistent mask strength.
    - Comfy dtype: COMBO['no', 'yes']
    - Python dtype: Literal['no', 'yes']
## Optional
- negative_prompt
    - A negative hint is an optional input that helps to fine-tune the mask by indicating what should be excluded from the partition. It increases the accuracy of the mask by providing additional context to the model.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- thresholded_mask
    - The threshold mask is the main output of the node, representing a binary partition of the image based on the text tips provided. It is a key component of an application that requires topic separation for further processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- raw_mask
    - The original mask output provides a continuous value for the split mask before applying any threshold value. It may be useful for applications that require a more sophisticated understanding of the split.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ClipSegNode:
    """
        Automatically calculates a mask based on the text prompt
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'prompt': ('STRING', {'multiline': True}), 'negative_prompt': ('STRING', {'multiline': True}), 'precision': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'normalize': (['no', 'yes'],)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE')
    RETURN_NAMES = ('thresholded_mask', 'raw_mask')
    FUNCTION = 'get_mask'
    CATEGORY = 'Masquerade Nodes'

    def get_mask(self, image, prompt, negative_prompt, precision, normalize):
        model = self.load_model()
        image = tensor2rgb(image)
        (B, H, W, _) = image.shape
        used_dim = max(W, H)
        transform = transforms.Compose([transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), transforms.Resize((used_dim, used_dim), antialias=True)])
        img = transform(image.permute(0, 3, 1, 2))
        prompts = prompt.split(DELIMITER)
        negative_prompts = negative_prompt.split(DELIMITER) if negative_prompt != '' else []
        with torch.no_grad():
            dup_prompts = [item for item in prompts for _ in range(B)]
            preds = model(img.repeat(len(prompts), 1, 1, 1), dup_prompts)[0]
            dup_neg_prompts = [item for item in negative_prompts for _ in range(B)]
            negative_preds = model(img.repeat(len(negative_prompts), 1, 1, 1), dup_neg_prompts)[0] if len(negative_prompts) > 0 else None
        preds = torch.nn.functional.interpolate(preds, size=(H, W), mode='nearest')
        preds = torch.sigmoid(preds)
        preds = preds.reshape(len(prompts), B, H, W)
        mask = torch.max(preds, dim=0).values
        if len(negative_prompts) > 0:
            negative_preds = torch.nn.functional.interpolate(negative_preds, size=(H, W), mode='nearest')
            negative_preds = torch.sigmoid(negative_preds)
            negative_preds = negative_preds.reshape(len(negative_prompts), B, H, W)
            mask_neg = torch.max(negative_preds, dim=0).values
            mask = torch.min(mask, 1.0 - mask_neg)
        if normalize == 'yes':
            mask_min = torch.min(mask)
            mask_max = torch.max(mask)
            mask_range = mask_max - mask_min
            mask = (mask - mask_min) / mask_range
        thresholded = torch.where(mask >= precision, 1.0, 0.0)
        return (thresholded.to(device=image.device), mask.to(device=image.device))

    def load_model(self):
        global cached_clipseg_model
        if cached_clipseg_model == None:
            ensure_package('clipseg', 'clipseg@git+https://github.com/timojl/clipseg.git@bbc86cfbb7e6a47fb6dae47ba01d3e1c2d6158b0')
            from clipseg.clipseg import CLIPDensePredT
            model = CLIPDensePredT(version='ViT-B/16', reduce_dim=64, complex_trans_conv=True)
            model.eval()
            d64_file = self.download_and_cache('rd64-uni-refined.pth', 'https://owncloud.gwdg.de/index.php/s/ioHbRzFx6th32hn/download?path=%2F&files=rd64-uni-refined.pth')
            d16_file = self.download_and_cache('rd16-uni.pth', 'https://owncloud.gwdg.de/index.php/s/ioHbRzFx6th32hn/download?path=%2F&files=rd16-uni.pth')
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            model.load_state_dict(torch.load(d64_file, map_location=device), strict=False)
            model = model.eval().to(device=device)
            cached_clipseg_model = model
        return cached_clipseg_model

    def download_and_cache(self, cache_name, url):
        cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download_cache')
        os.makedirs(cache_dir, exist_ok=True)
        file_name = os.path.join(cache_dir, cache_name)
        if not os.path.exists(file_name):
            print(f'Downloading and caching file: {cache_name}')
            with open(file_name, 'wb') as file:
                import requests
                r = requests.get(url, stream=True)
                r.raise_for_status()
                for block in r.iter_content(4096):
                    file.write(block)
            print('Finished downloading.')
        return file_name
```