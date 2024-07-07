# Documentation
- Class name: ModelMergeBlockNumber
- Category: model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

The ModelMergeBlockNumber node is designed to combine multiple models into a single, tight structure. It does so by combining two input blocks to ensure that the models produced maintain the function and performance of their components. The node plays a key role in creating a uniform model that can use the advantages of its components.

# Input types
## Required
- model1
    - The `model1' parameter is the first model for consolidation. It plays a key role in determining the structure and function of the eventual consolidation model. This parameter is critical because it makes a significant contribution to the overall structure and performance of the output model.
    - Comfy dtype: MODEL
    - Python dtype: Any
- model2
    - The `model2' parameter indicates a second model to be merged. It is, like `model1', essential for the final output, affecting the properties and performance of the merged model. The combination of `model1' and `model2' aims to create a model that is stronger and more common than any individual model.
    - Comfy dtype: MODEL
    - Python dtype: Any
## Optional
- time_embed.
    - The `time_embed.' parameter is used to embed time-related information into the model. It is particularly important for models that require a time context. This parameter allows the model to consider time-based features and enhance its ability to predict.
    - Comfy dtype: FLOAT
    - Python dtype: float
- input_blocks
    - Each `input_blocks.i.' parameter, in which `i' ranges from 0 to 11, represents a block in the model input layer. These blocks are essential for processing input data and preparing them for further modelling stages. They can be configured to significantly influence model learning and the ability to generalize from input data.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: List[float]
- middle_block
    - `middle_block.i.' parameters, for `i' range from 0 to 2, correspond to blocks in the middle of the model. These blocks are essential for the intermediate steps of the model and affect how the model converts and uses input data prior to final output.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: List[float]
- output_blocks
    - The 'output_blocks.i.' parameters, where 'i' ranges from 0 to 11, define the configuration of the output blocks. These blocks are responsible for converting the internal expressions of the model into the desired output format. Their settings are essential for the model to produce accurate and meaningful results.
    - Comfy dtype: COMBO[FLOAT]
    - Python dtype: List[float]
- out.
    - The 'out.'parameter specifies the ultimate output configuration of the model. It is a key component that determines the structure of the model's prediction or output. The parameter is correctly set to ensure that the model's output is consistent with the desired format and requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- label_emb.
    - The `label_emb.' parameter is used to embed label information in models. This is particularly useful when models need to understand and incorporate disaggregated data or class labels that they process. Embedding enhances the ability of models to make informed decisions based on label data.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The'merged_model' output represents a combination model generated by the consolidation process. It encapsifies the integrated properties and functions of the input model and provides a more robust and multifunctional solution for forecasting tasks.
    - Comfy dtype: MODEL
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ModelMergeBlockNumber(comfy_extras.nodes_model_merging.ModelMergeBlocks):

    @classmethod
    def INPUT_TYPES(s):
        arg_dict = {'model1': ('MODEL',), 'model2': ('MODEL',)}
        argument = ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})
        arg_dict['time_embed.'] = argument
        arg_dict['label_emb.'] = argument
        for i in range(12):
            arg_dict['input_blocks.{}.'.format(i)] = argument
        for i in range(3):
            arg_dict['middle_block.{}.'.format(i)] = argument
        for i in range(12):
            arg_dict['output_blocks.{}.'.format(i)] = argument
        arg_dict['out.'] = argument
        return {'required': arg_dict}
```