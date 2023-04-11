bl_info = {
    "name": "Custom Origin Macro",
    "author": "Maik Arnold",
    "category": "Object",
    "blender": (2, 91, 0),
    "version": (1, 2, 2),
    "support": "TESTING",
    "location": "Object > Set Origin > Origin to lower left corner",
    "warning": "",
    "wiki_url": "",
}

import bpy, bpy.ops, bpy.props, bpy.types, bpy.utils, bgl, blf, mathutils, math
from mathutils import *
"""from ..op.copy_paste_uv_object import (
    MUV_MT_CopyPasteUVObject_CopyUV,
    MUV_MT_CopyPasteUVObject_PasteUV,
)"""
import sys

# Give the UI Icons
class VIEW3D_PT_giveAllUv(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'
    bl_label = 'UV'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        sc = context.scene
        layout = self.layout
        row = layout.row(align=True)

        self.layout.operator("object.adduv", text='Normal UV geben', icon='DOCUMENTS')
        self.layout.operator("object.clearuv", text='Überflüssige UV löschen', icon='DOCUMENTS')
        self.layout.operator("object.removeuv", text='Zusätzliche Normal UV  enternen', icon='DOCUMENTS')
        
        self.layout.operator("object.dupenormal", text='Master normal duplizieren', icon='DOCUMENTS')

        
#Clear the UVMap
class ClearUV(bpy.types.Operator):
    """UV für Export entfernen"""
    bl_idname = "object.clearuv"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
        # Make sure this is a mesh object and that it doesn't already use this UV Map
            if obj.type == 'MESH' and "UVMap" in obj.data.uv_layers:
                uvlayer = obj.data.uv_layers[1:]
                if uvlayer != 0:
                    while uvlayer[0:] != 'UVMap':
                            obj.data.uv_layers.remove(uvlayer[0])
                else:
                    print ("Nichts zu löschen")
                    
        return {'FINISHED'}
 
                    
    
        return {'FINISHED'}

#Remove unnecessary UVMaps
class RemoveUV(bpy.types.Operator):
    """UV für Export entfernen"""
    bl_idname = "object.removeuv"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
        # Make sure this is a mesh object and that it doesn't already use this UV Map
            if obj.type == 'MESH' and "UV_normal" in obj.data.uv_layers:
                print ("Zusätzliche Normal UV entfernt")
                obj.data.uv_layers.remove(obj.data.uv_layers['UV_normal'])
                
    
        return {'FINISHED'}

#Give UVMap with appropriate syntax
class GiveUV(bpy.types.Operator):
    """UV für Export hinzufuegen"""
    bl_idname = "object.adduv"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
    # Make sure this is a mesh object and that it doesn't already use this UV Map
            if obj.type == 'MESH' and "UV_ao" not in obj.data.uv_layers:
                obj.data.uv_layers.new(name="UV_normal")
                
        return {'FINISHED'} 
       
class DupeNormal(bpy.types.Operator):
    """Normal UV von Master auf Auswahl übertragen"""
    bl_idname = "object.dupenormal"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        return {'FINISHED'} 

class VIEW3D_PT_customTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'
    bl_label = 'Origin Setter'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    def draw(self, context):
        sc = context.scene
        layout = self.layout
        row = layout.row(align=True)
        
        
        self.layout.operator('object.fllcorner', 
        text='Vorne Unten Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.fulcorner', 
        text='Vorne Oben Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.bulcorner', 
        text='Hinten Oben Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.bllcorner', 
        text='Hinten Unten Links (main)', icon='OBJECT_ORIGIN')

        self.layout.operator('object.flrcorner', 
        text='Vorne Unten Rechts', icon='OBJECT_ORIGIN')

        self.layout.operator('object.furcorner', 
        text='Vorne Oben Rechts', icon='OBJECT_ORIGIN')

        self.layout.operator('object.burcorner', 
        text='Hinten Oben Rechts', icon='OBJECT_ORIGIN')

        self.layout.operator('object.blrcorner', 
        text='Hinten Unten Rechts', icon='OBJECT_ORIGIN')

   
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class FLLCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.fllcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die vordere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[0]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class FULCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.fulcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die vordere obere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[1]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class BULCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.bulcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere obere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[2]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class BLLCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.bllcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die vordere untere rechte Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[3]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}
    
class FLRCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.flrcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die vordere obere rechte Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[4]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class FURCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.furcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[5]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}
    
class BURCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.burcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere obere rechte Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[6]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}
    
class BLRCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.blrcorner"
    bl_label = "Custom Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, properties=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere rechte Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[7]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}


    
addon_keymaps = []

def register():
    bpy.utils.register_class(ClearUV)
    bpy.utils.register_class(RemoveUV)
    bpy.utils.register_class(GiveUV)
    bpy.utils.register_class(DupeNormal)
    bpy.utils.register_class(VIEW3D_PT_giveAllUv)
    bpy.utils.register_class(VIEW3D_PT_customTools)
    bpy.utils.register_class(FLLCorner)    
    bpy.utils.register_class(FULCorner)
    bpy.utils.register_class(BULCorner)
    bpy.utils.register_class(BLLCorner)
    bpy.utils.register_class(FLRCorner)
    bpy.utils.register_class(FURCorner)
    bpy.utils.register_class(BURCorner)
    bpy.utils.register_class(BLRCorner)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(BLLCorner.bl_idname, 'F5', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(ClearUV)
    bpy.utils.unregister_class(GiveUV)
    bpy.utils.unregister_class(RemoveUV)
    bpy.utils.unregister_class(DupeNormal)
    bpy.utils.unregister_class(VIEW3D_PT_giveAllUv)
    bpy.utils.unregister_class(VIEW3D_PT_customTools)
    bpy.utils.unregister_class(FLLCorner)    
    bpy.utils.unregister_class(FULCorner)
    bpy.utils.unregister_class(BULCorner)
    bpy.utils.unregister_class(BLLCorner)
    bpy.utils.unregister_class(FLRCorner)
    bpy.utils.unregister_class(FURCorner)
    bpy.utils.unregister_class(BURCorner)
    bpy.utils.unregister_class(BLRCorner)

    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
