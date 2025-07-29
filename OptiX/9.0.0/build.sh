VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://github.com/NVIDIA/optix-dev/archive/refs/tags"
TAR_FILE="v$VERSION.tar.gz"
SOURCE_DIR="$VERSION"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

tar -xzf $TAR_FILE --strip-components=1 -C $REZ_BUILD_INSTALL_PATH
