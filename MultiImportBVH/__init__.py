bl_info = {
    "name": "Add BVH",
    "author": "Xiangjun Tang",
    "version": (2, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Add > BVH",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Add BVH",
}

import bpy
import logging
from . import import_bvh


def register():
    import_bvh.register()


def unregister():
    import_bvh.unregister()

if __name__ == "__main__":
    register()