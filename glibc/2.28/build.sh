VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://mirror.cyberbits.eu/gnu/glibc"
TAR_FILE="glibc-$VERSION.tar.gz"
SOURCE_DIR="glibc-$VERSION"

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

cd $SOURCE_DIR

mkdir -p ../glibc_build
cd ../glibc_build
"../$SOURCE_DIR/configure" --prefix=$REZ_BUILD_INSTALL_PATH

# Build and install
echo "Building glibc..."
make -j$(nproc)
make install

echo -e "\n[REZ] glibc $VERSION Install finished!\n"