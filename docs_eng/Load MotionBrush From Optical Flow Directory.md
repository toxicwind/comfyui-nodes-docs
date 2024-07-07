# Documentation
- Class name: LoadMotionBrushFromOpticalFlowDirectory
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node is capable of extracting and processing kinetic data from the optical file in the specified directory for the generation of motion brushes for further analysis and application.

# Input types
## Required
- model
    - Model parameters are essential because they define the particular algorithms or frameworks used to process light flow data and affect the accuracy and efficiency of motion brush generation.
    - Comfy dtype: DragNUWA
    - Python dtype: DragNUWA
- optical_flow_directory
    - This parameter specifies a directory containing light flow files, which is essential for positioning nodes and processing the movement data required.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MotionBrush
    - The output representative's campaign data, processed in motion brush form, can be used in a variety of applications, such as animation, video editing and effect generation.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionBrushFromOpticalFlowDirectory:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'optical_flow_directory': ('STRING', {'default': 'X://path/to/optical_flow', 'vhs_path_extensions': []})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, optical_flow_directory):
        return (model.load_motionbrush_from_optical_flow_directory(optical_flow_directory),)
```