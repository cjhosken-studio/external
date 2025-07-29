VERSION=$(basename "$(dirname "$0")")
VERSION_NO_DOTS="${VERSION//./}"  # Remove all dots (e.g., "2020.3.4" → "202034")

SOURCE_URL="https://damassets.autodesk.net/content/dam/autodesk/www/files"
TAR_FILE="fbx"$VERSION_NO_DOTS"_fbxsdk_gcc_linux.tar.gz"
SOURCE_DIR="fbx"$VERSION_NO_DOTS"_fbxsdk_linux"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Extracting $TAR_FILE..."
    tar -xzf $TAR_FILE
else
    echo "Source directory $SOURCE_DIR already exists, skipping extraction."
fi


"./$SOURCE_DIR" $REZ_BUILD_INSTALL_PATH

echo -e "\n[REZ] FBX $VERSION Install finished!\n"