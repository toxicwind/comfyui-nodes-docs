# Documentation
- Class name: PromptImage
- Category: ♾️Mixlab/Prompt
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

PromptImage node is designed to process and operate images based on text tips. It receives tips and images as input and then generates a series of images that are influenced by input tips. The node has the ability to save these images to the specified directory, providing seamless integration between text and image processing for creative or analytical purposes.

# Input types
## Required
- prompts
    - The `prompts' parameter is an important input to the node because it provides the text content that guides image processing. Each hint is linked to a set of images and affects the final output.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- images
    - The `images' parameter is the basic input that contains the image data that you want to process. It is expected to be a list of image lengths and nodes will be operated according to the tips provided.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- save_to_image
    - The'save_to_image' parameter decides whether to save the processed image to the output directory. It allows the user to enable or disable the save function as necessary.
    - Comfy dtype: COMBO['enable', 'disable']
    - Python dtype: List[str]

# Output types
- ui
    - The 'ui'parameter in the output contains the user interface elements that display the processed image and its associated hints. It provides a structured way of presenting the results for further interaction or analysis.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptImage:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.prefix_append = 'PromptImage'
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompts': ('STRING', {'multiline': True, 'default': '', 'dynamicPrompts': False}), 'images': ('IMAGE', {'default': None}), 'save_to_image': (['enable', 'disable'],)}}
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    INPUT_IS_LIST = True
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'

    def run(self, prompts, images, save_to_image):
        filename_prefix = 'mixlab_'
        filename_prefix += self.prefix_append
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        save_to_image = save_to_image[0] == 'enable'
        for index in range(len(images)):
            res = []
            imgs = images[index]
            for image in imgs:
                img = tensor2pil(image)
                metadata = None
                if save_to_image:
                    metadata = PngInfo()
                    prompt_text = prompts[index]
                    if prompt_text is not None:
                        metadata.add_text('prompt_text', prompt_text)
                file = f'{filename}_{index}_{counter:05}_.png'
                img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=self.compress_level)
                res.append({'filename': file, 'subfolder': subfolder, 'type': self.type})
                counter += 1
            results.append(res)
        return {'ui': {'_images': results, 'prompts': prompts}}
```