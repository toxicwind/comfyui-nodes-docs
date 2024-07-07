# Documentation
- Class name: HF_TransformersClassifierProvider
- Category: ImpactPack/HuggingFace
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The HF_TransformersClassifierProvider node is designed to facilitate the creation and use of text classifyors using models in the Hugging Face Transformers library. It abstractes the complexity of model selection and equipment allocation, allowing users to focus on the classification tasks at hand. The main function of the node is to simplify the process of obtaining the sorter, which can be applied immediately to the given text data set.

# Input types
## Required
- preset_repo_id
    - The preset_repo_id parameter is essential for identifying pre-configured model repositories from the Hugging Face model centre. It streamlines the model selection process by providing a predefined set of options. This parameter plays a key role in determining the underlying model on which the sorter will be based, thus directly affecting the classification function.
    - Comfy dtype: STRING
    - Python dtype: Union[str, List[str]]
- device_mode
    - The parameter determines the computing device to be used for model reasoning. It provides automatic selection of the device, or, if available, a preference for the GPU, or a clear selection of the CPU. This parameter is important because it can affect the speed and efficiency of the classification process, especially for large models or data sets.
    - Comfy dtype: STRING
    - Python dtype: Literal['AUTO', 'Prefer GPU', 'CPU']
## Optional
- manual_repo_id
    - When the preset_repo_id is set to 'Manual repo id', the manual_repo_id parameter allows the assignment of a custom model repository ID. This provides flexibility for users wishing to use models other than the predefined option, allowing nodes to adapt to broader classification tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- TRANSFORMERS_CLASSIFIER
    - TRANSFORMER_CLASSIFIER provides a pre-training model from the Hugging Face Transformers library for text classification tasks. It encapsulates the model's reasoning capability and allows seamless integration into downstream applications.
    - Comfy dtype: TRANSFORMERS_CLASSIFIER
    - Python dtype: Any

# Usage tips
- Infra type: GPU

# Source code
```
class HF_TransformersClassifierProvider:

    @classmethod
    def INPUT_TYPES(s):
        global hf_transformer_model_urls
        return {'required': {'preset_repo_id': (hf_transformer_model_urls + ['Manual repo id'],), 'manual_repo_id': ('STRING', {'multiline': False}), 'device_mode': (['AUTO', 'Prefer GPU', 'CPU'],)}}
    RETURN_TYPES = ('TRANSFORMERS_CLASSIFIER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/HuggingFace'

    def doit(self, preset_repo_id, manual_repo_id, device_mode):
        from transformers import pipeline
        if preset_repo_id == 'Manual repo id':
            url = manual_repo_id
        else:
            url = preset_repo_id
        if device_mode != 'CPU':
            device = comfy.model_management.get_torch_device()
        else:
            device = 'cpu'
        classifier = pipeline(model=url, device=device)
        return (classifier,)
```