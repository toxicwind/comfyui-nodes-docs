# Documentation
- Class name: FaceParsingResultsParser
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The node type covers the logic of condensing and interpreting facial resolution results and extracts various facial properties from the input data. It is the core component of the facial analysis process, focusing on the division and identification of different facial features.

# Input types
## Required
- result
    - The result parameter is essential because it contains the original facial resolution data to be processed at the node. It is the main input that determines the accuracy of subsequent operations and facial feature extraction.
    - Comfy dtype: FACE_PARSING_RESULT
    - Python dtype: torch.Tensor
## Optional
- background
    - This parameter controls whether background partitions are taken into account in the analysis process. Inclusion or exclusion of background can significantly affect the clarity of the composition and facial features of the overall facial mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- skin
    - Skin parameters are essential for identifying the skin area in the facial area. They play a crucial role in isolating the skin for further analysis or treatment (e.g. skin condition assessment).
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- nose
    - By enabling or disallowing nose parameters, nodes can focus on the nose area, which is important for character-based facial recognition or beauty effects.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- eye_g
    - Eye_g parameters are used to contain or exclude general eye areas, which are important for tasks such as eye-trace or eye-glass recommendations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- r_eye
    - The r_eye parameter allows for the specific inclusion or exclusion of the right eye, which is essential for detailed facial expression analysis or asymmetric testing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- l_eye
    - Similarly, the l_eye parameter is used to contain or exclude the left eye in a specific way, playing a role similar to the right eye parameter in facial analysis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- r_brow
    - The r_brow parameter is used in the right eyebrow area, which is important for understanding facial expressions and emotional analysis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- l_brow
    - l_brow parameters correspond to the left eyebrow area and play a similar role to the right eyebrow in conveying facial expressions and emotions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- r_ear
    - The r_ar parameter is used in the right ear area and may be important for some audio-visual applications or hearing aids integration.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- l_ear
    - I_EAR parameters correspond to the left ear area, playing a role similar to the right ear in audio-visual applications.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mouth
    - Mouth parameters are essential for identifying mouth areas, which are important for tasks such as lip reading or speech recognition.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- u_lip
    - The u_lip parameter focuses on the upper lip area, which is important for detailed facial expression analysis and beauty-related applications.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- l_lip
    - l_lip parameters are used in the lower lip area to play a role similar to the upper lip in facial expression analysis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- hair
    - Hair parameters are used to contain or exclude hair areas, which may be important for style analysis or recommendations for hair-related products.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- hat
    - The cap parameters allow for the specific inclusion or exclusion of the hat area, which is important for fashion analysis or recommendations for apparel.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- ear_r
    - The year_r parameter is used in the right ear area and may be important for hearing aid integration or ear health monitoring.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- neck_l
    - The neck_l parameter corresponds to the left neck area and may be important in position analysis or clothing adaptation recommendations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- neck
    - The neck parameters are used in the neck area and are important in tasks such as position analysis and contribute to the interpretation of the overall body language.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- cloth
    - The clothing parameters are used to contain or exclude clothing areas, which is important for fashion analysis or virtual test clothes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- MASK
    - The output mask is a binary expression that divides and recognizes various facial features according to input parameters. It is a key output for further facial analysis and can be used in a variety of applications, such as facial face recognition, beauty analysis, etc.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FaceParsingResultsParser:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'result': ('FACE_PARSING_RESULT', {}), 'background': ('BOOLEAN', {'default': False}), 'skin': ('BOOLEAN', {'default': True}), 'nose': ('BOOLEAN', {'default': True}), 'eye_g': ('BOOLEAN', {'default': True}), 'r_eye': ('BOOLEAN', {'default': True}), 'l_eye': ('BOOLEAN', {'default': True}), 'r_brow': ('BOOLEAN', {'default': True}), 'l_brow': ('BOOLEAN', {'default': True}), 'r_ear': ('BOOLEAN', {'default': True}), 'l_ear': ('BOOLEAN', {'default': True}), 'mouth': ('BOOLEAN', {'default': True}), 'u_lip': ('BOOLEAN', {'default': True}), 'l_lip': ('BOOLEAN', {'default': True}), 'hair': ('BOOLEAN', {'default': True}), 'hat': ('BOOLEAN', {'default': True}), 'ear_r': ('BOOLEAN', {'default': True}), 'neck_l': ('BOOLEAN', {'default': True}), 'neck': ('BOOLEAN', {'default': True}), 'cloth': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, result: Tensor, background: bool, skin: bool, nose: bool, eye_g: bool, r_eye: bool, l_eye: bool, r_brow: bool, l_brow: bool, r_ear: bool, l_ear: bool, mouth: bool, u_lip: bool, l_lip: bool, hair: bool, hat: bool, ear_r: bool, neck_l: bool, neck: bool, cloth: bool):
        masks = []
        for item in result:
            mask = torch.zeros(item.shape, dtype=torch.uint8)
            if background:
                mask = mask | torch.where(item == 0, 1, 0)
            if skin:
                mask = mask | torch.where(item == 1, 1, 0)
            if nose:
                mask = mask | torch.where(item == 2, 1, 0)
            if eye_g:
                mask = mask | torch.where(item == 3, 1, 0)
            if r_eye:
                mask = mask | torch.where(item == 4, 1, 0)
            if l_eye:
                mask = mask | torch.where(item == 5, 1, 0)
            if r_brow:
                mask = mask | torch.where(item == 6, 1, 0)
            if l_brow:
                mask = mask | torch.where(item == 7, 1, 0)
            if r_ear:
                mask = mask | torch.where(item == 8, 1, 0)
            if l_ear:
                mask = mask | torch.where(item == 9, 1, 0)
            if mouth:
                mask = mask | torch.where(item == 10, 1, 0)
            if u_lip:
                mask = mask | torch.where(item == 11, 1, 0)
            if l_lip:
                mask = mask | torch.where(item == 12, 1, 0)
            if hair:
                mask = mask | torch.where(item == 13, 1, 0)
            if hat:
                mask = mask | torch.where(item == 14, 1, 0)
            if ear_r:
                mask = mask | torch.where(item == 15, 1, 0)
            if neck_l:
                mask = mask | torch.where(item == 16, 1, 0)
            if neck:
                mask = mask | torch.where(item == 17, 1, 0)
            if cloth:
                mask = mask | torch.where(item == 18, 1, 0)
            masks.append(mask.float())
        final = torch.cat(masks, dim=0).unsqueeze(0)
        return (final,)
```