# Documentation
- Class name: TESTNODE_
- Category: ♾️Mixlab/__TEST
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

TESTNODE_ node is designed to analyse and process a list of any type of element. It uses the ListStatistics tool to measure the number of occurrences of different data types in the list and to provide summaries of data compositions. The node also dynamically imports and executes functions from external modules that demonstrate their adaptability in dealing with various operations based on the input list. The node is intended to provide a comprehensive overview of the types of data that exist in the input list and to execute predefined functions on the input data.

# Input types
## Required
- ANY
    - The ANY parameter is a multifunctional input that accepts a list of any type of element. It is the basis for node operations, as it directly affects type counts and subsequent external functions. The diversity of elements in ANY influences the analysis of node and the results of function execution.
    - Comfy dtype: any
    - Python dtype: List[Any]

# Output types
- result
    - The result parameter contains the output of the type count operations performed by the ListStatistics tool. It is important because it provides a detailed description of the type of elements in the input list and their respective counts. This information is essential to understand the composition of the input data.
    - Comfy dtype: Dict[str, List[Any]]
    - Python dtype: Dict[str, List[Any]]
- ui
    - The ui parameter is a structured output, including data and type information. It is designed to make it easier to display the results of nodes in the user interface. Data fields contain the results of type counts, while type fields indicate the type of data in the first element of the list.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Union[Dict[str, List[Any]], str]]

# Usage tips
- Infra type: CPU

# Source code
```
class TESTNODE_:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ANY': (any_type,)}}
    RETURN_TYPES = (any_type,)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/__TEST'
    OUTPUT_NODE = True
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, ANY):
        list_stats = ListStatistics()
        result = list_stats.count_types(ANY)
        module_path = os.path.join(os.path.dirname(__file__), 'test.py')
        spec = importlib.util.spec_from_file_location('test', module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        functions = getattr(module, 'run')
        functions(ANY)
        return {'ui': {'data': result, 'type': [str(type(ANY[0]))]}, 'result': (ANY,)}
```