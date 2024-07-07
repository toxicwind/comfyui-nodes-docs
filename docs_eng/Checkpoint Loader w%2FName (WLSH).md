# Documentation
- Class name: WLSH_Checkpoint_Loader_Model_Name
- Category: WLSH Nodes/loaders
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Checkpoint_Loader_Model_Name node is designed to load and manage the checkpoint in the stream. It is essential for continuity and repeatability of machine learning experiments, ensuring seamless integration and use of the saved model state. The node provides a direct interface to models, CLIP and VAE components by abstracting the complexity of search points.

# Input types
## Required
- ckpt_name
    - The 'ckpt_name'parameter is essential for identifying a particular check point to load. It guides node to the correct file path and is essential for successfully restoring model status from the stored checkpoint.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MODEL
    - The `MODEL' output provides a loaded model state that can be used for further processing or extrapolation during the follow-up phase of the workflow.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The `CLIP' output provides contextual language embedded in the check point to facilitate advanced language modelling functions in the application.
    - Comfy dtype: CLIP
    - Python dtype: Any
- VAE
    - The `VAE' output represents a variable-based encoder component retrieved from the checkpoint, which is essential for the generation of modeling or decomposition tasks.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- modelname
    - The'modelname' output returns the name of the check point after the resolution, which is very useful for recording, identifying or entering as other nodes that require the model name.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Checkpoint_Loader_Model_Name:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'modelname')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'WLSH Nodes/loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        name = self.parse_name(ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        new_out = list(out)
        new_out.pop()
        new_out.append(name)
        out = tuple(new_out)
        return out

    def parse_name(self, ckpt_name):
        path = ckpt_name
        filename = path.split('/')[-1]
        filename = filename.split('.')[:-1]
        filename = '.'.join(filename)
        return filename
```