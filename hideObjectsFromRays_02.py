bl_info = {
    "name": "Show and hide",
    "author": "Fredrik Svärd",
    "version": (0,1),
    "blender": (3,1,2),
    "location": "View 3D > Tool",
    "warning": "", 
    "wiki_url":"",
    "category": "Show and hide", 
}


import bpy # Import Blender Python


class HideShowPanel(bpy.types.Panel):
    bl_idname = "HideShowPanelID"
    bl_label = "Test panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Show and Hide" # The category (tab) in which the panel will be displayed, when applicable
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text= "Hide - Camera ray visibility.", icon= "CUBE")
        
        row.operator ('HideCameraRays')
        row.operator ('ShowCameraRays')
        
       
       
class HideButton(bpy.types.Operator):
    bl_label = "Hide"
    bl_idname = 'HideCameraRays'
    
    # Everything inside execute will be executed when we push the button.
    def execute(self, context):
    
        for c in bpy.data.collections:
            for o in c.objects:
                if o.type == "MESH":
                    o.visible_camera = False
                
    return {'FINISHED'}



        
class ShowButton(bpy.types.Operator):
    bl_label = "Show"
    bl_idname = 'ShowCameraRays'
    
    # Everything inside execute will be executed when we push the button.
    def execute(self, context):
    
        for c in bpy.data.collections:
            for o in c.objects:
                if o.type == "MESH":
                    o.visible_camera = True
                
    return {'FINISHED'}
               
               
               
                    
        
def register():
    bpy.utils.register_class(HideShowPanel)
    bpy.utils.register_class(HideButton)
    bpy.utils.register_class(ShowButton)
        
def unregifter():
    bpy.utils.unregister_class(HideShowPanel)
    bpy.utils.unregister_class(HideButton)
    bpy.utils.unregister_class(ShowButton)
    
if __name__ == "__main__":
    register()   
        
        
        
        
        
        
        
        
        
        

