# Documentation
- Class name: SaveFaceModel
- Category: 🌌 ReActor
- Output node: True
- Repo Ref: https://github.com/Gourieff/comfyui-reactor-node.git

The node is designed to preserve the facial identification model and encapsulates the process of converting image data into a structured format that can be used for further analysis or identification. It emphasizes the preservation of facial properties and features for future use, without exploring in depth the details of underlying algorithms or data structures.

# Input types
## Required
- save_mode
    - This parameter determines whether to preserve the model as a switch for the entire preservation process. It plays a key role in determining the output of the node and the subsequent actions of the system.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- face_model_name
    - The name given to the facial model as the identifier for the preservation of the model allows easy retrieval and reference in future operations. It is essential to maintain the organization and clarity of the model inventory.
    - Comfy dtype: STRING
    - Python dtype: str
- select_face_index
    - This index selects a particular face from the analytical data, guiding nodes to focus on the specific facial characteristics of the model. It plays an important role in targeting specific data in a broader data concentration.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image
    - The input image provides the visual data needed for facial analysis and model creation. Its quality and resolution directly influence the accuracy and detail of the facial model generated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- face_model
    - Facial model input is an optional parameter that, if provided, allows nodes to bypass facial analysis steps and save the given model directly. This simplifys the process when a pre-analysed model is available.
    - Comfy dtype: FACE_MODEL
    - Python dtype: insightface.Face

# Output types
- face_model_name
    - The output reflects the name of the preserved facial model, indicating the successful completion of the preservation process. It is used as a confirmation and reference to interact with the future of the saved model.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SaveFaceModel:

    def __init__(self):
        self.output_dir = FACE_MODELS_PATH

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'save_mode': ('BOOLEAN', {'default': True, 'label_off': 'OFF', 'label_on': 'ON'}), 'face_model_name': ('STRING', {'default': 'default'}), 'select_face_index': ('INT', {'default': 0, 'min': 0})}, 'optional': {'image': ('IMAGE',), 'face_model': ('FACE_MODEL',)}}
    RETURN_TYPES = ()
    FUNCTION = 'save_model'
    OUTPUT_NODE = True
    CATEGORY = '🌌 ReActor'

    def save_model(self, save_mode, face_model_name, select_face_index, image=None, face_model=None, det_size=(640, 640)):
        if save_mode and image is not None:
            source = tensor_to_pil(image)
            source = cv2.cvtColor(np.array(source), cv2.COLOR_RGB2BGR)
            apply_logging_patch(1)
            logger.status('Building Face Model...')
            face_model_raw = analyze_faces(source, det_size)
            if len(face_model_raw) == 0:
                det_size_half = half_det_size(det_size)
                face_model_raw = analyze_faces(source, det_size_half)
            try:
                face_model = face_model_raw[select_face_index]
            except:
                logger.error('No face(s) found')
                return face_model_name
            logger.status('--Done!--')
        if save_mode and (face_model != 'none' or face_model is not None):
            face_model_path = os.path.join(self.output_dir, face_model_name + '.safetensors')
            save_face_model(face_model, face_model_path)
        if image is None and face_model is None:
            logger.error('Please provide `face_model` or `image`')
        return face_model_name
```