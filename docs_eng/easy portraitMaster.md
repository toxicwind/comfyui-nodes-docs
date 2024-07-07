# Documentation
- Class name: portraitMaster
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The portrait Master node is designed to generate detailed portrait generation tips based on a comprehensive set of parameters. By combining properties such as facial features, emoticons and light conditions, it achieves a high degree of customization and authenticity in the output, thus encapsulating the essence of the image creation.

# Input types
## Required
- shot
    - The "shot" parameter is essential for defining the image type to be generated. It affects the image's overall configuration and frame, which is essential for capturing the aesthetics and narratives required.
    - Comfy dtype: COMBO
    - Python dtype: List[str]
## Optional
- gender
    - The “gender” parameter is essential to guide the creation of the portrait body. It helps to determine physical characteristics and emoticons that match the selected gender and helps to enhance the authenticity and credibility of the portrait.
    - Comfy dtype: COMBO
    - Python dtype: List[str]
- age
    - The "age " parameter plays an important role in determining the appearance of the portrait body. It influences facial characteristics, skin details and the rendering of other age-related properties, ensuring that the portrait accurately reflects the selected age group.
    - Comfy dtype: INT
    - Python dtype: int
- nationality_1
    - The “nationality_1” parameter, together with the “nationality_2” parameter, helps to define the cultural and ethnic background of the portrait body. This adds to the diversity and richness of the images generated, as well as to the depth and context.
    - Comfy dtype: COMBO
    - Python dtype: List[str]
- facial_expression
    - The “facial_expression” parameter is essential to convey the emotional state of the portrait subject. It guides the creation of facial features and expressions that match the selected emotions and enhances the emotional impact and narrative nature of the portrait.
    - Comfy dtype: COMBO
    - Python dtype: List[str]

