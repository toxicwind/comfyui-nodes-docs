# Documentation
- Class name: NoiseInjectionHookProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The NoiseInjectionHookProvider node is designed to inject noise into the image generation process, allowing for the creation of changes or “reverse sampling” of images. It provides a simple timetable to control the noise injection process and is able to handle CPU and GPU sources. This node is critical to the need to finely control noise workflows, such as generating subtle changes or reconstructing images with specific noise properties.

# Input types
## Required
- schedule_for_iteration
    - The schedule_for_iteration parameter determines the schedule of noise injections, which is essential for the consistent application of noise over time. It is a key factor in the ability of nodes to generate changes or “reverse sampling” images.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- source
    - The source parameter specifies whether the CPU or GPU should be used for noise generation. This option significantly affects the performance and efficiency of the noise injection process.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- seed
    - Seed parameter initializes the noise generation process to ensure that the noise mode is recreated. It plays a vital role in maintaining consistency between nodes and different operations.
    - Comfy dtype: INT
    - Python dtype: int
- start_strength
    - Start_strength parameters set the initial strength of the noise to be injected. This is the key factor in determining the extent of change to be achieved or “resampled”.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_strength
    - End_strength parameters define the ultimate strength of noise at the end of the injection process. It is used in conjunction with start_strength to create a gradient of noise intensity throughout the process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- hook
    - Hook output provides a way to integrate noise injection functions into a larger image generation workflow. It covers node definition settings and behaviours and allows seamless application in a broader process.
    - Comfy dtype: PK_HOOK
    - Python dtype: PixelKSampleHook

# Usage tips
- Infra type: GPU

# Source code
```
class NoiseInjectionHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_iteration': (s.schedules,), 'source': (['CPU', 'GPU'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'start_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 200.0, 'step': 0.01}), 'end_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 200.0, 'step': 0.01})}}
    RETURN_TYPES = ('PK_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, schedule_for_iteration, source, seed, start_strength, end_strength):
        try:
            hook = None
            if schedule_for_iteration == 'simple':
                hook = hooks.InjectNoiseHook(source, seed, start_strength, end_strength)
            return (hook,)
        except Exception as e:
            print("[ERROR] NoiseInjectionHookProvider: 'ComfyUI Noise' custom node isn't installed. You must install 'BlenderNeko/ComfyUI Noise' extension to use this node.")
            print(f'\t{e}')
            pass
```