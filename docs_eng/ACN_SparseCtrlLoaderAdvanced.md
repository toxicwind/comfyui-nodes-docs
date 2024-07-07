# Documentation
- Class name: SparseCtrlLoaderAdvanced
- Category: Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

SparseCtrlLoaderAdvanced is designed to efficiently load and manage a high-level control network with thin control capabilities. It abstracts the complexity of processing thin control data, enabling users to integrate motion features seamlessly into their control network. It streamlines the process of loading control networks using thin control methods, enhancing the overall performance and functionality of the system.

# Input types
## Required
- sparsectrl_name
    - The sparsectrl_name parameter is essential to identify the specific control network that you want to load. It influences the execution of the node by determining which control network data you want to access and process.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- use_motion
    - Use_motion parameters to decide whether to include motion properties in the control network. It plays an important role in the function of the node by enabling or disableing the control network.
    - Comfy dtype: bool
    - Python dtype: bool
- motion_strength
    - Motion_strength parameters adjust the intensity of the control of motion properties within the network. It is important to fine-tune the effect of motion on the control of the final output of the network.
    - Comfy dtype: float
    - Python dtype: float
- motion_scale
    - The motion_scale parameter adjusts the movement effects in the control network. It is essential to control the extent to which the movement affects network behaviour.
    - Comfy dtype: float
    - Python dtype: float
- sparse_method
    - The sparse_method parameter defines the method of processing dilution control data within the control network. It is essential to determine the strategy for processing and integrating dilution data.
    - Comfy dtype: SparseMethod
    - Python dtype: SparseMethod
- tk_optional
    - The tk_optional parameter provides a way to assign an optional time-step key frame to control the network. This is important for users who need to customize the time-specific features of the network.
    - Comfy dtype: TimestepKeyframeGroup
    - Python dtype: TimestepKeyframeGroup

# Output types
- CONTROL_NET
    - The CONTROL_NET output represents the loaded high-level control network, which combines the specified dilution control settings and motion features. It is important because it is the main output of nodes and allows further processing and use in the system.
    - Comfy dtype: ControlNetAdvanced
    - Python dtype: ControlNetAdvanced

# Usage tips
- Infra type: GPU

# Source code
```
class SparseCtrlLoaderAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sparsectrl_name': (folder_paths.get_filename_list('controlnet'),), 'use_motion': ('BOOLEAN', {'default': True}), 'motion_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'motion_scale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'sparse_method': ('SPARSE_METHOD',), 'tk_optional': ('TIMESTEP_KEYFRAME',)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl'

    def load_controlnet(self, sparsectrl_name: str, use_motion: bool, motion_strength: float, motion_scale: float, sparse_method: SparseMethod=SparseSpreadMethod(), tk_optional: TimestepKeyframeGroup=None):
        sparsectrl_path = folder_paths.get_full_path('controlnet', sparsectrl_name)
        sparse_settings = SparseSettings(sparse_method=sparse_method, use_motion=use_motion, motion_strength=motion_strength, motion_scale=motion_scale)
        sparsectrl = load_sparsectrl(sparsectrl_path, timestep_keyframe=tk_optional, sparse_settings=sparse_settings)
        return (sparsectrl,)
```