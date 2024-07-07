# Documentation
- Class name: LoadVideoUpload
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The LoadVideoUpload node is designed to manage and process video files efficiently. It can load videos from multiple sources, including local files and URLs, and provide functionality for sampling and operating video frames. The node ensures that video data are properly formatted and ready for follow-up processing.

# Input types
## Required
- video
    - The 'video' parameter is essential because it specifies the source of the video file to be processed. It can refer to the path to the local file or to the URL of the online video. This parameter directly affects the ability of nodes to load and access video content.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- force_rate
    - The 'force_rate' parameter allows the frame rate of the video to be adjusted. This is an optional setting that can be used to ensure consistency of frame rates between different videos, which is important for some video processing tasks.
    - Comfy dtype: INT
    - Python dtype: int
- force_size
    - The 'force_size' parameter is used to specify the desired resolution of the video frame. It provides several preset options and allows for custom sizes, which may be necessary to maintain a vertical ratio or to adapt to specific display requirements.
    - Comfy dtype: STRING
    - Python dtype: str
- custom_width
    - When a custom video size is required, 'custom_width' sets the width of the video frame. This is an important parameter for the video-size adjustment operation to ensure that the video adapts to the width limits required.
    - Comfy dtype: INT
    - Python dtype: int
- custom_height
    - The 'custom_height' parameter supplements 'custom_width' by setting the height of the video frame. It plays an important role in the re-sizeing of the video, especially when video content requires a specific height.
    - Comfy dtype: INT
    - Python dtype: int
- frame_load_cap
    - The 'frame_load_cap' parameter determines the maximum number of frames to be loaded from the video. It helps to control memory usage and processing times, especially when processing long videos.
    - Comfy dtype: INT
    - Python dtype: int
- skip_first_frames
    - The'skip_first_frames' parameter allows nodes to skip the number of frames specified at the beginning of the video. This is useful for omitting unwanted content or fragments from the video processing workflow.
    - Comfy dtype: INT
    - Python dtype: int
- select_every_nth
    - The'select_every_nth' parameter is used to select frames at regular intervals from the video. It helps to reduce frame rates or create summaries of video content.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The 'IMAGE' output provides video frames in volume, a multi-dimensional array for further video analysis and processing.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor
- frame_count
    - The total number of frames that the `frame_count' output indicates are loaded from the video is essential for understanding the extent of the video data.
    - Comfy dtype: INT
    - Python dtype: int
- audio
    - The 'udio' output is a function that, when called, provides access to the audio stream of the video. This can be used for audio analysis or for further processing with the frame of the video.
    - Comfy dtype: FUNCTION
    - Python dtype: Callable[[], Any]
- video_info
    - The 'video_info' output contains metadata about the video, such as frame rates, duration and dimensions. This information is valuable for various video processing tasks that need to understand video properties.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Union[int, float, str]]

# Usage tips
- Infra type: CPU

# Source code
```
class LoadVideoUpload:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = []
        for f in os.listdir(input_dir):
            if os.path.isfile(os.path.join(input_dir, f)):
                file_parts = f.split('.')
                if len(file_parts) > 1 and file_parts[-1] in video_extensions:
                    files.append(f)
        return {'required': {'video': (sorted(files),), 'force_rate': ('INT', {'default': 0, 'min': 0, 'max': 60, 'step': 1}), 'force_size': (['Disabled', 'Custom Height', 'Custom Width', 'Custom', '256x?', '?x256', '256x256', '512x?', '?x512', '512x512'],), 'custom_width': ('INT', {'default': 512, 'min': 0, 'max': DIMMAX, 'step': 8}), 'custom_height': ('INT', {'default': 512, 'min': 0, 'max': DIMMAX, 'step': 8}), 'frame_load_cap': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX, 'step': 1}), 'skip_first_frames': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX, 'step': 1}), 'select_every_nth': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}, 'optional': {'meta_batch': ('VHS_BatchManager',)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    RETURN_TYPES = ('IMAGE', 'INT', 'VHS_AUDIO', 'VHS_VIDEOINFO')
    RETURN_NAMES = ('IMAGE', 'frame_count', 'audio', 'video_info')
    FUNCTION = 'load_video'

    def load_video(self, **kwargs):
        return load_video_cv(**kwargs)

    @classmethod
    def IS_CHANGED(s, video, **kwargs):
        image_path = folder_paths.get_annotated_filepath(video)
        return calculate_file_hash(image_path)

    @classmethod
    def VALIDATE_INPUTS(s, video, force_size, **kwargs):
        import requests
        if video.startswith('http'):
            resp = requests.head(video)
            if resp.status_code != 200:
                return 'Invalid video file: {}'.format(video)
        elif not folder_paths.exists_annotated_filepath(video):
            return 'Invalid video file: {}'.format(video)
        return True
```