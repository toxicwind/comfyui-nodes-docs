# Load Video (Path) 🎥🅥🅗🅢
## Documentation
- Class name: VHS_LoadVideoPath
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

VHS_LoadVideoPath node is used to load video files from a given path for integration into video processing workflows. It ensures that video files are accessible, validates paths and prepares for video follow-up processing or analysis tasks.

## Input types
### Required
- video
    - Specifies the path to the video file that you want to load so that nodes can access and process the video.
    - Comfy dtype: STRING
    - Python dtype: str
- force_rate
    - The frame rate for determining the enforcement of the loaded video allows for consistent frame rate processing between different videos.
    - Comfy dtype: INT
    - Python dtype: int
- force_size
    - Allows the required resolution of the video to be specified for standardized processing of video sizes.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- custom_width
    - Sets the custom width of the video to allow accurate video size control.
    - Comfy dtype: INT
    - Python dtype: int
- custom_height
    - Sets the custom height of the video to allow accurate video size control.
    - Comfy dtype: INT
    - Python dtype: int
- frame_load_cap
    - Limiting the number of frames to be loaded from the video helps to process the video within the memory restraint.
    - Comfy dtype: INT
    - Python dtype: int
- skip_first_frames
    - Skipping the initial frame of the specified number in the video helps to start processing in the subsequent part of the video.
    - Comfy dtype: INT
    - Python dtype: int
- select_every_nth
    - Select to load each n frame and allow thin sampling of the video frame.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- meta_batch
    - Links the loaded video to a specific batch to facilitate batch processing in the video assistant package.
    - Comfy dtype: VHS_BatchManager
    - Python dtype: VHS_BatchManager

## Output types
- IMAGE
    - Comfy dtype: IMAGE
    - Loaded video frames are used as images and are prepared for further processing.
    - Python dtype: List[Image]
- frame_count
    - Comfy dtype: INT
    - Total number of frames loaded from the video.
    - Python dtype: int
- audio
    - Comfy dtype: VHS_AUDIO
    - Tracks (if any) that are extracted from the video.
    - Python dtype: VHS_AUDIO
- video_info
    - Comfy dtype: VHS_VIDEOINFO
    - Meta-data and information on the loading of the video.
    - Python dtype: VHS_VIDEOINFO

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadVideoPath:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video": ("STRING", {"default": "X://insert/path/here.mp4", "vhs_path_extensions": video_extensions}),
                "force_rate": ("INT", {"default": 0, "min": 0, "max": 60, "step": 1}),
                 "force_size": (["Disabled", "Custom Height", "Custom Width", "Custom", "256x?", "?x256", "256x256", "512x?", "?x512", "512x512"],),
                 "custom_width": ("INT", {"default": 512, "min": 0, "max": DIMMAX, "step": 8}),
                 "custom_height": ("INT", {"default": 512, "min": 0, "max": DIMMAX, "step": 8}),
                "frame_load_cap": ("INT", {"default": 0, "min": 0, "max": BIGMAX, "step": 1}),
                "skip_first_frames": ("INT", {"default": 0, "min": 0, "max": BIGMAX, "step": 1}),
                "select_every_nth": ("INT", {"default": 1, "min": 1, "max": BIGMAX, "step": 1}),
            },
            "optional": {
                "meta_batch": ("VHS_BatchManager",)
            },
            "hidden": {
                "unique_id": "UNIQUE_ID"
            },
        }

    CATEGORY = "Video Helper Suite 🎥🅥🅗🅢"

    RETURN_TYPES = ("IMAGE", "INT", "VHS_AUDIO", "VHS_VIDEOINFO",)
    RETURN_NAMES = ("IMAGE", "frame_count", "audio", "video_info",)

    FUNCTION = "load_video"

    def load_video(self, **kwargs):
        if kwargs['video'] is None or validate_path(kwargs['video']) != True:
            raise Exception("video is not a valid path: " + kwargs['video'])
        return load_video_cv(**kwargs)

    @classmethod
    def IS_CHANGED(s, video, **kwargs):
        return hash_path(video)

    @classmethod
    def VALIDATE_INPUTS(s, video, **kwargs):
        return validate_path(video, allow_none=True)