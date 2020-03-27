import bpy
import json

from . import create_mat

def test_import_file(context,filepath):

    b = filepath
    
    print(filepath)

    return {'FINISHED'}

# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportTestFile(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_test.importfile"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Base Color"


    def execute(self, context):
        return test_import_file(context,self.filepath)

def register():
    bpy.utils.register_class(ImportTestFile)

def unregister():
    bpy.utils.unregister_class(ImportTestFile)
