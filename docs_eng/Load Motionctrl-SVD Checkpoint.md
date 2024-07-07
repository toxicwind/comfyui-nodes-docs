# Documentation
- Class name: MotionctrlSVDLoader
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl-SVD.git

The MotionctrlSVDLoader class is a key component of the initialization and management of the Motionctrl-SVD model, focusing on efficient loading and preparation of the model for implementation. It encapsulates the search check points and the process of configuring the model according to the specified parameters, ensuring that the model is ready for motion sequence analysis and synthesis tasks.

# Input types
## Required
- ckpt_name
    - The ckpt_name parameter is essential to specify the check-point filename for the Motionctrl-SVD model. It guides the loader to use the correct model state, which is essential for subsequent model operations and results.
    - Comfy dtype: STRING
    - Python dtype: str
- frame_length
    - The frame_legth parameter is important because it defines the time dimensions of the model input data. It affects the ability of the model to process and generate a coherent sequence of motion within the frame range.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameter is essential to determine the number of overlaps that the model will perform during its operation. It directly affects the computational efficiency and the quality of the sequence of movements generated.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - The output model represents the loaded and configured Motionctrl-SVD, which is prepared for motion sequence analysis and synthesis. It is the crystallization of the input parameters and loader function, and it encapsulates the model for further use.
    - Comfy dtype: MOTIONCTRLSVD
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class MotionctrlSVDLoader:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'ckpt_name': (['motionctrl_svd.ckpt'], {'default': 'motionctrl_svd.ckpt'}), 'frame_length': ('INT', {'default': 14}), 'steps': ('INT', {'default': 25})}}
    RETURN_TYPES = ('MOTIONCTRLSVD',)
    RETURN_NAMES = ('model',)
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'motionctrl'

    def load_checkpoint(self, ckpt_name, frame_length, steps):
        global device
        comfy_path = os.path.dirname(folder_paths.__file__)
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        config_path = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl-SVD/configs/inference/config_motionctrl_cmcm.yaml')
        if not os.path.exists(ckpt_path):
            os.system(f'wget https://huggingface.co/TencentARC/MotionCtrl/resolve/main/motionctrl_svd.ckpt?download=true -P .')
            os.system(f'mv motionctrl_svd.ckpt?download=true {ckpt_path}')
        model = build_model(config_path, ckpt_path, device, frame_length, steps)
        return (model,)
```