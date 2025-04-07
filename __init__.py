bl_info = {
    "name": "Import OBJ from Trainz",
    "blender": (4, 1, 0),  # Minimum Blender version
    "category": "Import-Export",
    "author": "ChatGPT",
    "version": (1, 0, 0),
    "description": "Imports Trainz OBJ files, rotates them, adjusts UVs, and adds attachment nodes.",
}

import bpy
from . import operator

def register():
    operator.register()

def unregister():
    operator.unregister()