# Documentation
- Class name: Vec2ScalarOperation
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

Vec2ScallarOperation node is designed to perform various mathematical calculations between two-dimensional vectors (Vec2) and metrics (float). It encapsulates the functions of applying various vector-scale operations that are essential in calculating geometry and linear algebras. This node plays a key role in the manipulation of vector data in the mathematical context.

# Input types
## Required
- op
    - The ‘op’ parameter specifies the type of mathematical operation that you want to perform between vectors and metrics. It is essential to determine the computational nature of the node that will be executed. The choice of calculation directly affects the result of the vector-scale interaction.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The `a' parameter indicates the two-dimensional vector to be used in the calculation (Vec2), which, as a basic input, is essential to the mathematical process and directly contributes to the final result of the calculation. The fraction of the vector will be operated according to the specified calculation.
    - Comfy dtype: Vec2
    - Python dtype: Tuple[float, float]
- b
    - The `b' parameter is the metric value that will be used to calculate together with the vector `a'. Its significance is that it serves as a multiplier or operator in the vector-mark calculation and influences the final result of the calculation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The `result' output is a conversion of two-dimensional vectors (Vec2), after the specified calculation has been applied, which represents the final result of vector-scale calculations and directly reflects input parameters and selected calculations.
    - Comfy dtype: VEC2
    - Python dtype: Tuple[float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2ScalarOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_SCALAR_OPERATION.keys()),), 'a': DEFAULT_VEC2, 'b': ('FLOAT',)}}
    RETURN_TYPES = ('VEC2',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2, b: float) -> tuple[Vec2]:
        return (_vec2_from_numpy(VEC_SCALAR_OPERATION[op](numpy.array(a), b)),)
```