# Documentation
- Class name: LatentRotate
- Category: latent/transform
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentRotate node is designed to rotate the potential samples. It can handle rotational angles, such as 90, 180 or 270 degrees, and converts potential spatial data accordingly. The node plays a key role in the pre-processing phase of potential space operations, enabling the generation of a rotating version of the data for further analysis or modelling training.

# Input types
## Required
- samples
    - The'samples' parameter is essential for the operation of the node, as it represents potential spatial data that needs to be rotated. The validity of the node in converting data is directly related to the quality and format of the input sample.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- rotation
    - The 'rotation' parameter specifies the rotation angle to be applied to the potential sample. It is a key input that determines the direction of the rotating data and influences the output of the node.
    - Comfy dtype: COMBO[none, 90 degrees, 180 degrees, 270 degrees]
    - Python dtype: str

# Output types
- rotated_samples
    - The 'rotated_samples' output parameter represents potential space data after rotation. It is important because it is a direct result of node operations and contains conversion data ready for downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentRotate:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'rotation': (['none', '90 degrees', '180 degrees', '270 degrees'],)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'rotate'
    CATEGORY = 'latent/transform'

    def rotate(self, samples, rotation):
        s = samples.copy()
        rotate_by = 0
        if rotation.startswith('90'):
            rotate_by = 1
        elif rotation.startswith('180'):
            rotate_by = 2
        elif rotation.startswith('270'):
            rotate_by = 3
        s['samples'] = torch.rot90(samples['samples'], k=rotate_by, dims=[3, 2])
        return (s,)
```