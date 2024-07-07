# Documentation
- Class name: CheckpointLoaderSimpleMikey
- Category: Mikey/Loaders
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The CheckpointLoader Simple Mikey node is designed to simplify the loading and management process of the checkpoints in the machine learning workflow. It provides a simple interface to retrieve model status, associated clips and conversion encoders (VAEs) from the specified checkpoint directory. The node also calculates and returns the Hashi values of the check point files to ensure data integrity and traceability.

# Input types
## Required
- ckpt_name
    - The parameter 'ckpt_name' is essential to identify a particular check point that you want to load. Node uses it to locate and access the relevant model status and configuration file in the checkpoint directory.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The parameter 'output_vae' decides whether to load the variable coder associated with the check point. It provides flexibility in the operation of the node and allows the user to control the components of the search check point.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - Parameter 'output_clip'controls the loading of clips associated with the checkpoint. It allows nodes to contain or exclude clips selectively according to the user's needs.
    - Comfy dtype: bool
    - Python dtype: bool
- unique_id
    - Parameter'unique_id' is used for additional identification purposes in node operations. In some applications, multiple checkpoints may need to be distinguished by way of an extra filename, and then 'unique_id' becomes relevant.
    - Comfy dtype: str
    - Python dtype: str
- extra_pnginfo
    - The parameter 'extra_pnginfo' is designed to provide the additional information that may be required for certain operations in the node. Its use is optional and depends on the context, increasing the adaptability of the node to the various scenarios.
    - Comfy dtype: str
    - Python dtype: str
- prompt
    - The parameter 'prompt' is used for behaviour based on user input of the lead node. It can influence how the check point is handled or the information returned, providing a certain degree of customization for node execution.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- model
    - Output'model' represents the state of the machine learning model loaded from the checkpoint. It is the core component of the node function, allowing the model training process to continue or be analysed.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Output'clip' corresponds to the loaded clip associated with the check point. It is an optional component that can include additional context or function for some applications based on the 'output_clip' parameter.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- vae
    - Output 'vae' means the variable coder that is loaded from the check point. It is an optional part of the node output controlled by the 'output_vae' parameter that can be used to generate tasks or further analysis.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- ckpt_name
    - Output 'ckpt_name' provides the name of the checked-point file that is loaded. This is useful for recording, tracking or quoting a particular check-point in a follow-up operation.
    - Comfy dtype: str
    - Python dtype: str
- ckpt_hash
    - Output 'ckpt_hash' is the Hashi value derived from the check-point file. As the only identifier for the check-point, it is very useful for verifying the integrity of the data loaded or for recording purposes.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointLoaderSimpleMikey:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'vae', 'ckpt_name', 'ckpt_hash')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'Mikey/Loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True, unique_id=None, extra_pnginfo=None, prompt=None):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        hash = get_file_hash(ckpt_path)
        ckpt_name = os.path.basename(ckpt_name)
        return out[:3] + (ckpt_name, hash)
```