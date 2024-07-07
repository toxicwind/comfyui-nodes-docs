# Documentation
- Class name: MotionctrlSample
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl.git

The MotionctrlSample class is designed to facilitate the generation of dynamic visual content by integrating motion control into the rendering process. It uses the power of advanced algorithms to interpret user-defined camera and trajectory input, enabling the creation of complex sequences of motion with live animations. The node abstractes the complexity of motion simulations and allows users to focus on creative expression rather than bottom-level technical details.

# Input types
## Required
- prompt
    - A reminder parameter, as an innovative input for the MotionctrlSample node, guides the whole theme and style of the content generated. It is essential for setting the context in which a motion simulation takes place and directly affects the narrative and visual elements generated during the rendering process.
    - Comfy dtype: STRING
    - Python dtype: str
- camera
    - Camera parameters define the perspective and point of view for capturing the sequence of motion. They play a key role in shaping the spatial and temporal relationships and depth perceptions of the rendering landscape, thus significantly influencing the final visual output.
    - Comfy dtype: STRING
    - Python dtype: str
- traj
    - The trajectory parameters provide an overview of the path and motion of the object in the scene and form the basis for motion simulations. It is essential to guide the dynamics of animation and the interaction of elements, ensuring consistency and fluidity in motor performance.
    - Comfy dtype: STRING
    - Python dtype: str
