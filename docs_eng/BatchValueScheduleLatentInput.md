# Documentation
- Class name: BatchValueScheduleLatentInput
- Category: FizzNodes 📅🅕🅝/BatchScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

CatchValueScheduleLatentInput is designed to process and animate a number of potential inputs according to the given text schedule. It explains the text to generate the key frame and inserts these values accordingly, providing a smooth transition between the key frames. This node is particularly suitable for creating animations or conversions, requiring smooth progress of potential variables.

# Input types
## Required
- text
    - The parameter'text' defines the schedule for the potential input animation. It is a string that specifies the key frame and its corresponding values to be used to generate animated sequences. This parameter is essential because it determines the pattern of the animation and the values that the potential input will use in the process.
    - Comfy dtype: STRING
    - Python dtype: str
- num_latents
    - Parameter'num_latents' is a dictionary that contains potential variables to be animated. Each key in the dictionary corresponds to a different potential variable, the value of which is the weight of the initial state of these variables. This parameter is essential because it provides the starting point for the animation and defines the variables that will be operated over time.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- print_output
    - The parameter 'print_output' is a boolean symbol that, when set to True, prints the key frame generated and its plug-in results to the control table. This is useful for debugging or visualizing the animation sequence before further processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- t
    - Output 't' represents the plug-in key frame generated from the input text schedule. It is a series of floating points that indicate animated progress over time.
    - Comfy dtype: FLOAT
    - Python dtype: pandas.Series
- list(map(int, t))
    - This output is derived from an integer list of the plug-in key frames. It provides a discrete version of the animation sequence and is very useful for applications that require an integer value rather than a float number.
    - Comfy dtype: INT
    - Python dtype: List[int]
- num_latents
    - Output 'num_latents' is a potential variable dictionary that is animated by the input schedule. It contains an update of the potential variables after the animation process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchValueScheduleLatentInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultValue}), 'num_latents': ('LATENT',), 'print_output': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('FLOAT', 'INT', 'LATENT')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/BatchScheduleNodes'

    def animate(self, text, num_latents, print_output):
        num_elements = sum((tensor.size(0) for tensor in num_latents.values()))
        max_frames = num_elements
        t = batch_get_inbetweens(batch_parse_key_frames(text, max_frames), max_frames)
        if print_output is True:
            print('ValueSchedule: ', t)
        return (t, list(map(int, t)), num_latents)
```