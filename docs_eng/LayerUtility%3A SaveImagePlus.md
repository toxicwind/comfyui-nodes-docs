# Documentation
- Class name: SaveImagePlus
- Category: 😺dzNodes/LayerUtility/SystemIO
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

An enhanced version of the saved picture nodes. A directory of images can be customised, the filenames added a time stamp, the file format selected, the image compression rate set, whether the workflow is saved or not, and the selected image can be added invisible watermarks (information added in a way that is not perceptible to the naked eye, which can be decoded using the accompanying ShowBlindWater Mark node). You can choose whether to export the json files of the workflow at the same time.

* Enter %date for current date (YY-mm-dd), %time for current time (HH-MM-SS). You can enter/ indicate subdirectories. For example, %date/name_%time will prefix the output picture to the YY-mm-dd folder with the name_HH-MM-SS.

# Input types

## Required

- images
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- custom_path
    - User-defined directory. Enter the directory name in the correct format. If empty, save the output directory at the ComfyUI default.
    - Comfy dtype: STRING
    - Python dtype: str

- filename_prefix
    - Filename prefix.
    - Comfy dtype: STRING
    - Python dtype: str

- timestamp
    - Add a time stamp to the filename to select the date, time to seconds and time to milliseconds.
    - Comfy dtype: ["None", "second", "millisecond"]
    - Python dtype: str

- format
    - Images save format. Both png and jpg are currently available. Note that pictures in RGBA mode support only the png format.
    - Comfy dtype: ["png", "jpg"]
    - Python dtype: str

- quality
    - Picture quality, range 10-100, the higher the value, the better the quality of the picture and the corresponding volume of the document.
    - Comfy dtype: INT
    - Python dtype: int

- meta_data
    - Whether to save metadata is the workflow information in the png file. If you do not want to leak the workflow, set here as false.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- blind_watermark
    - Text entered here (which does not support multilingualism) will be converted to a two-dimensional code to be saved as an invisible watermark, which can be decoded using the ShowBlind Watermark node. Note that pictures with watermarks are proposed to be saved in ng format, and the lower quality jpg format will result in the loss of watermark information.
    - Comfy dtype: STRING
    - Python dtype: str

- save_workflow_as_json
    - Whether to output the workflow at the same time as a json file (the output json is in the same directory as the picture).
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- preview
    - Preview.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

## Hidden

- prompt
    - Hint.
    - Comfy dtype: PROMPT
    - Python dtype: str

- extra_pnginfo
    - Additional PNG information.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict

# Output types

- None

# Usage tips
- Infra type: CPU

