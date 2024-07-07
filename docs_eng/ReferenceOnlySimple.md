# Documentation
- Class name: ReferenceOnlySimple
- Category: custom_node_experiments
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

The `reference_only' method in the `ReferenceOnly Simple'node is designed to enhance the given model by integrating the reference structure. It operates by cloning the model and applying a self-defined reference application function to its attention mechanism, allowing for the integration of additional potential samples. This method is particularly applicable to experiments involving model adaptation and potential space operations.

# Input types
## Required
- model
    - The `model' parameter is essential because it represents a machine learning model to be enhanced by nodes. It is the main input and determines the follow-up and conversion of applications within nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- reference
    - The'reference' parameter is a key input that provides a potential spatial sample to be integrated with the model. It plays an important role in the function of the node by influencing the structure and content of the potential space.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- batch_size
    - The `batch_size' parameter determines the batch size to be used in model operations. It affects the efficiency and memory usage of nodes and allows customization according to the specific requirements of the task at hand.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model_reference
    - The `model_reference' output is a modified model that has been enhanced by the reference structure. It is a direct result of node operations and can be further used or evaluated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- latent
    - The `latent' output contains a combination of potential space samples from the reference and node. It represents the ability to operate the node and expand the potential space.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class ReferenceOnlySimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'reference': ('LATENT',), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('MODEL', 'LATENT')
    FUNCTION = 'reference_only'
    CATEGORY = 'custom_node_experiments'

    def reference_only(self, model, reference, batch_size):
        model_reference = model.clone()
        size_latent = list(reference['samples'].shape)
        size_latent[0] = batch_size
        latent = {}
        latent['samples'] = torch.zeros(size_latent)
        batch = latent['samples'].shape[0] + reference['samples'].shape[0]

        def reference_apply(q, k, v, extra_options):
            k = k.clone().repeat(1, 2, 1)
            offset = 0
            if q.shape[0] > batch:
                offset = batch
            for o in range(0, q.shape[0], batch):
                for x in range(1, batch):
                    k[x + o, q.shape[1]:] = q[o, :]
            return (q, k, k)
        model_reference.set_model_attn1_patch(reference_apply)
        out_latent = torch.cat((reference['samples'], latent['samples']))
        if 'noise_mask' in latent:
            mask = latent['noise_mask']
        else:
            mask = torch.ones((64, 64), dtype=torch.float32, device='cpu')
        if len(mask.shape) < 3:
            mask = mask.unsqueeze(0)
        if mask.shape[0] < latent['samples'].shape[0]:
            print(latent['samples'].shape, mask.shape)
            mask = mask.repeat(latent['samples'].shape[0], 1, 1)
        out_mask = torch.zeros((1, mask.shape[1], mask.shape[2]), dtype=torch.float32, device='cpu')
        return (model_reference, {'samples': out_latent, 'noise_mask': torch.cat((out_mask, mask))})
```