# Documentation
- Class name: SimpleDetectorForAnimateDiff
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SimpleDector ForAnimatéDiff node is designed to detect and process animation differences in a range of images. It uses boundary frames to detect and select semantic partition models to identify and divide areas of interest. The node can handle a variety of modes of operation, including using individual frames as a reference, grouping adjacent frames, or dividing each frame separately. It emphasizes the detection of significant changes and the creation of masks to isolate these changes for further analysis.

# Input types
## Required
- bbox_detector
    - The bbox_detector parameter is essential for the initial detection of the boundary frame in the frame. It provides the basis for further analysis and partitioning. The validity of bbox_detector directly influences the accuracy of the next step, making it a key component in node operations.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- image_frames
    - The image_frames parameter is essential because it represents input data for nodes. It contains the image sequences that nodes will analyse to detect animated differences. The quality and resolution of image_frames directly influences the ability of nodes to detect and accurately divide changes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- bbox_threshold
    - The bbox_threshold parameter defines the confidence level of the border box detection. It is a key factor in determining which boundary boxes are considered for further treatment. Adjusting this threshold significantly affects the ability to detect nodes and subsequent partitions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_dilation
    - The bbox_dilation parameter is used to expand the size of the detected boundary box. This extension is important to ensure that the partition process captures the entire area of interest, especially when the boundary frame is close to or close to the edge of the object.
    - Comfy dtype: INT
    - Python dtype: int
- crop_factor
    - Crop_factor parameters are very important because they determine the extent to which images are cropped around the detection area. This helps to focus analysis on the most relevant parts of the image and reduce noise in the surrounding area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- drop_size
    - The drop_size parameter determines the size of the discarded area during the partition process. It plays a crucial role in fine-tuning the mask to ensure that it accurately expresses the area of interest without unnecessary detail.
    - Comfy dtype: INT
    - Python dtype: int
- sub_threshold
    - The sub_threshold parameter is important for fine-tuning the partitioning process. It helps to determine the level of detail captured in the split mask and strikes a balance between accuracy and inclusion of relevant information.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sub_dilation
    - The sub_dilation parameter is used to control the extension of the partition mask. It is a key factor in ensuring that the mask completely encapsulates the area of interest, taking into account any potential inaccuracies that may exist in the initial test.
    - Comfy dtype: INT
    - Python dtype: int
- sub_bbox_expansion
    - The sub_bbox_expansion parameter allows the extension of the boundary box used in the partitioning process. This is particularly useful for capturing areas that may be slightly larger than those recommended for initial testing, ensuring a more comprehensive partition.
    - Comfy dtype: INT
    - Python dtype: int
- sam_mask_hint_threshold
    - The sam_mask_hint_threshold parameter is used with SAM (Semantic Comment Model) to fine-tune the mask. It helps to control the level of detail in the mask and ensures that the mask closely matches the desired area of interest.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS
    - Output SEGS parameters represent the results of the node analysis. It contains the interested segment areas identified in the input frame. These segments are essential for further processing and analysis, such as tracking changes or identifying particular features in animations.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]

# Usage tips
- Infra type: GPU

