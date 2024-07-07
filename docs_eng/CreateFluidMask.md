# Documentation
- Class name: CreateFluidMask
- Category: KJNodes/masking/generate
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CreateFluid Mask node is designed to generate fluid animated effects that can be used to create dynamic and visually attractive mask cover. It uses hydrodynamic principles to simulate the flow and dye movement of the specified resolution and duration, generating a series of images and their corresponding masks.

# Input types
## Required
- frames
    - The 'frames' parameter determines the total number of frames to be generated for the fluid mask animation. It is vital because it determines the length of the animation sequence and influences the overall visual narrative through fluid motion.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The 'width' parameter sets the width of the generated fluid mask in pixels. It is an important parameter because it defines the spatial resolution along the x-axis and affects the details and quality of output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter specifies the height of the fluid mask generated, in pixels. It plays an important role in creating the vertical resolution of the output and influences the level of detail visible in the animation.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- invert
    - The 'invert 'parameter allows the resulting mask to be inverted. When set to True, it flips the mask to create a comparison with the visual result.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- inflow_count
    - The 'inflow_count'parameter determines the number of inflow points to be considered in fluid simulations. It affects the complexity and distribution of fluid flows and contributes to the aesthetics of the overall mask.
    - Comfy dtype: INT
    - Python dtype: int
- inflow_velocity
    - The 'inflow_velocity' parameter sets the speed of the inflow point and affects the speed of fluid movement and dispersion in simulations. It is a key factor in controlling fluid animation dynamics.
    - Comfy dtype: INT
    - Python dtype: int
- inflow_radius
    - The 'inflow_radius' parameter defines the impact radius of each point of entry and determines the area of impact. It plays a crucial role in shaping the face of the fluid mask.
    - Comfy dtype: INT
    - Python dtype: int
- inflow_padding
    - The 'inflow_padding'parameter is filled around the inflow point to prevent the fluid from impacting directly on the edge of the mask. It helps to create a smoother transition to the fluid flow at the boundary.
    - Comfy dtype: INT
    - Python dtype: int
- inflow_duration
    - The 'inflow_duration' parameter specifies the duration of the inflow that will be active during the simulation period. It is essential for controlling the time of fluid effects in the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The 'IMAGE'output provides a sequence of images generated by fluid simulations. Each image represents a frame in the animation that shows the dispersion of fluid movements and dyes over time.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - The 'MASK'output consists of binary masks corresponding to each frame in the 'IMAGE'output. These masks depict the area where the fluid exists and provide a clear distinction between the fluid and the background.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateFluidMask:
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'createfluidmask'
    CATEGORY = 'KJNodes/masking/generate'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'invert': ('BOOLEAN', {'default': False}), 'frames': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'width': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'inflow_count': ('INT', {'default': 3, 'min': 0, 'max': 255, 'step': 1}), 'inflow_velocity': ('INT', {'default': 1, 'min': 0, 'max': 255, 'step': 1}), 'inflow_radius': ('INT', {'default': 8, 'min': 0, 'max': 255, 'step': 1}), 'inflow_padding': ('INT', {'default': 50, 'min': 0, 'max': 255, 'step': 1}), 'inflow_duration': ('INT', {'default': 60, 'min': 0, 'max': 255, 'step': 1})}}

    def createfluidmask(self, frames, width, height, invert, inflow_count, inflow_velocity, inflow_radius, inflow_padding, inflow_duration):
        from .fluid import Fluid
        from scipy.spatial import erf
        out = []
        masks = []
        RESOLUTION = (width, height)
        DURATION = frames
        INFLOW_PADDING = inflow_padding
        INFLOW_DURATION = inflow_duration
        INFLOW_RADIUS = inflow_radius
        INFLOW_VELOCITY = inflow_velocity
        INFLOW_COUNT = inflow_count
        print('Generating fluid solver, this may take some time.')
        fluid = Fluid(RESOLUTION, 'dye')
        center = np.floor_divide(RESOLUTION, 2)
        r = np.min(center) - INFLOW_PADDING
        points = np.linspace(-np.pi, np.pi, INFLOW_COUNT, endpoint=False)
        points = tuple((np.array((np.cos(p), np.sin(p))) for p in points))
        normals = tuple((-p for p in points))
        points = tuple((r * p + center for p in points))
        inflow_velocity = np.zeros_like(fluid.velocity)
        inflow_dye = np.zeros(fluid.shape)
        for (p, n) in zip(points, normals):
            mask = np.linalg.norm(fluid.indices - p[:, None, None], axis=0) <= INFLOW_RADIUS
            inflow_velocity[:, mask] += n[:, None] * INFLOW_VELOCITY
            inflow_dye[mask] = 1
        for f in range(DURATION):
            print(f'Computing frame {f + 1} of {DURATION}.')
            if f <= INFLOW_DURATION:
                fluid.velocity += inflow_velocity
                fluid.dye += inflow_dye
            curl = fluid.step()[1]
            curl = (erf(curl * 2) + 1) / 4
            color = np.dstack((curl, np.ones(fluid.shape), fluid.dye))
            color = (np.clip(color, 0, 1) * 255).astype('uint8')
            image = np.array(color).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            mask = image[:, :, :, 0]
            masks.append(mask)
            out.append(image)
        if invert:
            return (1.0 - torch.cat(out, dim=0), 1.0 - torch.cat(masks, dim=0))
        return (torch.cat(out, dim=0), torch.cat(masks, dim=0))
```