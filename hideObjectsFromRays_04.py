bl_info = {
    "name": "Show and hide",
    "author": "Fredrik Svärd",
    "version": (0,3),
    "blender": (3,1,2),
    "location": "View 3D > Tool",
    "warning": "",
    "wiki_url":"",
    "category": "Custom tools",
}


import bpy
from bpy.types import (Panel, Operator)

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class HideOperator(Operator):
    bl_idname = "object.hide_operator"
    bl_label = "Hide Object Operator"

    def execute(self, context):
        for c in bpy.data.collection:
            for o in c.objects:
                if o.type == "MESH":
                    o.visible_camera = False
        return {'FINISHED'}


class ShowOperator(Operator):
    bl_idname = "object.show_operator"
    bl_label = "Show Object Operator"

    def execute(self, context):
        for c in bpy.data.collection:
            for o in c.objects:
                if o.type == "MESH":
                    o.visible_camera = True
        return {'FINISHED'}



# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class OBJECT_PT_CustomPanel(Panel):
    bl_idname = "object.custom_panel"
    bl_label = "NJORD"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Show / Hide"
    bl_context = "objectmode"


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.object

#        layout.label(text="Properties:")

#        col = layout.column(align=True)
#        row = col.row(align=True)
#        row.prop(obj, "show_name", toggle=True, icon="FILE_FONT")
#        row.prop(obj, "show_wire", toggle=True, text="Wireframe", icon="SHADING_WIRE")
#        col.prop(obj, "show_all_edges", toggle=True, text="Show all Edges", icon="MOD_EDGESPLIT")

#        layout.separator()

        layout.label(text="Show/Hide, Camera Rays.")

        col = layout.column(align=True)
        col.operator(HideOperator.bl_idname, text="Hide", icon="CONSOLE")
        col.operator(ShowOperator.bl_idname, text="Show", icon="CONSOLE")

        layout.separator()

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

def register():
    bpy.utils.register_class(OBJECT_PT_CustomPanel)
    bpy.utils.register_class(HideOperator)
    bpy.utils.register_class(ShowOperator)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_CustomPanel)
    bpy.utils.unregister_class(HideOperator)
    bpy.utils.unregister_class(ShowOperator)

if __name__ == "__main__":
    register()




