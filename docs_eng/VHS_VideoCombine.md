# Documentation
- Class name: VideoCombine
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: True
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The cobine_video method is designed to combine a series of images into video formats. It handles parameters, such as frame rates, loop counts and file formats, to create customized video output. It can generate videos in GIF and WebP formats, and also supports audio integration.

# Input types
## Required
- images
    - The parameters are the image data series that make up the visual content of the video. It is vital because it determines the frame of the final video output.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- frame_rate
    - The frame_rate parameter sets the number of frames per second of the video, affecting the speed of the video play.
    - Comfy dtype: FLOAT
    - Python dtype: int
- loop_count
    - Loop_count determines the number of times the video is repeated. Value 0 means the video will not be recycled.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- filename_prefix
    - Filename_prefix is the only identifier used to create the output video file, which helps file management.
    - Comfy dtype: STRING
    - Python dtype: str
- format
    - Format parameters specify the format of the output video. It can be an image format like GIF or WebP, or a custom video format.
    - Comfy dtype: COMBO[image/gif, image/webp, video/...]
    - Python dtype: str
- pingpong
    - When set to True, the pingpong parameter creates the ping-pong effect by inverting the order of the frame.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- save_output
    - Save_output parameters indicate whether the result video should be saved to the output directory.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- Filenames
    - Filenames output provides the path to the generated video files, allowing users to access and use them as needed.
    - Comfy dtype: VHS_FILENAMES
    - Python dtype: Tuple[bool, List[str]]

# Usage tips
- Infra type: CPU

