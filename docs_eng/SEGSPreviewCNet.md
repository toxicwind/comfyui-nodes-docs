# Documentation
- Class name: SEGSPreviewCNet
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSPreviewCN is a node for processing and previewing split results. It accepts split data as input and generates a series of preview images, which enhances visualization and analysis of splits. This node is essential in providing visual summaries of splits, allowing rapid assessment and further operation when needed.

# Input types
## Required
- segs
    - The'ssegs' parameter is essential for the operation of the node because it provides the split data that the node will process. This is a necessary input that directly influences the output of the node by determining the content of the preview image generated.
    - Comfy dtype: SEGS
    - Python dtype: List[Tuple[str, SEG]]

# Output types
- ui
    - The 'ui'parameter in the output is important because it contains the user interface elements that will be displayed to the user. It includes a list of images that represent split previews, which are essential for user interaction and visual feedback.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]
- result
    - The output'result' parameter is the collection of images processed by nodes. It is the main output of the nodes and contains visual expressions of the split data, which is the main objective of the node function.
    - Comfy dtype: COMBO[IMAGE]
    - Python dtype: Tuple[List[Image.Image], ...]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSPreviewCNet:

    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.type = 'temp'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('IMAGE',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'
    OUTPUT_NODE = True

    def doit(self, segs):
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path('impact_seg_preview', self.output_dir, segs[0][1], segs[0][0])
        results = list()
        result_image_list = []
        for seg in segs[1]:
            file = f'{filename}_{counter:05}_.webp'
            if seg.control_net_wrapper is not None and seg.control_net_wrapper.control_image is not None:
                cnet_image = seg.control_net_wrapper.control_image
                result_image_list.append(cnet_image)
            else:
                cnet_image = empty_pil_tensor(64, 64)
            cnet_pil = utils.tensor2pil(cnet_image)
            cnet_pil.save(os.path.join(full_output_folder, file))
            results.append({'filename': file, 'subfolder': subfolder, 'type': self.type})
            counter += 1
        return {'ui': {'images': results}, 'result': (result_image_list,)}
```