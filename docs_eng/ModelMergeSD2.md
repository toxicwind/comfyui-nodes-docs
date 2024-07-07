# Documentation
- Class name: ModelMergeSD1
- Category: advanced/model_merging/model_specific
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Model MergeSD1 node is designed to integrate multiple models into a single framework. It is dedicated to combining model-specific components, allowing seamless and efficient integration processes. The node plays a key role in advanced model consolidation and enhances the functionality and performance of integrated models.

# Input types
## Required
- model1
    - The `model1' parameter is essential because it represents the first model to be merged into the framework. Its integration is an essential step towards achieving the purpose of the node consolidation model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The `model2' parameter represents the second model to be merged. It is a key component of the consolidation process, complementary to the first model, forming a comprehensive model structure.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- time_embed.
    - The `time_embed.' parameter is used to embed time-related information into the model. It affects how time dynamics are captured within the merger model and enhances their ability to process time-sensitive data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- input_blocks.
    - For each index `i' in the range 0 to 11, `input_blocks.{}. } represents a block that handles input data. These blocks are essential during the initial stages of model consolidation to shape input features for subsequent processing.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- middle_block.
    - `middle_block.{}.' Parameters in which the range `i' is zero to two, representing intermediate treatment blocks within the model. These blocks play an important role in model integration and conversion of data in the merged architecture.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- output_blocks.
    - Similar to `input_blocks.', the range `output_blocks.{}.' in `output_blocks.} is 0 to 11, representing the final stage of processing of the merged model. These blocks are essential for refining the output of the model to meet specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- out.
    - The `out.' parameter defines the final output configuration of the merged model. It is important because it determines the format and structure of model predictions or results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class ModelMergeSD1(comfy_extras.nodes_model_merging.ModelMergeBlocks):
    CATEGORY = 'advanced/model_merging/model_specific'

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