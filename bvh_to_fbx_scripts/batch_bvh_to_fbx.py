import os
import subprocess
def traverse_folder(path):
    path_dir = os.listdir(path)
    for file in path_dir:
        print(file)
        file_name = os.path.join(path, file)
        if(file.endswith(".bvh")):
            print(file_name)
            command = '"C:/Program Files/Blender Foundation/Blender 2.83/blender.exe" -b --python "./bvh_to_fbx.py" -- '+'{}'.format(file_name)
            print(command)
            ps = subprocess.Popen(command)
            ps.wait()
        elif(os.path.isdir(file_name)):
            traverse_folder(file_name)
if __name__ == "__main__":
    #command = '"C:/Program Files/Blender Foundation/Blender 2.83/blender.exe" -b --python "./bvh_to_fbx.py" -- "E:/Projects/IBMTransfer_DEMO/Demo_animation/AAandBAonA/last_version/T_HighKnees_70_7_t=1_AA.bvh"'
    #command = str(r'"C:/Progra~1/Blende~1/Blender 2.83/blender.exe"' +' -b'+' --python' +' ./bvh_to_fbx.py' + ' -- "E:/Projects/IBMTransfer_DEMO/Demo_animation/AAandBAonA/last_version/T_HighKnees_70_7_t=1_AA.bvh"')
    #print(command)
    #ps = subprocess.Popen(command)
    #ps.wait()
    #os.system(command)
    traverse_folder("E:\\Projects\\2023MotionTransfer\\examples\\T\\content_interpoolate\\differentpaces2\\")