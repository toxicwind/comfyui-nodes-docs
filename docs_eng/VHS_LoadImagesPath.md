# Load Images (Path) 🎥🅥🅗🅢
## Documentation
- Class name: VHS_LoadImagesPath
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

VHS_LoadImagesPath node is used to load images from the specified directory path into a video editing or processing workflow. It supports filtering and selection options to customize the loaded image collection, thereby efficiently managing and processing image batches in the video assistant package.

## Input types
### Required
- directory
    - Specifies the directory from which the image is to be loaded. This parameter is essential for determining the source of the image to be processed.
    - Comfy dtype: STRING
    - Python dtype: str

### Optional
- image_load_cap
    - Limits the number of images loaded from the directory and allows the size of the batch to be controlled.
    - Comfy dtype: INT
    - Python dtype: int
- skip_first_images
    - Skips the number of images specified at the beginning of the directory and allows the image to be loaded selectively in order.
    - Comfy dtype: INT
    - Python dtype: int
- select_every_nth
    - The loading of each n image in the directory provides a way to dilute the set of images to be processed.
    - Comfy dtype: INT
    - Python dtype: int

## Output types
- image
    - Comfy dtype: IMAGE
    - Loaded images for further processing or operation in the workflow.
    - Python dtype: torch.Tensor
- mask
    - Comfy dtype: MASK
    - The masked version generated for the loaded image is useful for image editing tasks that need to be split or selectively edited.
    - Python dtype: torch.Tensor
- int
    - Comfy dtype: INT
    - The total number of images loaded provides a view of the batch size after applying the load parameters.
    - Python dtype: int

## Usage tips
- Infra type: CPU
- Common nodes:
    - [ImpactImageBatchToImageList](../../ComfyUI-Impact-Pack/Nodes/ImpactImageBatchToImageList.md)
    - [PreviewImage](../../Comfy/Nodes/PreviewImage.md)
    - [IPAdapterEncoder](../../ComfyUI_IPAdapter_plus/Nodes/IPAdapterEncoder.md)
    - LinearBatchCreativeInterpolation

## Source code
```python
class LoadImagesFromDirectoryPath:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory": ("STRING", {"default": "X://path/to/images", "vhs_path_extensions": []}),
            },
            "optional": {
                "image_load_cap": ("INT", {"default": 0, "min": 0, "max": BIGMAX, "step": 1}),
                "skip_first_images": ("INT", {"default": 0, "min": 0, "max": BIGMAX, "step": 1}),
                "select_every_nth": ("INT", {"default": 1, "min": 1, "max": BIGMAX, "step": 1}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK", "INT")
    FUNCTION = "load_images"

    CATEGORY = "Video Helper Suite 🎥🅥🅗🅢"

    def load_images(self, directory: str, **kwargs):
        if directory is None or validate_load_images(directory) != True:
            raise Exception("directory is not valid: " + directory)

        return load_images(directory, **kwargs)

    @classmethod
    def IS_CHANGED(s, directory: str, **kwargs):
        if directory is None:
            return "input"
        return is_changed_load_images(directory, **kwargs)

    @classmethod
    def VALIDATE_INPUTS(s, directory: str, **kwargs):
        if directory is None:
            return True
        return validate_load_images(directory)