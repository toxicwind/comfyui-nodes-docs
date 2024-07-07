# Documentation
- Class name: SEGSLabelFilter
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSLabelFilter node is designed to process and filter segments according to a predefined tab set. It allows for the inclusion of specific paragraph types and handles the classification of paragraphs into two groups: those that match the specified label and those that do not. This node plays a key role in the selection of the paragraph that is used for further analysis or processing in the ImpactPack application package.

# Input types
## Required
- segs
    - The'segs' parameter is essential because it represents a pool of segments to be filtered. It directly influences the operation of nodes by determining the input data set to be processed.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Any, List[impact.core.SEG]]
- preset
    - The 'preset'parameter specifies a list of predefined detection labels for the filters. It is a key component in defining the filter criteria.
    - Comfy dtype: STRING
    - Python dtype: str
- labels
    - The 'labels' parameter is a multi-line string that allows users to list the type of segment they want to allow. It is important because it sets filter standards based on user input.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- filtered_SEGS
    - The 'filtered_SEGS' output contains segments that match the specified label, which is the main result of the filtering process.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Any, List[impact.core.SEG]]
- remained_SEGS
    - The'remained_SEGS' output includes a segment that does not match the specified label as a secondary result of node operations.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Any, List[impact.core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSLabelFilter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'preset': (['all'] + defs.detection_labels,), 'labels': ('STRING', {'multiline': True, 'placeholder': 'List the types of segments to be allowed, separated by commas'})}}
    RETURN_TYPES = ('SEGS', 'SEGS')
    RETURN_NAMES = ('filtered_SEGS', 'remained_SEGS')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    @staticmethod
    def filter(segs, labels):
        labels = set([label.strip() for label in labels])
        if 'all' in labels:
            return (segs, (segs[0], []))
        else:
            res_segs = []
            remained_segs = []
            for x in segs[1]:
                if x.label in labels:
                    res_segs.append(x)
                elif 'eyes' in labels and x.label in ['left_eye', 'right_eye']:
                    res_segs.append(x)
                elif 'eyebrows' in labels and x.label in ['left_eyebrow', 'right_eyebrow']:
                    res_segs.append(x)
                elif 'pupils' in labels and x.label in ['left_pupil', 'right_pupil']:
                    res_segs.append(x)
                else:
                    remained_segs.append(x)
        return ((segs[0], res_segs), (segs[0], remained_segs))

    def doit(self, segs, preset, labels):
        labels = labels.split(',')
        return SEGSLabelFilter.filter(segs, labels)
```