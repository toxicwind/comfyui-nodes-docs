# Documentation
- Class name: PreviewBridgeLatent
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Preview BridgeLatent class, as a bridge for efficient visualization and management of potential representation of images, provides a way to convert these potential expressions into preview formats that can be easily explained and used in the system.

# Input types
## Required
- latent
    - The latent parameter is necessary because it contains an encoded representation of the image that needs to be visualized. It plays a key role in the function of the node by providing the raw data needed for the image reconstruction process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- image
    - The Image parameter is essential for the node because it identifies the particular image to be processed. It influences the node's execution by determining the potential expression of which image to visualize.
    - Comfy dtype: STRING
    - Python dtype: str
- preview_method
    - The preview_method parameter determines the method used to generate visual expressions from potential data. It is part of the node operation because it shapes the output image according to the visualization method chosen.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
## Optional
- vae_opt
    - When the vae_opt parameter is provided, a specific VAE model is allowed to decode potential data. It contains elements that can significantly affect the quality and style of the final preview of the image.
    - Comfy dtype: VAE
    - Python dtype: Union[torch.nn.Module, None]
- unique_id
    - The unique_id parameter is used to track and manage the cache of processed images. It is important for the efficiency of nodes, as it helps to avoid redundancy and ensures that up-to-date versions of images are always available.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- ui
    - ui output provides a user interface for post-processing images, which includes information such as file names and subfolders. This output is essential for the visualization of datasets into the system user interface.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]
- result
    - The result output contains potential expressions and masks of the post-processed image. This output is essential because it provides the raw data needed for further analysis or operation within the system.
    - Comfy dtype: TUPLE
    - Python dtype: Tuple[Dict[str, Any], torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class PreviewBridgeLatent:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent': ('LATENT',), 'image': ('STRING', {'default': ''}), 'preview_method': (['Latent2RGB-SDXL', 'Latent2RGB-SD15', 'TAESDXL', 'TAESD15'],)}, 'optional': {'vae_opt': ('VAE',)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('LATENT', 'MASK')
    FUNCTION = 'doit'
    OUTPUT_NODE = True
    CATEGORY = 'ImpactPack/Util'

    def __init__(self):
        super().__init__()
        self.output_dir = folder_paths.get_temp_directory()
        self.type = 'temp'
        self.prev_hash = None
        self.prefix_append = '_temp_' + ''.join((random.choice('abcdefghijklmnopqrstupvxyz') for x in range(5)))

    @staticmethod
    def load_image(pb_id):
        is_fail = False
        if pb_id not in core.preview_bridge_image_id_map:
            is_fail = True
        (image_path, ui_item) = core.preview_bridge_image_id_map[pb_id]
        if not os.path.isfile(image_path):
            is_fail = True
        if not is_fail:
            i = Image.open(image_path)
            i = ImageOps.exif_transpose(i)
            image = i.convert('RGB')
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1.0 - torch.from_numpy(mask)
            else:
                mask = None
        else:
            image = empty_pil_tensor()
            mask = None
            ui_item = {'filename': 'empty.png', 'subfolder': '', 'type': 'temp'}
        return (image, mask, ui_item)

    def doit(self, latent, image, preview_method, vae_opt=None, unique_id=None):
        need_refresh = False
        if unique_id not in core.preview_bridge_cache:
            need_refresh = True
        elif core.preview_bridge_cache[unique_id][0] is not latent or (vae_opt is None and core.preview_bridge_cache[unique_id][2] is not None) or (vae_opt is None and core.preview_bridge_cache[unique_id][1] != preview_method) or (vae_opt is not None and core.preview_bridge_cache[unique_id][2] is not vae_opt):
            need_refresh = True
        if not need_refresh:
            (pixels, mask, path_item) = PreviewBridge.load_image(image)
            if mask is None:
                mask = torch.ones(latent['samples'].shape[2:], dtype=torch.float32, device='cpu').unsqueeze(0)
                if 'noise_mask' in latent:
                    res_latent = latent.copy()
                    del res_latent['noise_mask']
                else:
                    res_latent = latent
            else:
                res_latent = latent.copy()
                res_latent['noise_mask'] = mask
            res_image = [path_item]
        else:
            decoded_image = decode_latent(latent, preview_method, vae_opt)
            if 'noise_mask' in latent:
                mask = latent['noise_mask']
                decoded_pil = to_pil(decoded_image)
                inverted_mask = 1 - mask
                resized_mask = resize_mask(inverted_mask, (decoded_image.shape[1], decoded_image.shape[2]))
                result_pil = apply_mask_alpha_to_pil(decoded_pil, resized_mask)
                (full_output_folder, filename, counter, _, _) = folder_paths.get_save_image_path('PreviewBridge/PBL-' + self.prefix_append, folder_paths.get_temp_directory(), result_pil.size[0], result_pil.size[1])
                file = f'{filename}_{counter}.png'
                result_pil.save(os.path.join(full_output_folder, file), compress_level=4)
                res_image = [{'filename': file, 'subfolder': 'PreviewBridge', 'type': 'temp'}]
            else:
                mask = torch.ones(latent['samples'].shape[2:], dtype=torch.float32, device='cpu').unsqueeze(0)
                res = nodes.PreviewImage().save_images(decoded_image, filename_prefix='PreviewBridge/PBL-')
                res_image = res['ui']['images']
            path = os.path.join(folder_paths.get_temp_directory(), 'PreviewBridge', res_image[0]['filename'])
            core.set_previewbridge_image(unique_id, path, res_image[0])
            core.preview_bridge_image_id_map[image] = (path, res_image[0])
            core.preview_bridge_image_name_map[unique_id, path] = (image, res_image[0])
            core.preview_bridge_cache[unique_id] = (latent, preview_method, vae_opt, res_image)
            res_latent = latent
        return {'ui': {'images': res_image}, 'result': (res_latent, mask)}
```