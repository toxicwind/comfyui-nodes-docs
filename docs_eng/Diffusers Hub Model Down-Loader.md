# Documentation
- Class name: WAS_Diffusers_Hub_Model_Loader
- Category: WAS Suite/Loaders/Advanced
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Diffuses_Hub_Model_Loader is designed to facilitate the loading of advanced machine learning models from the Hugging Face modelling centre. It streamlines the process of downloading and initializing models, clips and VAEs so that users can quickly integrate these components into their workflows. This node is essential for tasks such as natural language processing and generating AI, which require complex model capabilities.

# Input types
## Required
- repo_id
    - Repo_id parameters are essential for identifying specific model repositories on Hugging Face Hub. They play a key role in the implementation of nodes by pointing the download process to the right source and ensuring that the models required are accurately retrieved.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- revision
    - The reference parameter allows the specified version of the model in the repository to be specified. It is important for users who need a specific model to overlap in order to perform their task, ensuring the replicability and consistency of model performance.
    - Comfy dtype: STRING
    - Python dtype: Union[str, None]

# Output types
- model
    - Model output provides a loaded machine learning model that can be reasoned or further processed. It is the core component of the node function and provides users with direct access to the predictive capabilities of the model.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - Clip output is a component normally used in conjunction with the model for tasks involving text and image interaction. It is important for users using this node for advanced natural language processing applications.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - The vae output is a variable-based encoder that generates the type of neural network of the task. It is a valuable asset for users who want to generate new data examples based on the distribution of the learning data sets.
    - Comfy dtype: VAE
    - Python dtype: Any
- name_string
    - The name_string output returns the memory ID in string form, providing a human readable identifier for the loaded model. It is very useful for reference and recording purposes in the workflow.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Diffusers_Hub_Model_Loader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'repo_id': ('STRING', {'multiline': False}), 'revision': ('STRING', {'default': 'None', 'multiline': False})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', TEXT_TYPE)
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'NAME_STRING')
    FUNCTION = 'load_hub_checkpoint'
    CATEGORY = 'WAS Suite/Loaders/Advanced'

    def load_hub_checkpoint(self, repo_id=None, revision=None):
        if revision in ['', 'None', 'none', None]:
            revision = None
        model_path = comfy_paths.get_folder_paths('diffusers')[0]
        self.download_diffusers_model(repo_id, model_path, revision)
        diffusersLoader = nodes.DiffusersLoader()
        (model, clip, vae) = diffusersLoader.load_checkpoint(os.path.join(model_path, repo_id))
        return (model, clip, vae, repo_id)

    def download_diffusers_model(self, repo_id, local_dir, revision=None):
        if 'huggingface-hub' not in packages():
            install_package('huggingface_hub')
        from huggingface_hub import snapshot_download
        model_path = os.path.join(local_dir, repo_id)
        ignore_patterns = ['*.ckpt', '*.safetensors', '*.onnx']
        snapshot_download(repo_id=repo_id, repo_type='model', local_dir=model_path, revision=revision, use_auth_token=False, ignore_patterns=ignore_patterns)
```