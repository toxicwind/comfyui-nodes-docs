# Documentation
- Class name: ApplyInstantID
- Category: InstantID
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

The ApplyInstantID node is designed to integrate facial recognition and image-processing functions, using advanced machine learning models to improve the quality and relevance of input images. It ultimately improves the accuracy and detail of output by applying a series of changes to input images and contemplation of models according to specific facial characteristics.

# Input types
## Required
- instantid
    - The instantid parameter is essential to the operation of the node, as it provides the necessary facial recognition data and model structure for processing. Without it, node cannot carry out its expected facial analysis and enhancement tasks.
    - Comfy dtype: INSTANTID
    - Python dtype: Dict[str, Any]
- insightface
    - The insightface parameter is essential for the node because it contains a facial analysis model for extracting and processing facial features from input images. This parameter directly affects the accuracy and quality of facial signature tests.
    - Comfy dtype: FACEANALYSIS
    - Python dtype: Any
- control_net
    - The control_net parameter is a key component of the node, which allows node management and adjustment to be applied to the modelling process of conditionality. It helps fine-tune output to meet specific requirements and enhances overall performance enhanced by facial features.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Any
- image
    - The image parameter is the basis of the node function, which is extracted and enhanced as input for facial features. The quality and resolution of the image directly influences the validity and final output of facial recognition.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- model
    - Model parameters are at the core of node operations and provide a basic machine learning model for the implementation of facial characterization analysis and enhancement. The selection and quality of models significantly influence the performance and output of nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - The positionive parameter plays a crucial role in the operation of the node, guiding the enhancement process by providing positive condition data. It helps improve facial features and ensures that the output meets expectations.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - The nigative parameter is as important as the positive parameter, providing negative-condition data to help nodes avoid undesirable features in the output. It helps to enhance the accuracy of the facial signature process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
## Optional
- weight
    - The impact of the weight parameter should be applied to the strength of the conditions of the model, affecting the visibility of the desired characteristics in the final output. It provides a method of controlling the balance between the input conditions and the inherent capabilities of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - The start_at parameter defines the starting point of the condition process and determines the start of the enhancement of facial features. It is essential for controlling the timing and sequencing of the enhancement of features.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters set the end date of the conditional process and determine the end time of the enhanced facial feature. It works with start_at to ensure that the increased spacing of the enhanced facial feature is controlled and accurate.
    - Comfy dtype: FLOAT
    - Python dtype: float
- image_kps
    - The image_kps parameter provides key point data for facial features to guide the model to accurately locate and enhance specific facial elements. It helps to improve the accuracy and accuracy of facial features.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- mask
    - The mask parameter is used to apply a specific limit or focus area to the facial feature enhancement process. It allows targeted adjustments and improvements to ensure that enhancements are applied only to the desired area of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- MODEL
    - The output model is an enhanced machine learning model that is conditioned by input data to improve the accuracy and quality of facial feature extraction. It represents the results of node processing and is prepared for further use or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Positive output represents a positive face feature that has been successfully enhanced and conditioned, and can be used as a reference or input for the follow-up process. It is a key part of node output, indicating that facial enhancement has been successfully applied.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - Negative output includes adjusted conditional negative facial features to prevent undesirable features from appearing in the final output. It reflects the ability of nodes to fine-tune and control the output to meet specific requirements.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]

# Usage tips
- Infra type: GPU

