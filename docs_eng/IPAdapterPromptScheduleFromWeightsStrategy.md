# Documentation
- Class name: IPAdapterPromptScheduleFromWeightsStrategy
- Category: ipadapter/weights
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

This node is based on weighting strategy and allows users to better control the process of generating text. By adjusting the weights at different stages, the node helps to generate text content that is more appropriate to the user’s needs.

# Input types

## Required

- weights_strategy
    - The weight policy is used to specify the weight policy for generating the image. This parameter is used to control the weight policy for generating the image in order to achieve better results.
    - Comfy dtype: WEIGHTS_STRATEGY
    - Python dtype: str
- prompt
    - hint, which specifies the hint for generating the image. This parameter is used to control the hint for generating the image in order to achieve better results.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt_schedule
    - Prompt_schedule output represents the results of the application of the specified method to input weights. It contains the essence of node purposes and provides a synthesis of input data that can be used for further analysis or modelling training.
    - Comfy dtype: STRING
    - Python dtype: str


# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterPromptScheduleFromWeightsStrategy():
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "weights_strategy": ("WEIGHTS_STRATEGY",),
            "prompt": ("STRING", {"default": "", "multiline": True }),
            }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt_schedule", )
    FUNCTION = "prompt_schedule"
    CATEGORY = "ipadapter/weights"

    def prompt_schedule(self, weights_strategy, prompt=""):
        frames = weights_strategy["frames"]
        add_starting_frames = weights_strategy["add_starting_frames"]
        add_ending_frames = weights_strategy["add_ending_frames"]
        frame_count = weights_strategy["frame_count"]

        out = ""

        prompt = [p for p in prompt.split("\n") if p.strip() != ""]

        if len(prompt) > 0 and frame_count > 0:
            # prompt_pos must be the same size as the image batch
            if len(prompt) > frame_count:
                prompt = prompt[:frame_count]
            elif len(prompt) < frame_count:
                prompt += [prompt[-1]] * (frame_count - len(prompt))

            if add_starting_frames > 0:
                out += f"\"0\": \"{prompt[0]}\",\n"
            for i in range(frame_count):
                out += f"\"{i * frames + add_starting_frames}\": \"{prompt[i]}\",\n"
            if add_ending_frames > 0:
                out += f"\"{frame_count * frames + add_starting_frames}\": \"{prompt[-1]}\",\n"

        return (out, )
```