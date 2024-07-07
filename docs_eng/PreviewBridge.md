# Documentation
- Class name: PreviewBridge
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Preview Bridge is designed to process and manage image data and provide a bridge between the input image and the subsequent processing phase. It is responsible for loading, converting and cacheing images to optimize workflows and ensure the efficient processing of visual data in the system.

# Input types
## Required
- images
    - The `images' parameter is essential for the node because it represents the input image data that needs to be processed. It plays a key role in the implementation of the node because it directly affects output and subsequent image operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- unique_id
    - The `unique_id' parameter is essential for the function of the node, as it only identifies each image or data set processed by the node. It ensures that the node is able to accurately track and manage the image, which is essential for the operation of the node and the integrity of the result.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
## Optional
- image
    - The 'image'parameter is an optional identifier for a particular image in a node operation. It can be used to quote or retrieve specific image data based on the identifier provided, and thus plays an important role in custom node behaviour.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ui
    - The 'ui'output parameter is important because it contains user interface elements associated with node operations. It usually includes image data that can be displayed or used to interact further within the system's UI.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]
- result
    - The `redault' output parameter covers the processed image data and the corresponding mask. It is a key component of the node function because it provides the final output that can be used for downstream tasks or analyses.
    - Comfy dtype: TUPLE[torch.Tensor, torch.Tensor]
    - Python dtype: Tuple[torch.Tensor, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class PreviewBridge:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'image': ('STRING', {'default': ''})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'doit'
    OUTPUT_NODE = True
    CATEGORY = 'ImpactPack/Util'

    def __init__(self):
        super().__init__()
        self.output_dir = folder_paths.get_temp_directory()
        self.type = 'temp'
        self.prev_hash = None

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
                mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
        else:
            image = empty_pil_tensor()
            mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
            ui_item = {'filename': 'empty.png', 'subfolder': '', 'type': 'temp'}
        return (image, mask.unsqueeze(0), ui_item)

    def doit(self, images, image, unique_id):
        need_refresh = False
        if unique_id not in core.preview_bridge_cache:
            need_refresh = True
        elif core.preview_bridge_cache[unique_id][0] is not images:
            need_refresh = True
        if not need_refresh:
            (pixels, mask, path_item) = PreviewBridge.load_image(image)
            image = [path_item]
        else:
            res = nodes.PreviewImage().save_images(images, filename_prefix='PreviewBridge/PB-')
            image2 = res['ui']['images']
            pixels = images
            mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
            path = os.path.join(folder_paths.get_temp_directory(), 'PreviewBridge', image2[0]['filename'])
            core.set_previewbridge_image(unique_id, path, image2[0])
            core.preview_bridge_image_id_map[image] = (path, image2[0])
            core.preview_bridge_image_name_map[unique_id, path] = (image, image2[0])
            core.preview_bridge_cache[unique_id] = (images, image2)
            image = image2
        return {'ui': {'images': image}, 'result': (pixels, mask)}
```