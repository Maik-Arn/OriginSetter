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

class SetOriginToLeftCorner(bpy.types.Operator):
    bl_idname = "object.polipol_origin"
    bl_label = "Polipol Origin Macro"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        #aktuelles Object designiert    
        obj = bpy.context.object
        
        #Bounding Box Coordinaten beziehen und auf Welt projezieren
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        #3D Cursor auf die hintere untere linke Ecke setzen
        bpy.context.scene.cursor.location = bbox_corners[3]
        
        #Origin auf den 3D Cursor setzen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        return {'FINISHED'}
    
    
    
    
addon_keymaps = []

def register():
    bpy.utils.register_class(SetOriginToLeftCorner)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(SetOriginToLeftCorner.bl_idname, 'F5', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(SetOriginToLeftCorner)

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