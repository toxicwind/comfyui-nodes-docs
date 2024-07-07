# Documentation
- Class name: SparseCtrlMergedLoaderAdvanced
- Category: Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl/experimental
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

SparseCtrlMergedLoaderAdvanced is designed to efficiently manage and load an advanced control network with rare control features. It integrates motion properties into the control network, allowing dynamic and self-adaptation control based on motion intensity and size parameters. This node is essential for applications requiring fine control of complex systems, ensuring seamless integration of movement and control to improve performance.

# Input types
## Required
- sparsectrl_name
    - The parameter'sparsectrl_name' specifies the name of the rare control model that you want to load, which is essential for identifying and accessing the correct control settings. This parameter is essential for the operation of the node, as it directly affects the control capabilities of the application.
    - Comfy dtype: str
    - Python dtype: str
- control_net_name
    - The parameter 'control_net_name' is used to define the name of the control network model. It plays an important role in the function of the node because it determines the specific control network to be used and affects the control strategy as a whole.
    - Comfy dtype: str
    - Python dtype: str
- use_motion
    - The parameter 'use_motion'indicates whether motor properties should be incorporated into the control network. This is an important parameter because it enables or disables dynamic adaptation of movement-based controls, leading to different control behaviours.
    - Comfy dtype: bool
    - Python dtype: bool
- motion_strength
    - Parameter'motion_strength' adjusts the intensity of the control effect within the network. This is a key parameter that allows users to fine-tune the effect of the control results and customizes the control response.
    - Comfy dtype: float
    - Python dtype: float
- motion_scale
    - The parameter'motion_scale' is defined as the size of the movement's effects to control the network. It is an influential parameter that changes the scope of the movement's integration and affects overall control dynamics.
    - Comfy dtype: float
    - Python dtype: float
## Optional
- sparse_method
    - The parameter'sparse_method' selects the method of handling diluted data within the control network. Although it is optional, it can significantly influence the processing of diluted data and may change the performance of nodes.
    - Comfy dtype: SPARSE_METHOD
    - Python dtype: SparseMethod
- tk_optional
    - The 'tk_optional' parameter is provided to provide additional control of the time-step key frame in the control network. This optional parameter can be used to specify a particular key frame to achieve more fine particle size control.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: TimestepKeyframeGroup

# Output types
- CONTROL_NET
    - Output 'CONTROL_NET' means the installed control network with integrated motion properties. It is a complex data structure, which covers control settings and movement parameters and is prepared to be applied in a higher control system.
    - Comfy dtype: CONTROL_NET
    - Python dtype: ControlNetAdvanced

# Usage tips
- Infra type: GPU

# Source code
```
class SparseCtrlMergedLoaderAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sparsectrl_name': (folder_paths.get_filename_list('controlnet'),), 'control_net_name': (folder_paths.get_filename_list('controlnet'),), 'use_motion': ('BOOLEAN', {'default': True}), 'motion_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'motion_scale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'sparse_method': ('SPARSE_METHOD',), 'tk_optional': ('TIMESTEP_KEYFRAME',)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl/experimental'

    def load_controlnet(self, sparsectrl_name: str, control_net_name: str, use_motion: bool, motion_strength: float, motion_scale: float, sparse_method: SparseMethod=SparseSpreadMethod(), tk_optional: TimestepKeyframeGroup=None):
        sparsectrl_path = folder_paths.get_full_path('controlnet', sparsectrl_name)
        controlnet_path = folder_paths.get_full_path('controlnet', control_net_name)
        sparse_settings = SparseSettings(sparse_method=sparse_method, use_motion=use_motion, motion_strength=motion_strength, motion_scale=motion_scale, merged=True)
        controlnet = load_controlnet(controlnet_path, timestep_keyframe=tk_optional)
        if controlnet is None or type(controlnet) != ControlNetAdvanced:
            raise ValueError(f'controlnet_path must point to a normal ControlNet, but instead: {type(controlnet).__name__}')
        sparsectrl = load_sparsectrl(sparsectrl_path, timestep_keyframe=tk_optional, sparse_settings=SparseSettings.default())
        new_state_dict = controlnet.control_model.state_dict()
        for (key, value) in sparsectrl.control_model.motion_holder.motion_wrapper.state_dict().items():
            new_state_dict[key] = value
        sparsectrl = load_sparsectrl(sparsectrl_path, controlnet_data=new_state_dict, timestep_keyframe=tk_optional, sparse_settings=sparse_settings)
        return (sparsectrl,)
```