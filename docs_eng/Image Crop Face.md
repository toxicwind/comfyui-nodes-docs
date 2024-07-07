# Documentation
- Class name: WAS_Image_Crop_Face
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Crop_Face node is designed to intelligently detect and tailor the face in the image. It uses a predefined cascade classifier to locate the face and allows for filling adjustments around the detected facial area. The node is capable of processing various facial scenes and returning a cropped face image, as well as the original image size and tailor coordinates.

# Input types
## Required
- image
    - Enter the image from which you will detect and crop the face. This is a mandatory parameter, because the operation of the node depends essentially on the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- crop_padding_factor
    - The filling factor determines the amount of filling around the detected face. A filling factor of 0.25 means 25% of the size of the face is used for filling. This is optional, if not provided, default is 0.25.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cascade_xml
    - A cascade XML file for facial testing. If the first XML file is not detected to the face, the node attempts to use multiple cascade files. This parameter is optional, and if not specified, the node uses the default cascade file.
    - Comfy dtype: COMBO[lbpcascade_animeface.xml, haarcascade_frontalface_default.xml, haarcascade_frontalface_alt.xml, haarcascade_frontalface_alt2.xml, haarcascade_frontalface_alt_tree.xml, haarcascade_profileface.xml, haarcascade_upperbody.xml]
    - Python dtype: str

# Output types
- cropped_face_image
    - The output is the image of the face after the clipping, which is adjusted and filled as necessary to extract it from the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- crop_data
    - This output provides metadata on facial cutting, including the original size of the face in the image and the coordinates of the crop frame.
    - Comfy dtype: COMBO[original_size, (left, top, right, bottom)]
    - Python dtype: Tuple[Tuple[int, int], Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Crop_Face:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'crop_padding_factor': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 2.0, 'step': 0.01}), 'cascade_xml': (['lbpcascade_animeface.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_profileface.xml', 'haarcascade_upperbody.xml', 'haarcascade_eye.xml'],)}}
    RETURN_TYPES = ('IMAGE', 'CROP_DATA')
    FUNCTION = 'image_crop_face'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_crop_face(self, image, cascade_xml=None, crop_padding_factor=0.25):
        return self.crop_face(tensor2pil(image), cascade_xml, crop_padding_factor)

    def crop_face(self, image, cascade_name=None, padding=0.25):
        import cv2
        img = np.array(image.convert('RGB'))
        face_location = None
        cascades = [os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'lbpcascade_animeface.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_frontalface_default.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_frontalface_alt.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_frontalface_alt2.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_frontalface_alt_tree.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_profileface.xml'), os.path.join(os.path.join(WAS_SUITE_ROOT, 'res'), 'haarcascade_upperbody.xml')]
        if cascade_name:
            for cascade in cascades:
                if os.path.basename(cascade) == cascade_name:
                    cascades.remove(cascade)
                    cascades.insert(0, cascade)
                    break
        faces = None
        if not face_location:
            for cascade in cascades:
                if not os.path.exists(cascade):
                    cstr(f'Unable to find cascade XML file at `{cascade}`. Did you pull the latest files from https://github.com/WASasquatch/was-node-suite-comfyui repo?').error.print()
                    return (pil2tensor(Image.new('RGB', (512, 512), (0, 0, 0))), False)
                face_cascade = cv2.CascadeClassifier(cascade)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                if len(faces) != 0:
                    cstr(f'Face found with: {os.path.basename(cascade)}').msg.print()
                    break
            if len(faces) == 0:
                cstr('No faces found in the image!').warning.print()
                return (pil2tensor(Image.new('RGB', (512, 512), (0, 0, 0))), False)
        else:
            cstr('Face found with: face_recognition model').warning.print()
            faces = face_location
        (x, y, w, h) = faces[0]
        left_adjust = max(0, -x)
        right_adjust = max(0, x + w - img.shape[1])
        top_adjust = max(0, -y)
        bottom_adjust = max(0, y + h - img.shape[0])
        if left_adjust < w:
            x += right_adjust
        elif right_adjust < w:
            x -= left_adjust
        if top_adjust < h:
            y += bottom_adjust
        elif bottom_adjust < h:
            y -= top_adjust
        w -= left_adjust + right_adjust
        h -= top_adjust + bottom_adjust
        face_size = min(h, w)
        y_pad = int(face_size * padding)
        x_pad = int(face_size * padding)
        center_x = x + w // 2
        center_y = y + h // 2
        half_size = (face_size + max(x_pad, y_pad)) // 2
        top = max(0, center_y - half_size)
        bottom = min(img.shape[0], center_y + half_size)
        left = max(0, center_x - half_size)
        right = min(img.shape[1], center_x + half_size)
        crop_size = min(right - left, bottom - top)
        left = center_x - crop_size // 2
        right = center_x + crop_size // 2
        top = center_y - crop_size // 2
        bottom = center_y + crop_size // 2
        face_img = img[top:bottom, left:right, :]
        size = max(face_img.copy().shape[:2])
        pad_h = (size - face_img.shape[0]) // 2
        pad_w = (size - face_img.shape[1]) // 2
        face_img = cv2.copyMakeBorder(face_img, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        min_size = 64
        if size < min_size:
            size = min_size
        face_img = cv2.resize(face_img, (size, size))
        face_img = Image.fromarray(face_img)
        original_size = face_img.size
        face_img.resize((face_img.size[0] // 64 * 64 + 64, face_img.size[1] // 64 * 64 + 64))
        return (pil2tensor(face_img.convert('RGB')), (original_size, (left, top, right, bottom)))
```