# Source code
```
class SimpleDetectorForAnimateDiff:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bbox_detector': ('BBOX_DETECTOR',), 'image_frames': ('IMAGE',), 'bbox_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_dilation': ('INT', {'default': 0, 'min': -255, 'max': 255, 'step': 1}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'sub_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'sub_dilation': ('INT', {'default': 0, 'min': -255, 'max': 255, 'step': 1}), 'sub_bbox_expansion': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1}), 'sam_mask_hint_threshold': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'masking_mode': (['Pivot SEGS', 'Combine neighboring frames', "Don't combine"],), 'segs_pivot': (['Combined mask', '1st frame mask'],), 'sam_model_opt': ('SAM_MODEL',), 'segm_detector_opt': ('SEGM_DETECTOR',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    @staticmethod
    def detect(bbox_detector, image_frames, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, masking_mode='Pivot SEGS', segs_pivot='Combined mask', sam_model_opt=None, segm_detector_opt=None):
        h = image_frames.shape[1]
        w = image_frames.shape[2]
        segs_by_frames = []
        for image in image_frames:
            image = image.unsqueeze(0)
            segs = bbox_detector.detect(image, bbox_threshold, bbox_dilation, crop_factor, drop_size)
            if sam_model_opt is not None:
                mask = core.make_sam_mask(sam_model_opt, segs, image, 'center-1', sub_dilation, sub_threshold, sub_bbox_expansion, sam_mask_hint_threshold, False)
                segs = core.segs_bitwise_and_mask(segs, mask)
            elif segm_detector_opt is not None:
                segm_segs = segm_detector_opt.detect(image, sub_threshold, sub_dilation, crop_factor, drop_size)
                mask = core.segs_to_combined_mask(segm_segs)
                segs = core.segs_bitwise_and_mask(segs, mask)
            segs_by_frames.append(segs)

        def get_masked_frames():
            masks_by_frame = []
            for (i, segs) in enumerate(segs_by_frames):
                masks_in_frame = segs_nodes.SEGSToMaskList().doit(segs)[0]
                current_frame_mask = (masks_in_frame[0] * 255).to(torch.uint8)
                for mask in masks_in_frame[1:]:
                    current_frame_mask |= (mask * 255).to(torch.uint8)
                current_frame_mask = (current_frame_mask / 255.0).to(torch.float32)
                current_frame_mask = utils.to_binary_mask(current_frame_mask, 0.1)[0]
                masks_by_frame.append(current_frame_mask)
            return masks_by_frame

        def get_empty_mask():
            return torch.zeros((h, w), dtype=torch.float32, device='cpu')

        def get_neighboring_mask_at(i, masks_by_frame):
            prv = masks_by_frame[i - 1] if i > 1 else get_empty_mask()
            cur = masks_by_frame[i]
            nxt = masks_by_frame[i - 1] if i > 1 else get_empty_mask()
            prv = prv if prv is not None else get_empty_mask()
            cur = cur.clone() if cur is not None else get_empty_mask()
            nxt = nxt if nxt is not None else get_empty_mask()
            return (prv, cur, nxt)

        def get_merged_neighboring_mask(masks_by_frame):
            if len(masks_by_frame) <= 1:
                return masks_by_frame
            result = []
            for i in range(0, len(masks_by_frame)):
                (prv, cur, nxt) = get_neighboring_mask_at(i, masks_by_frame)
                cur = (cur * 255).to(torch.uint8)
                cur |= (prv * 255).to(torch.uint8)
                cur |= (nxt * 255).to(torch.uint8)
                cur = (cur / 255.0).to(torch.float32)
                cur = utils.to_binary_mask(cur, 0.1)[0]
                result.append(cur)
            return result

        def get_whole_merged_mask():
            all_masks = []
            for segs in segs_by_frames:
                all_masks += segs_nodes.SEGSToMaskList().doit(segs)[0]
            merged_mask = (all_masks[0] * 255).to(torch.uint8)
            for mask in all_masks[1:]:
                merged_mask |= (mask * 255).to(torch.uint8)
            merged_mask = (merged_mask / 255.0).to(torch.float32)
            merged_mask = utils.to_binary_mask(merged_mask, 0.1)[0]
            return merged_mask

        def get_pivot_segs():
            if segs_pivot == '1st frame mask':
                return segs_by_frames[0][1]
            else:
                merged_mask = get_whole_merged_mask()
                return segs_nodes.MaskToSEGS().doit(merged_mask, False, crop_factor, False, drop_size, contour_fill=True)[0]

        def get_merged_neighboring_segs():
            pivot_segs = get_pivot_segs()
            masks_by_frame = get_masked_frames()
            masks_by_frame = get_merged_neighboring_mask(masks_by_frame)
            new_segs = []
            for seg in pivot_segs[1]:
                cropped_mask = torch.zeros(seg.cropped_mask.shape, dtype=torch.float32, device='cpu').unsqueeze(0)
                pivot_mask = torch.from_numpy(seg.cropped_mask)
                (x1, y1, x2, y2) = seg.crop_region
                for mask in masks_by_frame:
                    cropped_mask_at_frame = (mask[y1:y2, x1:x2] * pivot_mask).unsqueeze(0)
                    cropped_mask = torch.cat((cropped_mask, cropped_mask_at_frame), dim=0)
                if len(cropped_mask) > 1:
                    cropped_mask = cropped_mask[1:]
                new_seg = SEG(seg.cropped_image, cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
                new_segs.append(new_seg)
            return (pivot_segs[0], new_segs)

        def get_separated_segs():
            pivot_segs = get_pivot_segs()
            masks_by_frame = get_masked_frames()
            new_segs = []
            for seg in pivot_segs[1]:
                cropped_mask = torch.zeros(seg.cropped_mask.shape, dtype=torch.float32, device='cpu').unsqueeze(0)
                (x1, y1, x2, y2) = seg.crop_region
                for mask in masks_by_frame:
                    cropped_mask_at_frame = mask[y1:y2, x1:x2]
                    cropped_mask = torch.cat((cropped_mask, cropped_mask_at_frame), dim=0)
                new_seg = SEG(seg.cropped_image, cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
                new_segs.append(new_seg)
            return (pivot_segs[0], new_segs)
        if masking_mode == 'Pivot SEGS':
            return (get_pivot_segs(),)
        elif masking_mode == 'Combine neighboring frames':
            return (get_merged_neighboring_segs(),)
        else:
            return (get_separated_segs(),)

    def doit(self, bbox_detector, image_frames, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, masking_mode='Pivot SEGS', segs_pivot='Combined mask', sam_model_opt=None, segm_detector_opt=None):
        return SimpleDetectorForAnimateDiff.detect(bbox_detector, image_frames, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, masking_mode, segs_pivot, sam_model_opt, segm_detector_opt)
```