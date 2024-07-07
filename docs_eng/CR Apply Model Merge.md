# Documentation
- Class name: CR_ApplyModelMerge
- Category: Comfyroll/Model Merge
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ApplyModelMrage node is designed to facilitate the consolidation of multiple models into a single single uniform model. It uses intelligent combinations of model ratios and clipping scales, i.e., the standardization where necessary, and the application of the specified combination method to create a harmonious mix of selected models. This node is essential for advanced model management, enabling users to try different models and scales to achieve the desired results.

# Input types
## Required
- model_stack
    - Modelbed parameters are essential because it defines the sequence of models to be merged. It plays a central role in the implementation of nodes, determining the model that will contribute to the eventual consolidation model.
    - Comfy dtype: MODEL_STACK
    - Python dtype: List[Tuple[str, float, float]]
- merge_method
    - The parameters of the consolidation method determine how the model is to be combined. It is a key element of the node function, as it determines the algorithm to be used for consolidation, which can significantly influence the characteristics of the result model.
    - Comfy dtype: COMBO['Recursive', 'Weighted']
    - Python dtype: str
- normalise_ratios
    - The normaise_ratios parameter is important because it indicates whether the ratio should be normalized. It is important to ensure that the ratio accurately reflects the expected contribution of each model to the consolidated results.
    - Comfy dtype: COMBO['Yes', 'No']
    - Python dtype: str
- weight_factor
    - The weight factor parameter influences the weight of the model during the consolidation process. It is essential to fine-tune the contribution of each model to the eventual consolidation model, allowing for precise control of results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - MODEL output provides a consolidation model obtained by applying the consolidation method and specifying parameters. It represents the top point of node processing and is essential to the user's workflow.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- CLIP
    - The CLIP output provides a CLIP model associated with the merger model. It is important because it makes it possible to use the CLIP model framework for further processing or analysis.
    - Comfy dtype: CLIP
    - Python dtype: comfy.model_management.CLIP
- model_mix_info
    - The model_mix_info output provides a detailed report on the consolidation process, including the name and scale of the model used. This information is valuable for understanding the composition of the merger model and for recording the consolidation process.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help provides a link to the document for further help. This is a useful resource for users seeking more information on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ApplyModelMerge:

    @classmethod
    def INPUT_TYPES(s):
        merge_methods = ['Recursive', 'Weighted']
        return {'required': {'model_stack': ('MODEL_STACK',), 'merge_method': (merge_methods,), 'normalise_ratios': (['Yes', 'No'],), 'weight_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'model_mix_info', 'show_help')
    FUNCTION = 'merge'
    CATEGORY = icons.get('Comfyroll/Model Merge')

    def merge(self, model_stack, merge_method, normalise_ratios, weight_factor):
        sum_clip_ratio = 0
        sum_model_ratio = 0
        model_mix_info = str('Merge Info:\n')
        if len(model_stack) == 0:
            print(f'[Warning] Apply Model Merge: No active models selected in the model merge stack')
            return ()
        if len(model_stack) == 1:
            print(f'[Warning] Apply Model Merge: Only one active model found in the model merge stack. At least 2 models are normally needed for merging. The active model will be output.')
            (model_name, model_ratio, clip_ratio) = model_stack[0]
            ckpt_path = folder_paths.get_full_path('checkpoints', model_name)
            return comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        for (i, model_tuple) in enumerate(model_stack):
            (model_name, model_ratio, clip_ratio) = model_tuple
            sum_model_ratio += model_ratio
            sum_clip_ratio += clip_ratio
        model_mix_info = model_mix_info + 'Ratios are applied using the Recursive method\n\n'
        for (i, model_tuple) in enumerate(model_stack):
            (model_name, model_ratio, clip_ratio) = model_tuple
            ckpt_path = folder_paths.get_full_path('checkpoints', model_name)
            merge_model = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
            print(f'Apply Model Merge: Model Name {model_name}, Model Ratio {model_ratio}, CLIP Ratio {clip_ratio}')
            if sum_model_ratio != 1 and normalise_ratios == 'Yes':
                print(f'[Warning] Apply Model Merge: Sum of model ratios != 1. Ratios will be normalised')
                model_ratio = round(model_ratio / sum_model_ratio, 2)
                clip_ratio = round(clip_ratio / sum_clip_ratio, 2)
            if merge_method == 'Weighted':
                if i == 1:
                    model_ratio = 1 - weight_factor + weight_factor * model_ratio
                    clip_ratio = 1 - weight_factor + weight_factor * clip_ratio
            if i == 0:
                model1 = merge_model[0].clone()
                clip1 = merge_model[1].clone()
                model_mix_info = model_mix_info + 'Base Model Name: ' + model_name
            else:
                model2 = merge_model[0].clone()
                kp = model2.get_key_patches('diffusion_model.')
                for k in kp:
                    model1.add_patches({k: kp[k]}, model_ratio, 1.0 - model_ratio)
                clip2 = merge_model[1].clone()
                kp = clip2.get_key_patches()
                for k in kp:
                    if k.endswith('.position_ids') or k.endswith('.logit_scale'):
                        continue
                    clip1.add_patches({k: kp[k]}, clip_ratio, 1.0 - clip_ratio)
                model_mix_info = model_mix_info + '\nModel Name: ' + model_name + '\nModel Ratio: ' + str(model_ratio) + '\nCLIP Ratio: ' + str(clip_ratio) + '\n'
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Model-Merge-Nodes#cr-apply-model-merge'
        return (model1, clip1, model_mix_info, show_help)
```