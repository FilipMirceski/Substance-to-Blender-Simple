import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

from . import import_file

import json


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Import Material"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    def draw(self, context):
        layout = self.layout



        row = layout.row()
        row.operator("import_test.importfile", text="Import file test")

        row = layout.row()
        row.operator("object.createbsdf")


      

def register():
    bpy.utils.register_class(HelloWorldPanel)



def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


    


if __name__ == "__main__":
    register()
