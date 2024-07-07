# Documentation
- Class name: VideoInfoSource
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The node is intended to extract and provide basic information on video sources, such as frame numbers per second, total frame numbers, duration and dimensions. It is an important tool for understanding and further processing and analysing the underlying properties of video data.

# Input types
## Required
- video_info
    - The video_info parameter is a structured object that contains video-source metadata. It is essential for the node to function correctly and to provide accurate video information, as it directly affects the data extracted and subsequent analysis.
    - Comfy dtype: VHS_VIDEOINFO
    - Python dtype: VHS_VIDEOINFO

# Output types
- fps
    - The fps output represents the number of frames per second of the video, which is a key parameter for video play and editing, affecting the fluidity and temporal resolution of the video.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_count
    - The total number of frames in the frame_count output indicator video is important for video processing tasks such as frame extraction, animation and frame-based analysis.
    - Comfy dtype: INT
    - Python dtype: int
- duration
    - The total duration (seconds) of the output of the video is a key factor in the planning of video-related tasks and the time frame for understanding content.
    - Comfy dtype: FLOAT
    - Python dtype: float
- width
    - Width output represents the horizontal resolution of the video, which is essential to ensure the correct display and scaling of the video content.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height output represents the vertical resolution of the video, which is an important aspect of maintaining horizontal and visual quality in video processing.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class VideoInfoSource:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'video_info': ('VHS_VIDEOINFO',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    RETURN_TYPES = ('FLOAT', 'INT', 'FLOAT', 'INT', 'INT')
    RETURN_NAMES = ('fps🟨', 'frame_count🟨', 'duration🟨', 'width🟨', 'height🟨')
    FUNCTION = 'get_video_info'

    def get_video_info(self, video_info):
        keys = ['fps', 'frame_count', 'duration', 'width', 'height']
        source_info = []
        for key in keys:
            source_info.append(video_info[f'source_{key}'])
        return (*source_info,)
```