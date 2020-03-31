import bpy

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Import Material"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Import Material!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        # Button for Import Base Map
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import Base Map")

        
        # Button for Import Specular Map

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import Specular Map")

        # Button for Import Metallic Map

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import Metallic Map")

        # Button for Import Roughness Map

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import Roughness Map")

        # Button for Import DIsplacement Map
        
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import DIsplacement Map")

        # Button for Import Normal Map

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Import Normal Map")

        
        row = layout.row()
        row = layout.row()
        row = layout.row()
        # Button for Create BSDF Material
        row = layout.row()
        row.scale_y = 3.0
        row.operator("mesh.primitive_cube_add", text="Create BSDF Material")

      


def register():
    bpy.utils.register_class(HelloWorldPanel)



def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


    


if __name__ == "__main__":
    register()
