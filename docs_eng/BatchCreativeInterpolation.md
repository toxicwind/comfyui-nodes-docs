# Documentation
- Class name: BatchCreativeInterpolationNode
- Category: Steerable-Motion
- Output node: False
- Repo Ref: https://github.com/banodoco/steerable-motion

BattCreative Interpolation Node is designed to perform creative plugs for a group of images. It uses a variety of parameters to control the distribution of frames, key frame effects and intensity values during the plug-in process. This node is particularly suitable for creating smooth transitions between different image states, and it provides a high degree of control over the final output, making it applicable to a wide range of creative applications.

# Input types
## Required
- positive
    - The positive condition image is a key input that affects the direction and style of the plug value.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- negative
    - The negative condition image is used to limit or direct the plug value to the opposite direction of the positive image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- images
    - Enter the image that will be plugged in. This parameter is vital because it defines what is to be converted.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- model
    - Models for the plug-in process. They are essential for generating consistent conversions.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The IPA adaptor is used to apply specific conversions or styles to images during the plug-in.
    - Comfy dtype: IPADAPTER
    - Python dtype: dict
- clip_vision
    - The CLIP Vision model is used to analyse and process images in a way that supports plugs.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.nn.Module
- type_of_frame_distribution
    - The frame distribution method for determining the plug value may be linear or dynamic.
    - Comfy dtype: COMBO[linear, dynamic]
    - Python dtype: str
- type_of_key_frame_influence
    - Specifies whether the impact of the key frame is linear or follows a dynamic pattern.
    - Comfy dtype: COMBO[linear, dynamic]
    - Python dtype: str
- type_of_strength_distribution
    - Indicates the type of intensity distribution of the plug value, which may be linear or dynamic.
    - Comfy dtype: COMBO[linear, dynamic]
    - Python dtype: str
## Optional
- linear_frame_distribution_value
    - Values for linear frame distribution. Only relevant if the frame distribution type is set to 'linear'.
    - Comfy dtype: INT
    - Python dtype: int
- dynamic_frame_distribution_values
    - Defines the comma separated value string for the dynamic frame distribution. If the frame distribution type is 'dynamic', this parameter is required.
    - Comfy dtype: STRING
    - Python dtype: str
- linear_key_frame_influence_value
    - Determines the value of the key frame linear effect. If the key frame impact type is 'linear', it applies.
    - Comfy dtype: STRING
    - Python dtype: str
