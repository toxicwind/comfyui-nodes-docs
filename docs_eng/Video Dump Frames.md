# Documentation
- Class name: WAS_Video_Frame_Dump
- Category: WAS Suite/Animation
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Video_Frame_Dump node is designed to process video files and save them as image files by extracting separate frames. This practical tool is particularly suitable for animation and video analysis processes, allowing users to decompose video content into a series of static images. Node can be configured to specify a video source, an output directory, the name prefix for extracting frames, and the required image formatting. In addition, it provides options for setting the ffmpeg binary path required for file number numbers and advanced users. The node is configured in its dump_video_frames method, which coordinates the frame extraction process and returns the path to the output directory and the number of frames processed.

# Input types
## Required
- video_path
    - The video_path parameter specifies the file path of the video file from which you want to extract the frame. This input is vital because it determines the source content of the frame transfer operation. The node uses this path to locate and process the video, making it the basic part of the execution.
    - Comfy dtype: STRING
    - Python dtype: str
- output_path
    - The output_path parameter defines the directory that saves the extraction frame. It is a necessary parameter because it determines the location of the image file after the video frame extraction process. Users should ensure that the directory is written and that there is sufficient space to accommodate the output file.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prefix
    - The prefix parameter is used to define the name agreement for the saved image file. It is an optional input that allows the user to add a specific string at the beginning of each filename. This may be useful for organizing files or integrating with other systems that expect a naming pattern.
    - Comfy dtype: STRING
    - Python dtype: str
- filenumber_digits
    - The filenumber_digits parameter determines the number of digits in the saved image filenames for the zero-filled file number. This is an optional setup that can be adjusted to the user's preferences or to the consistency of file names. This parameter affects the formatting of the output filenames.
    - Comfy dtype: INT
    - Python dtype: int
- extension
    - The output parameter specifies the file format for the image frame to be extracted. Users can select from a combination of 'png ', 'jpg ', 'gif ', or 'tiff '. This input influences the type of image file that will be generated, which may depend on the intended use of the frame to extract.
    - Comfy dtype: COMBO['png', 'jpg', 'gif', 'tiff']
    - Python dtype: str

# Output types
- output_path
    - The output output_path parameter reflects the directory in which the extraction frame is stored. It is important because it provides the location of the image file after the video frame transfer process. This information is essential for the user to locate and further process the output file.
    - Comfy dtype: STRING
    - Python dtype: str
- processed_count
    - Processed_count output parameters indicate the number of frames that are successfully extracted from the video. It serves as confirmation for nodes and can be used to verify the integrity of the frame extraction process.
    - Comfy dtype: NUMBER
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Video_Frame_Dump:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'video_path': ('STRING', {'default': './ComfyUI/input/MyVideo.mp4', 'multiline': False}), 'output_path': ('STRING', {'default': './ComfyUI/input/MyVideo', 'multiline': False}), 'prefix': ('STRING', {'default': 'frame_', 'multiline': False}), 'filenumber_digits': ('INT', {'default': 4, 'min': -1, 'max': 8, 'step': 1}), 'extension': (['png', 'jpg', 'gif', 'tiff'],)}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
    RETURN_TYPES = (TEXT_TYPE, 'NUMBER')
    RETURN_NAMES = ('output_path', 'processed_count')
    FUNCTION = 'dump_video_frames'
    CATEGORY = 'WAS Suite/Animation'

    def dump_video_frames(self, video_path, output_path, prefix='fame_', extension='png', filenumber_digits=-1):
        conf = getSuiteConfig()
        if not conf.__contains__('ffmpeg_bin_path'):
            cstr(f'Unable to use dump frames because the `ffmpeg_bin_path` is not set in `{WAS_CONFIG_FILE}`').error.print()
            return ('', 0)
        if conf.__contains__('ffmpeg_bin_path'):
            if conf['ffmpeg_bin_path'] != '/path/to/ffmpeg':
                sys.path.append(conf['ffmpeg_bin_path'])
                os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
                os.environ['OPENCV_FFMPEG_BINARY'] = conf['ffmpeg_bin_path']
        if output_path.strip() in [None, '', '.']:
            output_path = './ComfyUI/input/frames'
        tokens = TextTokens()
        output_path = os.path.abspath(os.path.join(*tokens.parseTokens(output_path).split('/')))
        prefix = tokens.parseTokens(prefix)
        WTools = WAS_Tools_Class()
        MP4Writer = WTools.VideoWriter()
        processed = MP4Writer.extract(video_path, output_path, prefix, extension, filenumber_digits)
        return (output_path, processed)
```