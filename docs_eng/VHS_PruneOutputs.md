# Documentation
- Class name: PruneOutputs
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: True
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

Method 'prune_outputs'is designed to manage and clean intermediate and practical files generated in video processing workflows. It selects which files are deleted according to the chosen option intelligence, ensuring that the directory structure remains orderly and only the necessary files are kept.

# Input types
## Required
- filenames
    - Parameter 'filenames' is a list of file names that will be operated by nodes. It plays a key role in identifying the files to be trimmed. Node uses this list to determine the scope of its operations and to execute the file deletion process.
    - Comfy dtype: List[str]
    - Python dtype: List[str]
- options
    - The parameter 'options' determines the cut-off behaviour of the node. It specifies whether to delete the middle file, the practical file or both. This parameter is essential because it guides the decision-making process for which documents to delete.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- None
    - The method 'prune_outputs' does not produce any output because its main function is to delete files. It is a practical method that focuses on maintaining the cleaning and organization of the document system, rather than generating new data or results.
    - Comfy dtype: NoneType
    - Python dtype: NoneType

# Usage tips
- Infra type: CPU

# Source code
```
class PruneOutputs:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'filenames': ('VHS_FILENAMES',), 'options': (['Intermediate', 'Intermediate and Utility'],)}}
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    FUNCTION = 'prune_outputs'

    def prune_outputs(self, filenames, options):
        if len(filenames[1]) == 0:
            return ()
        assert len(filenames[1]) <= 3 and len(filenames[1]) >= 2
        delete_list = []
        if options in ['Intermediate', 'Intermediate and Utility', 'All']:
            delete_list += filenames[1][1:-1]
        if options in ['Intermediate and Utility', 'All']:
            delete_list.append(filenames[1][0])
        if options in ['All']:
            delete_list.append(filenames[1][-1])
        output_dirs = [os.path.abspath('output'), os.path.abspath('temp')]
        for file in delete_list:
            if os.path.commonpath([output_dirs[0], file]) != output_dirs[0] and os.path.commonpath([output_dirs[1], file]) != output_dirs[1]:
                raise Exception('Tried to prune output from invalid directory: ' + file)
            if os.path.exists(file):
                os.remove(file)
        return ()
```