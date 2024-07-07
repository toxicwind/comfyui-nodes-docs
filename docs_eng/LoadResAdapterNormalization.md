# Documentation
- Class name: LoadResAdapterNormalization
- Category: KJNodes/experimental
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

Methodology `load_res_adapter'is designed to integrate the RResAdapter standardized weights into the given model. It ensures that the weights are correctly loaded from the specified path and applied to the standardized layer of the model, which enhances the ability of the model to process input data with standardized characteristics.

# Input types
## Required
- model
    - The parameter'model' is necessary because it represents a machine learning model that will apply the standard weight of ResAdapter. It is a key component that determines the function of nodes and the results of the standardization process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- resadapter_path
    - The parameter'resadapter_path' specifies the path to the directory that will store the standardized weight of ResAdapter. For nodes, finding and loading the right weight is essential to ensure that standardization is successfully applied to the model.
    - Comfy dtype: folder_paths.get_filename_list('checkpoints')
    - Python dtype: List[str]

# Output types
- model_clone
    - The output'model_clone' is the original model that applied the standard weight of ResAdapter. It marks a successful integration of weights, allowing the model to use standardized features to improve data processing.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LoadResAdapterNormalization:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'resadapter_path': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'load_res_adapter'
    CATEGORY = 'KJNodes/experimental'

    def load_res_adapter(self, model, resadapter_path):
        print('ResAdapter: Checking ResAdapter path')
        resadapter_full_path = folder_paths.get_full_path('checkpoints', resadapter_path)
        if not os.path.exists(resadapter_full_path):
            raise Exception('Invalid model path')
        else:
            print('ResAdapter: Loading ResAdapter normalization weights')
            prefix_to_remove = 'diffusion_model.'
            model_clone = model.clone()
            norm_state_dict = comfy.utils.load_torch_file(resadapter_full_path)
            new_values = {key[len(prefix_to_remove):]: value for (key, value) in norm_state_dict.items() if key.startswith(prefix_to_remove)}
            print('ResAdapter: Attempting to add patches with ResAdapter weights')
            try:
                for key in model.model.diffusion_model.state_dict().keys():
                    if key in new_values:
                        original_tensor = model.model.diffusion_model.state_dict()[key]
                        new_tensor = new_values[key].to(model.model.diffusion_model.dtype)
                        if original_tensor.shape == new_tensor.shape:
                            model_clone.add_object_patch(f'diffusion_model.{key}.data', new_tensor)
                        else:
                            print('ResAdapter: No match for key: ', key)
            except:
                raise Exception('Could not patch model, this way of patching was added to ComfyUI on March 3rd 2024, is your ComfyUI up to date?')
            print('ResAdapter: Added resnet normalization patches')
            return (model_clone,)
```