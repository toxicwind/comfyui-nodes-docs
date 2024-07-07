# Documentation
- Class name: AppInfo
- Category: ♾️Mixlab
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

AppInfo is a node for managing and organizing information on applications, which facilitates the installation and operation of applications in the system. It streamlines the input and output of application details to ensure the efficient processing of application data. The node is conceptually focused on providing structured application information management methods, rather than tied to specific realization details.

# Input types
## Required
- name
    - Name parameters are essential for identifying the application in the system. As a unique identifier, they help to organize and retrieve the application-related data. Names affect the application's references and management in the system.
    - Comfy dtype: STRING
    - Python dtype: str
- input_ids
    - The input IDs play a key role in tracking the components or modules of the application. They are critical to systematically analysing and managing the structure of the application, ensuring that each part is recorded and can be accessed as required.
    - Comfy dtype: STRING
    - Python dtype: str
- output_ids
    - The output ID is essential to map the results and outcomes of the application. They define the structure and format of the output data so that the output of the application can be effectively monitored and used. The proper management of the output ID is essential for the successful operation of the application and integration with other system components.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- IMAGE
    - Images provide the visual performance of the application and enhance understanding and communication. They can be used to display interfaces, icons or other visual elements of the application, which are important for user interaction and branding. The inclusion of images can significantly improve user experience and perception of the application.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- description
    - Description parameters are essential to provide information about the context and context of the application. They help convey the purpose, characteristics and context of the application, and are beneficial to both users and developers. A clear and concise description can greatly assist in the development and dissemination of the application's documents.
    - Comfy dtype: STRING
    - Python dtype: str
- version
    - Version parameters are essential for tracking the development and updating of the application. They help to record changes and improvements and thus better manage the development cycle of the application. Version numbers are the key reference points for users and developers when solving problems or planning new features.
    - Comfy dtype: INT
    - Python dtype: int
- share_prefix
    - The sharing prefix is important to define how the data and resources of the application are shared and accessed. It provides the basis for data exchange and collaboration within the system and ensures that the application sharing mechanisms are consistent with the overall system architecture.
    - Comfy dtype: STRING
    - Python dtype: str
- link
    - Link parameters are important to guide users to the application-related additional resources or content. They provide access to documents, support or supplementary material, which is valuable for enhancing user understanding of and participation in the application.
    - Comfy dtype: STRING
    - Python dtype: str
- category
    - Category parameters help to categorize applications into specific fields or types, which are very useful for organizing and navigation. They help to group similar applications together, making it easier for users to find and select applications suitable for their needs.
    - Comfy dtype: STRING
    - Python dtype: str
- auto_save
    - Autosave parameters are important for determining the data durability and recovery behaviour of the application. It determines whether the status of the application should be automatically saved at fixed time intervals to ensure that users can resume their work in case of interruption or system failure.
    - Comfy dtype: COMBO['enable', 'disable']
    - Python dtype: str

# Output types
- ui.json
    - ui.json output is a structured expression of application information, including its name, image and various IDs. It is a comprehensive summary that can be used for further processing or displaying of the system. This output is important for integrating application data with other components and providing a clear overview of application status.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class AppInfo:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'name': ('STRING', {'multiline': False, 'default': 'Mixlab-App', 'dynamicPrompts': False}), 'input_ids': ('STRING', {'multiline': True, 'default': '\n'.join(['1', '2', '3']), 'dynamicPrompts': False}), 'output_ids': ('STRING', {'multiline': True, 'default': '\n'.join(['5', '9']), 'dynamicPrompts': False})}, 'optional': {'IMAGE': ('IMAGE',), 'description': ('STRING', {'multiline': True, 'default': '', 'dynamicPrompts': False}), 'version': ('INT', {'default': 1, 'min': 1, 'max': 10000, 'step': 1, 'display': 'number'}), 'share_prefix': ('STRING', {'multiline': False, 'default': '', 'dynamicPrompts': False}), 'link': ('STRING', {'multiline': False, 'default': 'https://', 'dynamicPrompts': False}), 'category': ('STRING', {'multiline': False, 'default': '', 'dynamicPrompts': False}), 'auto_save': (['enable', 'disable'],)}}
    RETURN_TYPES = ()
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab'
    OUTPUT_NODE = True
    INPUT_IS_LIST = True

    def run(self, name, input_ids, output_ids, IMAGE, description, version, share_prefix, link, category, auto_save):
        name = name[0]
        im = None
        if IMAGE:
            im = IMAGE[0][0]
            im = create_temp_file(im)
        input_ids = input_ids[0]
        output_ids = output_ids[0]
        description = description[0]
        version = version[0]
        share_prefix = share_prefix[0]
        link = link[0]
        category = category[0]
        return {'ui': {'json': [name, im, input_ids, output_ids, description, version, share_prefix, link, category]}, 'result': ()}
```