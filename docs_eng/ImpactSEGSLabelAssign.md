# Documentation
- Class name: SEGSLabelAssign
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSLabelAssign node is designed to assign labels to a series of paragraphs. It receives a list of paragraphs and corresponding labels, ensuring that each paragraph is linked to the correct label in their order. The node plays a key role in organizing and disaggregating data for further processing and analysis.

# Input types
## Required
- segs
    - The'segs' parameter is the sum of the paragraphs that need to be marked. It is essential for the operation of the nodes because it defines the data that will receive the assigned labels. It directly influences the output of the nodes and determines the paragraphs that will be classified.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Any, List[impact.core.SEG]]
- labels
    - The 'labels' parameter is a string that contains comma-separated labels. It is essential for the execution of nodes because it specifies the labels that will be assigned to the paragraphs. The content of the parameters determines how the paragraphs are classified and affects the overall output of the nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- SEGS
    - Output 'SEGS' is the sum of the paragraphs marked after the distribution process. It represents the main result of the nodes and contains the paragraphs with the new distribution labels, which are essential for the follow-up task.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Any, List[impact.core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSLabelAssign:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'labels': ('STRING', {'multiline': True, 'placeholder': 'List the label to be assigned in order of segs, separated by commas'})}}
    RETURN_TYPES = ('SEGS',)
    RETURN_NAMES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    @staticmethod
    def assign(segs, labels):
        labels = [label.strip() for label in labels]
        if len(labels) != len(segs[1]):
            print(f'Warning (SEGSLabelAssign): length of labels ({len(labels)}) != length of segs ({len(segs[1])})')
        labeled_segs = []
        idx = 0
        for x in segs[1]:
            if len(labels) > idx:
                x = x._replace(label=labels[idx])
            labeled_segs.append(x)
            idx += 1
        return ((segs[0], labeled_segs),)

    def doit(self, segs, labels):
        labels = labels.split(',')
        return SEGSLabelAssign.assign(segs, labels)
```