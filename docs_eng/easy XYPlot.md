# Documentation
- Class name: pipeXYPlot
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

PipeXYPlot is designed to simplify the process of generating and managing XY maps, providing users with a simplified interface to visualize data relationships. It focuses on providing a user-friendly experience that allows for the creation of graphics with a variety of custom options even without extensive technical knowledge.

# Input types
## Required
- grid_spacing
    - Grid spacing is a key parameter that determines the resolution of the chart. It affects the visible particle size, with higher values leading to rougher expressions, while lower values provide more detailed details.
    - Comfy dtype: INT
    - Python dtype: int
- output_individuals
    - Output individual parameters allow users to control whether each data point is drawn separately. This can significantly affect the clarity of the chart in particular when processing large data sets.
    - Comfy dtype: BOOL
    - Python dtype: bool
- flip_xy
    - Enable flip XY to allow the user to reverse the axis of the chart, which is very useful for aligning data or better visualization on the basis of a specific agreement.
    - Comfy dtype: BOOL
    - Python dtype: bool
- x_axis
    - The x_axis parameter is essential to define the horizontal axis of the chart. It determines the category or variable that will be used to represent the x value, thus shaping the structure of the chart as a whole.
    - Comfy dtype: COMBO
    - Python dtype: str
- x_values
    - The x values are essential for the construction of the chart because they provide the data points for the x axis. The correct input of these values ensures the accuracy and relevance of the chart.
    - Comfy dtype: STRING
    - Python dtype: str
- y_axis
    - The y_axis parameter is essential to define the vertical axis of the chart. It specifies the categories or variables that will be used to indicate the y-values, thereby affecting the overall interpretation of the data.
    - Comfy dtype: COMBO
    - Python dtype: str
- y_values
    - y values are essential for drawing because they represent the data points on the y axis. The accurate input of these values is necessary for the true reflection of the data in the chart.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- pipe
    - The output is called 'pipe', an integrated structure that contains the entire chart configuration, including axes, values and other settings. It serves as a channel for visualization, ensuring that the chart is generated according to the user's specifications.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict

# Usage tips
- Infra type: CPU

# Source code
```
class pipeXYPlot:
    lora_list = ['None'] + folder_paths.get_filename_list('loras')
    lora_strengths = {'min': -4.0, 'max': 4.0, 'step': 0.01}
    token_normalization = ['none', 'mean', 'length', 'length+mean']
    weight_interpretation = ['comfy', 'A1111', 'compel', 'comfy++']
    loader_dict = {'ckpt_name': folder_paths.get_filename_list('checkpoints'), 'vae_name': ['Baked-VAE'] + folder_paths.get_filename_list('vae'), 'clip_skip': {'min': -24, 'max': -1, 'step': 1}, 'lora_name': lora_list, 'lora_model_strength': lora_strengths, 'lora_clip_strength': lora_strengths, 'positive': [], 'negative': []}
    sampler_dict = {'steps': {'min': 1, 'max': 100, 'step': 1}, 'cfg': {'min': 0.0, 'max': 100.0, 'step': 1.0}, 'sampler_name': comfy.samplers.KSampler.SAMPLERS, 'scheduler': comfy.samplers.KSampler.SCHEDULERS, 'denoise': {'min': 0.0, 'max': 1.0, 'step': 0.01}, 'seed': {'min': 0, 'max': MAX_SEED_NUM}}
    plot_dict = {**sampler_dict, **loader_dict}
    plot_values = ['None']
    plot_values.append('---------------------')
    for k in sampler_dict:
        plot_values.append(f'preSampling: {k}')
    plot_values.append('---------------------')
    for k in loader_dict:
        plot_values.append(f'loader: {k}')

    def __init__(self):
        pass
    rejected = ['None', '---------------------', 'Nothing']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'grid_spacing': ('INT', {'min': 0, 'max': 500, 'step': 5, 'default': 0}), 'output_individuals': (['False', 'True'], {'default': 'False'}), 'flip_xy': (['False', 'True'], {'default': 'False'}), 'x_axis': (pipeXYPlot.plot_values, {'default': 'None'}), 'x_values': ('STRING', {'default': '', 'multiline': True, 'placeholder': 'insert values seperated by "; "'}), 'y_axis': (pipeXYPlot.plot_values, {'default': 'None'}), 'y_values': ('STRING', {'default': '', 'multiline': True, 'placeholder': 'insert values seperated by "; "'})}, 'optional': {'pipe': ('PIPE_LINE',)}, 'hidden': {'plot_dict': (pipeXYPlot.plot_dict,)}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'plot'
    CATEGORY = 'EasyUse/Pipe'

    def plot(self, grid_spacing, output_individuals, flip_xy, x_axis, x_values, y_axis, y_values, pipe=None):

        def clean_values(values):
            original_values = values.split('; ')
            cleaned_values = []
            for value in original_values:
                cleaned_value = value.strip(';').strip()
                if cleaned_value == '':
                    continue
                try:
                    cleaned_value = int(cleaned_value)
                except ValueError:
                    try:
                        cleaned_value = float(cleaned_value)
                    except ValueError:
                        pass
                cleaned_values.append(cleaned_value)
            return cleaned_values
        if x_axis in self.rejected:
            x_axis = 'None'
            x_values = []
        else:
            x_values = clean_values(x_values)
        if y_axis in self.rejected:
            y_axis = 'None'
            y_values = []
        else:
            y_values = clean_values(y_values)
        if flip_xy == 'True':
            (x_axis, y_axis) = (y_axis, x_axis)
            (x_values, y_values) = (y_values, x_values)
        xy_plot = {'x_axis': x_axis, 'x_vals': x_values, 'y_axis': y_axis, 'y_vals': y_values, 'grid_spacing': grid_spacing, 'output_individuals': output_individuals}
        if pipe is not None:
            new_pipe = pipe
            new_pipe['loader_settings'] = {**pipe['loader_settings'], 'xyplot': xy_plot}
            del pipe
        return (new_pipe, xy_plot)
```