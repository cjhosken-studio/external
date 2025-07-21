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

tools = [

]

variants = [
    ["studio_core-2026"],
]

requires = [

]


build_command = f"""
#!/bin/bash

# Download FBX SDK
wget https://damassets.autodesk.net/content/dam/autodesk/www/files/fbx{version.replace(".", "")}_fbxsdk_gcc_linux.tar.gz -O fbx_sdk.tar.gz || exit 1

# Extract and install
tar -xzvf fbx_sdk.tar.gz || exit 1
chmod +x fbx{version.replace(".", "")}_fbxsdk_linux
./fbx{version.replace(".", "")}_fbxsdk_linux $REZ_BUILD_INSTALL_PATH || exit 1

# Cleanup
rm fbx_sdk.tar.gz
"""

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib/release")
    env.FBX_ROOT.set("{root}")
    env.FBX_INCLUDE_DIR.set("{root}/include")
    env.FBX_LIBRARY_DIR.set("{root}/lib/release")