import bpy


#from . import import_file
#from import_file import *


def createmat(context):
    activeObject = bpy.context.active_object  #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName")    #set new material to variable
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    activeObject.data.materials.append(mat)   #add the material to the object
    mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.5, 0.5, 0.5, 1)

    return mat


class CreateBSDF(bpy.types.Operator):#create material
    """Tooltip"""
    bl_idname = "object.createbsdf"
    bl_label = "Create Principled BSDF"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        createmat(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(CreateBSDF)


def unregister():
    bpy.utils.unregister_class(CreateBSDF)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.simple_operator()
