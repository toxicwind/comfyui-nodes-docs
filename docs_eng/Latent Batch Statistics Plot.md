# Documentation
- Class name: LatentBatchStatisticsPlot
- Category: tests
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The LatinBatchStatisticsPlot node is designed to analyse the statistical properties of a group of potential variables. It carries out a comprehensive statistical analysis to determine the regularity of each of the potential variables in the batch. The node generates visualization of the statistical results, providing insight into the distribution characteristics of potential variables. This is particularly useful for researchers and data scientists who need graphic analysis tools to understand underlying data patterns.

# Input types
## Required
- batch
    - The `batch' parameter is essential for the operation of the node, as it represents a pool of potential variables to be analysed. It is a key input that directly influences statistical analysis and charts generated. It ensures that the node receives the correct data to perform its intended function.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- plot_image
    - The 'plot_image'output is a graphical expression of the statistical analysis performed by the nodes. It contains the p, mean and standard deviations of potential variables in the chart and provides a visual summary of the data distribution. This output is important because it enables users to quickly grasp the statistical properties of potential batches.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBatchStatisticsPlot:
    """
    Generate a plot of the statistics of a batch of latents for analysis.
    Outputs an image.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch': ('LATENT',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('plot_image',)
    FUNCTION = 'statistics'
    CATEGORY = 'tests'

    @torch.no_grad()
    def statistics(self, batch):
        """
        Run a statistical test on each latent in a batch to see how
        close to normal each latent is.
        """
        from scipy import stats
        batch = batch['samples']
        batch_size = batch.shape[0]
        p_values = []
        means = []
        std_devs = []
        for i in trange(batch.shape[0]):
            tensor_1d = batch[i].flatten()
            numpy_array = tensor_1d.numpy()
            (_, p) = stats.shapiro(numpy_array)
            p_values.append(p)
            means.append(numpy_array.mean())
            std_devs.append(numpy_array.std())
        (fig, axs) = plt.subplots(3, 1, figsize=(10, 15))
        axs[0].plot(p_values, label='p-values', marker='o', linestyle='-')
        axs[0].set_title('Shapiro-Wilk Test P-Values')
        axs[0].set_xlabel('Batch Number')
        axs[0].set_ylabel('P-Value')
        axs[0].axhline(y=0.05, color='r', linestyle='--', label='Normal Threshold')
        axs[0].legend()
        axs[1].plot(means, marker='o', linestyle='-')
        axs[1].set_title('Mean of Each Batch Latent')
        axs[1].set_xlabel('Batch Number')
        axs[1].set_ylabel('Mean')
        axs[2].plot(std_devs, marker='o', linestyle='-')
        axs[2].set_title('Standard Deviation of Each Batch Latent')
        axs[2].set_xlabel('Batch Number')
        axs[2].set_ylabel('Standard Deviation')
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        pil_image = Image.open(buf)
        image_tensor = pil2tensor(pil_image)
        batch_output = image_tensor.unsqueeze(0)
        return batch_output
```