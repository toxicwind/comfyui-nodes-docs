# Documentation
- Class name: KfGetScheduleConditionSlice
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to extract and process the data on the conditions of the given time interval from the given timetable. By dividing the schedule into a series of time sheets, it assesses the conditions of each piece of time and aggregates the results to provide a comprehensive overview of the conditions within the specified time span.

# Input types
## Required
- schedule
    - Time frame parameters are essential because they contain structured data that define conditions over time. It is the main input parameter, which determines the operation of nodes and the quality of output.
    - Comfy dtype: SCHEDULE
    - Python dtype: dict
## Optional
- start
    - The starting parameter specifies the start of the time interval of the node processing schedule. It is important because it sets the starting point for the time slice operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- step
    - The step parameter defines the interval between each piece of time. It is important because it affects the particle size of the condition data extracted.
    - Comfy dtype: FLOAT
    - Python dtype: float
- n
    - The n parameter determines how many time sheets the schedule is divided into. It is critical because it determines the number of individual evaluations performed at the node.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- CONDITIONING
    - The output provides a detailed and structured indication of the conditions to be extracted from the schedule at specified intervals. It is important because it contains the results of node operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: list

# Usage tips
- Infra type: CPU

# Source code
```
class KfGetScheduleConditionSlice:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('CONDITIONING',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'schedule': ('SCHEDULE', {}), 'start': ('FLOAT', {'default': 0}), 'step': ('FLOAT', {'default': 1}), 'n': ('INT', {'default': 24})}}

    def main(self, schedule, start, step, n):
        stop = start + n * step
        times = np.linspace(start=start, stop=stop, num=n, endpoint=True)
        conds = [evaluate_schedule_at_time(schedule, time)[0] for time in times]
        lerped_tokenized = [c[0] for c in conds]
        lerped_pooled = [c[1]['pooled_output'] for c in conds]
        lerped_tokenized_t = torch.cat(lerped_tokenized, dim=0)
        out_dict = deepcopy(conds[0][1])
        if isinstance(lerped_pooled[0], torch.Tensor) and isinstance(lerped_pooled[-1], torch.Tensor):
            out_dict['pooled_output'] = torch.cat(lerped_pooled, dim=0)
        return [[(lerped_tokenized_t, out_dict)]]
```