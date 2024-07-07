# Documentation
- Class name: CR_XYFromFolder
- Category: Comfyroll/XY Grid
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_XYFromFolder node is designed to facilitate the creation of a visually structured grid by allowing users to specify comments for each image, setting font sizes and controlling the spacing between pictures. This node is particularly suitable for generating annotated grids for different purposes such as demonstration, directory or data visualization.

# Input types
## Required
- image_folder
    - Picture folder parameters are essential to define the source of the image that will be organized into a grid. It determines the directory of nodes to retrieve and process the picture.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- start_index
    - Starts indexing is an optional parameter that determines the starting point of the selection process. It allows control over which images are included in the grid, starting at a given location.
    - Comfy dtype: INT
    - Python dtype: int
- end_index
    - Ends the index parameter by specifying the end point for the selected picture. It defines the range of images to be included in the final grid layout.
    - Comfy dtype: INT
    - Python dtype: int
- max_columns
    - The maximum column parameter determines the number of columns in the grid. It is essential to define the grid structure and ensure a visual balance layout.
    - Comfy dtype: INT
    - Python dtype: int
- x_annotation
    - The x_annotation parameter is used to comment on the grid column. It adds a layer of information and context to the visual expression of the picture.
    - Comfy dtype: STRING
    - Python dtype: str
- y_annotation
    - y_annotation parameters are similar to x_annotation, but are used for rows in grids. It ensures that each line is correctly marked and commented on.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - Font size parameters control the size of the text used in the comment. It is an important aspect of the node function because it affects the readability and beauty of the grid.
    - Comfy dtype: INT
    - Python dtype: int
- gap
    - The spacing parameter defines the distance between images in the grid. It plays a role in the overall visual presentation to ensure that the picture is not overcrowded.
    - Comfy dtype: INT
    - Python dtype: int
- trigger
    - The trigger parameter is an optional switch that starts image processing and grid creation when activated. It provides a way of controlling when node operations are performed.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - The IMAGE output provides an annotated final photo grid for applications. It represents the results of node processing and layout work.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- trigger
    - The trigger output indicates whether the operation of the node is performed according to the input trigger. It serves as a feedback mechanism for node activation status.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - Show_help output provides a URL link to the node document page. It provides users with easy access to additional information and guidance on the use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYFromFolder:

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, t.Any]:
        input_dir = folder_paths.output_directory
        image_folder = [name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name))]
        return {'required': {'image_folder': (sorted(image_folder),), 'start_index': ('INT', {'default': 1, 'min': 0, 'max': 10000}), 'end_index': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'max_columns': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'x_annotation': ('STRING', {'multiline': True}), 'y_annotation': ('STRING', {'multiline': True}), 'font_size': ('INT', {'default': 50, 'min': 1}), 'gap': ('INT', {'default': 0, 'min': 0})}, 'optional': {'trigger': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE', 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('IMAGE', 'trigger', 'show_help')
    FUNCTION = 'load_images'
    CATEGORY = icons.get('Comfyroll/XY Grid')

    def load_images(self, image_folder, start_index, end_index, max_columns, x_annotation, y_annotation, font_size, gap, trigger=False):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes#cr-xy-from-folder'
        if trigger == False:
            return ((), False, show_help)
        input_dir = folder_paths.output_directory
        image_path = os.path.join(input_dir, image_folder)
        file_list = sorted(os.listdir(image_path), key=lambda s: sum(((s, int(n)) for (s, n) in re.findall('(\\D+)(\\d+)', 'a%s0' % s)), ()))
        sample_frames = []
        pillow_images = []
        if len(file_list) < end_index:
            end_index = len(file_list)
        for num in range(start_index, end_index + 1):
            i = Image.open(os.path.join(image_path, file_list[num - 1]))
            image = i.convert('RGB')
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            image = image.squeeze()
            sample_frames.append(image)
        resolved_font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts\\Roboto-Regular.ttf')
        font = ImageFont.truetype(str(resolved_font_path), size=font_size)
        start_x_ann = start_index % max_columns - 1
        start_y_ann = int(start_index / max_columns)
        column_list = x_annotation.split(';')[start_x_ann:]
        row_list = y_annotation.split(';')[start_y_ann:]
        column_list = [item.strip() for item in column_list]
        row_list = [item.strip() for item in row_list]
        annotation = Annotation(column_texts=column_list, row_texts=row_list, font=font)
        images = torch.stack(sample_frames)
        pillow_images = [tensor_to_pillow(i) for i in images]
        pillow_grid = create_images_grid_by_columns(images=pillow_images, gap=gap, annotation=annotation, max_columns=max_columns)
        tensor_grid = pillow_to_tensor(pillow_grid)
        return (tensor_grid, trigger, show_help)
```