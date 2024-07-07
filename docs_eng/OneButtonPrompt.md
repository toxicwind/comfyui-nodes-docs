# Documentation
- Class name: OneButtonPrompt
- Category: OneButtonPrompt
- Output node: False
- Repo Ref: https://github.com/AIrjen/OneButtonPrompt

The node is designed to generate dynamic tips based on various input parameters, and is designed to produce diverse and attractive outputs for content creation. It combines elements such as themes, artistic styles and environmental background to produce tips that have a cohesive and rich theme.

# Input types
## Required
- insanitylevel
    - This parameter determines the complexity and precision of generating the reminder, and a higher level will result in more detailed and subtle output. It directly affects the diversity and depth of the elements contained in the reminder.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- artist
    - Artist parameters allow for the designation of specific artistic styles or creators to guide the aesthetic and thematic direction in which the tips are generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- imagetype
    - The parameter sets out the type of image or visual expression expected, influencing the medium, style and overall visual method of generating the content.
    - Comfy dtype: COMBO
    - Python dtype: str
- subject
    - Theme parameters are critical in determining the main focus or theme that generates the reminder, affecting narratives, personalities and set-up elements.
    - Comfy dtype: COMBO
    - Python dtype: str
- imagemodechance
    - This parameter adjusts the possibility of including some image patterns in the reminder, thus affecting visual diversity and creativity.
    - Comfy dtype: INT
    - Python dtype: int
- custom_subject
    - Customized theme parameters allow the input of specific themes that users wish to focus on, ensuring that the tips generated are tailored to their interests.
    - Comfy dtype: STRING
    - Python dtype: str
- custom_outfit
    - This parameter enables the user to assign specific clothing or clothing to the subject, adding a personalized sense of the tips generated.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - The output is a reminder of an integrated and creative construction that covers input parameters and provides a rich basis for content creation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class OneButtonPrompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'insanitylevel': ('INT', {'default': 5, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'artist': (artists, {'default': 'all'}), 'imagetype': (imagetypes, {'default': 'all'}), 'imagemodechance': ('INT', {'default': 20, 'min': 1, 'max': 100, 'step': 1}), 'subject': (subjects, {'default': 'all'}), 'custom_subject': ('STRING', {'multiline': False, 'default': ''}), 'custom_outfit': ('STRING', {'multiline': False, 'default': ''}), 'subject_subtype_objects': (subjectsubtypesobject, {'default': 'all'}), 'subject_subtypes_humanoids': (subjectsubtypeshumanoid, {'default': 'all'}), 'humanoids_gender': (genders, {'default': 'all'}), 'subject_subtypes_concepts': (subjectsubtypesconcept, {'default': 'all'}), 'emojis': (emojis, {'default': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('prompt', 'prompt_g', 'prompt_l')
    FUNCTION = 'Comfy_OBP'
    CATEGORY = 'OneButtonPrompt'

    def Comfy_OBP(self, insanitylevel, custom_subject, seed, artist, imagetype, subject, imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts, emojis, custom_outfit):
        generatedpromptlist = build_dynamic_prompt(insanitylevel, subject, artist, imagetype, False, '', '', '', 1, '', custom_subject, True, '', imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts, False, emojis, seed, custom_outfit, True)
        generatedprompt = generatedpromptlist[0]
        prompt_g = generatedpromptlist[1]
        prompt_l = generatedpromptlist[2]
        return (generatedprompt, prompt_g, prompt_l)
```