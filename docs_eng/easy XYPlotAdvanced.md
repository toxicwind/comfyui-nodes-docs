# Documentation
- Class name: pipeXYPlotAdvanced
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node provides an advanced XY mapping function designed specifically to meet the needs of the pipe line. It is integrated with various data types and settings to generate visualized graphs that provide insight into the structure and relationships of data in the pipe. The node is designed to emphasize adaptability and ease of use, ensuring that users can quickly generate meaningful visualized charts without the need for extensive configuration.

# Input types
## Required
- pipe
    - The `pipe' parameter is the backbone of this node, representing the conduit lines from which data are extracted and visualized. It is essential for the operation of the node, because it contains all the necessary information and settings for drawing.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- grid_spacing
    - The `grid_spacing' parameter determines the distance between grid lines in the chart, affecting the overall clarity and readability of visualization. It plays an important role in presenting data points and trends in an understandable way.
    - Comfy dtype: INT
    - Python dtype: int
- output_individuals
    - The `output_individuals' parameter allows users to control whether individual data points are shown separately in the chart. This is important for the analysis of particular data points and their relationship to data concentration.
    - Comfy dtype: BOOL
    - Python dtype: bool
- flip_xy
    - The `flip_xy' parameter allows users to flip X-axis and Y-axis, which is very useful in some data visualization scenarios, especially when traditional directions are not the best option.
    - Comfy dtype: BOOL
    - Python dtype: bool
