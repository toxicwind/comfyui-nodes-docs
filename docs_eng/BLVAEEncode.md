# Documentation
- Class name: BLVAEEncode
- Category: latent
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The BLVEEncode node is designed to encode images as potential spaces using a variable self-codifier (VAE). It provides the functionality to load existing potential expressions or to encode new ones from input images. The node also provides options for managing potential data, such as storing them for future use or removing them from workflows.

# Input types
## Required
- vae
    - The VAE parameter is critical to the encoding process, as it represents the variable coder model that will be used to convert input images to potential expressions.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- tiled
    - The tiled parameter decides whether the coding process should be performed in a flat format, which may be useful in processing larger images, which may not be fully RAMable at the time of overall coding.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tile_size
    - The tile_size parameter specifies the tile size in which the image will be divided into flattening codes. This is an important parameter when processing large images that need to be levelled.
    - Comfy dtype: INT
    - Python dtype: int
- store_or_load_latent
    - Whether the store_or_load_latent parameter control node should attempt to load potential indications from the workflow or to store the potential indications of the new code back into the workflow for future use.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- remove_latent_on_load
    - When set to true, the indicator node for remove_latet_on_load parameters removes it from the workflow after it has been successfully loaded with potential indications in order to release space and resources.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- delete_workflow_latent
    - When set to True, the derete_workflow_latent parameter indicator indicates the deletion of any existing potential expression in the workflow, whether or not it is encoded.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- image
    - The Image parameter is to encode the input image of the potential space. This is a mandatory parameter when there is no existing potential indication that you can load it from the workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- extra_pnginfo
    - Extra_pnginfo parameters are used to store and retrieve additional information relevant to the image, such as metadata or other supporting data that may be required for the coding process.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]
- unique_id
    - The unique_id parameter is the only identifier for the node example in the workflow and is used to manage the storage and retrieval of potential expressions.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- latent
    - The latent parameter represents the potential space for the encoding of the image. It is the main output of the BLVAEENDE node and is used for further processing or analysis in the workflow.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class BLVAEEncode:

    def __init__(self):
        self.VAEEncode = nodes.VAEEncode()
        self.VAEEncodeTiled = nodes.VAEEncodeTiled()
        self.last_hash = None

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'vae': ('VAE',), 'tiled': ('BOOLEAN', {'default': False}), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64}), 'store_or_load_latent': ('BOOLEAN', {'default': True}), 'remove_latent_on_load': ('BOOLEAN', {'default': True}), 'delete_workflow_latent': ('BOOLEAN', {'default': False})}, 'optional': {'image': ('IMAGE',)}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latent',)
    FUNCTION = 'encode'
    CATEGORY = 'latent'

    def encode(self, vae, tiled, tile_size, store_or_load_latent, remove_latent_on_load, delete_workflow_latent, image=None, extra_pnginfo=None, unique_id=None):
        workflow_latent = None
        latent_key = f'latent_{unique_id}'
        if self.last_hash and torch.is_tensor(image):
            if self.last_hash is not self.sha256(image):
                delete_workflow_latent = True
        if torch.is_tensor(image):
            self.last_hash = self.sha256(image)
        if delete_workflow_latent:
            if extra_pnginfo['workflow']['extra'].__contains__(latent_key):
                try:
                    del extra_pnginfo['workflow']['extra'][latent_key]
                except Exception:
                    print(f'Unable to delete latent image from workflow node: {unqiue_id}')
                    pass
        if store_or_load_latent and unique_id:
            if latent_key in extra_pnginfo['workflow']['extra']:
                print(f'Loading latent image from workflow node: {unique_id}')
                try:
                    workflow_latent = self.deserialize(extra_pnginfo['workflow']['extra'][latent_key])
                except Exception as e:
                    print('There was an issue extracting the latent tensor from the workflow. Is it corrupted?')
                    workflow_latent = None
                    if not torch.is_tensor(image):
                        raise ValueError(f'Node {unique_id}: There was no image provided, and workflow latent missing. Unable to proceed.')
                if workflow_latent and remove_latent_on_load:
                    try:
                        del extra_pnginfo['workflow']['extra'][latent_key]
                    except Exception:
                        pass
        if workflow_latent:
            print(f'Loaded workflow latent from node: {unique_id}')
            return (workflow_latent, {'extra_pnginfo': extra_pnginfo})
        if not torch.is_tensor(image):
            raise ValueError(f'Node {unique_id}: No workflow latent was loaded, and no image provided to encode. Unable to proceed. ')
        if tiled:
            encoded = self.VAEEncodeTiled.encode(pixels=image, tile_size=tile_size, vae=vae)
        else:
            encoded = self.VAEEncode.encode(pixels=image, vae=vae)
        if store_or_load_latent and unique_id:
            print(f'Saving latent to workflow node {unique_id}')
            new_workflow_latent = self.serialize(encoded[0])
            extra_pnginfo['workflow']['extra'][latent_key] = new_workflow_latent
        return (encoded[0], {'extra_pnginfo': extra_pnginfo})

    def sha256(self, tensor):
        tensor_bytes = tensor.cpu().contiguous().numpy().tobytes()
        hash_obj = hashlib.sha256()
        hash_obj.update(tensor_bytes)
        return hash_obj.hexdigest()

    def serialize(self, obj):
        json_str = json.dumps(obj, default=lambda o: {'__tensor__': True, 'value': o.cpu().numpy().tolist()} if torch.is_tensor(o) else o.__dict__)
        compressed_data = zlib.compress(json_str.encode('utf-8'))
        base64_encoded = base64.b64encode(compressed_data).decode('utf-8')
        return base64_encoded

    def deserialize(self, base64_str):
        compressed_data = base64.b64decode(base64_str)
        json_str = zlib.decompress(compressed_data).decode('utf-8')
        obj = json.loads(json_str, object_hook=lambda d: torch.tensor(d['value']) if '__tensor__' in d else d)
        return obj
```