# Output types
- prompt
    - The " prompt " output is a comprehensive string that integrates all input parameters into a coherent and structured format. It serves as the basis for the portrait generation process, ensuring that the desired details and nuances are captured in the final image.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - The "negative_prompt" output is a supplementary string that provides additional instructions to refine portraits. It addresses aspects that should be minimized or avoided and helps to improve the overall quality and accuracy of the image generated.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class portraitMaster:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 1.95
        prompt_path = os.path.join(RESOURCES_DIR, 'portrait_prompt.json')
        if not os.path.exists(prompt_path):
            response = urlopen('https://raw.githubusercontent.com/yolain/ComfyUI-Easy-Use/main/resources/portrait_prompt.json')
            temp_prompt = json.loads(response.read())
            prompt_serialized = json.dumps(temp_prompt, indent=4)
            with open(prompt_path, 'w') as f:
                f.write(prompt_serialized)
            del response, temp_prompt
        with open(prompt_path, 'r') as f:
            list = json.load(f)
        keys = [['shot', 'COMBO', {'key': 'shot_list'}], ['shot_weight', 'FLOAT'], ['gender', 'COMBO', {'default': 'Woman', 'key': 'gender_list'}], ['age', 'INT', {'default': 30, 'min': 18, 'max': 90, 'step': 1, 'display': 'slider'}], ['nationality_1', 'COMBO', {'default': 'Chinese', 'key': 'nationality_list'}], ['nationality_2', 'COMBO', {'key': 'nationality_list'}], ['nationality_mix', 'FLOAT'], ['body_type', 'COMBO', {'key': 'body_type_list'}], ['body_type_weight', 'FLOAT'], ['model_pose', 'COMBO', {'key': 'model_pose_list'}], ['eyes_color', 'COMBO', {'key': 'eyes_color_list'}], ['facial_expression', 'COMBO', {'key': 'face_expression_list'}], ['facial_expression_weight', 'FLOAT'], ['face_shape', 'COMBO', {'key': 'face_shape_list'}], ['face_shape_weight', 'FLOAT'], ['facial_asymmetry', 'FLOAT'], ['hair_style', 'COMBO', {'key': 'hair_style_list'}], ['hair_color', 'COMBO', {'key': 'hair_color_list'}], ['disheveled', 'FLOAT'], ['beard', 'COMBO', {'key': 'beard_list'}], ['skin_details', 'FLOAT'], ['skin_pores', 'FLOAT'], ['dimples', 'FLOAT'], ['freckles', 'FLOAT'], ['moles', 'FLOAT'], ['skin_imperfections', 'FLOAT'], ['skin_acne', 'FLOAT'], ['tanned_skin', 'FLOAT'], ['eyes_details', 'FLOAT'], ['iris_details', 'FLOAT'], ['circular_iris', 'FLOAT'], ['circular_pupil', 'FLOAT'], ['light_type', 'COMBO', {'key': 'light_type_list'}], ['light_direction', 'COMBO', {'key': 'light_direction_list'}], ['light_weight', 'FLOAT']]
        widgets = {}
        for (i, obj) in enumerate(keys):
            if obj[1] == 'COMBO':
                key = obj[2]['key'] if obj[2] and 'key' in obj[2] else obj[0]
                _list = list[key].copy()
                _list.insert(0, '-')
                widgets[obj[0]] = (_list, {**obj[2]})
            elif obj[1] == 'FLOAT':
                widgets[obj[0]] = ('FLOAT', {'default': 0, 'step': 0.05, 'min': 0, 'max': max_float_value, 'display': 'slider'})
            elif obj[1] == 'INT':
                widgets[obj[0]] = (obj[1], obj[2])
        del list
        return {'required': {**widgets, 'photorealism_improvement': (['enable', 'disable'],), 'prompt_start': ('STRING', {'multiline': True, 'default': 'raw photo, (realistic:1.5)'}), 'prompt_additional': ('STRING', {'multiline': True, 'default': ''}), 'prompt_end': ('STRING', {'multiline': True, 'default': ''}), 'negative_prompt': ('STRING', {'multiline': True, 'default': ''})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative')
    FUNCTION = 'pm'
    CATEGORY = 'EasyUse/Prompt'

    def pm(self, shot='-', shot_weight=1, gender='-', body_type='-', body_type_weight=0, eyes_color='-', facial_expression='-', facial_expression_weight=0, face_shape='-', face_shape_weight=0, nationality_1='-', nationality_2='-', nationality_mix=0.5, age=30, hair_style='-', hair_color='-', disheveled=0, dimples=0, freckles=0, skin_pores=0, skin_details=0, moles=0, skin_imperfections=0, wrinkles=0, tanned_skin=0, eyes_details=1, iris_details=1, circular_iris=1, circular_pupil=1, facial_asymmetry=0, prompt_additional='', prompt_start='', prompt_end='', light_type='-', light_direction='-', light_weight=0, negative_prompt='', photorealism_improvement='disable', beard='-', model_pose='-', skin_acne=0):
        prompt = []
        if gender == '-':
            gender = ''
        else:
            if age <= 25 and gender == 'Woman':
                gender = 'girl'
            if age <= 25 and gender == 'Man':
                gender = 'boy'
            gender = ' ' + gender + ' '
        if nationality_1 != '-' and nationality_2 != '-':
            nationality = f'[{nationality_1}:{nationality_2}:{round(nationality_mix, 2)}]'
        elif nationality_1 != '-':
            nationality = nationality_1 + ' '
        elif nationality_2 != '-':
            nationality = nationality_2 + ' '
        else:
            nationality = ''
        if prompt_start != '':
            prompt.append(f'{prompt_start}')
        if shot != '-' and shot_weight > 0:
            prompt.append(f'({shot}:{round(shot_weight, 2)})')
        prompt.append(f'({nationality}{gender}{round(age)}-years-old:1.5)')
        if body_type != '-' and body_type_weight > 0:
            prompt.append(f'({body_type}, {body_type} body:{round(body_type_weight, 2)})')
        if model_pose != '-':
            prompt.append(f'({model_pose}:1.5)')
        if eyes_color != '-':
            prompt.append(f'({eyes_color} eyes:1.25)')
        if facial_expression != '-' and facial_expression_weight > 0:
            prompt.append(f'({facial_expression}, {facial_expression} expression:{round(facial_expression_weight, 2)})')
        if face_shape != '-' and face_shape_weight > 0:
            prompt.append(f'({face_shape} shape face:{round(face_shape_weight, 2)})')
        if hair_style != '-':
            prompt.append(f'({hair_style} hairstyle:1.25)')
        if hair_color != '-':
            prompt.append(f'({hair_color} hair:1.25)')
        if beard != '-':
            prompt.append(f'({beard}:1.15)')
        if disheveled != '-' and disheveled > 0:
            prompt.append(f'(disheveled:{round(disheveled, 2)})')
        if prompt_additional != '':
            prompt.append(f'{prompt_additional}')
        if skin_details > 0:
            prompt.append(f'(skin details, skin texture:{round(skin_details, 2)})')
        if skin_pores > 0:
            prompt.append(f'(skin pores:{round(skin_pores, 2)})')
        if skin_imperfections > 0:
            prompt.append(f'(skin imperfections:{round(skin_imperfections, 2)})')
        if skin_acne > 0:
            prompt.append(f'(acne, skin with acne:{round(skin_acne, 2)})')
        if wrinkles > 0:
            prompt.append(f'(skin imperfections:{round(wrinkles, 2)})')
        if tanned_skin > 0:
            prompt.append(f'(tanned skin:{round(tanned_skin, 2)})')
        if dimples > 0:
            prompt.append(f'(dimples:{round(dimples, 2)})')
        if freckles > 0:
            prompt.append(f'(freckles:{round(freckles, 2)})')
        if moles > 0:
            prompt.append(f'(skin pores:{round(moles, 2)})')
        if eyes_details > 0:
            prompt.append(f'(eyes details:{round(eyes_details, 2)})')
        if iris_details > 0:
            prompt.append(f'(iris details:{round(iris_details, 2)})')
        if circular_iris > 0:
            prompt.append(f'(circular iris:{round(circular_iris, 2)})')
        if circular_pupil > 0:
            prompt.append(f'(circular pupil:{round(circular_pupil, 2)})')
        if facial_asymmetry > 0:
            prompt.append(f'(facial asymmetry, face asymmetry:{round(facial_asymmetry, 2)})')
        if light_type != '-' and light_weight > 0:
            if light_direction != '-':
                prompt.append(f'({light_type} {light_direction}:{round(light_weight, 2)})')
            else:
                prompt.append(f'({light_type}:{round(light_weight, 2)})')
        if prompt_end != '':
            prompt.append(f'{prompt_end}')
        prompt = ', '.join(prompt)
        prompt = prompt.lower()
        if photorealism_improvement == 'enable':
            prompt = prompt + ', (professional photo, balanced photo, balanced exposure:1.2), (film grain:1.15)'
        if photorealism_improvement == 'enable':
            negative_prompt = negative_prompt + ', (shinny skin, reflections on the skin, skin reflections:1.25)'
        log_node_info('Portrait Master as generate the prompt:', prompt)
        return (prompt, negative_prompt)
```