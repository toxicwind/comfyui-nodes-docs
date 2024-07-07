# Documentation
- Class name: Vec4ScalarOperation
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

Vec4ScallarOperation provides a way to operate vector data through mathematical calculations. It is designed to be flexible and efficient, allowing for direct application in scenarios that require vector arithmetic.

# Input types
## Required
- op
    - The operating parameter defines the specific metric operation that you want to perform on the vector. It is vital because it determines the mathematical function applied to each fraction of the vector.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the four-dimensional vector on which the mark is calculated. It is essential because it is the main input for node operations to produce results.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]
- b
    - The mark 'b' is the floating point number that will be used with vector 'a' for operations defined by 'op'. It plays an important role in the calculation because it directly influences the outcome of vector changes.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - It contains the results of a metric calculation performed for the input vector 'a '. It contains the results of applying the specified mathematical function to each fraction of the vector.
    - Comfy dtype: VEC4
    - Python dtype: Tuple[float, float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4ScalarOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_SCALAR_OPERATION.keys()),), 'a': DEFAULT_VEC4, 'b': ('FLOAT',)}}
    RETURN_TYPES = ('VEC4',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4, b: float) -> tuple[Vec4]:
        return (_vec4_from_numpy(VEC_SCALAR_OPERATION[op](numpy.array(a), b)),)
```