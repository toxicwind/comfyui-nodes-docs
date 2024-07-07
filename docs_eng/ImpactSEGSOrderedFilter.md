# Documentation
- Class name: SEGSOrderedFilter
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSOrderedFilter node is designed to process and sort the SEGS (Semantic Enriched Geographic Councils, semantic geographical sections) according to specified criteria (e.g. size, width, altitude or coordinates). It allows users to define the sequence and scope of SEGS to be extracted. The function of the node is focused on organizing SEGS in a meaningful way so that it can be further analysed or visualized.

# Input types
## Required
- segs
    - The `segs' parameter is the set of SEGS objects that the node will process. It is vital because it forms the basis for all sorting operations performed by the node. This parameter directly affects the results of the node execution and determines which SEGS are sorted and how they are sorted.
    - Comfy dtype: SEGS
    - Python dtype: List[impact.core.SEG]
- target
    - The `target' parameter determines which properties are to be sorted according to SEGS. It can be the coordinates of the size, width, height or corner of the area that is to be cropped. This parameter is important because it determines the sorting criteria and affects the SEGS list of the final sorting.
    - Comfy dtype: COMBO['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2']
    - Python dtype: str
## Optional
- order
    - The `order' parameter specifies whether the order is descending or ascending when sorting according to the `target' properties. It is important because it controls the direction of the sorting, and for some applications the order of SEGS is essential.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- take_start
    - The `take_start' parameter defines which index will start with the extraction of SEGS. It is important because it allows for the selection of a specific SEGS range from the sorted list, which is very useful for focusing on specific subsets of data.
    - Comfy dtype: INT
    - Python dtype: int
- take_count
    - The `take_count' parameter specifies the number of SEGS to be extracted from the sorted list, starting with the `take_start' index. It is important because it determines the size of the SEGS subset to be extracted, which is important for managing the amount of data processed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- filtered_SEGS
    - The 'filtered_SEGS' output contains a subset of SEGS that is sorted and selected according to the 'take_start' and 'take_count' parameters. It is important because it represents the main result of node operations and provides a filter view of input data.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[impact.core.SEG, List[impact.core.SEG]]
- remained_SEGS
    - The'remained_SEGS' output includes the unselected SEGS from the node filtering process. These are the remaining SEGS after the extraction of the 'filtered_SEGS'. This output is important for considering the applications of selected and unselected data.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[impact.core.SEG, List[impact.core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSOrderedFilter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'target': (['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2'],), 'order': ('BOOLEAN', {'default': True, 'label_on': 'descending', 'label_off': 'ascending'}), 'take_start': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'take_count': ('INT', {'default': 1, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    RETURN_TYPES = ('SEGS', 'SEGS')
    RETURN_NAMES = ('filtered_SEGS', 'remained_SEGS')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, target, order, take_start, take_count):
        segs_with_order = []
        for seg in segs[1]:
            x1 = seg.crop_region[0]
            y1 = seg.crop_region[1]
            x2 = seg.crop_region[2]
            y2 = seg.crop_region[3]
            if target == 'area(=w*h)':
                value = (y2 - y1) * (x2 - x1)
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
            segs_with_order.append((value, seg))
        if order:
            sorted_list = sorted(segs_with_order, key=lambda x: x[0], reverse=True)
        else:
            sorted_list = sorted(segs_with_order, key=lambda x: x[0], reverse=False)
        result_list = []
        remained_list = []
        for (i, item) in enumerate(sorted_list):
            if take_start <= i < take_start + take_count:
                result_list.append(item[1])
            else:
                remained_list.append(item[1])
        return ((segs[0], result_list), (segs[0], remained_list))
```