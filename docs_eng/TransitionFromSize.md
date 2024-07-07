# Documentation
- Class name: TransitionFromSize
- Category: AIGC
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The TranslationFromSize node is designed to generate a series of images that depict a smooth transition from one image size to another. It uses the Bézier curve to control the deformation process and ensure a visual attraction. The function of the node is to create dynamic visual content that can be used in various applications, such as animation or visual effects.

# Input types
## Required
- image
    - The image parameter is the source image that will generate the transition sequence. This is a key input, as it defines the content and starting point of the transition.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or numpy.ndarray
- from_image_width
    - From_image_width parameters specify the initial width of the image at the beginning of the transition. It plays an important role in determining the initial dimensions of the deformation.
    - Comfy dtype: INT
    - Python dtype: int
- from_image_height
    - From_image_height parameters define the initial height of the image. It is essential to create the vertical dimensions of the frame in the transition sequence.
    - Comfy dtype: INT
    - Python dtype: int
- total_frames
    - Total_frames parameters specify the total number of frames in the transition sequence. It affects the duration and level of detail of the deformation process.
    - Comfy dtype: INT
    - Python dtype: int
- begin_and_end_frames
    - Begin_and_end_frames parameters determine the number of duplicate frames to be added at the beginning and end of the transition. This can be used to create a more gradual start and end sequence.
    - Comfy dtype: INT
    - Python dtype: int
- beiser_point_x
    - The beiser_point_x parameter is a control point on the Bézier curve, which affects the level of transition. It is a key factor in forming a deformation path curve.
    - Comfy dtype: FLOAT
    - Python dtype: float
- beiser_point_y
    - The beiser_point_y parameter is a control point on the Bézier curve, which affects the vertical aspects of the transition. It is essential to define the vertical curvature of the deformation path.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- IMAGE
    - The output of the TranslationFromSize node is a series of images representing the transition from the original size to the new size. Each frame in the sequence is the result of a deformation process controlled by the Bézier curve.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class TransitionFromSize:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'from_image_width': ('INT', {'min': 1}), 'from_image_height': ('INT', {'min': 1}), 'total_frames': ('INT', {'default': 40, 'min': 1}), 'begin_and_end_frames': ('INT', {'default': 10, 'min': 0}), 'beiser_point_x': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'beiser_point_y': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'get_transition_from_size'
    CATEGORY = 'AIGC'

    def get_transition_from_size(self, image, from_image_width, from_image_height, total_frames, begin_and_end_frames, beiser_point_x, beiser_point_y):
        outpating_image = image[0]
        frames = []
        origin_width = from_image_width
        origin_height = from_image_height
        new_width = outpating_image.shape[1]
        new_height = outpating_image.shape[0]
        if (origin_width > new_width) | (origin_height > new_height):
            origin_width = new_width * 0.75
            origin_height = new_height * 0.75
        white_origin_left = (new_width - origin_width) / 2
        white_origin_top = (new_height - origin_height) / 2
        print(f'image rect origin_width = {origin_width} origin_height = {origin_height} new_width = {new_width} new_height = {new_height}image white_origin_left = {white_origin_left} white_origin_top = {white_origin_top}')
        a = np.array([[0.0, beiser_point_x, 1.0], [0.0, beiser_point_y, 1.0]])
        curve = bezier.Curve(a, degree=2)
        s_vals = np.linspace(0.0, 1.0, total_frames)
        data = curve.evaluate_multi(s_vals)
        print(f' curve data = {data}')
        for a in range(total_frames):
            i = data[1][a]
            current_left = white_origin_left * (1 - i)
            current_top = white_origin_top * (1 - i)
            current_width = origin_width + 2 * i * white_origin_left
            current_height = origin_height + 2 * i * white_origin_top
            current_right = int(current_left + current_width)
            current_bottom = int(current_top + current_height)
            print(f'a = {a} i = {i}  current rect left = {current_left} width = {current_width} top = {current_top} height = {current_height}')
            current_img = outpating_image[int(current_top):current_bottom, int(current_left):current_right]
            current_img = current_img.numpy().astype(np.float32)
            img = cv2.resize(current_img, (new_width, new_height))
            frames.append(img)
            if a == 0:
                for j in range(begin_and_end_frames):
                    frames.append(img)
            elif a == total_frames - 1:
                for j in range(begin_and_end_frames):
                    frames.append(img)
        return_array = torch.Tensor(np.asarray(frames))
        return (return_array,)
```