## Optional
- X
    - The `X' parameter represents the configuration of the X axis, including the axle labels and associated values. It is essential to define the horizontal dimensions of the chart and can be customized through various models and settings.
    - Comfy dtype: X_Y
    - Python dtype: Dict
- Y
    - The 'Y' parameter corresponds to the configuration of the Y axis, specifying the axle labels and corresponding values. It is essential for building the vertical dimensions of the chart and can be adjusted by different models and settings.
    - Comfy dtype: X_Y
    - Python dtype: Dict

# Output types
- pipe
    - The ‘pipe’ output is an updated version of the input ‘pipe’, which now contains the generated XY chart information. It represents the progress of the pipeline and re-assembles the visualization results into the data stream for further analysis or processing.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class pipeXYPlotAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'grid_spacing': ('INT', {'min': 0, 'max': 500, 'step': 5, 'default': 0}), 'output_individuals': (['False', 'True'], {'default': 'False'}), 'flip_xy': (['False', 'True'], {'default': 'False'})}, 'optional': {'X': ('X_Y',), 'Y': ('X_Y',)}, 'hidden': {'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'plot'
    CATEGORY = 'EasyUse/Pipe'

    def plot(self, pipe, grid_spacing, output_individuals, flip_xy, X=None, Y=None, my_unique_id=None):
        if X != None:
            x_axis = X.get('axis')
            x_values = X.get('values')
        else:
            x_axis = 'Nothing'
            x_values = ['']
        if Y != None:
            y_axis = Y.get('axis')
            y_values = Y.get('values')
        else:
            y_axis = 'Nothing'
            y_values = ['']
        if pipe is not None:
            new_pipe = pipe
            positive = pipe['loader_settings']['positive'] if 'positive' in pipe['loader_settings'] else ''
            negative = pipe['loader_settings']['negative'] if 'negative' in pipe['loader_settings'] else ''
            if x_axis == 'advanced: ModelMergeBlocks':
                models = X.get('models')
                vae_use = X.get('vae_use')
                if models is None:
                    raise Exception('models is not found')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'models': models, 'vae_use': vae_use}
            if y_axis == 'advanced: ModelMergeBlocks':
                models = Y.get('models')
                vae_use = Y.get('vae_use')
                if models is None:
                    raise Exception('models is not found')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'models': models, 'vae_use': vae_use}
            if x_axis in ['advanced: Lora', 'advanced: Checkpoint']:
                lora_stack = X.get('lora_stack')
                _lora_stack = []
                if lora_stack is not None:
                    for lora in lora_stack:
                        _lora_stack.append({'lora_name': lora[0], 'model': pipe['model'], 'clip': pipe['clip'], 'model_strength': lora[1], 'clip_strength': lora[2]})
                del lora_stack
                x_values = '; '.join(x_values)
                lora_stack = pipe['lora_stack'] + _lora_stack if 'lora_stack' in pipe else _lora_stack
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'lora_stack': lora_stack}
            if y_axis in ['advanced: Lora', 'advanced: Checkpoint']:
                lora_stack = Y.get('lora_stack')
                _lora_stack = []
                if lora_stack is not None:
                    for lora in lora_stack:
                        _lora_stack.append({'lora_name': lora[0], 'model': pipe['model'], 'clip': pipe['clip'], 'model_strength': lora[1], 'clip_strength': lora[2]})
                del lora_stack
                y_values = '; '.join(y_values)
                lora_stack = pipe['lora_stack'] + _lora_stack if 'lora_stack' in pipe else _lora_stack
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'lora_stack': lora_stack}
            if x_axis == 'advanced: Seeds++ Batch':
                if new_pipe['seed']:
                    value = x_values
                    x_values = []
                    for index in range(value):
                        x_values.append(str(new_pipe['seed'] + index))
                    x_values = '; '.join(x_values)
            if y_axis == 'advanced: Seeds++ Batch':
                if new_pipe['seed']:
                    value = y_values
                    y_values = []
                    for index in range(value):
                        y_values.append(str(new_pipe['seed'] + index))
                    y_values = '; '.join(y_values)
            if x_axis == 'advanced: Positive Prompt S/R':
                if positive:
                    x_value = x_values
                    x_values = []
                    for (index, value) in enumerate(x_value):
                        (search_txt, replace_txt, replace_all) = value
                        if replace_all:
                            txt = replace_txt if replace_txt is not None else positive
                            x_values.append(txt)
                        else:
                            txt = positive.replace(search_txt, replace_txt, 1) if replace_txt is not None else positive
                            x_values.append(txt)
                    x_values = '; '.join(x_values)
            if y_axis == 'advanced: Positive Prompt S/R':
                if positive:
                    y_value = y_values
                    y_values = []
                    for (index, value) in enumerate(y_value):
                        (search_txt, replace_txt, replace_all) = value
                        if replace_all:
                            txt = replace_txt if replace_txt is not None else positive
                            y_values.append(txt)
                        else:
                            txt = positive.replace(search_txt, replace_txt, 1) if replace_txt is not None else positive
                            y_values.append(txt)
                    y_values = '; '.join(y_values)
            if x_axis == 'advanced: Negative Prompt S/R':
                if negative:
                    x_value = x_values
                    x_values = []
                    for (index, value) in enumerate(x_value):
                        (search_txt, replace_txt, replace_all) = value
                        if replace_all:
                            txt = replace_txt if replace_txt is not None else negative
                            x_values.append(txt)
                        else:
                            txt = negative.replace(search_txt, replace_txt, 1) if replace_txt is not None else negative
                            x_values.append(txt)
                    x_values = '; '.join(x_values)
            if y_axis == 'advanced: Negative Prompt S/R':
                if negative:
                    y_value = y_values
                    y_values = []
                    for (index, value) in enumerate(y_value):
                        (search_txt, replace_txt, replace_all) = value
                        if replace_all:
                            txt = replace_txt if replace_txt is not None else negative
                            y_values.append(txt)
                        else:
                            txt = negative.replace(search_txt, replace_txt, 1) if replace_txt is not None else negative
                            y_values.append(txt)
                    y_values = '; '.join(y_values)
            if 'advanced: ControlNet' in x_axis:
                x_value = x_values
                x_values = []
                cnet = []
                for (index, value) in enumerate(x_value):
                    cnet.append(value)
                    x_values.append(str(index))
                x_values = '; '.join(x_values)
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'cnet_stack': cnet}
            if 'advanced: ControlNet' in y_axis:
                y_value = y_values
                y_values = []
                cnet = []
                for (index, value) in enumerate(y_value):
                    cnet.append(value)
                    y_values.append(str(index))
                y_values = '; '.join(y_values)
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'cnet_stack': cnet}
            if 'advanced: Pos Condition' in x_axis:
                x_values = '; '.join(x_values)
                cond = X.get('cond')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'positive_cond_stack': cond}
            if 'advanced: Pos Condition' in y_axis:
                y_values = '; '.join(y_values)
                cond = Y.get('cond')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'positive_cond_stack': cond}
            if 'advanced: Neg Condition' in x_axis:
                x_values = '; '.join(x_values)
                cond = X.get('cond')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'negative_cond_stack': cond}
            if 'advanced: Neg Condition' in y_axis:
                y_values = '; '.join(y_values)
                cond = Y.get('cond')
                new_pipe['loader_settings'] = {**pipe['loader_settings'], 'negative_cond_stack': cond}
            del pipe
        return pipeXYPlot().plot(grid_spacing, output_individuals, flip_xy, x_axis, x_values, y_axis, y_values, new_pipe)
```