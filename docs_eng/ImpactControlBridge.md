# Documentation
- Class name: ImpactControlBridge
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactControl Bridge node is designed to manage the operational state of the middle flow node. It ensures that the node is active, silent or by-passing in accordance with the conditions and behaviour provided, thereby controlling the data in the system and the processes implemented.

# Input types
## Required
- value
    - The `value' parameter is essential to the decision-making process of the node, as it determines the initial state that affects follow-up operations in the workflow.
    - Comfy dtype: any_typ
    - Python dtype: Any
- mode
    - The'mode' parameter indicates whether the node should enforce some operational state in the workflow, affecting the execution path.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- behavior
    - The 'behavior' parameter allows for the application of a conditionality logic within the node to modify its response according to the specific conditions met.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- unique_id
    - The 'unique_id' parameter is used to identify specific nodes in the workflow, achieve target control and operation.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- prompt
    - The 'prompt' parameter provides contextual information, which may be necessary for nodes to make informed decisions in the workflow.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The 'extra_pnginfo' parameter contains additional data that may be required for nodes to perform their operations effectively.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- value
    - The 'value' output reflects the final state of node processing and includes the results of node operations.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactControlBridge:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': (any_typ,), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'Active', 'label_off': 'Mute/Bypass'}), 'behavior': ('BOOLEAN', {'default': True, 'label_on': 'Mute', 'label_off': 'Bypass'})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('value',)
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(self, value, mode, behavior=True, unique_id=None, prompt=None, extra_pnginfo=None):
        (nodes, links) = workflow_to_map(extra_pnginfo['workflow'])
        next_nodes = []
        for link in nodes[unique_id]['outputs'][0]['links']:
            node_id = str(links[link][2])
            impact.utils.collect_non_reroute_nodes(nodes, links, next_nodes, node_id)
        return next_nodes

    def doit(self, value, mode, behavior=True, unique_id=None, prompt=None, extra_pnginfo=None):
        global error_skip_flag
        (nodes, links) = workflow_to_map(extra_pnginfo['workflow'])
        active_nodes = []
        mute_nodes = []
        bypass_nodes = []
        for link in nodes[unique_id]['outputs'][0]['links']:
            node_id = str(links[link][2])
            next_nodes = []
            impact.utils.collect_non_reroute_nodes(nodes, links, next_nodes, node_id)
            for next_node_id in next_nodes:
                node_mode = nodes[next_node_id]['mode']
                if node_mode == 0:
                    active_nodes.append(next_node_id)
                elif node_mode == 2:
                    mute_nodes.append(next_node_id)
                elif node_mode == 4:
                    bypass_nodes.append(next_node_id)
        if mode:
            should_be_active_nodes = mute_nodes + bypass_nodes
            if len(should_be_active_nodes) > 0:
                PromptServer.instance.send_sync('impact-bridge-continue', {'node_id': unique_id, 'actives': list(should_be_active_nodes)})
                error_skip_flag = True
                raise Exception('IMPACT-PACK-SIGNAL: STOP CONTROL BRIDGE\nIf you see this message, your ComfyUI-Manager is outdated. Please update it.')
        elif behavior:
            should_be_mute_nodes = active_nodes + bypass_nodes
            if len(should_be_mute_nodes) > 0:
                PromptServer.instance.send_sync('impact-bridge-continue', {'node_id': unique_id, 'mutes': list(should_be_mute_nodes)})
                error_skip_flag = True
                raise Exception('IMPACT-PACK-SIGNAL: STOP CONTROL BRIDGE\nIf you see this message, your ComfyUI-Manager is outdated. Please update it.')
        else:
            should_be_bypass_nodes = active_nodes + mute_nodes
            if len(should_be_bypass_nodes) > 0:
                PromptServer.instance.send_sync('impact-bridge-continue', {'node_id': unique_id, 'bypasses': list(should_be_bypass_nodes)})
                error_skip_flag = True
                raise Exception('IMPACT-PACK-SIGNAL: STOP CONTROL BRIDGE\nIf you see this message, your ComfyUI-Manager is outdated. Please update it.')
        return (value,)
```