# Documentation
- Class name: SeargeModelSelector
- Category: UI.CATEGORY_UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeModelSelector node simplifies the process of selecting and collating model checkpoints for further processing. It encapsifies the complexity of processing the various check-point types, allowing users to focus on model analysis and application without worrying about the technical details at the bottom.

# Input types
## Required
- base_checkpoint
    - Base_checkpoint parameters are essential because it designates a base model check point as the starting point for follow-up operations. Its selection affects the overall performance and accuracy of the downstream task.
    - Comfy dtype: UI.CHECKPOINTS()
    - Python dtype: Union[str, None]
- refiner_checkpoint
    - The refinder_checkpoint parameter is essential to enhance the performance of the underlying model. It introduces the possibility of improving the prediction of the model, thereby improving the quality of the final output.
    - Comfy dtype: UI.CHECKPOINTS_WITH_NONE()
    - Python dtype: Union[str, None]
- vae_checkpoint
    - The vae_checkpoint parameter plays a key role in integrating the variable encoder in the workflow. It makes it possible to integrate potential indications that this may be critical to complex data-processing tasks.
    - Comfy dtype: UI.VAE_WITH_EMBEDDED()
    - Python dtype: List[str]
## Optional
- data
    - The data parameter is used as a container for additional information that may be required during the model selection process. It supports the efficient and effective operation of the nodes.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- data
    - The output data parameters include the results of the model selection process, including the checkpoints of the combinations. It is a key component of the workflow into the follow-up phase and facilitates further analysis and application.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeModelSelector:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'base_checkpoint': (UI.CHECKPOINTS(),), 'refiner_checkpoint': (UI.CHECKPOINTS_WITH_NONE(),), 'vae_checkpoint': (UI.VAE_WITH_EMBEDDED(),)}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(base_checkpoint, refiner_checkpoint, vae_checkpoint):
        return {UI.F_BASE_CHECKPOINT: base_checkpoint, UI.F_REFINER_CHECKPOINT: refiner_checkpoint, UI.F_VAE_CHECKPOINT: vae_checkpoint}

    def get(self, base_checkpoint, refiner_checkpoint, vae_checkpoint, data=None):
        if data is None:
            data = {}
        data[UI.S_CHECKPOINTS] = self.create_dict(base_checkpoint, refiner_checkpoint, vae_checkpoint)
        return (data,)
```