# Source code
```python
class SaveImagePlus:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"images": ("IMAGE", ),
                     "custom_path": ("STRING", {"default": ""}),
                     "filename_prefix": ("STRING", {"default": "comfyui"}),
                     "timestamp": (["None", "second", "millisecond"],),
                     "format": (["png", "jpg"],),
                     "quality": ("INT", {"default": 80, "min": 10, "max": 100, "step": 1}),
                     "meta_data": ("BOOLEAN", {"default": False}),
                     "blind_watermark": ("STRING", {"default": ""}),
                     "save_workflow_as_json": ("BOOLEAN", {"default": False}),
                     "preview": ("BOOLEAN", {"default": True}),
                     },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ()
    FUNCTION = "save_image_plus"
    OUTPUT_NODE = True
    CATEGORY = '😺dzNodes/LayerUtility/SystemIO'

    def save_image_plus(self, images, custom_path, filename_prefix, timestamp, format, quality,
                           meta_data, blind_watermark, preview, save_workflow_as_json,
                           prompt=None, extra_pnginfo=None):

        now = datetime.datetime.now()
        custom_path = custom_path.replace("%date", now.strftime("%Y-%m-%d"))
        custom_path = custom_path.replace("%time", now.strftime("%H-%M-%S"))
        filename_prefix = filename_prefix.replace("%date", now.strftime("%Y-%m-%d"))
        filename_prefix = filename_prefix.replace("%time", now.strftime("%H-%M-%S"))
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        temp_sub_dir = generate_random_name('_savepreview_', '_temp', 16)
        temp_dir = os.path.join(folder_paths.get_temp_directory(), temp_sub_dir)
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            if blind_watermark != "":
                img_mode = img.mode
                wm_size = watermark_image_size(img)
                import qrcode
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=20,
                    border=1,
                )
                qr.add_data(blind_watermark.encode('utf-8'))
                qr.make(fit=True)
                qr_image = qr.make_image(fill_color="black", back_color="white")
                qr_image = qr_image.resize((wm_size, wm_size), Image.BICUBIC).convert("L")

                y, u, v, _ = image_channel_split(img, mode='YCbCr')
                _u = add_invisibal_watermark(u, qr_image)
                wm_img = image_channel_merge((y, _u, v), mode='YCbCr')

                if img.mode == "RGBA":
                    img = RGB2RGBA(wm_img, img.split()[-1])
                else:
                    img = wm_img.convert(img_mode)

            metadata = None
            if meta_data:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text("prompt", json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            if timestamp == "millisecond":
                file = f'{filename}_{now.strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]}'
            elif timestamp == "second":
                file = f'{filename}_{now.strftime("%Y-%m-%d_%H-%M-%S")}'
            else:
                file = f'{filename}_{counter:05}'


            preview_filename = ""
            if custom_path != "":
                if not os.path.exists(custom_path):
                    try:
                        os.makedirs(custom_path)
                    except Exception as e:
                        log(f"Error: {NODE_NAME} skipped, because unable to create temporary folder.",
                            message_type='warning')
                        raise FileNotFoundError(f"cannot create custom_path {custom_path}, {e}")

                full_output_folder = os.path.normpath(custom_path)
                # save preview image to temp_dir
                if os.path.isdir(temp_dir):
                    shutil.rmtree(temp_dir)
                try:
                    os.makedirs(temp_dir)
                except Exception as e:
                    print(e)
                    log(f"Error: {NODE_NAME} skipped, because unable to create temporary folder.",
                        message_type='warning')
                try:
                    preview_filename = os.path.join(generate_random_name('saveimage_preview_', '_temp', 16) + '.png')
                    img.save(os.path.join(temp_dir, preview_filename))
                except Exception as e:
                    print(e)
                    log(f"Error: {NODE_NAME} skipped, because unable to create temporary file.", message_type='warning')

            # check if file exists, change filename
            while os.path.isfile(os.path.join(full_output_folder, f"{file}.{format}")):
                counter += 1
                if timestamp == "millisecond":
                    file = f'{filename}_{now.strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]}_{counter:05}'
                elif timestamp == "second":
                    file = f'{filename}_{now.strftime("%Y-%m-%d_%H-%M-%S")}_{counter:05}'
                else:
                    file = f"{filename}_{counter:05}"

            image_file_name = os.path.join(full_output_folder, f"{file}.{format}")
            json_file_name = os.path.join(full_output_folder, f"{file}.json")

            if format == "png":
                img.save(image_file_name, pnginfo=metadata, compress_level= (100 - quality) // 10)
            else:
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                img.save(image_file_name, quality=quality)
            log(f"{NODE_NAME} -> Saving image to {image_file_name}")

            if save_workflow_as_json:
                try:
                    workflow = (extra_pnginfo or {}).get('workflow')
                    if workflow is None:
                        log('No workflow found, skipping saving of JSON')
                    with open(f'{json_file_name}', 'w') as workflow_file:
                        json.dump(workflow, workflow_file)
                        log(f'Saved workflow to {json_file_name}')
                except Exception as e:
                    log(
                        f'Failed to save workflow as json due to: {e}, proceeding with the remainder of saving execution', message_type="warning")

            if preview:
                if custom_path == "":
                    results.append({
                        "filename": f"{file}.{format}",
                        "subfolder": subfolder,
                        "type": self.type
                    })
                else:
                    results.append({
                        "filename": preview_filename,
                        "subfolder": temp_sub_dir,
                        "type": "temp"
                    })

            counter += 1

        return { "ui": { "images": results } }
```