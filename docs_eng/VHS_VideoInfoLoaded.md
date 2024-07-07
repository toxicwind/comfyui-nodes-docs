# Documentation
- Class name: VideoInfoLoaded
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The `get_video_info' method of the VideoInfoLoded node is designed to extract and return key video messages, including frame numbers (fps), number of frames, length, width and height per second. This node plays a key role in providing structured summaries of video metadata, which is critical for further video processing and analysis tasks.

# Input types
## Required
- video_info
    - The 'video_info' parameter is the key input to the VideoInfoLoaded node, as it contains the loaded video metadata needed to run the node. It directly affects the ability of the node to extract and return accurate video information.
    - Comfy dtype: VHS_VIDEOINFO
    - Python dtype: Dict[str, Union[float, int]]

# Output types
- fps
    - The 'fps' output represents the number of frames per second of the video, which is a key parameter for understanding the speed of video play and is essential for the compatibility of video editing and play.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_count
    - The 'frame_count' output provides the total number of frames in the video, which is essential for estimating the duration of the video and the various analytical and processing workflows.
    - Comfy dtype: INT
    - Python dtype: int
- duration
    - The 'duration' output represents the total length of the video in seconds, which is the basic information used for timing and synchronization in video production.
    - Comfy dtype: FLOAT
    - Python dtype: float
- width
    - The 'width' output, which represents the width of the video in pixels, determines with height the width of the video, which is important for presentation and format considerations.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' output assigns the height of the video in pixels, complements the width, defines the overall resolution of the video and is a key factor in the visual clarity of the video.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class VideoInfoLoaded:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'video_info': ('VHS_VIDEOINFO',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    RETURN_TYPES = ('FLOAT', 'INT', 'FLOAT', 'INT', 'INT')
    RETURN_NAMES = ('fps🟦', 'frame_count🟦', 'duration🟦', 'width🟦', 'height🟦')
    FUNCTION = 'get_video_info'

    def get_video_info(self, video_info):
        keys = ['fps', 'frame_count', 'duration', 'width', 'height']
        loaded_info = []
        for key in keys:
            loaded_info.append(video_info[f'loaded_{key}'])
        return (*loaded_info,)
```