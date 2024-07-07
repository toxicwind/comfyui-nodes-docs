# Documentation
- Class name: FacialFeatureSegment
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

The Mediape model is used to test the face of five officers and divides the left and right eye, eye, lip and tooth.

# Input types

## Required

- image
    - Enter the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- left_eye
    - Whether to include the left eye.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- left_eyebrow
    - Whether to include left eyebrows.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- right_eye
    - Whether to include the right eye.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- right_eyebrow
    - Whether to include right eyebrows.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- lips
    - Does it contain lips?
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- tooth
    - Does it contain teeth?
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types

- image
    - Output images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Output mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code

```python
class FacialFeatureSegment:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE",),  #
                "left_eye": ("BOOLEAN", {"default": True}),
                "left_eyebrow": ("BOOLEAN", {"default": True}),
                "right_eye": ("BOOLEAN", {"default": True}),
                "right_eyebrow": ("BOOLEAN", {"default": True}),
                "lips": ("BOOLEAN", {"default": True}),
                "tooth": ("BOOLEAN", {"default": True}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = 'facial_feature_segment'
    CATEGORY = '😺dzNodes/LayerMask'

    def facial_feature_segment(self, image,
                              left_eye, left_eyebrow, right_eye, right_eyebrow, lips, tooth
                  ):

        # Define facial characterization index
        left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        right_eye_indices = [263, 249, 390, 373, 374, 380, 381, 382, 362, 398, 384, 385, 386, 387, 388, 466]
        left_eyebrow_indices = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
        right_eyebrow_indices = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]
        tooth_indices = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308, 415, 310, 311, 312, 13, 82, 81, 80, 191, 78]
        lips_indices = [61, 76, 62, 78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178,
                         88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 375, 321, 405, 314, 17, 84, 181, 91, 146,
                         61]

        ret_images = []
        ret_masks = []
        scale_factor = 4

        for i in image:
            face_image = tensor2pil(i.unsqueeze(0)).convert('RGB')
            width, height = face_image.size
            width *= scale_factor
            height *= scale_factor
            cv2_image = pil2cv2(face_image)
            mp_face_mesh = mp.solutions.face_mesh
            fase_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
            results = fase_mesh.process(cv2_image)
            mask = np.zeros((height, width), dtype=np.uint8)


            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # Draw various facial features
                    if left_eye:
                        draw_feature(left_eye_indices, mask, face_landmarks, width, height)
                    if right_eye:
                        draw_feature(right_eye_indices, mask, face_landmarks, width, height)
                    if left_eyebrow:
                        draw_feature(left_eyebrow_indices, mask, face_landmarks, width, height)
                    if right_eyebrow:
                        draw_feature(right_eyebrow_indices, mask, face_landmarks, width, height)
                    if lips:
                        draw_feature(lips_indices, mask, face_landmarks, width, height)
                    if tooth:
                        draw_feature(tooth_indices, mask, face_landmarks, width, height)

            mask = cv22pil(mask).convert('L')
            mask = gaussian_blur(mask, 2)
            mask = mask.resize(face_image.size, Image.BILINEAR)
            ret_images.append(pil2tensor(RGB2RGBA(face_image, mask)))
            ret_masks.append(image2mask(mask))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), torch.cat(ret_masks, dim=0),)
```