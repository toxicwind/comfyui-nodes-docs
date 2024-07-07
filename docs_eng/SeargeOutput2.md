# Documentation
- Class name: SeargeOutput2
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is intended to process and replicate input parameters and assign them to specific outputs to meet various reprocessing and analytical tasks.

# Input types
## Required
- parameters
    - The parameter is a dictionary that contains all inputs required for node operations. It is vital because it determines the behaviour of node and the data it processes.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The original input parameter is passed as the basis for the follow-up operation.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- seed
    - Seed values are essential to ensure the replicability of the output generation process.
    - Comfy dtype: Int
    - Python dtype: int
- image_width
    - This output defines the width of the image generated, which is essential for image processing and display purposes.
    - Comfy dtype: Int
    - Python dtype: int
- image_height
    - This output specifies the height of the image, which is a key factor in determining the size and layout of the image.
    - Comfy dtype: Int
    - Python dtype: int
- steps
    - The sequence or progress of the step number output indicator process may affect the complexity and duration of the operation.
    - Comfy dtype: Int
    - Python dtype: int
- cfg
    - Configures the parameters to save the settings that are essential for adjusting node behaviour and output characteristics.
    - Comfy dtype: Float
    - Python dtype: float
- sampler_name
    - The name of the sampler is a string used to identify the particular sampling methods used, which is important for the accuracy and diversity of the results.
    - Comfy dtype: Str
    - Python dtype: str
- scheduler
    - The scheduler name output provides information on the movement control method, which is essential for resource management and timing.
    - Comfy dtype: Str
    - Python dtype: str
- save_image
    - This boolean output determines whether to save the image, which is important for preserving the results of the operation.
    - Comfy dtype: Bool
    - Python dtype: bool
- save_directory
    - The storage directory output specifies the location where the results will be stored, which is essential for organizing and accessing the output data.
    - Comfy dtype: Str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'INT', 'INT', 'INT', 'INT', 'FLOAT', 'SAMPLER_NAME', 'SCHEDULER_NAME', 'ENABLE_STATE', 'SAVE_FOLDER')
    RETURN_NAMES = ('parameters', 'seed', 'image_width', 'image_height', 'steps', 'cfg', 'sampler_name', 'scheduler', 'save_image', 'save_directory')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        seed = parameters['seed']
        image_width = parameters['image_width']
        image_height = parameters['image_height']
        steps = parameters['steps']
        cfg = parameters['cfg']
        sampler_name = parameters['sampler_name']
        scheduler = parameters['scheduler']
        save_image = parameters['save_image']
        save_directory = parameters['save_directory']
        return (parameters, seed, image_width, image_height, steps, cfg, sampler_name, scheduler, save_image, save_directory)
```