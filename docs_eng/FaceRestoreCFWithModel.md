# Documentation
- Class name: FaceRestoreCFWithModel
- Category: facerestore_cf
- Output node: False
- Repo Ref: https://github.com/mav-rik/facerestore_cf

The node is designed to improve and restore the quality of facial images using advanced in-depth learning models. It handles input images to improve overall clarity and detail through the detection of faces, alignment, and the application of restoration techniques. The main objective of the node is to generate high-quality facial images suitable for various applications, such as photo enhancement, identification and social media sharing.

# Input types
## Required
- facerestore_model
    - This parameter is assigned to the in-depth learning model for facial recovery. It is essential for the operation of the node, as it determines the ability of a particular model and the quality of the output to be restored.
    - Comfy dtype: string
    - Python dtype: str
- image
    - The input image of the facial recovery process will be applied. It is the main data input that directly affects output quality and recovery effects.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray
- facedetection
    - Select the facial test model used to identify and locate the image. The selection of the model affects the accuracy and reliability of the facial test and, consequently, the subsequent recovery process.
    - Comfy dtype: combo
    - Python dtype: str
## Optional
- codeformer_fidelity
    - Adjusts the authenticity of the recovery process, with higher values indicating closer to the original image details. This parameter allows fine-tuning of the balance between quality and computational efficiency.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- image
    - Output is a facial restoration image that is processed to improve its quality and clarity. This is the main result of node operations and represents the end result of the recovery process.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray

# Usage tips
- Infra type: GPU

# Source code
```
class FaceRestoreCFWithModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'facerestore_model': ('FACERESTORE_MODEL',), 'image': ('IMAGE',), 'facedetection': (['retinaface_resnet50', 'retinaface_mobile0.25', 'YOLOv5l', 'YOLOv5n'],), 'codeformer_fidelity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'restore_face'
    CATEGORY = 'facerestore_cf'

    def __init__(self):
        self.face_helper = None

    def restore_face(self, facerestore_model, image, facedetection, codeformer_fidelity):
        print(f'\tStarting restore_face with codeformer_fidelity: {codeformer_fidelity}')
        device = model_management.get_torch_device()
        facerestore_model.to(device)
        if self.face_helper is None:
            self.face_helper = FaceRestoreHelper(1, face_size=512, crop_ratio=(1, 1), det_model=facedetection, save_ext='png', use_parse=True, device=device)
        image_np = 255.0 * image.cpu().numpy()
        total_images = image_np.shape[0]
        out_images = np.ndarray(shape=image_np.shape)
        for i in range(total_images):
            cur_image_np = image_np[i, :, :, ::-1]
            original_resolution = cur_image_np.shape[0:2]
            if facerestore_model is None or self.face_helper is None:
                return image
            self.face_helper.clean_all()
            self.face_helper.read_image(cur_image_np)
            self.face_helper.get_face_landmarks_5(only_center_face=False, resize=640, eye_dist_threshold=5)
            self.face_helper.align_warp_face()
            restored_face = None
            for (idx, cropped_face) in enumerate(self.face_helper.cropped_faces):
                cropped_face_t = img2tensor(cropped_face / 255.0, bgr2rgb=True, float32=True)
                normalize(cropped_face_t, (0.5, 0.5, 0.5), (0.5, 0.5, 0.5), inplace=True)
                cropped_face_t = cropped_face_t.unsqueeze(0).to(device)
                try:
                    with torch.no_grad():
                        output = facerestore_model(cropped_face_t, w=codeformer_fidelity)[0]
                        restored_face = tensor2img(output, rgb2bgr=True, min_max=(-1, 1))
                    del output
                    torch.cuda.empty_cache()
                except Exception as error:
                    print(f'\tFailed inference for CodeFormer: {error}', file=sys.stderr)
                    restored_face = tensor2img(cropped_face_t, rgb2bgr=True, min_max=(-1, 1))
                restored_face = restored_face.astype('uint8')
                self.face_helper.add_restored_face(restored_face)
            self.face_helper.get_inverse_affine(None)
            restored_img = self.face_helper.paste_faces_to_input_image()
            restored_img = restored_img[:, :, ::-1]
            if original_resolution != restored_img.shape[0:2]:
                restored_img = cv2.resize(restored_img, (0, 0), fx=original_resolution[1] / restored_img.shape[1], fy=original_resolution[0] / restored_img.shape[0], interpolation=cv2.INTER_LINEAR)
            self.face_helper.clean_all()
            out_images[i] = restored_img
        restored_img_np = np.array(out_images).astype(np.float32) / 255.0
        restored_img_tensor = torch.from_numpy(restored_img_np)
        return (restored_img_tensor,)
```