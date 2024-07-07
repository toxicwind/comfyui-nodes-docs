# Documentation
- Class name: MotionctrlSampleSimple
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl.git

MotionctrlSampleSimple node is designed to generate and control motion sequences using a range of models and sampling techniques. It uses the power of motion control models to create coherent and realistic trajectories. The node is good at processing inputs, including embedded and noise shapes, to produce image sequences that represent motion.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the movement control models that will be used to generate the sequence of motion. This is a key component that allows nodes to generate accurate and realistic trajectories.
    - Comfy dtype: MOTIONCTRL
    - Python dtype: torch.nn.Module
- steps
    - The step parameter determines the number of steps to be used in the sampling process. It affects the particle size of the motion sequence and may affect the quality of the movement generated.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - Context_overlap parameters specify the amount of overlap between the context frame and the generation frame. This is important for creating smooth transitions and ensuring the consistency of the motion sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output of the MotionstrlSampleSimple node is an image sequence that represents the generation of motion. This sequence is the result of node processing and reflects the ability to enter parameters and bottom motion control models.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MotionctrlSampleSimple:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MOTIONCTRL',), 'clip': ('EMBEDDER',), 'vae': ('VAE',), 'ddim_sampler': ('SAMPLER',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'traj_list': ('TRAJ_LIST',), 'rt_list': ('RT_LIST',), 'traj': ('TRAJ_FEATURES',), 'rt': ('RT',), 'steps': ('INT', {'default': 50}), 'seed': ('INT', {'default': 1234}), 'noise_shape': ('NOISE_SHAPE',), 'context_overlap': ('INT', {'default': 0, 'min': 0, 'max': 32})}, 'optional': {'traj_tool': ('STRING', {'multiline': False, 'default': 'https://chaojie.github.io/ComfyUI-MotionCtrl/tools/draw.html'}), 'draw_traj_dot': ('BOOLEAN', {'default': False}), 'draw_camera_dot': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run_inference'
    CATEGORY = 'motionctrl'

    def run_inference(self, model, clip, vae, ddim_sampler, positive, negative, traj_list, rt_list, traj, rt, steps, seed, noise_shape, context_overlap, traj_tool='https://chaojie.github.io/ComfyUI-MotionCtrl/tools/draw.html', draw_traj_dot=False, draw_camera_dot=False):
        frame_length = model.temporal_length
        device = model.betas.device
        print(f'frame_length{frame_length}')
        unconditional_guidance_scale = 7.5
        unconditional_guidance_scale_temporal = None
        n_samples = 1
        ddim_steps = steps
        ddim_eta = 1.0
        cond_T = 800
        if n_samples < 1:
            n_samples = 1
        if n_samples > 4:
            n_samples = 4
        seed_everything(seed)
        batch_images = []
        batch_variants = []
        intermediates = {}
        x0 = None
        x_T = None
        pre_x0 = None
        pre_x_T = None
        comfy_path = os.path.dirname(folder_paths.__file__)
        pred_x0_path = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/pred_x0.pt')
        x_inter_path = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/x_inter.pt')
        randt = torch.randn([noise_shape[0], noise_shape[1], frame_length - context_overlap, noise_shape[3], noise_shape[4]], device=device)
        randt_np = randt.detach().cpu().numpy()
        if context_overlap > 0:
            if os.path.exists(pred_x0_path):
                pre_x0 = torch.load(pred_x0_path)
                pre_x0_np = pre_x0[-1].detach().cpu().numpy()
                pre_x0_np_overlap = np.concatenate((pre_x0_np[:, :, -context_overlap:], randt_np), axis=2)
                x0 = torch.tensor(pre_x0_np_overlap, device=device)
            if os.path.exists(x_inter_path):
                pre_x_T = torch.load(x_inter_path)
                pre_x_T_np = pre_x_T[-1].detach().cpu().numpy()
                pre_x_T_np_overlap = np.concatenate((pre_x_T_np[:, :, -context_overlap:], randt_np), axis=2)
                x_T = torch.tensor(pre_x_T_np_overlap, device=device)
        for _ in range(n_samples):
            if ddim_sampler is not None:
                (samples, intermediates) = ddim_sampler.sample(S=ddim_steps, conditioning=positive, batch_size=noise_shape[0], shape=noise_shape[1:], verbose=False, unconditional_guidance_scale=unconditional_guidance_scale, unconditional_conditioning=negative, eta=ddim_eta, temporal_length=noise_shape[2], conditional_guidance_scale_temporal=unconditional_guidance_scale_temporal, features_adapter=traj, pose_emb=rt, cond_T=cond_T, x0=x0, x_T=x_T)
            batch_images = model.decode_first_stage(samples)
            batch_variants.append(batch_images)
            "\n            batch_images = model.decode_first_stage(intermediates['pred_x0'][0])\n            batch_variants.append(batch_images)\n            batch_images = model.decode_first_stage(intermediates['pred_x0'][1])\n            batch_variants.append(batch_images)\n            batch_images = model.decode_first_stage(intermediates['pred_x0'][2])\n            batch_variants.append(batch_images)\n            batch_images = model.decode_first_stage(intermediates['x_inter'][0])\n            batch_variants.append(batch_images)\n            batch_images = model.decode_first_stage(intermediates['x_inter'][1])\n            batch_variants.append(batch_images)\n            batch_images = model.decode_first_stage(intermediates['x_inter'][2])\n            batch_variants.append(batch_images)\n            "
        batch_variants = torch.stack(batch_variants, dim=1)
        batch_variants = batch_variants[0]
        torch.save(intermediates['x_inter'], x_inter_path)
        torch.save(intermediates['pred_x0'], pred_x0_path)
        ret = save_results(batch_variants, fps=10, traj=traj_list, draw_traj_dot=draw_traj_dot, cameras=rt_list, draw_camera_dot=draw_camera_dot, context_overlap=context_overlap)
        return ret
```