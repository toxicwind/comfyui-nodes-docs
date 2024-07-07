# Documentation
- Class name: PoseEditor3D
- Category: image
- Output node: False
- Repo Ref: https://github.com/hinablue/ComfyUI_3dPoseEditor.git

PoseEditor 3D facilitates the operation and processing of 3D postures from images, allowing for the extraction and analysis of attitude data for various applications.

# Input types
## Optional
- pose
    - Posture parameters are essential for initializing 3D positions from the image, allowing nodes to focus on particular characters.
    - Comfy dtype: COMBO[sorted(os.listdir(temp_dir),)]
    - Python dtype: Union[str, None]
- depth
    - Deep images provide critical information for the 3D reconstruction process and improve the accuracy of attitude estimates.
    - Comfy dtype: COMBO[sorted(os.listdir(temp_dir),)]
    - Python dtype: Union[str, None]
- normal
    - The French-line image helps to understand the surface direction of the 3D image and improves visual representation of gestures.
    - Comfy dtype: COMBO[sorted(os.listdir(temp_dir),)]
    - Python dtype: Union[str, None]
- canny
    - Canny images are used for border detection, which is essential for identifying the contours and boundaries of the 3D posture.
    - Comfy dtype: COMBO[sorted(os.listdir(temp_dir),)]
    - Python dtype: Union[str, None]

# Output types
- OpenPose
    - The OpenPose output provides a detailed indication of the 3D posture, which is essential for further analysis and processing.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- Depth
    - The Depth output contains processed in-depth information that is essential to re-establishing and understanding the spatial relationship of the scene.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- Normal
    - The Normal output represents the surface direction of the 3D image and enhances the visual accuracy of the posture.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- Canny
    - Canny output provides marginal detection data, which is essential for identifying the contours and boundaries of the 3D posture.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PoseEditor3D(object):

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        temp_dir = folder_paths.get_temp_directory()
        temp_dir = os.path.join(temp_dir, '3dposeeditor')
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir)
        return {'required': {}, 'optional': {'pose': (sorted(os.listdir(temp_dir)),), 'depth': (sorted(os.listdir(temp_dir)),), 'normal': (sorted(os.listdir(temp_dir)),), 'canny': (sorted(os.listdir(temp_dir)),)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('OpenPose', 'Depth', 'Normal', 'Canny')
    FUNCTION = 'output_pose'
    CATEGORY = 'image'

    def output_pose(self, pose=None, depth=None, normal=None, canny=None):
        if pose is None:
            return (None, None, None, None)
        temp_dir = folder_paths.get_temp_directory()
        temp_dir = os.path.join(temp_dir, '3dposeeditor')
        image_path = os.path.join(temp_dir, pose)
        if pose.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(pose)
        else:
            i = Image.open(image_path)
        poseImage = i.convert('RGB')
        poseImage = np.array(poseImage).astype(np.float32) / 255.0
        poseImage = torch.from_numpy(poseImage)[None,]
        image_path = os.path.join(temp_dir, depth)
        if depth.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(depth)
        else:
            i = Image.open(image_path)
        depthImage = i.convert('RGB')
        depthImage = np.array(depthImage).astype(np.float32) / 255.0
        depthImage = torch.from_numpy(depthImage)[None,]
        image_path = os.path.join(temp_dir, normal)
        if normal.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(normal)
        else:
            i = Image.open(image_path)
        normalImage = i.convert('RGB')
        normalImage = np.array(normalImage).astype(np.float32) / 255.0
        normalImage = torch.from_numpy(normalImage)[None,]
        image_path = os.path.join(temp_dir, canny)
        if canny.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(canny)
        else:
            i = Image.open(image_path)
        cannyImage = i.convert('RGB')
        cannyImage = np.array(cannyImage).astype(np.float32) / 255.0
        cannyImage = torch.from_numpy(cannyImage)[None,]
        return (poseImage, depthImage, normalImage, cannyImage)

    @staticmethod
    def IS_CHANGED(self, pose=None, depth=None, normal=None, canny=None):
        if pose is None:
            return False
        temp_dir = folder_paths.get_temp_directory()
        temp_dir = os.path.join(temp_dir, '3dposeeditor')
        image_path = os.path.join(temp_dir, pose)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()
```