- dynamic_key_frame_influence_values
    - Strings that indicate the dynamic impact values of the key frame, when the key frame impact type is `dynamic'.
    - Comfy dtype: STRING
    - Python dtype: str
- linear_strength_value
    - If you select a linear intensity distribution, the linear strength value for the plug value is selected.
    - Comfy dtype: STRING
    - Python dtype: str
- dynamic_strength_values
    - Defines the comma separator string for the dynamic intensity distribution of the frame.
    - Comfy dtype: STRING
    - Python dtype: str
- buffer
    - The buffer value adds a fill to the key frame position, affecting the range of the plug value.
    - Comfy dtype: INT
    - Python dtype: int
- high_detail_mode
    - When enabled, the high detail mode adjusts the IPA settings to obtain more detailed and refined plugs.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- base_ipa_advanced_settings
    - Advanced settings for basic IPA applications, allowing fine-tuning of the plug-in process.
    - Comfy dtype: ADVANCED_IPA_SETTINGS
    - Python dtype: dict
- detail_ipa_advanced_settings
    - Advanced settings for detailed IPA applications, used in high detail mode.
    - Comfy dtype: ADVANCED_IPA_SETTINGS
    - Python dtype: dict

# Output types
- GRAPH
    - The comparison of weights applied during GRAPH output visualization plug-in provides insight into how different frames are affected.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- POSITIVE
    - POSITIVE output reflects the positive conditions used in the plug value and captures the direction of the process.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- NEGATIVE
    - NEGATIVE output represents a negative condition that limits the plug value in the desired manner.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- MODEL
    - MODEL output is a modified model with plug-in values and contains creative conversions applied to input images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- KEYFRAME_POSITIONS
    - The KEYFRAME_POSITIONS output provides a thin indexing method for plug-in, detailing the location of the key frame.
    - Comfy dtype: SPARSE_METHOD
    - Python dtype: SparseIndexMethodImport
- BATCH_SIZE
    - The BATCH_SIZE output indicates the volume of batches to be processed during the plug value, reflecting the number of images converted.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: GPU

# Source code
```
class BatchCreativeInterpolationNode:

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'images': ('IMAGE',), 'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'clip_vision': ('CLIP_VISION',), 'type_of_frame_distribution': (['linear', 'dynamic'],), 'linear_frame_distribution_value': ('INT', {'default': 16, 'min': 4, 'max': 64, 'step': 1}), 'dynamic_frame_distribution_values': ('STRING', {'multiline': True, 'default': '0,10,26,40'}), 'type_of_key_frame_influence': (['linear', 'dynamic'],), 'linear_key_frame_influence_value': ('STRING', {'multiline': False, 'default': '(1.0,1.0)'}), 'dynamic_key_frame_influence_values': ('STRING', {'multiline': True, 'default': '(1.0,1.0),(1.0,1.5)(1.0,0.5)'}), 'type_of_strength_distribution': (['linear', 'dynamic'],), 'linear_strength_value': ('STRING', {'multiline': False, 'default': '(0.3,0.4)'}), 'dynamic_strength_values': ('STRING', {'multiline': True, 'default': '(0.0,1.0),(0.0,1.0),(0.0,1.0),(0.0,1.0)'}), 'buffer': ('INT', {'default': 4, 'min': 1, 'max': 16, 'step': 1}), 'high_detail_mode': ('BOOLEAN', {'default': True})}, 'optional': {'base_ipa_advanced_settings': ('ADVANCED_IPA_SETTINGS',), 'detail_ipa_advanced_settings': ('ADVANCED_IPA_SETTINGS',)}}
    RETURN_TYPES = ('IMAGE', 'CONDITIONING', 'CONDITIONING', 'MODEL', 'SPARSE_METHOD', 'INT')
    RETURN_NAMES = ('GRAPH', 'POSITIVE', 'NEGATIVE', 'MODEL', 'KEYFRAME_POSITIONS', 'BATCH_SIZE')
    FUNCTION = 'combined_function'
    CATEGORY = 'Steerable-Motion'

    def combined_function(self, positive, negative, images, model, ipadapter, clip_vision, type_of_frame_distribution, linear_frame_distribution_value, dynamic_frame_distribution_values, type_of_key_frame_influence, linear_key_frame_influence_value, dynamic_key_frame_influence_values, type_of_strength_distribution, linear_strength_value, dynamic_strength_values, buffer, high_detail_mode, base_ipa_advanced_settings=None, detail_ipa_advanced_settings=None):

        def get_keyframe_positions(type_of_frame_distribution, dynamic_frame_distribution_values, images, linear_frame_distribution_value):
            if type_of_frame_distribution == 'dynamic':
                if isinstance(dynamic_frame_distribution_values, str):
                    return sorted([int(kf.strip()) for kf in dynamic_frame_distribution_values.split(',')])
                elif isinstance(dynamic_frame_distribution_values, list):
                    return sorted(dynamic_frame_distribution_values)
            else:
                return [i * linear_frame_distribution_value for i in range(len(images))]

        def create_mask_batch(last_key_frame_position, weights, frames):
            (width, height) = (512, 512)
            frame_to_weight = {frame: weights[i] for (i, frame) in enumerate(frames)}
            masks = []
            for frame_number in range(last_key_frame_position):
                strength = frame_to_weight.get(frame_number, 0.0)
                mask = torch.full((height, width), strength)
                masks.append(mask)
            masks_tensor = torch.stack(masks, dim=0)
            return masks_tensor

        def plot_weight_comparison(cn_frame_numbers, cn_weights, ipadapter_frame_numbers, ipadapter_weights, buffer):
            plt.figure(figsize=(12, 8))
            colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
            cn_frame_numbers = cn_frame_numbers if cn_frame_numbers is not None else []
            cn_weights = cn_weights if cn_weights is not None else []
            ipadapter_frame_numbers = ipadapter_frame_numbers if ipadapter_frame_numbers is not None else []
            ipadapter_weights = ipadapter_weights if ipadapter_weights is not None else []
            max_length = max(len(cn_frame_numbers), len(ipadapter_frame_numbers))
            label_counter = 1 if buffer < 0 else 0
            for i in range(max_length):
                if i < len(cn_frame_numbers):
                    label = 'cn_strength_buffer' if i == 0 and buffer > 0 else f'cn_strength_{label_counter}'
                    plt.plot(cn_frame_numbers[i], cn_weights[i], marker='o', color=colors[i % len(colors)], label=label)
                if i < len(ipadapter_frame_numbers):
                    label = 'ipa_strength_buffer' if i == 0 and buffer > 0 else f'ipa_strength_{label_counter}'
                    plt.plot(ipadapter_frame_numbers[i], ipadapter_weights[i], marker='x', linestyle='--', color=colors[i % len(colors)], label=label)
                if label_counter == 0 or buffer < 0 or i > 0:
                    label_counter += 1
            plt.legend()
            all_weights = cn_weights + ipadapter_weights
            max_weight = max((max(sublist) for sublist in all_weights if sublist)) * 1.5
            plt.ylim(0, max_weight)
            buffer_io = BytesIO()
            plt.savefig(buffer_io, format='png', bbox_inches='tight')
            plt.close()
            buffer_io.seek(0)
            img = Image.open(buffer_io)
            img_tensor = transforms.ToTensor()(img)
            img_tensor = img_tensor.unsqueeze(0)
            img_tensor = img_tensor.permute([0, 2, 3, 1])
            return (img_tensor,)

        def extract_strength_values(type_of_key_frame_influence, dynamic_key_frame_influence_values, keyframe_positions, linear_key_frame_influence_value):
            if type_of_key_frame_influence == 'dynamic':
                if isinstance(dynamic_key_frame_influence_values, str):
                    dynamic_values = eval(dynamic_key_frame_influence_values)
                else:
                    dynamic_values = dynamic_key_frame_influence_values
                dynamic_values_corrected = []
                for value in dynamic_values:
                    if len(value) == 2:
                        value = (value[0], value[1], value[0])
                    dynamic_values_corrected.append(value)
                return dynamic_values_corrected
            else:
                if len(linear_key_frame_influence_value) == 2:
                    linear_key_frame_influence_value = (linear_key_frame_influence_value[0], linear_key_frame_influence_value[1], linear_key_frame_influence_value[0])
                return [linear_key_frame_influence_value for _ in range(len(keyframe_positions) - 1)]

        def extract_influence_values(type_of_key_frame_influence, dynamic_key_frame_influence_values, keyframe_positions, linear_key_frame_influence_value):
            if isinstance(linear_key_frame_influence_value, str) and linear_key_frame_influence_value[0] == '(':
                linear_key_frame_influence_value = eval(linear_key_frame_influence_value)
            if not isinstance(linear_key_frame_influence_value, tuple):
                if isinstance(linear_key_frame_influence_value, (float, str)):
                    try:
                        value = float(linear_key_frame_influence_value)
                        linear_key_frame_influence_value = (value, value)
                    except ValueError:
                        raise ValueError('linear_key_frame_influence_value must be a float or a string representing a float')
            number_of_outputs = len(keyframe_positions) - 1
            if type_of_key_frame_influence == 'dynamic':
                if all((isinstance(x, float) for x in dynamic_key_frame_influence_values)):
                    dynamic_values = [(value, value) for value in dynamic_key_frame_influence_values]
                elif isinstance(dynamic_key_frame_influence_values[0], str) and dynamic_key_frame_influence_values[0] == '(':
                    string_representation = ''.join(dynamic_key_frame_influence_values)
                    dynamic_values = eval(f'[{string_representation}]')
                else:
                    dynamic_values = dynamic_key_frame_influence_values if isinstance(dynamic_key_frame_influence_values, list) else [dynamic_key_frame_influence_values]
                return dynamic_values[:number_of_outputs]
            else:
                return [linear_key_frame_influence_value for _ in range(number_of_outputs)]

        def calculate_weights(batch_index_from, batch_index_to, strength_from, strength_to, interpolation, revert_direction_at_midpoint, last_key_frame_position, i, number_of_items, buffer):
            range_start = batch_index_from
            range_end = batch_index_to
            if i == number_of_items - 1:
                range_end = last_key_frame_position
            steps = range_end - range_start
            diff = strength_to - strength_from
            index = np.linspace(0, 1, steps // 2 + 1) if revert_direction_at_midpoint else np.linspace(0, 1, steps)
            if interpolation == 'linear':
                weights = np.linspace(strength_from, strength_to, len(index))
            elif interpolation == 'ease-in':
                weights = diff * np.power(index, 2) + strength_from
            elif interpolation == 'ease-out':
                weights = diff * (1 - np.power(1 - index, 2)) + strength_from
            elif interpolation == 'ease-in-out':
                weights = diff * ((1 - np.cos(index * np.pi)) / 2) + strength_from
            if revert_direction_at_midpoint:
                weights = np.concatenate([weights, weights[::-1]])
            frame_numbers = np.arange(range_start, range_start + len(weights))
            if range_start < 0 and i > 0:
                drop_count = abs(range_start)
                weights = weights[drop_count:]
                frame_numbers = frame_numbers[drop_count:]
            if range_end > last_key_frame_position and i < number_of_items - 1:
                drop_count = range_end - last_key_frame_position
                weights = weights[:-drop_count]
                frame_numbers = frame_numbers[:-drop_count]
            return (weights, frame_numbers)

        def process_weights(frame_numbers, weights, multiplier):
            adjusted_weights = [min(max(weight * multiplier, 0.0), 1.0) for weight in weights]
            filtered_frames_and_weights = [(frame, weight) for (frame, weight) in zip(frame_numbers, adjusted_weights) if weight > 0.0]
            (filtered_frame_numbers, filtered_weights) = zip(*filtered_frames_and_weights) if filtered_frames_and_weights else ([], [])
            return (list(filtered_frame_numbers), list(filtered_weights))

        def calculate_influence_frame_number(key_frame_position, next_key_frame_position, distance):
            key_frame_distance = abs(next_key_frame_position - key_frame_position)
            extended_distance = key_frame_distance * distance
            if key_frame_position < next_key_frame_position:
                influence_frame_number = key_frame_position + extended_distance
            else:
                influence_frame_number = key_frame_position - extended_distance
            return round(influence_frame_number)
        keyframe_positions = get_keyframe_positions(type_of_frame_distribution, dynamic_frame_distribution_values, images, linear_frame_distribution_value)
        shifted_keyframes_position = [position + buffer - 2 for position in keyframe_positions]
        shifted_keyframe_positions_string = ','.join((str(pos) for pos in shifted_keyframes_position))
        sparseindexmethod = SparseIndexMethodNodeImport()
        (sparse_indexes,) = sparseindexmethod.get_method(shifted_keyframe_positions_string)
        if buffer > 0:
            keyframe_positions = [position + buffer - 1 for position in keyframe_positions]
            keyframe_positions.insert(0, 0)
            last_position_with_buffer = keyframe_positions[-1] + buffer - 1
            keyframe_positions.append(last_position_with_buffer)
        if base_ipa_advanced_settings is None:
            if high_detail_mode:
                base_ipa_advanced_settings = {'ipa_starts_at': 0.0, 'ipa_ends_at': 0.3, 'ipa_weight_type': 'ease in-out', 'ipa_weight': 1.0, 'ipa_embeds_scaling': 'V only', 'ipa_noise_strength': 0.0, 'use_image_for_noise': False, 'type_of_noise': 'fade', 'noise_blur': 0}
            else:
                base_ipa_advanced_settings = {'ipa_starts_at': 0.0, 'ipa_ends_at': 0.75, 'ipa_weight_type': 'ease in-out', 'ipa_weight': 1.0, 'ipa_embeds_scaling': 'V only', 'ipa_noise_strength': 0.0, 'use_image_for_noise': False, 'type_of_noise': 'fade', 'noise_blur': 0}
        if detail_ipa_advanced_settings is None:
            if high_detail_mode:
                detail_ipa_advanced_settings = {'ipa_starts_at': 0.25, 'ipa_ends_at': 0.75, 'ipa_weight_type': 'ease in-out', 'ipa_weight': 1.0, 'ipa_embeds_scaling': 'V only', 'ipa_noise_strength': 0.0, 'use_image_for_noise': False, 'type_of_noise': 'fade', 'noise_blur': 0}
        strength_values = extract_strength_values(type_of_strength_distribution, dynamic_strength_values, keyframe_positions, linear_strength_value)
        strength_values = [literal_eval(val) if isinstance(val, str) else val for val in strength_values]
        corrected_strength_values = []
        for val in strength_values:
            if len(val) == 2:
                val = (val[0], val[1], val[0])
            corrected_strength_values.append(val)
        strength_values = corrected_strength_values
        key_frame_influence_values = extract_influence_values(type_of_key_frame_influence, dynamic_key_frame_influence_values, keyframe_positions, linear_key_frame_influence_value)
        key_frame_influence_values = [literal_eval(val) if isinstance(val, str) else val for val in key_frame_influence_values]
        last_key_frame_position = keyframe_positions[-1] + 1
        all_cn_frame_numbers = []
        all_cn_weights = []
        all_ipa_weights = []
        all_ipa_frame_numbers = []
        for i in range(len(keyframe_positions)):
            keyframe_position = keyframe_positions[i]
            interpolation = 'ease-in-out'
            if i == 0:
                image = images[0]
                strength_from = strength_to = strength_values[0][1]
                batch_index_from = 0
                batch_index_to_excl = buffer
                (weights, frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, strength_from, strength_to, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
            elif i == 1:
                image = images[i - 1]
                (key_frame_influence_from, key_frame_influence_to) = key_frame_influence_values[i - 1]
                (start_strength, mid_strength, end_strength) = strength_values[i - 1]
                keyframe_position = keyframe_positions[i]
                next_key_frame_position = keyframe_positions[i + 1]
                batch_index_from = keyframe_position
                batch_index_to_excl = calculate_influence_frame_number(keyframe_position, next_key_frame_position, key_frame_influence_to)
                (weights, frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, mid_strength, end_strength, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
            elif i == len(keyframe_positions) - 2:
                image = images[i - 1]
                (key_frame_influence_from, key_frame_influence_to) = key_frame_influence_values[i - 1]
                (start_strength, mid_strength, end_strength) = strength_values[i - 1]
                keyframe_position = keyframe_positions[i]
                previous_key_frame_position = keyframe_positions[i - 1]
                batch_index_from = calculate_influence_frame_number(keyframe_position, previous_key_frame_position, key_frame_influence_from)
                batch_index_to_excl = keyframe_position
                (weights, frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, start_strength, mid_strength, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
            elif i == len(keyframe_positions) - 1:
                image = images[i - 2]
                strength_from = strength_to = strength_values[i - 2][1]
                batch_index_from = keyframe_positions[i - 1]
                batch_index_to_excl = last_key_frame_position
                (weights, frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, strength_from, strength_to, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
            else:
                image = images[i - 1]
                (key_frame_influence_from, key_frame_influence_to) = key_frame_influence_values[i - 1]
                (start_strength, mid_strength, end_strength) = strength_values[i - 1]
                keyframe_position = keyframe_positions[i]
                previous_key_frame_position = keyframe_positions[i - 1]
                batch_index_from = calculate_influence_frame_number(keyframe_position, previous_key_frame_position, key_frame_influence_from)
                batch_index_to_excl = keyframe_position
                (first_half_weights, first_half_frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, start_strength, mid_strength, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
                next_key_frame_position = keyframe_positions[i + 1]
                batch_index_from = keyframe_position
                batch_index_to_excl = calculate_influence_frame_number(keyframe_position, next_key_frame_position, key_frame_influence_to)
                (second_half_weights, second_half_frame_numbers) = calculate_weights(batch_index_from, batch_index_to_excl, mid_strength, end_strength, interpolation, False, last_key_frame_position, i, len(keyframe_positions), buffer)
                weights = np.concatenate([first_half_weights, second_half_weights])
                frame_numbers = np.concatenate([first_half_frame_numbers, second_half_frame_numbers])
            (ipa_frame_numbers, ipa_weights) = process_weights(frame_numbers, weights, 1.0)
            prepare_for_clip_vision = PrepImageForClipVisionImport()
            (prepped_image,) = prepare_for_clip_vision.prep_image(image=image.unsqueeze(0), interpolation='LANCZOS', crop_position='pad', sharpening=0.1)
            mask = create_mask_batch(last_key_frame_position, ipa_weights, ipa_frame_numbers)
            if base_ipa_advanced_settings['ipa_noise_strength'] > 0:
                if base_ipa_advanced_settings['use_image_for_noise']:
                    noise_image = prepped_image
                else:
                    noise_image = None
                ipa_noise = IPAdapterNoiseImport()
                (negative_noise,) = ipa_noise.make_noise(type=base_ipa_advanced_settings['type_of_noise'], strength=base_ipa_advanced_settings['ipa_noise_strength'], blur=base_ipa_advanced_settings['noise_blur'], image_optional=noise_image)
            else:
                negative_noise = None
            ipadapter_application = IPAdapterAdvancedImport()
            (model,) = ipadapter_application.apply_ipadapter(model=model, ipadapter=ipadapter, image=prepped_image, weight=base_ipa_advanced_settings['ipa_weight'], weight_type=base_ipa_advanced_settings['ipa_weight_type'], start_at=base_ipa_advanced_settings['ipa_starts_at'], end_at=base_ipa_advanced_settings['ipa_ends_at'], clip_vision=clip_vision, attn_mask=mask, image_negative=negative_noise, embeds_scaling=base_ipa_advanced_settings['ipa_embeds_scaling'])
            if high_detail_mode:
                if detail_ipa_advanced_settings['ipa_noise_strength'] > 0:
                    if detail_ipa_advanced_settings['use_image_for_noise']:
                        noise_image = image.unsqueeze(0)
                    else:
                        noise_image = None
                    ipa_noise = IPAdapterNoiseImport()
                    (negative_noise,) = ipa_noise.make_noise(type=detail_ipa_advanced_settings['type_of_noise'], strength=detail_ipa_advanced_settings['ipa_noise_strength'], blur=detail_ipa_advanced_settings['noise_blur'], image_optional=noise_image)
                else:
                    negative_noise = None
                tiled_ipa_application = IPAdapterTiledImport()
                (model, *_) = tiled_ipa_application.apply_tiled(model=model, ipadapter=ipadapter, image=image.unsqueeze(0), weight=detail_ipa_advanced_settings['ipa_weight'], weight_type=detail_ipa_advanced_settings['ipa_weight_type'], start_at=detail_ipa_advanced_settings['ipa_starts_at'], end_at=detail_ipa_advanced_settings['ipa_ends_at'], clip_vision=clip_vision, attn_mask=mask, sharpening=0.1, image_negative=negative_noise, embeds_scaling=detail_ipa_advanced_settings['ipa_embeds_scaling'])
            all_ipa_frame_numbers.append(ipa_frame_numbers)
            all_ipa_weights.append(ipa_weights)
        (comparison_diagram,) = plot_weight_comparison(all_cn_frame_numbers, all_cn_weights, all_ipa_frame_numbers, all_ipa_weights, buffer)
        return (comparison_diagram, positive, negative, model, sparse_indexes, last_key_frame_position)
```