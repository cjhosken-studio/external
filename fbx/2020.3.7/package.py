name = "fbx"

version = "2020.3.7"

authors = [
    "Kaydara",
    "Autodesk"
]

description = \
    """
    FBX, short for Filmbox, is a proprietary file format developed by Kaydara (now owned by Autodesk). 
    It's widely used for exchanging 3D models and animations between different software applications, particularly in the fields of 3D animation, game development, and visual effects. 
    """

tools = []

variants = []

requires = []

def commands():
    import platform
    import os

    env.LD_LIBRARY_PATH.append("{root}/lib/release")

    if building:
        env.FBX_ROOT.set("{root}")
        env.FBX_INCLUDE_DIR.set("{root}/include")
        env.FBX_LIBRARY_DIR.set("{root}/lib/release")

build_command = "{root}/build.sh"