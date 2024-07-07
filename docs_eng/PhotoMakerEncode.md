# Documentation
- Class name: PhotoMakerEncode
- Category: _for_testing/photomaker
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The PhotoMakerEncode node is designed to use a combination of text, clip features and images to apply the photomaker effect to input images. It processes input to generate conditions that can be used for further image operation tasks.

# Input types
## Required
- photomaker
    - The photomaker parameter is essential for applying the photomaker effect. It is expected to be a pre-training model or compatible object that can handle the image accordingly.
    - Comfy dtype: PHOTOMAKER
    - Python dtype: torch.nn.Module
- image
    - The image parameter represents the input image that the node will process. This is a key input, because the photomaker effect is applied directly to this image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- clip
    - The clip parameter is used to mark the text and encode it into a format that you can use to generate a condition output.
    - Comfy dtype: CLIP
    - Python dtype: Callable
- text
    - The text parameter provides a descriptive input that guides photomaker to apply the desired effect to the image. It is a multi-line string that contains dynamic tips.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- CONDITIONING
    - CONDITONING output is the key result of node operations. It encapsifies the encoded expression used to guide subsequent image operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]

# Usage tips
- Infra type: GPU

# Source code
```
class PhotoMakerEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'photomaker': ('PHOTOMAKER',), 'image': ('IMAGE',), 'clip': ('CLIP',), 'text': ('STRING', {'multiline': True, 'dynamicPrompts': True, 'default': 'photograph of photomaker'})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'apply_photomaker'
    CATEGORY = '_for_testing/photomaker'

    def apply_photomaker(self, photomaker, image, clip, text):
        special_token = 'photomaker'
        pixel_values = comfy.clip_vision.clip_preprocess(image.to(photomaker.load_device)).float()
        try:
            index = text.split(' ').index(special_token) + 1
        except ValueError:
            index = -1
        tokens = clip.tokenize(text, return_word_ids=True)
        out_tokens = {}
        for k in tokens:
            out_tokens[k] = []
            for t in tokens[k]:
                f = list(filter(lambda x: x[2] != index, t))
                while len(f) < len(t):
                    f.append(t[-1])
                out_tokens[k].append(f)
        (cond, pooled) = clip.encode_from_tokens(out_tokens, return_pooled=True)
        if index > 0:
            token_index = index - 1
            num_id_images = 1
            class_tokens_mask = [True if token_index <= i < token_index + num_id_images else False for i in range(77)]
            out = photomaker(id_pixel_values=pixel_values.unsqueeze(0), prompt_embeds=cond.to(photomaker.load_device), class_tokens_mask=torch.tensor(class_tokens_mask, dtype=torch.bool, device=photomaker.load_device).unsqueeze(0))
        else:
            out = cond
        return ([[out, {'pooled_output': pooled}]],)
```