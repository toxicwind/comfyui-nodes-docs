# Documentation
- Class name: ModelMergeSDXL
- Category: Model Merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

Model MergeSDXL nodes are designed to integrate multiple models into a single structure that allows for complex interactions and performance enhancement. It focuses on combining different models in a way that preserves their respective characteristics and achieves collective functions.

# Input types
## Required
- model1
    - The `model1' parameter is the first model to be merged, which is essential to the initial structure of the consolidated model. It sets the basis for the integration process and affects the ultimate capacity of the unified model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The `model2' parameter represents the second model to be merged, which complements the first model and contributes to the overall complexity and performance of the merged model. Integration is key to achieving the desired function.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- time_embed.
    - The `time_embed.' parameter allows time dynamics to be incorporated into the model, influencing how the model processes and interprets time-based data. It is an optional but important feature for time-sensitive applications.
    - Comfy dtype: FLOAT
    - Python dtype: float
- input_blocks.
    - The `input_blocks.' parameter is a combination of nine FLOAT values, defining the conversion blocks of the input layer. Each index `i' represents a unique block in the range 0-8 and facilitates initial data processing.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- middle_block.
    - The `middle_block.' parameters consist of three FLOAT values, each corresponding to a block in the middle of the model. These blocks are essential for intermediate processing steps and affect the ability to model learning and generalization.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- output_blocks.
    - The `output_blocks.' parameter consists of nine FLOAT values used to configure the conversion blocks of the output layer. Similar to `input_blocks.', each index `i' specifies a block from 0 to 8 that forms the final output of the model.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- out.
    - The `out.' parameter is a FLOAT value that represents the final output configuration of the merged model. It is used to fine-tune the predictions or results of the model according to the characteristics of the integrated model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The'merged_model' output is the result of a consolidation process that contains a combination of input model functions. It is a key component for further analysis or deployment in various applications.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class ModelMergeSDXL(comfy_extras.nodes_model_merging.ModelMergeBlocks):

    @classmethod
    def INPUT_TYPES(s):
        arg_dict = {'model1': ('MODEL',), 'model2': ('MODEL',)}
        argument = ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})
        arg_dict['time_embed.'] = argument
        arg_dict['label_emb.'] = argument
        for i in range(9):
            arg_dict['input_blocks.{}'.format(i)] = argument
        for i in range(3):
            arg_dict['middle_block.{}'.format(i)] = argument
        for i in range(9):
            arg_dict['output_blocks.{}'.format(i)] = argument
        arg_dict['out.'] = argument
        return {'required': arg_dict}
```