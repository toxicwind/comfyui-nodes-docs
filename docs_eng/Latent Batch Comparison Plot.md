# Documentation
- Class name: LatentBatchComparator
- Category: test
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The node is designed to compare the two sets of potential variables by generating visualization indications that demonstrate their differences. It uses a cosine resemblance matrix to quantify the differences in potential vectors and to provide a clear intuitive understanding of their relative position in potential space.

# Input types
## Required
- latent_batch_1
    - This parameter represents the first batch of potential variables to be compared. It plays a key role in the operation of the node, as it forms the side of the comparison. The potential variable in this batch is expected to be structured in a way that allows meaningful comparison with the second batch.
    - Comfy dtype: "LATENT"
    - Python dtype: Dict[str, torch.Tensor]
- latent_batch_2
    - This parameter saves the second batch of potential variables to be compared with the first batch. It is as important as the first batch because it has completed a comparative analysis. The structure and format of the potential variables in this batch should be compatible with the potential variables in the first batch for accurate comparison.
    - Comfy dtype: "LATENT"
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- plot_image
    - The output of the node is an image of a cosine resemblance matrix between two sets of potential variables. As a visual tool, it clearly understands the similarities or differences between potential variables.
    - Comfy dtype: "IMAGE"
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBatchComparator:
    """
    Generate plots showing the differences between two batches of latents.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent_batch_1': ('LATENT',), 'latent_batch_2': ('LATENT',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('plot_image',)
    CATEGORY = 'test'
    FUNCTION = 'plot_latent_differences'

    def plot_latent_differences(self, latent_batch_1, latent_batch_2):
        """
        Generate a plot of the differences between two batches of latents.
        """
        import torch.nn.functional as F
        (tensor1, tensor2) = [x['samples'] for x in (latent_batch_1, latent_batch_2)]
        if tensor1.shape != tensor2.shape:
            raise ValueError('Latent batches must have the same shape: %s != %s' % (tensor1.shape, tensor2.shape))
        (B, C, H, W) = tensor1.shape
        tensor1_flat = tensor1.view(B, -1)
        tensor2_flat = tensor2.view(B, -1)
        tensor1_flat_expanded = tensor1_flat.unsqueeze(1)
        cosine_similarities_vectorized = F.cosine_similarity(tensor1_flat_expanded, tensor2_flat.unsqueeze(0), dim=2)
        plt.figure(figsize=(15, 10))
        plt.imshow(cosine_similarities_vectorized, cmap='viridis')
        plt.title('Cosine Similarity Matrix')
        plt.xlabel('Batch 1 Index')
        plt.ylabel('Batch 2 Index')
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        pil_image = Image.open(buf)
        image_tensor = pil2tensor(pil_image)
        batch_output = image_tensor.unsqueeze(0)
        return batch_output
```