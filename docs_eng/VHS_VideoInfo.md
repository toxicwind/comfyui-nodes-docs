# Documentation
- Class name: VideoInfo
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The `get_video_info' method at the VideoInfo node is designed to extract and return key video messages from the video information dictionary provided. It focuses on providing a simple set of video properties, such as frame rates, frame numbers, duration and dimensions, applicable to the video's source state and post-loading state. The method is used as a tool to standardize and simplify access to video metadata, which is essential for various video processing tasks.

# Input types
## Required
- video_info
    - The 'video_info' parameter is essential because it is the source of the video metadata needed for nodes. It contains detailed properties of the video, such as frame rates, frame numbers and dimensions, whether in its original state or after loading. This parameter is essential for nodes to perform the function of extracting and providing video messages.
    - Comfy dtype: VHS_VIDEOINFO
    - Python dtype: Dict[str, Union[float, int]]

# Output types
- source_fps
    - The'source_fps' output provides the number of frames per second of the original video source, which is a basic parameter for understanding the speed of video play.
    - Comfy dtype: FLOAT
    - Python dtype: float
- source_frame_count
    - The total number of frames in the'source_frame_count' output indicator original video provides insight into the frame composition of the video length.
    - Comfy dtype: INT
    - Python dtype: int
- source_duration
    - The'source_duration' output represents the duration of the original video in seconds, allowing for an assessment of the length of the video.
    - Comfy dtype: FLOAT
    - Python dtype: float
- source_width
    - The'source_width' output provides video width in pixels, which is one of the key dimensions of video resolution.
    - Comfy dtype: INT
    - Python dtype: int
- source_height
    - The'source_height' output specifies the height of the video, in pixels, defining the resolution of the video with width.
    - Comfy dtype: INT
    - Python dtype: int
- loaded_fps
    - The 'loaded_fps' output represents the number of frames per second of a video load, which may differ from the source video as a result of processing or playing adjustments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- loaded_frame_count
    - The 'loaded_frame_count' output reflects the total frame number of video loads and may be affected by video processing operations.
    - Comfy dtype: INT
    - Python dtype: int
- loaded_duration
    - The 'loaded_duration' output represents the duration of the video after loading, which may differ from the original video because of changes in the speed of play or editing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- loaded_width
    - The 'loaded_width' output provides the width of the video load, which may differ from the source video by scaling or resizing.
    - Comfy dtype: INT
    - Python dtype: int
- loaded_height
    - The 'loaded_height' output specifies the height of the video load, which may differ in size from the source video as a result of video processing.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class VideoInfo:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'video_info': ('VHS_VIDEOINFO',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    RETURN_TYPES = ('FLOAT', 'INT', 'FLOAT', 'INT', 'INT', 'FLOAT', 'INT', 'FLOAT', 'INT', 'INT')
    RETURN_NAMES = ('source_fps🟨', 'source_frame_count🟨', 'source_duration🟨', 'source_width🟨', 'source_height🟨', 'loaded_fps🟦', 'loaded_frame_count🟦', 'loaded_duration🟦', 'loaded_width🟦', 'loaded_height🟦')
    FUNCTION = 'get_video_info'

    def get_video_info(self, video_info):
        keys = ['fps', 'frame_count', 'duration', 'width', 'height']
        source_info = []
        loaded_info = []
        for key in keys:
            source_info.append(video_info[f'source_{key}'])
            loaded_info.append(video_info[f'loaded_{key}'])
        return (*source_info, *loaded_info)
```