# Documentation
- Class name: DenseposeSubjectEstimation
- Category: util
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The DenseposeSubjectEstimation node is designed to process and analyse the positions in the input image and select the most relevant positions based on the specified criteria through a series of filters. It contributes to the high-level tasks of the position by refining the input data to a more focused set of positions that meet the required themes and physical requirements.

# Input types
## Required
- openpose_image
    - The openpose_image parameter is essential because it is a visual input for position testing. It is the basis for node analysis and determines the existence and visibility of body parts, which subsequently influences the choice of position.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- subject
    - The subject parameter defines the subject-specific criteria to be used for filtering positions. It plays an important role in narrowing positions related to topics of interest, thereby enhancing the ability of nodes to provide targeted results.
    - Comfy dtype: STRING
    - Python dtype: str
- densepose_select_every_nth
    - The Densepose_select_every_nth parameter is an optional integer that determines the frequency of the position chosen from the post-filter position. It provides a mechanism for controlling the density of the output position, allowing for a balance between detail and computational efficiency.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- DENSEPOSE
    - DENSEPOSE output represents the final selected position in the input image after refining a series of theme-based and body-based filters. It marks the culmination of node analysis and is the main output for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- DENSEPOSE_NAME
    - DENSEPOSE_NAME output provides a selected pose identifier or name, provides a text reference that can be used for recording, marking or extra processing outside the main function of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class DenseposeSubjectEstimation:

    @classmethod
    def INPUT_TYPES(s):
        Return {required':'openpose_image': (`IMAGE',),'subject': ([`subject III',]), 'densepose_select_every_nth': (`INT', {default':1,'min':1,'step',}
    RETURN_TYPES = ['IMAGE', 'STRING']
    RETURN_NAMES = ['DENSEPOSE', 'DENSEPOSE_NAME']
    FUNCTION = 'main'
    CATEGORY = 'util'

    def apply_physique_filter(self, poses):
        return poses

    def apply_region_filter(self, openpose_image, poses):
        batch_size = openpose_image.shape[0]
        if batch_size != 1:
            raise ValueError('Batch size must be 1')
        limb_colors = {'left_foot': (85, 0, 255), 'left_lower_leg': (0, 51, 153), 'left_knee': (0, 0, 255), 'left_upper_leg': (0, 102, 153), 'right_foot': (0, 170, 255), 'right_lower_leg': (0, 153, 102), 'right_knee': (0, 255, 255), 'right_upper_leg': (0, 153, 51)}
        image_tensor = (openpose_image * 255).to(torch.uint8)
        limb_pixel_count = {}
        for (limb, color) in limb_colors.items():
            count = count_color_pixels(image_tensor, color)
            limb_pixel_count[limb] = count
        foot_visible = limb_pixel_count['left_foot'] > 0 and limb_pixel_count['right_foot'] > 0
        upper_leg_visible = limb_pixel_count['left_upper_leg'] > 0 and limb_pixel_count['right_upper_leg'] > 0
        lower_leg_visible = limb_pixel_count['left_lower_leg'] > 0 and limb_pixel_count['right_lower_leg'] > 0
        knee_visible = limb_pixel_count['left_knee'] > 0 and limb_pixel_count['right_knee'] > 0
        if foot_visible and upper_leg_visible and lower_leg_visible:
            return self.filter_poses(poses, 'full_body')
        if upper_leg_visible:
            return self.filter_poses(poses, 'knee_body')
        return self.filter_poses(poses, 'upper_body')

    @staticmethod
    def filter_poses(poses, positive_tag=None):
        res = []
        for (i, pose) in enumerate(poses):
            if positive_tag is not None and positive_tag not in pose['tags']:
                continue
            res.append(pose)
        return res

    def main(self, openpose_image, subject, densepose_select_every_nth=1):
        all_poses = self.filter_poses(densepose_subject_presets, subject)
        poses = self.filter_poses(all_poses)
        poses = self.apply_region_filter(openpose_image, poses)
        poses = self.apply_physique_filter(poses)
        print('filtered densepose tags', list(set((tag for pose in poses for tag in pose['tags']))))
        if len(poses) == 0:
            poses = self.filter_poses(all_poses, 'fallback')
        pose = random.choice(poses)
        densepose_name = pose.get('name')
        densepose = load_densepose(densepose_name, densepose_select_every_nth=densepose_select_every_nth)
        print(f'selected densepose is {densepose_name}')
        return (densepose, densepose_name)
```