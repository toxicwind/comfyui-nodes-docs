# Documentation
- Class name: WAS_Samples_Passthrough_Stat_System
- Category: WAS Suite/Debug
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Samples_Passthrough_Stat_System is designed to provide a statistical overview of the current state of the system. It captures and records key system indicators, such as the use of RAM and VRAM, as well as the use of hard disk space. This method is essential for monitoring the health and performance of the system and provides insight into resource consumption without going into the details of the bottom-level data collection process.

# Input types
## Required
- samples
    - The “samples” parameter is essential for the implementation of the `stat_system'method, as it represents a potential spatial sample of system operations. It is through these samples that the resource utilization of the system is assessed, making this parameter an integral part of the node function.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Output types
- samples
    - The " samples" output parameter represents the original potential space sample passed through the system. It ensures the integrity of the data for further use or analysis as confirmation that the system has processed input and has not changed.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Samples_Passthrough_Stat_System:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'samples': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('samples',)
    FUNCTION = 'stat_system'
    CATEGORY = 'WAS Suite/Debug'

    def stat_system(self, samples):
        log = ''
        for stat in self.get_system_stats():
            log += stat + '\n'
        cstr('\n' + log).msg.print()
        return (samples,)

    def get_system_stats(self):
        import psutil
        ram = psutil.virtual_memory()
        ram_used = ram.used / 1024 ** 3
        ram_total = ram.total / 1024 ** 3
        ram_stats = f'Used RAM: {ram_used:.2f} GB / Total RAM: {ram_total:.2f} GB'
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        vram_used = torch.cuda.memory_allocated(device) / 1024 ** 3
        vram_total = torch.cuda.get_device_properties(device).total_memory / 1024 ** 3
        vram_stats = f'Used VRAM: {vram_used:.2f} GB / Total VRAM: {vram_total:.2f} GB'
        hard_drive = psutil.disk_usage('/')
        used_space = hard_drive.used / 1024 ** 3
        total_space = hard_drive.total / 1024 ** 3
        hard_drive_stats = f'Used Space: {used_space:.2f} GB / Total Space: {total_space:.2f} GB'
        return [ram_stats, vram_stats, hard_drive_stats]
```