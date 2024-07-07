# Documentation
- Class name: LatentKeyframeGroupNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/keyframes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

LatentKeyframameGroupNode’s load_keyframes method is designed to process and organize the potential key frames according to the index intensity provided. It takes into account both the earlier and the potential parameters available to construct a new key frame. This approach is essential in controlling the complexity of potential space operations in the network, ensuring consistency and a structured approach to the processing of the key frames.

# Input types
## Required
- index_strengths
    - The index_strengths parameter is a string that defines the distribution and strength of the potential key frame within the group. It is essential to determine how the key frame affects the potential space and is essential to the operation of the node.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prev_latent_kf
    - The prev_latent_kf parameter is an optional LatentKeyframeGroup, which provides context for the current key set. It is important to maintain continuity and consistency in potential space operations.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup
- latent_optional
    - The latent_optional parameter is an optional potential expression that can be used to further refine key frames. It plays a role in fine-tuning potential spatial adjustments.
    - Comfy dtype: LATENT
    - Python dtype: Union[Tensor, None]
- print_keyframes
    - The print_keyframes parameter is a boolean symbol that allows the log of key frame information when set to True. This is very useful for debugging and understanding nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- LATENT_KF
    - The output of the laad_keyframes method is a LatentKeyframameGroup, which covers the key frame after processing. This group is important for further downstream processing and represents structured output for node operations.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class LatentKeyframeGroupNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index_strengths': ('STRING', {'multiline': True, 'default': ''})}, 'optional': {'prev_latent_kf': ('LATENT_KEYFRAME',), 'latent_optional': ('LATENT',), 'print_keyframes': ('BOOLEAN', {'default': False})}}
    RETURN_NAMES = ('LATENT_KF',)
    RETURN_TYPES = ('LATENT_KEYFRAME',)
    FUNCTION = 'load_keyframes'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/keyframes'

    def validate_index(self, index: int, latent_count: int=0, is_range: bool=False, allow_negative=False) -> int:
        if is_range:
            return index
        if latent_count > 0 and index > latent_count - 1:
            raise IndexError(f"Index '{index}' out of range for the total {latent_count} latents.")
        if index < 0:
            if not allow_negative:
                raise IndexError(f'Negative indeces not allowed, but was {index}.')
            conv_index = latent_count + index
            if conv_index < 0:
                raise IndexError(f"Index '{index}', converted to '{conv_index}' out of range for the total {latent_count} latents.")
            index = conv_index
        return index

    def convert_to_index_int(self, raw_index: str, latent_count: int=0, is_range: bool=False, allow_negative=False) -> int:
        try:
            return self.validate_index(int(raw_index), latent_count=latent_count, is_range=is_range, allow_negative=allow_negative)
        except ValueError as e:
            raise ValueError(f"index '{raw_index}' must be an integer.", e)

    def convert_to_latent_keyframes(self, latent_indeces: str, latent_count: int) -> set[LatentKeyframe]:
        if not latent_indeces:
            return set()
        int_latent_indeces = [i for i in range(0, latent_count)]
        allow_negative = latent_count > 0
        chosen_indeces = set()
        groups = latent_indeces.split(',')
        groups = [g.strip() for g in groups]
        for g in groups:
            strength = 1.0
            if '=' in g:
                (g, strength_str) = g.split('=', 1)
                g = g.strip()
                try:
                    strength = float(strength_str.strip())
                except ValueError as e:
                    raise ValueError(f"strength '{strength_str}' must be a float.", e)
                if strength < 0:
                    raise ValueError(f"Strength '{strength}' cannot be negative.")
            if ':' in g:
                index_range = g.split(':', 1)
                index_range = [r.strip() for r in index_range]
                start_index = self.convert_to_index_int(index_range[0], latent_count=latent_count, is_range=True, allow_negative=allow_negative)
                end_index = self.convert_to_index_int(index_range[1], latent_count=latent_count, is_range=True, allow_negative=allow_negative)
                if len(int_latent_indeces) > 0:
                    for i in int_latent_indeces[start_index:end_index]:
                        chosen_indeces.add(LatentKeyframe(i, strength))
                else:
                    for i in range(start_index, end_index):
                        chosen_indeces.add(LatentKeyframe(i, strength))
            else:
                chosen_indeces.add(LatentKeyframe(self.convert_to_index_int(g, latent_count=latent_count, allow_negative=allow_negative), strength))
        return chosen_indeces

    def load_keyframes(self, index_strengths: str, prev_latent_kf: LatentKeyframeGroup=None, prev_latent_keyframe: LatentKeyframeGroup=None, latent_image_opt=None, print_keyframes=False):
        prev_latent_keyframe = prev_latent_keyframe if prev_latent_keyframe else prev_latent_kf
        if not prev_latent_keyframe:
            prev_latent_keyframe = LatentKeyframeGroup()
        else:
            prev_latent_keyframe = prev_latent_keyframe.clone()
        curr_latent_keyframe = LatentKeyframeGroup()
        latent_count = -1
        if latent_image_opt:
            latent_count = latent_image_opt['samples'].size()[0]
        latent_keyframes = self.convert_to_latent_keyframes(index_strengths, latent_count=latent_count)
        for latent_keyframe in latent_keyframes:
            curr_latent_keyframe.add(latent_keyframe)
        if print_keyframes:
            for keyframe in curr_latent_keyframe.keyframes:
                logger.info(f'keyframe {keyframe.batch_index}:{keyframe.strength}')
        for latent_keyframe in prev_latent_keyframe.keyframes:
            curr_latent_keyframe.add(latent_keyframe)
        return (curr_latent_keyframe,)
```