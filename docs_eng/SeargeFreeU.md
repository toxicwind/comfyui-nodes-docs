# Documentation
- Class name: SeargeFreeU
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node helps to configure and manage the parameters of a system that is designed to operate in a search-free environment, and provides a simplified way to define operating patterns and settings.

# Input types
## Required
- freeu_mode
    - Determining the mode of operation of the system is essential for adjusting the behaviour and performance of the system to specific requirements.
    - Comfy dtype: COMBO[FREEU_MODES]
    - Python dtype: Enum
- b1
    - The initial setting of impact parameters is essential for establishing the basic conditions for the operation of the system.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2
    - A secondary setting that affects working with the main settings to refine the operating parameters of the system.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s1
    - Modify the parameters of the control system's sensitivity, adjust its response to input data and ensure optimal interaction.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s2
    - Adjust another parameter to fine-tune the operation of the system and focus on improving its adaptability and accuracy.
    - Comfy dtype: FLOAT
    - Python dtype: float
- freeu_version
    - Specifying the version of the system in use is important to ensure compatibility and functional availability.
    - Comfy dtype: FREEU_VERSION
    - Python dtype: Enum

# Output types
- data
    - Contains structured configuration data for setting and guiding system operations.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeFreeU:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'freeu_mode': (UI.FREEU_MODES,), 'b1': ('FLOAT', {'default': 1.3, 'min': 1.0, 'max': 1.4, 'step': 0.01}), 'b2': ('FLOAT', {'default': 1.4, 'min': 1.2, 'max': 1.6, 'step': 0.01}), 's1': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 's2': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'freeu_version': (UI.FREEU_VERSION,)}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(freeu_mode, b1, b2, s1, s2, freeu_version):
        return {UI.F_FREEU_MODE: freeu_mode, UI.F_FREEU_B1: b1, UI.F_FREEU_B2: b2, UI.F_FREEU_S1: s1, UI.F_FREEU_S2: s2, UI.F_FREEU_VERSION: freeu_version}

    def get(self, freeu_mode, b1, b2, s1, s2, freeu_version, data=None):
        if data is None:
            data = {}
        data[UI.S_FREEU] = self.create_dict(freeu_mode, b1, b2, s1, s2, freeu_version)
        return (data,)
```