import bpy


#from . import import_file
#from import_file import *


def base_color(context, filepath):
    #actevemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)

    activemat = bpy.context.object.active_material # Select active material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, 600)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]
    activemat.node_tree.links.new(newbsdf.inputs['Base Color'], texImage.outputs['Color'])
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector'])
        

def specular(context, filepath):
    #activemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
    activemat = bpy.context.object.active_material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, 300)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]
    activemat.node_tree.links.new(newbsdf.inputs['Specular'], texImage.outputs['Color'])
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector'])

def metallic(context, filepath):
    #activemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
    activemat = bpy.context.object.active_material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, 0)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]
    activemat.node_tree.links.new(newbsdf.inputs['Metallic'], texImage.outputs['Color'])
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector'])

def roughness(context, filepath):
    #activemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
    activemat = bpy.context.object.active_material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, -300)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]
    activemat.node_tree.links.new(newbsdf.inputs['Roughness'], texImage.outputs['Color'])
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector'])

def displacement(context, filepath):
    #activemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
    activemat = bpy.context.object.active_material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, -600)
    Texbump = activemat.node_tree.nodes.new(type="ShaderNodeBump")
    Texbump.location = (-500,-500)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector'])
    activemat.node_tree.links.new(Texbump.inputs['Height'], texImage.outputs['Color'])
    activemat.node_tree.links.new(newbsdf.inputs['Normal'], Texbump.outputs['Normal'])

def normal(context, filepath):
    #activemat = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
    activemat = bpy.context.object.active_material
    nodes = activemat.node_tree.nodes #Get all material nodes
    map_node = nodes.get("Mapping") #get the mapping node
    bump_node = nodes.get("Bump")
    texImage = activemat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.location = (-1500, -900)
    texNormalMap = activemat.node_tree.nodes.new('ShaderNodeNormalMap')
    texNormalMap.location = (-800,-800)
    texImage.image = bpy.data.images.load(filepath)
    newbsdf = activemat.node_tree.nodes["Principled BSDF"]

    activemat.node_tree.links.new(bump_node.inputs['Normal'], texNormalMap.outputs['Normal']) #Connect Normal Map to Bump
    activemat.node_tree.links.new(texNormalMap.inputs['Color'], texImage.outputs['Color']) #Connect TextImage to Normal Map
    activemat.node_tree.links.new(texImage.inputs['Vector'], map_node.outputs['Vector']) #Connect Mapping to TextImage
    activemat.node_tree.links.new(newbsdf.inputs['Normal'], bump_node.outputs['Normal']) #Connect Bump to Material

    


def createmat(context):
    activeObject = bpy.context.active_object  #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName")    #set new material to variable
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    activeObject.data.materials.append(mat)   #add the material to the object
    Texcoo = mat.node_tree.nodes.new(type="ShaderNodeTexCoord")
    Texcoo.location = (-2000, 100)
    Texmap = mat.node_tree.nodes.new(type = "ShaderNodeMapping")
    Texmap.location = (-1800, 100)
    mat.node_tree.links.new(Texmap.inputs['Vector'], Texcoo.outputs['UV'])
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
