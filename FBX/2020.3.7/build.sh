VERSION=$(basename "$(dirname "$0")")

VERSION_NO_DOTS=


# Download FBX SDK
wget https://damassets.autodesk.net/content/dam/autodesk/www/files/fbx"$VERSION_NO_DOTS"_fbxsdk_gcc_linux.tar.gz -O fbx_sdk.tar.gz || exit 1
# Extract and install
tar -xzvf fbx_sdk.tar.gz || exit 1
chmod +x fbx"$VERSION_NO_DOTS"_fbxsdk_linux
sh ./fbx"$VERSION_NO_DOTS"_fbxsdk_linux $REZ_BUILD_INSTALL_PATH || exit 1
# Cleanup
rm fbx_sdk.tar.gz
