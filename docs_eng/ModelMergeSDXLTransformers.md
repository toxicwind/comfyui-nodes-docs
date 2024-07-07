# Documentation
- Class name: ModelMergeSDXLTransformers
- Category: model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

ModelMergeSDXLTransformers nodes are designed to integrate multiple models into a single structure, using a transformer-based structure. Its purpose is to harmonize the functions of the models and improve overall performance through complex integration processes.

# Input types
## Required
- model1
    - The `model1' parameter is the first model to be merged, which is essential for the initial structure of the portfolio model. It sets the basis for the integration process and significantly affects the ability of the final model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The `model2' parameter represents the second model to be merged and plays a key role in the final configuration of the merged model. Its integration with `model1' is essential to achieving the desired performance enhancement.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- input_blocks
    - The `input_blocks' parameter defines the set of parameters for the initial change blocks within the model. Each block is adjustable and helps the model to process input data efficiently.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: Dict[str, Union[float, Dict[str, float]]]
- middle_block
    - The `middle_block' parameter includes a set of variable blocks located between model input and output. It plays an important role in further refining the processing capacity of the model.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: Dict[str, Dict[str, float]]
- output_blocks
    - The `output_blocks' parameters consist of variable blocks that make up the final stage of the model. These blocks are essential in determining the quality of model output and overall predictive capability.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: Dict[str, Union[float, Dict[str, float]]]
- out
    - The 'out'parameter is used to adjust the ultimate output layer of the model. It is important for fine-tuning model predictions to meet specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The `merged_model' output represents the integrated model produced during the consolidation process. It contains the combination capabilities and learning features of the original model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class ModelMergeSDXLTransformers(comfy_extras.nodes_model_merging.ModelMergeBlocks):

    @classmethod
    def INPUT_TYPES(s):
        arg_dict = {'model1': ('MODEL',), 'model2': ('MODEL',)}
        argument = ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})
        arg_dict['time_embed.'] = argument
        arg_dict['label_emb.'] = argument
        transformers = {4: 2, 5: 2, 7: 10, 8: 10}
        for i in range(9):
            arg_dict['input_blocks.{}.0.'.format(i)] = argument
            if i in transformers:
                arg_dict['input_blocks.{}.1.'.format(i)] = argument
                for j in range(transformers[i]):
                    arg_dict['input_blocks.{}.1.transformer_blocks.{}.'.format(i, j)] = argument
        for i in range(3):
            arg_dict['middle_block.{}.'.format(i)] = argument
            if i == 1:
                for j in range(10):
                    arg_dict['middle_block.{}.transformer_blocks.{}.'.format(i, j)] = argument
        transformers = {3: 2, 4: 2, 5: 2, 6: 10, 7: 10, 8: 10}
        for i in range(9):
            arg_dict['output_blocks.{}.0.'.format(i)] = argument
            t = 8 - i
            if t in transformers:
                arg_dict['output_blocks.{}.1.'.format(i)] = argument
                for j in range(transformers[t]):
                    arg_dict['output_blocks.{}.1.transformer_blocks.{}.'.format(i, j)] = argument
        arg_dict['out.'] = argument
        return {'required': arg_dict}
```