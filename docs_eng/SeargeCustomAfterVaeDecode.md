# Documentation
- Class name: SeargeCustomAfterVaeDecode
- Category: UI.CATEGORY_MAGIC_CUSTOM_STAGES
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to generate the final image by decoding and reprocessing of the output of the VAE. It encapsifies the logic needed to convert VAE's potential spatial expression into visual output and improves the efficiency and effectiveness of the entire workflow.

# Input types
## Required
- custom_output
    - The custom_output parameter is essential because it is an input into the VAE decoding process. It is the output of the previous phase and contains the necessary information for the node to perform its function.
    - Comfy dtype: SRG_STAGE_OUTPUT
    - Python dtype: Dict[str, Any]

# Output types
- image
    - The output image is the result of VAE decoding and reprocessing. It represents the final visual product after the node is completed and is essential for further analysis or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeCustomAfterVaeDecode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'custom_output': ('SRG_STAGE_OUTPUT',)}, 'optional': {}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'output'
    CATEGORY = UI.CATEGORY_MAGIC_CUSTOM_STAGES

    def output(self, custom_output):
        if custom_output is None:
            return (None,)
        vae_decoded = retrieve_parameter(Names.S_VAE_DECODED, custom_output)
        image = retrieve_parameter(Names.F_DECODED_IMAGE, vae_decoded)
        post_processed = retrieve_parameter(Names.F_POST_PROCESSED, vae_decoded)
        result = image if post_processed is None else post_processed
        return (result,)
```