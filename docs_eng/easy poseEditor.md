# Documentation
- Class name: poseEditor
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

PoeEditor nodes are designed to process and operate image data to extract and convert attitude-related features from input images. It is good at processing image data from different sources and converting them into formats suitable for further analysis or visualization.

# Input types
## Required
- image
    - The image parameter is essential because it defines the source image that will be processed at the node. It affects the operation of the node by determining the content and quality of the input data, which directly affects subsequent attitude analysis and conversion.
    - Comfy dtype: COMBO[sorted(os.listdir(temp_dir))]:string
    - Python dtype: str

# Output types
- output_pose
    - Output_pose represents the processed image data, which is converted and ready for further analysis. It encapsifies key information extracted from the input image, with a focus on attitude-related features.
    - Comfy dtype: tuple(torch.Tensor)
    - Python dtype: Tuple[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class poseEditor:

    @classmethod
    def INPUT_TYPES(self):
        temp_dir = folder_paths.get_temp_directory()
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir)
        temp_dir = folder_paths.get_temp_directory()
        return {'required': {}, 'optional': {'image': (sorted(os.listdir(temp_dir)),)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'output_pose'
    CATEGORY = 'EasyUse/Image'

    def output_pose(self, image):
        if image.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(image)
        else:
            image_path = os.path.join(folder_paths.get_temp_directory(), image)
            i = Image.open(image_path)
        image = i.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image,)

    @classmethod
    def IS_CHANGED(self, image):
        image_path = os.path.join(folder_paths.get_temp_directory(), image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()
```