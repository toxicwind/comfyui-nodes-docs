# Documentation
- Class name: EditDetailerPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

EditDetailer Pipe is a node that aims to enhance the text detail level by integrating models and components. It allows customizing the text generation process through the use of LoRA and wildcards and further refining by optional parameters such as models, clips and VAE. The main objective of this node is to provide a flexible and detailed text editing framework that can be adapted to specific needs.

# Input types
## Required
- detailer_pipe
    - The detailer_pipe parameter is essential for the operation of the EditDetailer Pipe node, as it represents the initial configuration or state of the text editing conduit. It is through this parameter that the node receives the basic components needed for further processing and customization.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]
- wildcard
    - The wildcard parameter plays a key role in the text editing process, allowing for the insertion of dynamic text elements. Its multiline and dynamicprompts properties indicate the flexibility and interaction of the text that can be generated, making it a key component to achieve the required level of detail.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- Select to add LoRA
    - The LoRA selection parameters enable the user to select a particular LORA model to enhance the details and nuances of the text. This selection can significantly influence the abundance and depth of the text being generated, making it an important aspect of the customization process.
    - Comfy dtype: COMBO[Select the LoRA to add to the text]
    - Python dtype: str
- Select to add Wildcard
    - This parameter allows the choice of wildcards to be included in the text, providing a mechanism for introducing variability and unpredictability in the text generation process. The wildcard selection can greatly influence the final result and make it an important factor in node operations.
    - Comfy dtype: COMBO[Select the Wildcard to add to the text]
    - Python dtype: str
- model
    - The model parameter is an optional input that can be used to specify a specific model during the text editing process. This allows customizing nodes according to the specific requirements of the task at hand.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - The clip parameter is another optional input that can be used to introduce a specific CLIP model into the text editing conduit. This changes the way text is processed and detailed, providing additional control over node output.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - The vae parameter provides an optional way to include the VAE in the text editing process. This can introduce abstraction and a learning level in the operation of nodes, which may improve the quality of the text generated.
    - Comfy dtype: VAE
    - Python dtype: Any
- positive
    - The positionive parameter is used to specify a positive condition input that guides the text generation process towards the desired result. This is particularly useful when guiding node behaviour to produce text with specific characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative parameters are used to define negative condition input and prevent the creation of certain text features. This helps to fine-tune the output of nodes by filtering out unwanted elements.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- bbox_detector
    - The bbox_detector parameter is an optional component that can be integrated into nodes to perform border box testing, which is very useful for applications involving spatial or geometric text analysis.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: Any
- sam_model
    - The sam_model parameter allows for the inclusion of a SAM (score-based confrontation model) that can guide the text generation process towards a more coherent and contextually relevant output.
    - Comfy dtype: SAM_MODEL
    - Python dtype: Any
- segm_detector
    - The segm_detector parameter is an optional input that integrates a partition detector into a node that assists in the identification and separation of different parts or components of the text.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: Any
- detailer_hook
    - The detailer_hook parameter provides a method for custom node behavior that allows the insertion of custom hooks or echoes in text editing. This enables advanced users to achieve specific functions or modifications.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Any
- refiner_model
    - The refinder_model parameter is an optional input that further refines the text editing process by designating a submodel. This is particularly useful for applications that require multi-stage text enhancement.
    - Comfy dtype: REFINER_MODEL
    - Python dtype: Any
- refiner_clip
    - The refinder_clip parameter allows the selection of a sub-CLIP model to enhance the detail and consistency of the text. It provides the user with an additional control layer to fine-tune the output of the point.
    - Comfy dtype: REFINER_CLIP
    - Python dtype: Any
- refiner_positive
    - The reference_positive parameter is used to provide a positive condition input for the subtext refinement phase. This helps to guide nodes to produce text with the required attributes in a more focused manner.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- refiner_negative
    - The reference_negative parameter is used to specify negative conditions for the process of refining subtexts. It helps to avoid unnecessary text features in the final stages of text editing.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Output types
- detailer_pipe
    - Output detailer_pipe represents a fine-tuning and customised text editing conduit processed through the EditDetaillePipe node. It covers all changes and enhancements to the initial pipe and provides a detailed and finely differentiated text-generation framework.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class EditDetailerPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],)}, 'optional': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'bbox_detector': ('BBOX_DETECTOR',), 'sam_model': ('SAM_MODEL',), 'segm_detector': ('SEGM_DETECTOR',), 'detailer_hook': ('DETAILER_HOOK',)}}
    RETURN_TYPES = ('DETAILER_PIPE',)
    RETURN_NAMES = ('detailer_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, *args, **kwargs):
        detailer_pipe = kwargs['detailer_pipe']
        wildcard = kwargs['wildcard']
        model = kwargs.get('model', None)
        clip = kwargs.get('clip', None)
        vae = kwargs.get('vae', None)
        positive = kwargs.get('positive', None)
        negative = kwargs.get('negative', None)
        bbox_detector = kwargs.get('bbox_detector', None)
        sam_model = kwargs.get('sam_model', None)
        segm_detector = kwargs.get('segm_detector', None)
        detailer_hook = kwargs.get('detailer_hook', None)
        refiner_model = kwargs.get('refiner_model', None)
        refiner_clip = kwargs.get('refiner_clip', None)
        refiner_positive = kwargs.get('refiner_positive', None)
        refiner_negative = kwargs.get('refiner_negative', None)
        (res_model, res_clip, res_vae, res_positive, res_negative, res_wildcard, res_bbox_detector, res_segm_detector, res_sam_model, res_detailer_hook, res_refiner_model, res_refiner_clip, res_refiner_positive, res_refiner_negative) = detailer_pipe
        if model is not None:
            res_model = model
        if clip is not None:
            res_clip = clip
        if vae is not None:
            res_vae = vae
        if positive is not None:
            res_positive = positive
        if negative is not None:
            res_negative = negative
        if bbox_detector is not None:
            res_bbox_detector = bbox_detector
        if segm_detector is not None:
            res_segm_detector = segm_detector
        if wildcard != '':
            res_wildcard = wildcard
        if sam_model is not None:
            res_sam_model = sam_model
        if detailer_hook is not None:
            res_detailer_hook = detailer_hook
        if refiner_model is not None:
            res_refiner_model = refiner_model
        if refiner_clip is not None:
            res_refiner_clip = refiner_clip
        if refiner_positive is not None:
            res_refiner_positive = refiner_positive
        if refiner_negative is not None:
            res_refiner_negative = refiner_negative
        pipe = (res_model, res_clip, res_vae, res_positive, res_negative, res_wildcard, res_bbox_detector, res_segm_detector, res_sam_model, res_detailer_hook, res_refiner_model, res_refiner_clip, res_refiner_positive, res_refiner_negative)
        return (pipe,)
```