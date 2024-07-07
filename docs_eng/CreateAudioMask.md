# Documentation
- Class name: CreateAudioMask
- Category: KJNodes/deprecated
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CreateAudio Mask node is designed to convert audio signals into visual expressions, specifically by creating a mask that corresponds to the content of the audio frequency. It uses the librosa library to generate spectrum maps from audio files, and then visualizes the spectrum map into a series of circles, the size of which is proportional to the range of audio at different frequencies. The node contributes to the audio-visual transformation process by providing a way of visualizing audio frequencies over time.

# Input types
## Required
- invert
    - The `invert' parameter determines whether the resulting mask should be inverted on colour. This may be very important in applications where the contrast between the mask and the background is essential.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- frames
    - The 'frames' parameter specifies the number of frames to be processed from audio files. It is essential for controlling the temporal resolution of audio to visual transformation.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - The `scale' parameter adjusts the size of the circle in the creation mask in proportion to the average range of the audio frames. It plays a vital role in the visual representation of the content of the audio frequency.
    - Comfy dtype: FLOAT
    - Python dtype: float
- audio_path
    - The `audio_path' parameter defines the path of the audio file used to generate the mask. It is a key input because it directly affects the content and quality of the mask generated.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The `width' parameter sets the width of the output image in pixels. It is an important parameter for defining the spatial dimensions of vision.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' parameter sets the height of the output image in pixels. It works with the 'width' parameter to determine the overall shape of the visual expression.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - 'output_image' is a visual expression of audio data that is generated as a result of the audio-to-visual conversion process. It encrypts the time and frequency features of audio in a single image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The'mask' output provides a binary representation of the content of the audio frequency, highlighting areas with a significant range of audio signals.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateAudioMask:

    def __init__(self):
        try:
            import librosa
            self.librosa = librosa
        except ImportError:
            print("Can not import librosa. Install it with 'pip install librosa'")
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'createaudiomask'
    CATEGORY = 'KJNodes/deprecated'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'invert': ('BOOLEAN', {'default': False}), 'frames': ('INT', {'default': 16, 'min': 1, 'max': 255, 'step': 1}), 'scale': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 2.0, 'step': 0.01}), 'audio_path': ('STRING', {'default': 'audio.wav'}), 'width': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1})}}

    def createaudiomask(self, frames, width, height, invert, audio_path, scale):
        batch_size = frames
        out = []
        masks = []
        if audio_path == 'audio.wav':
            audio_path = os.path.join(script_directory, audio_path)
        (audio, sr) = self.librosa.load(audio_path)
        spectrogram = np.abs(self.librosa.stft(audio))
        for i in range(batch_size):
            image = Image.new('RGB', (width, height), 'black')
            draw = ImageDraw.Draw(image)
            frame = spectrogram[:, i]
            circle_radius = int(height * np.mean(frame))
            circle_radius *= scale
            circle_center = (width // 2, height // 2)
            draw.ellipse([(circle_center[0] - circle_radius, circle_center[1] - circle_radius), (circle_center[0] + circle_radius, circle_center[1] + circle_radius)], fill='white')
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            mask = image[:, :, :, 0]
            masks.append(mask)
            out.append(image)
        if invert:
            return (1.0 - torch.cat(out, dim=0),)
        return (torch.cat(out, dim=0), torch.cat(masks, dim=0))
```