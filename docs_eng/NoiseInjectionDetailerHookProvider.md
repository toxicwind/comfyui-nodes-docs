# Documentation
- Class name: NoiseInjectionDetailerHookProvider
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

NoiseInjectionDetailerHookProvider is designed to enhance the details of the image generation process by strategically infusing noise at certain stages of the image generation cycle. It uses the power of noise to increase variability and fine-tune output to ensure more detailed and detailed results. This is essential for applications that are essential to the authenticity of the image, such as creating complex textures or patterns.

# Input types
## Required
- schedule_for_cycle
    - The schedule_for_cycle parameter determines the timing of noise injection during the generation cycle. It is essential to control the stage of introducing noise, allowing for precise manipulation of the level of detail of the image. This parameter is essential to achieve the desired balance between noise and clarity in the final output.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- source
    - The source parameter determines whether noise generation will take place on CPU or GPU. This option can significantly affect the performance and efficiency of the noise injection process, making it a key consideration in optimizing node operations.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- seed
    - Seed parameter initializes the random number generator to ensure the consistency and replicability of noise. It plays an important role in maintaining the predictability of noise injections, which is important for creating reliable and consistent output in the different operations of nodes.
    - Comfy dtype: INT
    - Python dtype: int
- start_strength
    - Start_strength parameters set the initial strength of noise that is injected at the start of the generation cycle. It is a key factor in determining the overall impact of noise on the image and allows for fine control of the level of detail introduced.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_strength
    - End_strength parameters define the intensity of noise at the end of the generation cycle. It allows noise intensity to increase or decrease over time, enabling the creation of images with details and texture smooth transitions.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- DETAILER_HOOK
    - The output of NoiseInjectionDetailerHookProvider node is a detailed hook, a special tool used to inject noise into the image generation process. This hook is important because it directly affects the final quality and detail of the image generated and provides a means of enhancing the visual authenticity of the output.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: DetailerHook

# Usage tips
- Infra type: GPU

# Source code
```
class NoiseInjectionDetailerHookProvider:
    schedules = ['skip_start', 'from_start']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_cycle': (s.schedules,), 'source': (['CPU', 'GPU'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'start_strength': ('FLOAT', {'default': 2.0, 'min': 0.0, 'max': 200.0, 'step': 0.01}), 'end_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 200.0, 'step': 0.01})}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, schedule_for_cycle, source, seed, start_strength, end_strength):
        try:
            hook = hooks.InjectNoiseHookForDetailer(source, seed, start_strength, end_strength, from_start='from_start' in schedule_for_cycle)
            return (hook,)
        except Exception as e:
            print("[ERROR] NoiseInjectionDetailerHookProvider: 'ComfyUI Noise' custom node isn't installed. You must install 'BlenderNeko/ComfyUI Noise' extension to use this node.")
            print(f'\t{e}')
            pass
```