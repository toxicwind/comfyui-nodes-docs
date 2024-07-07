# Documentation
- Class name: WD14Tagger
- Category: image
- Output node: True
- Repo Ref: https://github.com/pythongosssss/ComfyUI-WD14-Tagger

The node is designed to mark the image, classify the entered image data using the specified model and return the associated labels. By processing each image in the batch, it filters the label using a threshold value and respects any exclusion criteria provided. The main objective is to enhance the organization and retrieval of image data through automatic tags.

# Input types
## Required
- image
    - Image parameters are essential because they provide the raw data needed to mark the process. Without this input, nodes cannot perform their main function, i.e. classifying and tagging the image.
    - Comfy dtype: IMAGE
    - Python dtype: numpy.ndarray
- model
    - Model parameters are essential because they determine the specific machine learning model to be used in the image tagging process. It affects the accuracy and relevance of the labels generated.
    - Comfy dtype: all_models
    - Python dtype: callable
- threshold
    - The threshold parameter is important because it sets the minimum confidence level for the labels contained in the output. It directly influences the filtering of the labels and determines which are considered important enough to be reported.
    - Comfy dtype: FLOAT
    - Python dtype: float
- character_threshold
    - This parameter refines the marking process by setting a specific sub-threshold for character-level labels. It helps filter off less relevant character labels and improves the accuracy of the marking results.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- exclude_tags
    - The exclude_tags parameter allows the specification of labels that should not be included in the output. This is useful for customizing the marking results to specific requirements or avoiding certain labels for a variety of reasons.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- tags
    - The label output is the result of the image taging process and contains a list of relevant and important labels based on the input image and application thresholds. It is the key output, as it directly represents the primary function of the node and the validity of the taging process.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class WD14Tagger:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'model': (all_models,), 'threshold': ('FLOAT', {'default': defaults['threshold'], 'min': 0.0, 'max': 1, 'step': 0.05}), 'character_threshold': ('FLOAT', {'default': defaults['character_threshold'], 'min': 0.0, 'max': 1, 'step': 0.05}), 'exclude_tags': ('STRING', {'default': defaults['exclude_tags']})}}
    RETURN_TYPES = ('STRING',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'tag'
    OUTPUT_NODE = True
    CATEGORY = 'image'

    def tag(self, image, model, threshold, character_threshold, exclude_tags=''):
        tensor = image * 255
        tensor = np.array(tensor, dtype=np.uint8)
        pbar = comfy.utils.ProgressBar(tensor.shape[0])
        tags = []
        for i in range(tensor.shape[0]):
            image = Image.fromarray(tensor[i])
            tags.append(wait_for_async(lambda : tag(image, model, threshold, character_threshold, exclude_tags)))
            pbar.update(1)
        return {'ui': {'tags': tags}, 'result': (tags,)}
```