# Source code
```
class VideoCombine:

    @classmethod
    def INPUT_TYPES(s):
        ffmpeg_formats = get_video_formats()
        return {'required': {'images': ('IMAGE',), 'frame_rate': ('FLOAT', {'default': 8, 'min': 1, 'step': 1}), 'loop_count': ('INT', {'default': 0, 'min': 0, 'max': 100, 'step': 1}), 'filename_prefix': ('STRING', {'default': 'AnimateDiff'}), 'format': (['image/gif', 'image/webp'] + ffmpeg_formats,), 'pingpong': ('BOOLEAN', {'default': False}), 'save_output': ('BOOLEAN', {'default': True})}, 'optional': {'audio': ('VHS_AUDIO',), 'meta_batch': ('VHS_BatchManager',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('VHS_FILENAMES',)
    RETURN_NAMES = ('Filenames',)
    OUTPUT_NODE = True
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    FUNCTION = 'combine_video'

    def combine_video(self, images, frame_rate: int, loop_count: int, filename_prefix='AnimateDiff', format='image/gif', pingpong=False, save_output=True, prompt=None, extra_pnginfo=None, audio=None, unique_id=None, manual_format_widgets=None, meta_batch=None):
        output_dir = folder_paths.get_output_directory() if save_output else folder_paths.get_temp_directory()
        (full_output_folder, filename, _, subfolder, _) = folder_paths.get_save_image_path(filename_prefix, output_dir)
        output_files = []
        metadata = PngInfo()
        video_metadata = {}
        if prompt is not None:
            metadata.add_text('prompt', json.dumps(prompt))
            video_metadata['prompt'] = prompt
        if extra_pnginfo is not None:
            for x in extra_pnginfo:
                metadata.add_text(x, json.dumps(extra_pnginfo[x]))
                video_metadata[x] = extra_pnginfo[x]
        metadata.add_text('CreationTime', datetime.datetime.now().isoformat(' ')[:19])
        if meta_batch is not None and unique_id in meta_batch.outputs:
            (counter, output_process) = meta_batch.outputs[unique_id]
        else:
            max_counter = 0
            matcher = re.compile(f'{re.escape(filename)}_(\\d+)\\D*\\..+', re.IGNORECASE)
            for existing_file in os.listdir(full_output_folder):
                match = matcher.fullmatch(existing_file)
                if match:
                    file_counter = int(match.group(1))
                    if file_counter > max_counter:
                        max_counter = file_counter
            counter = max_counter + 1
            output_process = None
        file = f'{filename}_{counter:05}.png'
        file_path = os.path.join(full_output_folder, file)
        Image.fromarray(tensor_to_bytes(images[0])).save(file_path, pnginfo=metadata, compress_level=4)
        output_files.append(file_path)
        (format_type, format_ext) = format.split('/')
        if format_type == 'image':
            if meta_batch is not None:
                raise Exception("Pillow('image/') formats are not compatible with batched output")
            image_kwargs = {}
            if format_ext == 'gif':
                image_kwargs['disposal'] = 2
            if format_ext == 'webp':
                exif = Image.Exif()
                exif[ExifTags.IFD.Exif] = {36867: datetime.datetime.now().isoformat(' ')[:19]}
                image_kwargs['exif'] = exif
            file = f'{filename}_{counter:05}.{format_ext}'
            file_path = os.path.join(full_output_folder, file)
            if pingpong:
                images = to_pingpong(images)
            frames = map(lambda x: Image.fromarray(tensor_to_bytes(x)), images)
            next(frames).save(file_path, format=format_ext.upper(), save_all=True, append_images=frames, duration=round(1000 / frame_rate), loop=loop_count, compress_level=4, **image_kwargs)
            output_files.append(file_path)
        else:
            if ffmpeg_path is None:
                raise ProcessLookupError(f"ffmpeg is required for video outputs and could not be found.\nIn order to use video outputs, you must either:\n- Install imageoio-ffmpeg with pip,\n- Place a ffmpeg executable in {os.path.abspath('')}, or\n- Install ffmpeg and add it to the system path.")
            kwargs = None
            if manual_format_widgets is None:
                if prompt is not None:
                    kwargs = prompt[unique_id]['inputs']
                else:
                    manual_format_widgets = {}
            if kwargs is None:
                kwargs = get_format_widget_defaults(format_ext)
                missing = {}
                for k in kwargs.keys():
                    if k in manual_format_widgets:
                        kwargs[k] = manual_format_widgets[k]
                    else:
                        missing[k] = kwargs[k]
                if len(missing) > 0:
                    logger.warn('Extra format values were not provided, the following defaults will be used: ' + str(kwargs) + '\nThis is likely due to usage of ComfyUI-to-python. These values can be manually set by supplying a manual_format_widgets argument')
            video_format = apply_format_widgets(format_ext, kwargs)
            has_alpha = images[0].shape[-1] == 4
            dimensions = f'{len(images[0][0])}x{len(images[0])}'
            if loop_count > 0:
                loop_args = ['-vf', 'loop=loop=' + str(loop_count) + ':size=' + str(len(images))]
            else:
                loop_args = []
            if pingpong:
                if meta_batch is not None:
                    logger.error('pingpong is incompatible with batched output')
                images = to_pingpong(images)
            if video_format.get('input_color_depth', '8bit') == '16bit':
                images = map(tensor_to_shorts, images)
                if has_alpha:
                    i_pix_fmt = 'rgba64'
                else:
                    i_pix_fmt = 'rgb48'
            else:
                images = map(tensor_to_bytes, images)
                if has_alpha:
                    i_pix_fmt = 'rgba'
                else:
                    i_pix_fmt = 'rgb24'
            file = f"{filename}_{counter:05}.{video_format['extension']}"
            file_path = os.path.join(full_output_folder, file)
            bitrate_arg = []
            bitrate = video_format.get('bitrate')
            if bitrate is not None:
                bitrate_arg = ['-b:v', str(bitrate) + 'M' if video_format.get('megabit') == 'True' else str(bitrate) + 'K']
            args = [ffmpeg_path, '-v', 'error', '-f', 'rawvideo', '-pix_fmt', i_pix_fmt, '-s', dimensions, '-r', str(frame_rate), '-i', '-'] + loop_args + video_format['main_pass'] + bitrate_arg
            env = os.environ.copy()
            if 'environment' in video_format:
                env.update(video_format['environment'])
            if output_process is None:
                output_process = ffmpeg_process(args, video_format, video_metadata, file_path, env)
                output_process.send(None)
                if meta_batch is not None:
                    meta_batch.outputs[unique_id] = (counter, output_process)
            for image in images:
                output_process.send(image.tobytes())
            if meta_batch is not None:
                requeue_workflow((meta_batch.unique_id, not meta_batch.has_closed_inputs))
            if meta_batch is None or meta_batch.has_closed_inputs:
                try:
                    output_process.send(None)
                except StopIteration:
                    pass
                if meta_batch is not None:
                    meta_batch.outputs.pop(unique_id)
                    if len(meta_batch.outputs) == 0:
                        meta_batch.reset()
            else:
                return {'ui': {'unfinished_batch': [True]}, 'result': ((save_output, []),)}
            output_files.append(file_path)
            if 'gifski_pass' in video_format:
                gif_output = f'{filename}_{counter:05}.gif'
                gif_output_path = os.path.join(full_output_folder, gif_output)
                gifski_args = [gifski_path] + video_format['gifski_pass'] + ['-o', gif_output_path, file_path]
                try:
                    res = subprocess.run(gifski_args, env=env, check=True, capture_output=True)
                except subprocess.CalledProcessError as e:
                    raise Exception('An error occured in the gifski subprocess:\n' + e.stderr.decode('utf-8'))
                if res.stderr:
                    print(res.stderr.decode('utf-8'), end='', file=sys.stderr)
                format = 'image/gif'
                output_files.append(gif_output_path)
                file = gif_output
            elif audio is not None and audio() is not False:
                output_file_with_audio = f"{filename}_{counter:05}-audio.{video_format['extension']}"
                output_file_with_audio_path = os.path.join(full_output_folder, output_file_with_audio)
                if 'audio_pass' not in video_format:
                    logger.warn('Selected video format does not have explicit audio support')
                    video_format['audio_pass'] = ['-c:a', 'libopus']
                mux_args = [ffmpeg_path, '-v', 'error', '-n', '-i', file_path, '-i', '-', '-c:v', 'copy'] + video_format['audio_pass'] + ['-af', 'apad', '-shortest', output_file_with_audio_path]
                try:
                    res = subprocess.run(mux_args, input=audio(), env=env, capture_output=True, check=True)
                except subprocess.CalledProcessError as e:
                    raise Exception('An error occured in the ffmpeg subprocess:\n' + e.stderr.decode('utf-8'))
                if res.stderr:
                    print(res.stderr.decode('utf-8'), end='', file=sys.stderr)
                output_files.append(output_file_with_audio_path)
                file = output_file_with_audio
        previews = [{'filename': file, 'subfolder': subfolder, 'type': 'output' if save_output else 'temp', 'format': format}]
        return {'ui': {'gifs': previews}, 'result': ((save_output, output_files),)}

    @classmethod
    def VALIDATE_INPUTS(self, format, **kwargs):
        return True
```