# Source code
```
class ApplyInstantID:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'instantid': ('INSTANTID',), 'insightface': ('FACEANALYSIS',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'model': ('MODEL',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'weight': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 5.0, 'step': 0.01}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'image_kps': ('IMAGE',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('MODEL', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('MODEL', 'positive', 'negative')
    FUNCTION = 'apply_instantid'
    CATEGORY = 'InstantID'

    def apply_instantid(self, instantid, insightface, control_net, image, model, positive, negative, start_at, end_at, weight=0.8, ip_weight=None, cn_strength=None, noise=0.35, image_kps=None, mask=None):
        self.dtype = torch.float16 if comfy.model_management.should_use_fp16() else torch.float32
        self.device = comfy.model_management.get_torch_device()
        ip_weight = weight if ip_weight is None else ip_weight
        cn_strength = weight if cn_strength is None else cn_strength
        output_cross_attention_dim = instantid['ip_adapter']['1.to_k_ip.weight'].shape[1]
        is_sdxl = output_cross_attention_dim == 2048
        cross_attention_dim = 1280
        clip_extra_context_tokens = 16
        face_embed = extractFeatures(insightface, image)
        if face_embed is None:
            raise Exception('Reference Image: No face detected.')
        face_kps = extractFeatures(insightface, image_kps if image_kps is not None else image[0].unsqueeze(0), extract_kps=True)
        if face_kps is None:
            face_kps = torch.zeros_like(image) if image_kps is None else image_kps
            print(f'\x1b[33mWARNING: No face detected in the keypoints image!\x1b[0m')
        clip_embed = face_embed
        if clip_embed.shape[0] > 1:
            clip_embed = torch.mean(clip_embed, dim=0).unsqueeze(0)
        if noise > 0:
            seed = int(torch.sum(clip_embed).item()) % 1000000007
            torch.manual_seed(seed)
            clip_embed_zeroed = noise * torch.rand_like(clip_embed)
        else:
            clip_embed_zeroed = torch.zeros_like(clip_embed)
        clip_embeddings_dim = face_embed.shape[-1]
        self.instantid = InstantID(instantid, cross_attention_dim=cross_attention_dim, output_cross_attention_dim=output_cross_attention_dim, clip_embeddings_dim=clip_embeddings_dim, clip_extra_context_tokens=clip_extra_context_tokens)
        self.instantid.to(self.device, dtype=self.dtype)
        (image_prompt_embeds, uncond_image_prompt_embeds) = self.instantid.get_image_embeds(clip_embed.to(self.device, dtype=self.dtype), clip_embed_zeroed.to(self.device, dtype=self.dtype))
        image_prompt_embeds = image_prompt_embeds.to(self.device, dtype=self.dtype)
        uncond_image_prompt_embeds = uncond_image_prompt_embeds.to(self.device, dtype=self.dtype)
        work_model = model.clone()
        sigma_start = work_model.model.model_sampling.percent_to_sigma(start_at)
        sigma_end = work_model.model.model_sampling.percent_to_sigma(end_at)
        if mask is not None:
            mask = mask.to(self.device)
        patch_kwargs = {'number': 0, 'weight': ip_weight, 'ipadapter': self.instantid, 'cond': image_prompt_embeds, 'uncond': uncond_image_prompt_embeds, 'mask': mask, 'sigma_start': sigma_start, 'sigma_end': sigma_end, 'weight_type': 'original'}
        if not is_sdxl:
            for id in [1, 2, 4, 5, 7, 8]:
                _set_model_patch_replace(work_model, patch_kwargs, ('input', id))
                patch_kwargs['number'] += 1
            for id in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
                _set_model_patch_replace(work_model, patch_kwargs, ('output', id))
                patch_kwargs['number'] += 1
            _set_model_patch_replace(work_model, patch_kwargs, ('middle', 0))
        else:
            for id in [4, 5, 7, 8]:
                block_indices = range(2) if id in [4, 5] else range(10)
                for index in block_indices:
                    _set_model_patch_replace(work_model, patch_kwargs, ('input', id, index))
                    patch_kwargs['number'] += 1
            for id in range(6):
                block_indices = range(2) if id in [3, 4, 5] else range(10)
                for index in block_indices:
                    _set_model_patch_replace(work_model, patch_kwargs, ('output', id, index))
                    patch_kwargs['number'] += 1
            for index in range(10):
                _set_model_patch_replace(work_model, patch_kwargs, ('middle', 0, index))
                patch_kwargs['number'] += 1
        if mask is not None and len(mask.shape) < 3:
            mask = mask.unsqueeze(0)
        cnets = {}
        cond_uncond = []
        is_cond = True
        for conditioning in [positive, negative]:
            c = []
            for t in conditioning:
                d = t[1].copy()
                prev_cnet = d.get('control', None)
                if prev_cnet in cnets:
                    c_net = cnets[prev_cnet]
                else:
                    c_net = control_net.copy().set_cond_hint(face_kps.movedim(-1, 1), cn_strength, (start_at, end_at))
                    c_net.set_previous_controlnet(prev_cnet)
                    cnets[prev_cnet] = c_net
                d['control'] = c_net
                d['control_apply_to_uncond'] = False
                d['cross_attn_controlnet'] = image_prompt_embeds.to(comfy.model_management.intermediate_device()) if is_cond else uncond_image_prompt_embeds.to(comfy.model_management.intermediate_device())
                if mask is not None and is_cond:
                    d['mask'] = mask
                    d['set_area_to_bounds'] = False
                n = [t[0], d]
                c.append(n)
            cond_uncond.append(c)
            is_cond = False
        return (work_model, cond_uncond[0], cond_uncond[1])
```