- frame_length
    - Frame length parameters specify the duration of the animation sequence, which directly affects the level of detail and complexity of the trajectory. A longer frame length allows for a more complex mode of movement and a smoother transition, while a shorter frame length may lead to a simpler or more sudden movement.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the number of intermediate frames generated during motion simulations, which affects the smoothness and quality of animations. The higher the number of steps, the finer the track, and the lower the number of steps, the less detailed or incoherent.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters are used to initialize random number generators to ensure that motion simulation results are replicable and consistent. This is an important aspect for debugging and comparing different simulations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the MotionctrlSample node is a dynamic visual expression that encapsifies the results of motion simulations in the form of images or image sequences. It reflects the combined effect of input parameters and shows the creativity and complexity of the content generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MotionctrlSample:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'default': 'a rose swaying in the wind'}), 'camera': ('STRING', {'multiline': True, 'default': '[[1,0,0,0,0,1,0,0,0,0,1,0.2]]'}), 'traj': ('STRING', {'multiline': True, 'default': '[[117, 102]]'}), 'frame_length': ('INT', {'default': 16}), 'steps': ('INT', {'default': 50}), 'seed': ('INT', {'default': 1234})}, 'optional': {'traj_tool': ('STRING', {'multiline': False, 'default': 'https://chaojie.github.io/ComfyUI-MotionCtrl/tools/draw.html'}), 'draw_traj_dot': ('BOOLEAN', {'default': False}), 'draw_camera_dot': ('BOOLEAN', {'default': False}), 'ckpt_name': (['motionctrl.pth'], {'default': 'motionctrl.pth'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run_inference'
    CATEGORY = 'motionctrl'

    def run_inference(self, prompt, camera, traj, frame_length, steps, seed, traj_tool='https://chaojie.github.io/ComfyUI-MotionCtrl/tools/draw.html', draw_traj_dot=False, draw_camera_dot=False, ckpt_name='motionctrl.pth'):
        gpu_num = 1
        gpu_no = 0
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        comfy_path = os.path.dirname(folder_paths.__file__)
        config_path = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/configs/inference/config_both.yaml')
        args = {'savedir': f'./output/both_seed20230211', 'ckpt_path': f'{ckpt_path}', 'adapter_ckpt': None, 'base': f'{config_path}', 'condtype': 'both', 'prompt_dir': None, 'n_samples': 1, 'ddim_steps': 50, 'ddim_eta': 1.0, 'bs': 1, 'height': 256, 'width': 256, 'unconditional_guidance_scale': 1.0, 'unconditional_guidance_scale_temporal': None, 'seed': 1234, 'cond_T': 800, 'save_imgs': True, 'cond_dir': './custom_nodes/ComfyUI-MotionCtrl/examples/'}
        prompts = prompt
        RT = process_camera(camera, frame_length).reshape(-1, 12)
        RT_list = process_camera_list(camera, frame_length)
        traj_flow = process_traj(traj, frame_length).transpose(3, 0, 1, 2)
        print(prompts)
        print(RT.shape)
        print(traj_flow.shape)
        args['savedir'] = f"./output/{args['condtype']}_seed{args['seed']}"
        config = OmegaConf.load(args['base'])
        OmegaConf.update(config, 'model.params.unet_config.params.temporal_length', frame_length)
        model_config = config.pop('model', OmegaConf.create())
        model = instantiate_from_config(model_config)
        model = model.cuda(gpu_no)
        assert os.path.exists(args['ckpt_path']), f"Error: checkpoint {args['ckpt_path']} Not Found!"
        print(f"Loading checkpoint from {args['ckpt_path']}")
        model = load_model_checkpoint(model, args['ckpt_path'], args['adapter_ckpt'])
        model.eval()
        assert args['height'] % 16 == 0 and args['width'] % 16 == 0, 'Error: image size [h,w] should be multiples of 16!'
        (h, w) = (args['height'] // 8, args['width'] // 8)
        channels = model.channels
        frames = model.temporal_length
        noise_shape = [args['bs'], channels, frames, h, w]
        savedir = os.path.join(args['savedir'], 'samples')
        os.makedirs(savedir, exist_ok=True)
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
        camera_poses = RT
        trajs = traj_flow
        camera_poses = torch.tensor(camera_poses).float()
        trajs = torch.tensor(trajs).float()
        camera_poses = camera_poses.unsqueeze(0)
        trajs = trajs.unsqueeze(0)
        if torch.cuda.is_available():
            camera_poses = camera_poses.cuda()
            trajs = trajs.cuda()
        ddim_sampler = DDIMSampler(model)
        batch_size = noise_shape[0]
        prompts = prompt
        if isinstance(prompts, str):
            prompts = [prompts]
        for i in range(len(prompts)):
            prompts[i] = f'{prompts[i]}, {post_prompt}'
        cond = model.get_learned_conditioning(prompts)
        if camera_poses is not None:
            RT = camera_poses[..., None]
        else:
            RT = None
        traj_features = None
        if trajs is not None:
            traj_features = model.get_traj_features(trajs)
        else:
            traj_features = None
        uc = None
        if unconditional_guidance_scale != 1.0:
            prompts = batch_size * [DEFAULT_NEGATIVE_PROMPT]
            uc = model.get_learned_conditioning(prompts)
            if traj_features is not None:
                un_motion = model.get_traj_features(torch.zeros_like(trajs))
            else:
                un_motion = None
            uc = {'features_adapter': un_motion, 'uc': uc}
        else:
            uc = None
        batch_images = []
        batch_variants = []
        for _ in range(n_samples):
            if ddim_sampler is not None:
                (samples, _) = ddim_sampler.sample(S=ddim_steps, conditioning=cond, batch_size=noise_shape[0], shape=noise_shape[1:], verbose=False, unconditional_guidance_scale=unconditional_guidance_scale, unconditional_conditioning=uc, eta=ddim_eta, temporal_length=noise_shape[2], conditional_guidance_scale_temporal=unconditional_guidance_scale_temporal, features_adapter=traj_features, pose_emb=RT, cond_T=cond_T)
            batch_images = model.decode_first_stage(samples)
            batch_variants.append(batch_images)
        batch_variants = torch.stack(batch_variants, dim=1)
        batch_variants = batch_variants[0]
        ret = save_results(batch_variants, fps=10, traj=traj, draw_traj_dot=draw_traj_dot, cameras=RT_list, draw_camera_dot=draw_camera_dot)
        return ret
```