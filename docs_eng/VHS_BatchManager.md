# Documentation
- Class name: BatchManager
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

BatchManager nodes are designed to efficiently manage and organize a frame batch of video processing tasks. It handles complexity in abstract terms by dividing a large amount of data into manageable batches, ensuring that the flow line remains efficient and fluid.

# Input types
## Required
- frames_per_batch
    - The parameter'frames_per_batch' determines the number of frames to be dealt with in each batch. It is essential to control the workload and the use of memory, directly affecting the performance and efficiency of the video processing system.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- prompt
    - The 'prompt' parameter is provided to include additional instructions or context that may be required for batch processing. It can influence how BatchManager nodes interpret and process input data.
    - Comfy dtype: PROMPT
    - Python dtype: str
- unique_id
    - The parameter'unique_id' is used to identify specific batches in the system to ensure that the processing process can be accurately tracked and managed. It plays a critical role in maintaining the integrity and organizational nature of the batch processing workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- meta_batch
    - The'meta_batch' output provides a structured indication of the batch that has been processed. It covers results and metadata and is a key point for further analysis or downstream processing tasks.
    - Comfy dtype: VHS_BatchManager
    - Python dtype: BatchManager

# Usage tips
- Infra type: CPU

# Source code
```
class BatchManager:

    def __init__(self, frames_per_batch=-1):
        self.frames_per_batch = frames_per_batch
        self.inputs = {}
        self.outputs = {}
        self.unique_id = None
        self.has_closed_inputs = False

    def reset(self):
        self.close_inputs()
        for key in self.outputs:
            if getattr(self.outputs[key][-1], 'gi_suspended', False):
                try:
                    self.outputs[key][-1].send(None)
                except StopIteration:
                    pass
        self.__init__(self.frames_per_batch)

    def has_open_inputs(self):
        return len(self.inputs) > 0

    def close_inputs(self):
        for key in self.inputs:
            if getattr(self.inputs[key][-1], 'gi_suspended', False):
                try:
                    self.inputs[key][-1].send(1)
                except StopIteration:
                    pass
        self.inputs = {}

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'frames_per_batch': ('INT', {'default': 16, 'min': 1, 'max': 128, 'step': 1})}, 'hidden': {'prompt': 'PROMPT', 'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('VHS_BatchManager',)
    RETURN_NAMES = ('meta_batch',)
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    FUNCTION = 'update_batch'

    def update_batch(self, frames_per_batch, prompt=None, unique_id=None):
        if unique_id is not None and prompt is not None:
            requeue = prompt[unique_id]['inputs'].get('requeue', 0)
        else:
            requeue = 0
        if requeue == 0:
            self.reset()
            self.frames_per_batch = frames_per_batch
            self.unique_id = unique_id
        return (self,)
```