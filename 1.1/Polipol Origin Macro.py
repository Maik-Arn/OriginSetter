bl_info = {
    "name": "Polipol Origin Macro",
    "author": "Maik Arnold",
    "category": "Object",
    "blender": (2, 91, 0),
    "version": (1, 0),
    "support": "TESTING",
    "location": "Object > Set Origin > Origin to lower left corner",
    "warning": "",
    "wiki_url": "",
}

import bpy, bpy.ops, bpy.props, bpy.types, bpy.utils, bgl, blf, mathutils, math
from mathutils import *
import sys


class VIEW3D_PT_polipolTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Polipol'
    bl_label = 'Origin Setter'
    
    
    def draw(self, context):
        sc = context.scene
        layout = self.layout
        row = layout.row(align=False)
        
        
        self.layout.operator('object.fllcorner', 
        text='Vorne Unten Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.fulcorner', 
        text='Vorne Oben Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.bulcorner', 
        text='Hinten Oben Links', icon='OBJECT_ORIGIN')

        self.layout.operator('object.bllcorner', 
        text='Hinten Unten Links', icon='OBJECT_ORIGIN')

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
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
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
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[1]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class BULCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.bulcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[2]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class BLLCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.bllcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[3]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}
    
class FLRCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.flrcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[4]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}

class FURCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.furcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
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
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[6]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}
    
class BLRCorner(bpy.types.Operator):
    """Origin für Export setzen"""
    bl_idname = "object.blrcorner"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #aktuelles Object designiert    
        obj = bpy.context.object
        bpy.ops.object.transforms_to_deltas(mode='ALL', reset_values=True)
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #Auswahl der Ecke
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[7]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
    
        return {'FINISHED'}


    
addon_keymaps = []

def register():
    bpy.utils.register_class(VIEW3D_PT_polipolTools)
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
    bpy.utils.unregister_class(VIEW3D_PT_polipolTools)    
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




"""
bbox_lower_middle_corner_01 = bbox_corners[3]


bbox_lower_middle_corner_02 = bbox_corners[7]

bbox_lower_middle = bbox_lower_middle_corner_01 / bbox_lower_middle_corner_02


bpy.context.scene.cursor.location = bbox_lower_middle



  
#Um mehrere Objekte zu ändern müssen diese in einen Array gesetzt werden und daraus sortiert

"""



"""
# store keymaps here to access after registration




"""