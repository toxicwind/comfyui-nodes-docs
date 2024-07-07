# Documentation
- Class name: SEGSRangeFilter
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSRangeFilter node is designed to process and filter segments (SEGS) according to specific criteria associated with their spatial characteristics. It allows for the selection or exclusion of segments that meet the range of a given attribute value, such as size, width, height or percentage of length. The node meets the criteria provided by assessing each paragraph and classifys them accordingly as filtering or retaining segments.

# Input types
## Required
- segs
    - The'segs' parameter is essential because it represents the segment that will be filtered by the nodes. This is a series of objects that will be treated according to the criteria defined.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- target
    - The 'target'parameter determines the specific properties of the segment to be filtered. It can be one of several options, each corresponding to the different spatial characteristics of the segment.
    - Comfy dtype: COMBO['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2', 'length_percent']
    - Python dtype: str
- mode
    - The'mode' parameter determines whether the paragraph within the specified value is included in the filter output or excluded. It operates as a boolean switch in the 'inside' and 'outside' range.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- min_value
    - The'min_value'parameter sets the lower limit of the value range of the segment to be compared. It plays a key role in determining which paragraphs are filtered based on the object properties.
    - Comfy dtype: INT
    - Python dtype: int
- max_value
    - The'max_value'parameter determines the upper limit of the range of values to be used in the filter segment. It works with'min_value' to define the range of contents of the paragraph properties.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- filtered_SEGS
    - The 'filtered_SEGS' output contains sections that meet the filter criteria based on the specified target properties and range of values. It represents the main result of node operations.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]
- remained_SEGS
    - The'remained_SEGS' output includes segments that do not meet the filter criteria. These are sections that fall outside the specified value and are not included in the filter output.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSRangeFilter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'target': (['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2', 'length_percent'],), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'inside', 'label_off': 'outside'}), 'min_value': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'max_value': ('INT', {'default': 67108864, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    RETURN_TYPES = ('SEGS', 'SEGS')
    RETURN_NAMES = ('filtered_SEGS', 'remained_SEGS')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, target, mode, min_value, max_value):
        new_segs = []
        remained_segs = []
        for seg in segs[1]:
            x1 = seg.crop_region[0]
            y1 = seg.crop_region[1]
            x2 = seg.crop_region[2]
            y2 = seg.crop_region[3]
            if target == 'area(=w*h)':
                value = (y2 - y1) * (x2 - x1)
            elif target == 'length_percent':
                h = y2 - y1
                w = x2 - x1
                value = max(h / w, w / h) * 100
                print(f'value={value}')
            elif target == 'width':
                value = x2 - x1
            elif target == 'height':
                value = y2 - y1
            elif target == 'x1':
                value = x1
            elif target == 'x2':
                value = x2
            elif target == 'y1':
                value = y1
            else:
                value = y2
            if mode and min_value <= value <= max_value:
                print(f'[in] value={value} / {mode}, {min_value}, {max_value}')
                new_segs.append(seg)
            elif not mode and (value < min_value or value > max_value):
                print(f'[out] value={value} / {mode}, {min_value}, {max_value}')
                new_segs.append(seg)
            else:
                remained_segs.append(seg)
                print(f'[filter] value={value} / {mode}, {min_value}, {max_value}')
        return ((segs[0], new_segs), (segs[0], remained_segs))
```