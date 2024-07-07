# Documentation
- Class name: LoadVideo
- Category: Animate Diff/Utils
- Output node: False
- Repo Ref: https://github.com/ArtVentureX/comfyui-animatediff.git

The node is designed to extract frames from video files that allow for the selection of a given frame range based on starting points and limitations. It allows the frames to be used for further processing of various applications, such as animation or variance analysis.

# Input types
## Required
- video
    - Video parameters are essential because it defines the source from which the frame will be extracted. It influences the operation of the node by determining the content and frame sequence to be processed.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- frame_start
    - The frame_start parameter indicates which initial frame number to start with. It influences the execution of the node by setting the starting point of the frame selection.
    - Comfy dtype: INT
    - Python dtype: int
- frame_limit
    - The frame_mit parameter defines the maximum number of frames to be extracted after the frame_start. It directly affects the number of frames that the node handles.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- frames
    - Frames output is a series of extracted video frames that are converted into volume formats and are essential for further analysis or operation in downstream processes.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor
- frame_count
    - The frame_count output provides the total number of frames extracted and provides a reference for the amount of data processed by nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class LoadVideo:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = os.path.join(folder_paths.get_input_directory(), 'video')
        if not os.path.exists(input_dir):
            os.makedirs(input_dir, exist_ok=True)
        files = [f'video/{f}' for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'video': (sorted(files), {'video_upload': True})}, 'optional': {'frame_start': ('INT', {'default': 0, 'min': 0, 'max': 4294967295, 'step': 1}), 'frame_limit': ('INT', {'default': 16, 'min': 1, 'max': 10240, 'step': 1})}}
    CATEGORY = 'Animate Diff/Utils'
    RETURN_TYPES = ('IMAGE', 'INT')
    RETURN_NAMES = ('frames', 'frame_count')
    FUNCTION = 'load'

    def load_gif(self, gif_path: str, frame_start: int, frame_limit: int):
        image = Image.open(gif_path)
        frames = []
        for (i, frame) in enumerate(ImageSequence.Iterator(image)):
            if i < frame_start:
                continue
            elif i >= frame_start + frame_limit:
                break
            else:
                frames.append(pil2tensor(frame.copy().convert('RGB')))
        return frames

    def load_video(self, video_path, frame_start: int, frame_limit: int):
        ensure_opencv()
        import cv2
        video = cv2.VideoCapture(video_path)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_start)
        frames = []
        for i in range(frame_limit):
            (ret, frame) = video.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(pil2tensor(Image.fromarray(frame)))
            else:
                break
        video.release()
        return frames

    def load(self, video: str, frame_start=0, frame_limit=16):
        video_path = folder_paths.get_annotated_filepath(video)
        (_, ext) = os.path.splitext(video_path)
        if ext.lower() in {'.gif', '.webp'}:
            frames = self.load_gif(video_path, frame_start, frame_limit)
        elif ext.lower() in {'.webp', '.mp4', '.mov', '.avi', '.webm'}:
            frames = self.load_video(video_path, frame_start, frame_limit)
        else:
            raise ValueError(f'Unsupported video format: {ext}')
        return (torch.cat(frames, dim=0), len(frames))

    @classmethod
    def IS_CHANGED(s, image, *args, **kwargs):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, video, *args, **kwargs):
        if not folder_paths.exists_annotated_filepath(video):
            return 'Invalid video file: {}'.format(video)
        return True
```