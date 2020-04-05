import bpy
import json

from . import create_mat

def read_base_color(context,filepath):

    b = filepath
    print(filepath)
    create_mat.base_color(context, filepath)

    return {'FINISHED'}


def read_specular(context,filepath):

    b = filepath
    print(filepath)
    create_mat.specular(context, filepath)

    return {'FINISHED'}

def read_metallic(context,filepath):

    b = filepath
    print(filepath)
    create_mat.metallic(context, filepath)

    return {'FINISHED'}

def read_roughness(context,filepath):

    b = filepath
    print(filepath)
    create_mat.roughness(context, filepath)

    return {'FINISHED'}
def read_displacement(context,filepath):

    b = filepath
    print(filepath)
    create_mat.displacement(context, filepath)

    return {'FINISHED'}

def read_normal(context,filepath):

    b = filepath
    print(filepath)
    create_mat.normal(context, filepath)

    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportBaseColor(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.base_color"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Base Color"


    def execute(self, context):
        return read_base_color(context,self.filepath)

class ImportSpecular(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.specular"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Speculat Map"


    def execute(self, context):
        return read_specular(context,self.filepath)

class ImportMetallic(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.metallic"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Metallic Map"


    def execute(self, context):
        return read_metallic(context,self.filepath)

class ImportRoughness(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.roughness"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Roughness Map"


    def execute(self, context):
        return read_roughness(context,self.filepath)

class ImportDisplacement(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.displacement"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Displacement Map"


    def execute(self, context):
        return read_displacement(context,self.filepath)

class ImportNormal(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.normal"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Normal Map"


    def execute(self, context):
        return read_normal(context,self.filepath)





def register():
    bpy.utils.register_class(ImportBaseColor)
    bpy.utils.register_class(ImportSpecular)
    bpy.utils.register_class(ImportMetallic)
    bpy.utils.register_class(ImportRoughness)
    bpy.utils.register_class(ImportDisplacement)
    bpy.utils.register_class(ImportNormal)




def unregister():
    bpy.utils.unregister_class(ImportBaseColor)
    bpy.utils.unregister_class(ImportSpecular)
    bpy.utils.unregister_class(ImportMetallic)
    bpy.utils.unregister_class(ImportRoughness)
    bpy.utils.unregister_class(ImportDisplacement)
    bpy.utils.unregister_class(ImportNormal)
