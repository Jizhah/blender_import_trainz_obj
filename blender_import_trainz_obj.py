bl_info = {
    "name": "Import OBJ from Trainz",
    "blender": (4, 1, 0),  # Minimum Blender version
    "category": "Import-Export",
    "author": "Your Name",
    "version": (1, 0, 0),
    "description": "Imports Trainz OBJ files, rotates them, adjusts UVs, and adds attachment nodes.",
}

import bpy
import os
import math
import re

# Function to import .obj file
def import_obj(filepath):
    bpy.ops.wm.obj_import(filepath=filepath)  # Updated import method for Blender 4.x

# Function to rotate object by -90 degrees on the X-axis
def rotate_object_on_x_axis(obj):
    obj.rotation_euler[0] = math.radians(-90)  # -90 degrees in radians

# Function to rotate and mirror UV map
def rotate_and_mirror_uv(obj):
    # Ensure that the object has a UV map
    if obj.data.uv_layers:
        uv_layer = obj.data.uv_layers.active.data
        for uv in uv_layer:
            # Mirror the UV on the X-axis (flip the x-coordinate)
            uv.vector.x = uv.vector.x * -1
            # Rotate the Y-coordinate by 180 degrees (flip along the Y axis)
            uv.vector.y = uv.vector.y + 1
            if uv.vector.y > 1:
                uv.vector.y -= 2  # Keep the UV coordinates within 0-1 range

# Function to process the .ms (MaxScript) file
def process_ms_file(ms_filepath):
    attachment_nodes = []
    
    with open(ms_filepath, 'r') as ms_file:
        ms_content = ms_file.read()

    # Example: Simple regex to find attachment nodes in the MS file
    # You should adapt this to the structure of your MaxScript file
    attachment_pattern = re.compile(r'attach\s*(\w+)\s*=\s*([\d.]+),([\d.]+),([\d.]+)')
    matches = attachment_pattern.findall(ms_content)
    
    for match in matches:
        node_name = match[0]
        position = (float(match[1]), float(match[2]), float(match[3]))
        attachment_nodes.append((node_name, position))
    
    return attachment_nodes

# Function to create attachment nodes in Blender
def create_attachment_nodes(attachment_nodes):
    for node_name, position in attachment_nodes:
        # Create a new empty object at the specified position
        bpy.ops.object.empty_add(location=position)
        new_empty = bpy.context.object
        new_empty.name = node_name

# Main import function
def import_and_process_obj(obj_filepath, ms_filepath):
    # Import the OBJ file
    import_obj(obj_filepath)

    # Get the imported object
    imported_obj = bpy.context.selected_objects[0]

    # Rotate the object
    rotate_object_on_x_axis(imported_obj)

    # Rotate and mirror UV
    rotate_and_mirror_uv(imported_obj)

    # Process the MaxScript file and create attachment nodes
    attachment_nodes = process_ms_file(ms_filepath)
    create_attachment_nodes(attachment_nodes)

class ImportOBJFromTrainzOperator(bpy.types.Operator):
    bl_idname = "import_scene.obj_from_trainz"
    bl_label = "Import OBJ from Trainz"
    
    # Filepath property for OBJ file (hidden in file dialog)
    obj_filepath: bpy.props.StringProperty(name="OBJ File", subtype='NONE')
    
    # Filepath property for MS file (hidden in file dialog)
    ms_filepath: bpy.props.StringProperty(name="MS File", subtype='NONE')

    # Define the invoke function to open file dialog
    def invoke(self, context, event):
        # Open file dialog for the OBJ file, filter to show only .obj files
        self.filter_glob = "*.obj"
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    # After file selection, set the paths correctly
    def execute(self, context):
        # Check that the obj_filepath was selected
        if not self.obj_filepath:
            self.report({'ERROR'}, "No OBJ file selected")
            return {'CANCELLED'}

        # Extract the directory of the OBJ file
        obj_dir = os.path.dirname(self.obj_filepath)

        # Construct the path for the corresponding .ms file
        ms_filepath = os.path.join(obj_dir, os.path.basename(self.obj_filepath).replace('.obj', '.im.attachment.ms'))

        # Check if the corresponding .ms file exists
        if not os.path.isfile(ms_filepath):
            self.report({'ERROR'}, f"Attachment file not found: {ms_filepath}")
            return {'CANCELLED'}

        # Call the main function to process the OBJ and MS files
        try:
            import_and_process_obj(self.obj_filepath, ms_filepath)
        except Exception as e:
            self.report({'ERROR'}, f"An error occurred while processing files: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}

# Add operator to the Import menu
def menu_func_import(self, context):
    self.layout.operator(ImportOBJFromTrainzOperator.bl_idname)

# Register the addon
def register():
    bpy.utils.register_class(ImportOBJFromTrainzOperator)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportOBJFromTrainzOperator)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
