from transformer_gen.src.utils.BVH_mod import Anim,read_bvh,save_bvh
import numpy as np
import os
def add_T_pose(anim:Anim):
    anim.quats = np.concatenate([np.zeros_like(anim.quats[0:1]),anim.quats],axis=0)
    anim.hip_pos = np.concatenate([np.zeros_like(anim.hip_pos[0:1]),anim.hip_pos],axis=0)
    return anim

def traverse_folder(path):
    path_dir = os.listdir(path)
    for file in path_dir:
        print(file)
        file_name = os.path.join(path, file)
        if(file.endswith(".bvh")):
            print(file_name)
            anim = read_bvh(file_name)
            anim = add_T_pose(anim)
            file_name = os.path.join(path,"T_"+file)
            save_bvh(file_name,anim)
        elif(os.path.isdir(file_name)):
            traverse_folder(file_name)
if __name__ == '__main__':
    traverse_folder("./examples/T/content_interpoolate/differentpaces2/")
