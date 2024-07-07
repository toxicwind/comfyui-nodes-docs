# Documentation
- Class name: MotionctrlCond
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl.git

The MotionctrlCond node is designed to manage and process the movement control conditions in the dynamic system. It accepts various inputs, such as model configurations, text tips, camera settings and trajectories data, to generate a comprehensive set of motion controls. The node ensures that the movement is smooth and aligned with the content provided, and handles the mode of motion reasoning of the camera and the object. It produces the reconciliation signal, trajectory characteristics and other related motion parameters that are essential to the next steps in the movement control stream.

# Input types
## Required
- model
    - Model parameters are essential for nodes because it defines nodes that will be used to generate a bottom-level motion control model for motion control. This is a necessary input that directly affects the ability of nodes to process and produce accurate motion control outputs.
    - Comfy dtype: MOTIONCTRL
    - Python dtype: nn.Module
- prompt
    - The hint parameter allows the user to enter descriptive text to guide movement control behaviour. It is important because it provides the context for the model to generate a movement that is consistent with the description of the scene.
    - Comfy dtype: STRING
    - Python dtype: str
- camera
    - Camera parameters specify camera settings in a multi-frame environment. For nodes, the view of the right alignment camera is essential to the movement being controlled to ensure consistent visual output.
    - Comfy dtype: STRING
    - Python dtype: str
- traj
    - The trajectories outline the path to follow for the control of the movement. It is a key input that determines the order of the movement and is essential for node generation of the required mode of movement.
    - Comfy dtype: STRING
    - Python dtype: str
- infer_mode
    - The reasoning parameters determine how the node deals with motion and camera control. It provides flexibility in the operation of the node and allows it to adapt to different reasoning needs.
    - Comfy dtype: MODE
    - Python dtype: str
- context_overlap
    - The context overlap parameter is used to define the overlap range between the camera and the trajectory alignment. It affects how the previous context is integrated into the current motion control sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- positive
    - A set of signals is being provided to the reconciliation output to direct movement control to desired results based on input tips and settings.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative adjustment output is used to offset or suppress certain unwanted motor characteristics and to ensure that the movement is consistent with the expected context.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- traj_list
    - The trajectories list enumerates the movement control point series that defines the path of the movement. It is important for visualizing and implementing the campaign.
    - Comfy dtype: TRAJ_LIST
    - Python dtype: List[torch.Tensor]
- rt_list
    - The RT list output contains a list of camera rotation and moving parameters corresponding to each frame in the motion sequence.
    - Comfy dtype: RT_LIST
    - Python dtype: List[np.ndarray]
- traj
    - The trajectories characterization indicates the processed motion control data, which encapsulates the motion characteristics of each frame.
    - Comfy dtype: TRAJ_FEATURES
    - Python dtype: torch.Tensor
- rt
    - The RT output provides the final camera rotation and migration parameters aligned to the current frame's motion control.
    - Comfy dtype: RT
    - Python dtype: torch.Tensor
- noise_shape
    - Noise shape output defines the dimensions of noise applied to motion control systems, which are essential for certain types of simulation or training processes that inject noise.
    - Comfy dtype: NOISE_SHAPE
    - Python dtype: Tuple[int, int, int, int, int]
- context_overlap
    - The overlap output instruction in context controls the amount of overlap in context that was taken into account by the previous motion when generating the current sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class MotionctrlCond:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MOTIONCTRL',), 'prompt': ('STRING', {'multiline': True, 'default': 'a rose swaying in the wind'}), 'camera': ('STRING', {'multiline': True, 'default': '[[1,0,0,0,0,1,0,0,0,0,1,0.2]]'}), 'traj': ('STRING', {'multiline': True, 'default': '[[117, 102]]'}), 'infer_mode': (MODE, {'default': 'control both camera and object motion'}), 'context_overlap': ('INT', {'default': 0, 'min': 0, 'max': 32})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'TRAJ_LIST', 'RT_LIST', 'TRAJ_FEATURES', 'RT', 'NOISE_SHAPE', 'INT')
    RETURN_NAMES = ('positive', 'negative', 'traj_list', 'rt_list', 'traj', 'rt', 'noise_shape', 'context_overlap')
    FUNCTION = 'load_cond'
    CATEGORY = 'motionctrl'

    def load_cond(self, model, prompt, camera, traj, infer_mode, context_overlap):
        comfy_path = os.path.dirname(folder_paths.__file__)
        camera_align_file = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/camera.json')
        traj_align_file = os.path.join(comfy_path, 'custom_nodes/ComfyUI-MotionCtrl/traj.json')
        frame_length = model.temporal_length
        camera_align = json.loads(camera)
        for i in range(frame_length):
            if len(camera_align) <= i:
                camera_align.append(camera_align[len(camera_align) - 1])
        camera = json.dumps(camera_align)
        traj_align = json.loads(traj)
        for i in range(frame_length):
            if len(traj_align) <= i:
                traj_align.append(traj_align[len(traj_align) - 1])
        traj = json.dumps(traj_align)
        if context_overlap > 0:
            if os.path.exists(camera_align_file):
                with open(camera_align_file, 'r') as file:
                    pre_camera_align = json.load(file)
                    camera_align = pre_camera_align[:context_overlap] + camera_align[:-context_overlap]
            if os.path.exists(traj_align_file):
                with open(traj_align_file, 'r') as file:
                    pre_traj_align = json.load(file)
                    traj_align = pre_traj_align[:context_overlap] + traj_align[:-context_overlap]
            with open(camera_align_file, 'w') as file:
                json.dump(camera_align, file)
            with open(traj_align_file, 'w') as file:
                json.dump(traj_align, file)
        prompts = prompt
        RT = process_camera(camera, frame_length).reshape(-1, 12)
        RT_list = process_camera_list(camera, frame_length)
        traj_flow = process_traj(traj, frame_length).transpose(3, 0, 1, 2)
        print(prompts)
        print(RT.shape)
        print(traj_flow.shape)
        height = 256
        width = 256
        assert height % 16 == 0 and width % 16 == 0, 'Error: image size [h,w] should be multiples of 16!'
        (h, w) = (height // 8, width // 8)
        channels = model.channels
        frames = model.temporal_length
        noise_shape = [1, channels, frames, h, w]
        if infer_mode == MODE[0]:
            camera_poses = RT
            camera_poses = torch.tensor(camera_poses).float()
            camera_poses = camera_poses.unsqueeze(0)
            trajs = None
            if torch.cuda.is_available():
                camera_poses = camera_poses.cuda()
        elif infer_mode == MODE[1]:
            trajs = traj_flow
            trajs = torch.tensor(trajs).float()
            trajs = trajs.unsqueeze(0)
            camera_poses = None
            if torch.cuda.is_available():
                trajs = trajs.cuda()
        else:
            camera_poses = RT
            trajs = traj_flow
            camera_poses = torch.tensor(camera_poses).float()
            trajs = torch.tensor(trajs).float()
            camera_poses = camera_poses.unsqueeze(0)
            trajs = trajs.unsqueeze(0)
            if torch.cuda.is_available():
                camera_poses = camera_poses.cuda()
                trajs = trajs.cuda()
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
        prompts = batch_size * [DEFAULT_NEGATIVE_PROMPT]
        uc = model.get_learned_conditioning(prompts)
        if traj_features is not None:
            un_motion = model.get_traj_features(torch.zeros_like(trajs))
        else:
            un_motion = None
        uc = {'features_adapter': un_motion, 'uc': uc}
        return (cond, uc, traj, RT_list, traj_features, RT, noise_shape, context_overlap)
```