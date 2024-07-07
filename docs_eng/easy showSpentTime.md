# Documentation
- Class name: showSpentTime
- Category: EasyUse/Util
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

ShowSpentTime is designed to provide feedback on workflow processing time. It captures the time spent on reasoning and shows in UI that it allows users to see the efficiency of the system. This node is essential for monitoring performance and identifying potential bottlenecks in the execution pipeline.

# Input types
## Required
- pipe
    - The pipe parameter is essential because it represents the data pipeline that is being processed. It contains all the information that is needed for the normal operation of the node, including a loader setting that may contain the spent_time.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
## Optional
- spent_time
    - If this parameter is provided, it will be used to show the time spent in UI. If it is not provided, the node will try to retrieve the time spent in the Pipe's loader settings.
    - Comfy dtype: INFO
    - Python dtype: Union[str, None]
- unique_id
    - The unique_id parameter is used to identify a particular node in the workflow. This is essential to link the time spent to the correct node in the workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - This parameter contains additional information about the image processing workflow, including the workflow itself. It is used to locate specific nodes associated with unique_id.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- ui
    - ui Output is a dictionary that contains text that will be displayed in the user interface and provides information on the time spent.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, str
- result
    - The result output is an empty dictionary, indicating that the primary purpose of this node is to display information rather than to transmit data for further processing.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class showSpentTime:

    @classmethod
    def INPUT_TYPES(s):
        Return {required':'pipe': (`PIPE_LINE','),'spent_time': (`INFO', {default':'will show the time of reasoning', 'forceInput': False}), 'hidden': {unique_id':'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO')
    FUNCTION = 'notify'
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    CATEGORY = 'EasyUse/Util'

    def notify(self, pipe, spent_time=None, unique_id=None, extra_pnginfo=None):
        if unique_id and extra_pnginfo and ('workflow' in extra_pnginfo):
            workflow = extra_pnginfo['workflow']
            node = next((x for x in workflow['nodes'] if str(x['id']) == unique_id), None)
            if node:
                spent_time = pipe['loader_settings']['spent_time'] if 'spent_time' in pipe['loader_settings'] else ''
                node['widgets_values'] = [spent_time]
        return {'ui': {'text': spent_time}, 'result': {}}
```