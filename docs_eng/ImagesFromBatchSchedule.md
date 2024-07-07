# Documentation
- Class name: ImagesFromBatchSchedule
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The ImagesFromBatchSchedule node 'animate' method is designed to generate a series of images based on the texttips provided and the current frame, within the maximum frame specified. It processes the input text to create a series of hints and selects the appropriate image for each frame to ensure a smooth transition between the frame and the frame in the animated fruit.

# Input types
## Required
- images
    - The 'image'parameter is the collection of image data that the node uses to generate animations. It is essential for the operation of the node because it directly affects the animated sequence of output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - The 'text' parameter contains descriptive text, which is used by nodes to interpret and generate animation tips. It is very important because it defines the content and style of animation.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- current_frame
    - The 'current_frame' parameter specifies the frame that is currently being processed. It is important because it determines the starting point of the image for the animation.
    - Comfy dtype: INT
    - Python dtype: int
- max_frames
    - The'max_frames' parameter sets a ceiling on the number of frames in the animation. It is important because it limits the range of operations for nodes to generate animated sequences.
    - Comfy dtype: INT
    - Python dtype: int
- print_output
    - The 'print_output' parameter is a symbol that, when set to True, indicates that the output will be printed on the control table. This is useful for debugging purposes and allows you to see the intermediate results of the animation process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_images
    - The'seleted_images' output contains images selected for the current frame of the animation. This output is important because it represents the visual result of the node for the given frame operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImagesFromBatchSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'text': ('STRING', {'multiline': True, 'default': defaultPrompt}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, images, text, current_frame, max_frames, print_output):
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        start_frame = 0
        animation_prompts = json.loads(inputText.strip())
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(animation_prompts, max_frames, 0, '', '', 0, 0, 0, 0, print_output)
        selImages = selectImages(images, pos_cur_prompt[current_frame])
        return selImages
```