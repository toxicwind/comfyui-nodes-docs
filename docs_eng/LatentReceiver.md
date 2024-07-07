# Documentation
- Class name: LatentReceiver
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the LatentReceiver node handles potential data. It is inputted by a potential file and exports the amount of space that represents potential space. This node is essential for processing the conversion and loading of potential expressions, which are essential for various machine learning tasks.

# Input types
## Required
- latent
    - The parameter 'latent' is the file path of a potential file, and the node will process the path. It is essential for the operation of the node, as it determines the specific potential data to be loaded and used for subsequent calculations.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- link_id
    - Parameters'link_id' are identifiers for tracking or linking potential data. Although not necessary, they may be useful when organizing or quoting data in larger systems or workflows.
    - Comfy dtype: INT
    - Python dtype: int
- trigger_always
    - The parameter 'trigger_always' is a boolean symbol that, when set to True, means that node should always trigger its process without considering the changes in the input data.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - Output'reult' is a volume that represents potential data after processing. It is the main output of nodes and is used for further analysis or as input to other nodes in the workflow.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor
- ui
    - Output 'ui' is a dictionary that may contain UI elements, such as images, for visual purposes. It provides a way of presenting post-processing data in a user-friendly format.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[str]]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentReceiver:

    def __init__(self):
        self.input_dir = folder_paths.get_input_directory()
        self.type = 'input'

    @classmethod
    def INPUT_TYPES(s):

        def check_file_extension(x):
            return x.endswith('.latent') or x.endswith('.latent.png')
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and check_file_extension(f)]
        return {'required': {'latent': (sorted(files),), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'trigger_always': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'
    RETURN_TYPES = ('LATENT',)

    @staticmethod
    def load_preview_latent(image_path):
        if not os.path.exists(image_path):
            return None
        image = Image.open(image_path)
        exif_data = piexif.load(image.info['exif'])
        if piexif.ExifIFD.UserComment in exif_data['Exif']:
            compressed_data = exif_data['Exif'][piexif.ExifIFD.UserComment]
            compressed_data_io = BytesIO(compressed_data)
            with zipfile.ZipFile(compressed_data_io, mode='r') as archive:
                tensor_bytes = archive.read('latent')
            tensor = safetensors.torch.load(tensor_bytes)
            return {'samples': tensor['latent_tensor']}
        return None

    def parse_filename(self, filename):
        pattern = '^(.*)/(.*?)\\[(.*)\\]\\s*$'
        match = re.match(pattern, filename)
        if match:
            subfolder = match.group(1)
            filename = match.group(2).rstrip()
            file_type = match.group(3)
        else:
            subfolder = ''
            file_type = self.type
        return {'filename': filename, 'subfolder': subfolder, 'type': file_type}

    def doit(self, **kwargs):
        if 'latent' not in kwargs:
            return (torch.zeros([1, 4, 8, 8]),)
        latent = kwargs['latent']
        latent_name = latent
        latent_path = folder_paths.get_annotated_filepath(latent_name)
        if latent.endswith('.latent'):
            latent = safetensors.torch.load_file(latent_path, device='cpu')
            multiplier = 1.0
            if 'latent_format_version_0' not in latent:
                multiplier = 1.0 / 0.18215
            samples = {'samples': latent['latent_tensor'].float() * multiplier}
        else:
            samples = LatentReceiver.load_preview_latent(latent_path)
        if samples is None:
            samples = {'samples': torch.zeros([1, 4, 8, 8])}
        preview = self.parse_filename(latent_name)
        return {'ui': {'images': [preview]}, 'result': (samples,)}

    @classmethod
    def IS_CHANGED(s, latent, link_id, trigger_always):
        if trigger_always:
            return float('NaN')
        else:
            image_path = folder_paths.get_annotated_filepath(latent)
            m = hashlib.sha256()
            with open(image_path, 'rb') as f:
                m.update(f.read())
            return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, latent, link_id, trigger_always):
        if not folder_paths.exists_annotated_filepath(latent) or latent.startswith('/') or '..' in latent:
            return 'Invalid latent file: {}'.format(latent)
        return True
```