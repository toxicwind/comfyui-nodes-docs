# Documentation
- Class name: TripoSRViewer
- Category: Flowty TripoSR
- Output node: True
- Repo Ref: https://github.com/flowtyone/ComfyUI-Flowty-TripoSR

The TripoSRViewer class display method is designed to visualize and export the 3D grid. It uses a series of conversions to enter the grid to prepare it for visualization and saves the modified grid in the specified directory structure. The method enhances the user's ability to review and analyse the 3D render task output and contributes to the overall workflow for 3D model operation and evaluation.

# Input types
## Required
- mesh
    - The mesh parameter is essential for the display method, which represents a 3D model that needs to be visualized and exported. It directly influences the results performed by the nodes by identifying the objects to be processed and displayed. The quality and attributes of the grid influences the ultimate visualization and export files, making them key components of node operations.
    - Comfy dtype: MESH
    - Python dtype: torch_geometric.data.Batch

# Output types
- mesh
    - The output grid parameter represents the 3D model modified and saved after the display method has been implemented. It is important because it provides the user with tangible results of the visualization process, allowing further analysis or use in downstream applications. The output grid, as a key link in the 3D model operating chain, shows the validity of the changes applied.
    - Comfy dtype: MESH
    - Python dtype: List[Dict[str, Union[str, int, List[str]]]]

# Usage tips
- Infra type: CPU

# Source code
```
class TripoSRViewer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mesh': ('MESH',)}}
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = 'display'
    CATEGORY = 'Flowty TripoSR'

    def display(self, mesh):
        saved = list()
        (full_output_folder, filename, counter, subfolder, filename_prefix) = get_save_image_path('meshsave', get_output_directory())
        for (batch_number, single_mesh) in enumerate(mesh):
            filename_with_batch_num = filename.replace('%batch_num%', str(batch_number))
            file = f'{filename_with_batch_num}_{counter:05}_.obj'
            single_mesh.apply_transform(np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]]))
            single_mesh.export(path.join(full_output_folder, file))
            saved.append({'filename': file, 'type': 'output', 'subfolder': subfolder})
        return {'ui': {'mesh': saved}}
```