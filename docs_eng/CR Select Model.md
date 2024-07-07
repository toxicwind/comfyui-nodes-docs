# Documentation
- Class name: CR_SelectModel
- Category: Comfyroll/Essential/Core
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SelectModel is a node used to select and load models according to user-defined criteria. It allows multiple check-point files to be specified and the appropriate model to be selected based on the index provided by the user. This node can handle different check-point files and returns a cluster of selected models, their associated clip and wae objects, check-point names and links to the document for further help.

# Input types
## Required
- ckpt_name1
    - The parameter 'ckpt_name1' is the first check-point filename that the user can select. It plays a vital role in the operation of the node, as it determines one of the potential models that the node can load.
    - Comfy dtype: STRING
    - Python dtype: str
- ckpt_name2
    - The parameter 'ckpt_name2' is the second check-point filename that the user can select. It plays an important role in the selection item when providing the user with the selection model.
    - Comfy dtype: STRING
    - Python dtype: str
- ckpt_name3
    - The parameter 'ckpt_name3' is the third check-point filename that users can choose. It helps to increase the diversity of models that nodes can handle.
    - Comfy dtype: STRING
    - Python dtype: str
- ckpt_name4
    - The parameter 'ckpt_name4' is the fourth check-point filename that the user can select. It is part of the range of options available for model selection.
    - Comfy dtype: STRING
    - Python dtype: str
- ckpt_name5
    - Parameters 'ckpt_name5' are the fifth check-point filenames that users can select. It increases the range of models that nodes can load.
    - Comfy dtype: STRING
    - Python dtype: str
- select_model
    - The parameter'select_model' is an integer that determines which check-point file to load the model. It is very important because it directly affects the node selection and subsequent loading of the model.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MODEL
    - Output 'MODEL' is a model object that the user selects to load. It is important because it represents the core function of the node, making further processing or analysis possible.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - Output 'CLIP' is a clip object associated with the selected model. It is important to provide an additional context or function associated with the model.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- VAE
    - Output 'VAE' is a variable coder object in a model structure. It is important for tasks involving the generation of models or potential space operations.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- ckpt_name
    - Output 'ckpt_name'provides the name of the checkpoint file used to load the model. It is useful for tracking purposes or for further model management.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Output'show_help' is a URL linked to a node document. It is useful for users who need additional guidance or information on nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SelectModel:

    @classmethod
    def INPUT_TYPES(cls):
        checkpoint_files = ['None'] + folder_paths.get_filename_list('checkpoints')
        return {'required': {'ckpt_name1': (checkpoint_files,), 'ckpt_name2': (checkpoint_files,), 'ckpt_name3': (checkpoint_files,), 'ckpt_name4': (checkpoint_files,), 'ckpt_name5': (checkpoint_files,), 'select_model': ('INT', {'default': 1, 'min': 1, 'max': 5})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'ckpt_name', 'show_help')
    FUNCTION = 'select_model'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def select_model(self, ckpt_name1, ckpt_name2, ckpt_name3, ckpt_name4, ckpt_name5, select_model):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-select-model'
        model_list = list()
        if select_model == 1:
            model_name = ckpt_name1
        elif select_model == 2:
            model_name = ckpt_name2
        elif select_model == 3:
            model_name = ckpt_name3
        elif select_model == 4:
            model_name = ckpt_name4
        elif select_model == 5:
            model_name = ckpt_name5
        if model_name == 'None':
            print(f'CR Select Model: No model selected')
            return ()
        ckpt_path = folder_paths.get_full_path('checkpoints', model_name)
        (model, clip, vae, clipvision) = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        return (model, clip, vae, model_name, show_help)
```