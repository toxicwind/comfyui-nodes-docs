# Documentation
- Class name: MotionctrlLoader
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl.git

The MotionctrlLoader class is designed to efficiently manage and load motion control check points for advanced motion analysis and generation tasks. It abstractes the complexity of loading and initializing motion control models and provides a simplified interface for users to take advantage of motion control functions.

# Input types
## Required
- ckpt_name
    - The name of the check point is a key parameter that specifies the model check point that you want to load. This is essential to determine the weight and structure of the correct pre-training model.
    - Comfy dtype: str
    - Python dtype: str
- frame_length
    - The frame parameters determine the time frame of the motion control model. It is important for adjusting the model to deal with the sequence of motion over different durations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - Model output represents a loaded motion control model that can be used for reasoning or further processing. It covers the patterns and dynamics of the movement necessary for the production or analysis of the sequence of motion.
    - Comfy dtype: MOTIONCTRL
    - Python dtype: torch.nn.Module
- clip
    - Clip output is the mooring component of the motion control model, which extracts features from the motion sequence. It plays a vital role in the ability of the model to understand and process the movement data.
    - Comfy dtype: EMBEDDER
    - Python dtype: torch.nn.Module
- vae
    - vae output refers to the variable coder part of the motion control model, which plays an important role in the potential space for encoding and decoding of motion data to lower dimensions.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- ddim_sampler
    - ddim_sampler output is a sampling mechanism for generating new motion sequences based on loaded motion control models. It provides a method of creating diverse and realistic motor output.
    - Comfy dtype: SAMPLER
    - Python dtype: DDIMSampler

# Usage tips
- Infra type: GPU

# Source code
```
class MotionctrlLoader:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'ckpt_name': (['motionctrl.pth'], {'default': 'motionctrl.pth'}), 'frame_length': ('INT', {'default': 16})}}
    RETURN_TYPES = ('MOTIONCTRL', 'EMBEDDER', 'VAE', 'SAMPLER')
    RETURN_NAMES = ('model', 'clip', 'vae', 'ddim_sampler')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'motionctrl'

    def load_checkpoint(self, ckpt_name, frame_length):
        gpu_num = 1
        gpu_no = 0
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        comfy_path = os.path.dirname(folder_paths.__file__)
        config_path = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/configs/inference/config_both.yaml')
        args = {'ckpt_path': f'{ckpt_path}', 'adapter_ckpt': None, 'base': f'{config_path}', 'condtype': 'both', 'prompt_dir': None, 'n_samples': 1, 'ddim_steps': 50, 'ddim_eta': 1.0, 'bs': 1, 'height': 256, 'width': 256, 'unconditional_guidance_scale': 1.0, 'unconditional_guidance_scale_temporal': None, 'seed': 1234, 'cond_T': 800}
        config = OmegaConf.load(args['base'])
        OmegaConf.update(config, 'model.params.unet_config.params.temporal_length', frame_length)
        model_config = config.pop('model', OmegaConf.create())
        model = instantiate_from_config(model_config)
        model = model.cuda(gpu_no)
        assert os.path.exists(args['ckpt_path']), f"Error: checkpoint {args['ckpt_path']} Not Found!"
        print(f"Loading checkpoint from {args['ckpt_path']}")
        model = load_model_checkpoint(model, args['ckpt_path'], args['adapter_ckpt'])
        model.eval()
        ddim_sampler = DDIMSampler(model)
        return (model, model.cond_stage_model, model.first_stage_model, ddim_sampler)
```