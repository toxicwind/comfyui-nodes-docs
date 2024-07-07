# Documentation
- Class name: FaceBoundingBox
- Category: FaceAnalysis
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_FaceAnalysis.git

The node is designed to analyse images and detect facial boundary frames, providing critical functionality in image processing applications that require facial testing and analysis.

# Input types
## Required
- analysis_models
    - This parameter contains models and libraries for facial testing in the image, which have a significant impact on the ability of nodes to process and analyse input data.
    - Comfy dtype: DICT[str, Any]
    - Python dtype: Dict[str, Any]
- image
    - The image parameter is essential for the operation of the node, as it is the main input to the facial boundary frame detection and directly affects the accuracy and validity of the analysis.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- padding
    - Filling is an important parameter that ensures that there are sufficient boundaries to detect the face, prevents cutting problems and improves the overall quality of testing.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- index
    - Index parameters allow the selection of a specific face from multiple tests, concentrating the output of nodes on the required facial boundary box.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output image length represents the crop and processed image of the detected face and is an important component for further analysis or display purposes.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- x
    - The x-coordinate at the top left corner of the boundary box provides a reference point for facial testing, which helps to locate accurately the face in the image.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The y-coordinate at the top left corner of the boundary box is essential for accurately locating the detected face in the image context.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width of the boundary box is important because it determines the size of the detected face and affects the resolution and level of detail of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height of the boundary frame is essential to maintain the width and proportion of the detected face, and to ensure the integrity of the medium facial features of the output.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class FaceBoundingBox:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'analysis_models': ('ANALYSIS_MODELS',), 'image': ('IMAGE',), 'padding': ('INT', {'default': 0, 'min': 0, 'max': 4096, 'step': 1}), 'index': ('INT', {'default': -1, 'min': -1, 'max': 4096, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('IMAGE', 'x', 'y', 'width', 'height')
    FUNCTION = 'bbox'
    CATEGORY = 'FaceAnalysis'

    def bbox(self, analysis_models, image, padding, index=-1):
        out_img = []
        out_x = []
        out_y = []
        out_w = []
        out_h = []
        for i in image:
            img = T.ToPILImage()(i.permute(2, 0, 1)).convert('RGB')
            if analysis_models['library'] == 'insightface':
                faces = analysis_models['detector'].get(np.array(img))
                for face in faces:
                    (x, y, w, h) = face.bbox.astype(int)
                    w = w - x
                    h = h - y
                    x = max(0, x - padding)
                    y = max(0, y - padding)
                    w = min(img.width, w + 2 * padding)
                    h = min(img.height, h + 2 * padding)
                    crop = img.crop((x, y, x + w, y + h))
                    out_img.append(T.ToTensor()(crop).permute(1, 2, 0))
                    out_x.append(x)
                    out_y.append(y)
                    out_w.append(w)
                    out_h.append(h)
            else:
                faces = analysis_models['detector'](np.array(img), 1)
                for face in faces:
                    (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
                    x = max(0, x - padding)
                    y = max(0, y - padding)
                    w = min(img.width, w + 2 * padding)
                    h = min(img.height, h + 2 * padding)
                    crop = img.crop((x, y, x + w, y + h))
                    out_img.append(T.ToTensor()(crop).permute(1, 2, 0))
                    out_x.append(x)
                    out_y.append(y)
                    out_w.append(w)
                    out_h.append(h)
        if not out_img:
            raise Exception('No face detected in image.')
        if len(out_img) == 1:
            index = 0
        if index > len(out_img) - 1:
            index = len(out_img) - 1
        if index != -1:
            out_img = out_img[index].unsqueeze(0)
            out_x = out_x[index]
            out_y = out_y[index]
            out_w = out_w[index]
            out_h = out_h[index]
        else:
            w = out_img[0].shape[1]
            h = out_img[0].shape[0]
            out_img = [comfy.utils.common_upscale(img.unsqueeze(0).movedim(-1, 1), w, h, 'bilinear', 'center').movedim(1, -1).squeeze(0) for img in out_img]
            out_img = torch.stack(out_img)
        return (out_img, out_x, out_y, out_w, out_h)
```