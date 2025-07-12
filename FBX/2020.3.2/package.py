name = "fbx"

version = "2020.3.2"

authors = [
    "Kaydara",
    "Autodesk"
]

description = \
    """
    FBX, short for Filmbox, is a proprietary file format developed by Kaydara (now owned by Autodesk). 
    It's widely used for exchanging 3D models and animations between different software applications, particularly in the fields of 3D animation, game development, and visual effects. 
    """

tools = [

]

requires = [
    "cmake-3.31.7+",
]

build_command = """
chmod +x {root}/fbx202032_fbxsdk_linux
{root}/fbx202032_fbxsdk_linux $REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.FBX_ROOT.set("{root}")
    env.FBX_INCLUDE_DIR.set("{root}/include")
    env.FBX_LIBRARY_DIR.set("{root}/lib/gcc/x64/release")