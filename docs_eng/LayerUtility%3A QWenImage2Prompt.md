# Documentation
- Class name: QWenImage2Prompt
- Category: 😺dzNodes/LayerUtility/Prompt
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

This node is re-encapable from the UForm-Gen2 Qwen Node node in [ComfyUI_VLM_nodes] (https://github.com/gokayfem/ComfyUI_VLM_nodes), thanking the original author. Please download the model from [huggingface] (https://huggingface.co/unum-clud/uform-gen2-qwen-500m) or [100-degree web drive] (https://pan.baidu.com/s/1ztnVX_Sh800xWhMde-Ww?pwd=esyt) from [huggingface] (https://huggingface.co/um-clud/uform-gen2-qwen-500m) or from uform_gen2_qwen folder.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- question
    - A hint for the UForm-Gen-QWen model.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types

- text
    - text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```python
class QWenImage2Prompt:
    def __init__(self):
        self.chat_model = UformGen2QwenChat()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "question": ("STRING", {"multiline": False, "default": "describe this image",},),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "uform_gen2_qwen_chat"
    CATEGORY = '😺dzNodes/LayerUtility/Prompt'

    def uform_gen2_qwen_chat(self, image, question):
        history = []  # Example empty history
        pil_image = ToPILImage()(image[0].permute(2, 0, 1))
        temp_path = files_for_uform_gen2_qwen / "temp.png"
        pil_image.save(temp_path)

        response = self.chat_model.chat_response(question, history, temp_path)
        return (response.split("assistant\n", 1)[1], )
```