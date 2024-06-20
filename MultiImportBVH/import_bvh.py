import os 
try:
    import bpy 
except:
    print('Please run this file in blender.')




def batch_import_bvh(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.bvh'):
                filepath = os.path.join(root, file)
                print(filepath)
                bpy.ops.import_anim.bvh(filepath=filepath)

class ImportBVH(bpy.types.Operator):
    bl_idname = "batch.bvh"
    bl_label = "Import BVHs"
    #bl_category = "ImportBVH"
    files: bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    # new property for up-axis
    axis_up: bpy.props.EnumProperty(
        name="Up Axis",
        description="Select the up axis orientation",
        items=[        ("X", "X", "", 1),        ("Y", "Y", "", 2),        ("Z", "Z", "", 3)],
        default="Z"
        )
    def execute(self, context):
        # print(self.files)
        # for fi in self.files:
        #     print(fi)
        filepath = os.path.dirname(self.filepath)
        files = [f.name for f in self.files]
        for file in files:
            bpy.ops.import_anim.bvh(filepath = os.path.join(filepath,file),axis_up=self.axis_up)
        # batch_import_bvh(files)
        return {'FINISHED'}
 
    def invoke(self, context, event):


        # Add an option for up axis to the file selector window
        context.window_manager.fileselect_add(self)
        # context.window_manager.invoke_props_dialog(self)
       # return wm.invoke_props_dialog(self,width=400)
        return {'RUNNING_MODAL'}

class ImportBVHFolderRecursive(bpy.types.Operator):
    bl_idname = "batch.bvhrecur"
    bl_label = "Import BVHs recursive"
    #bl_category = "ImportBVH"
    files: bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        filepath = os.path.dirname(self.filepath)
        batch_import_bvh(filepath)
        # batch_import_bvh(files)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class BatchImportBVHMenu(bpy.types.Menu):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'HelloAddon'
 #   bl_idname = 'hello_world'
  #  bl_label = 'HelloWorld'
    bl_idname = "OBJECT_MT_batch_import_bvh"
    bl_label = "Batch Import BVH"

    def draw(self, context):
        self.layout.operator(ImportBVH.bl_idname,text="batch import")
        self.layout.operator(ImportBVHFolderRecursive.bl_idname,text="batch import recursive")
def register():
        bpy.utils.register_class(BatchImportBVHMenu)
        bpy.utils.register_class(ImportBVH)
        bpy.utils.register_class(ImportBVHFolderRecursive)
    #    bpy.types.TOPBAR_HT_upper_bar.append(menu_func_import)
        bpy.types.TOPBAR_HT_upper_bar.append(draw_menu)

def unregister():
        bpy.utils.unregister_class(ImportBVH)
        bpy.utils.unregister_class(BatchImportBVHMenu)
        bpy.utils.unregister_class(ImportBVHFolderRecursive)
   #     bpy.types.TOPBAR_HT_upper_bar.remove(menu_func_import)
        bpy.types.TOPBAR_HT_upper_bar.remove(draw_menu)
def draw_menu(self, context):
        layout = self.layout
        layout.menu(BatchImportBVHMenu.bl_idname, icon='PLUGIN')


def menu_func_import(self, context):
        self.layout.operator_context = 'INVOKE_DEFAULT'
        self.layout.operator(ImportBVH.bl_idname, text="Batch Import BVH")