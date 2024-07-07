# Documentation
- Class name: imageRemBg
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The ImageRemBg node is designed to remove the background from the image and provide a simplified and clean future for further use or display. It does so by applying a background-specific in-depth learning model that removes optimization, ensuring that the output image retains its main theme while minimizing background interference.

# Input types
## Required
- images
    - Entering image parameters is essential for the operation of the node, as it defines the data that will be applied to the background removal process. The quality and format of these images directly affect the effect of the background removal.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- rem_mode
    - rem_mode parameters specify the removal mode to be used. It is essential because it determines the algorithm method used to separate the background and affects the accuracy of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- image_output
    - Image_output parameters indicate how to handle the images generated after processing. It hides them, previews them, saves them, or hides and saves them, providing flexibility to manage output according to user needs.
    - Comfy dtype: COMBO['Hide', 'Preview', 'Save', 'Hide/Save']
    - Python dtype: str
- save_prefix
    - When the user selects to save the processed image, use the save_prefix parameter. It provides the basic name for the saved file, which is important for organizing and identifying the output image.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - Optional prompt parameters can be used to provide additional context or instructions for nodes, which may be necessary for certain operations or for fine-tuning outputs according to specific criteria.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The extra_pnginfo parameter is used to include any additional information that node operations may require. This may be the relevant detail for metadata or other effects processing or output.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str

# Output types
- image
    - An image output parameter is a processing image that removes the background. It is the main output of the node and is significant because it reflects the outcome of the background removal process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask output parameter provides a binary mask generated during the background removal process. It helps to separate the foreground object from the background in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class imageRemBg:

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'images': ('IMAGE',), 'rem_mode': (('RMBG-1.4',),), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save'], {'default': 'Preview'}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    RETURN_NAMES = ('image', 'mask')
    FUNCTION = 'remove'
    OUTPUT_NODE = True
    CATEGORY = 'EasyUse/Image'

    def remove(self, rem_mode, images, image_output, save_prefix, prompt=None, extra_pnginfo=None):
        if rem_mode == 'RMBG-1.4':
            model_url = REMBG_MODELS[rem_mode]['model_url']
            suffix = model_url.split('.')[-1]
            model_path = get_local_filepath(model_url, REMBG_DIR, rem_mode + '.' + suffix)
            net = BriaRMBG()
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            net.load_state_dict(torch.load(model_path, map_location=device))
            net.to(device)
            net.eval()
            model_input_size = [1024, 1024]
            new_images = list()
            masks = list()
            for image in images:
                orig_im = tensor2pil(image)
                (w, h) = orig_im.size
                image = preprocess_image(orig_im, model_input_size).to(device)
                result = net(image)
                result_image = postprocess_image(result[0][0], (h, w))
                mask_im = Image.fromarray(result_image)
                new_im = Image.new('RGBA', mask_im.size, (0, 0, 0, 0))
                new_im.paste(orig_im, mask=mask_im)
                new_images.append(pil2tensor(new_im))
                masks.append(pil2tensor(mask_im))
            new_images = torch.cat(new_images, dim=0)
            masks = torch.cat(masks, dim=0)
            results = easySave(new_images, save_prefix, image_output, prompt, extra_pnginfo)
            if image_output in ('Hide', 'Hide/Save'):
                return {'ui': {}, 'result': (new_images, masks)}
            return {'ui': {'images': results}, 'result': (new_images, masks)}
        else:
            return (None, None)
```