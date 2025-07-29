VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://www.python.org/ftp/python/$VERSION"
TAR_FILE="Python-$VERSION.tar.xz"
SOURCE_DIR="Python-$VERSION"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Extracting $TAR_FILE..."
    tar -xf "$TAR_FILE" 
else
    echo "Source directory $SOURCE_DIR already exists, skipping extraction."
fi

cd $SOURCE_DIR

./configure --prefix=$REZ_BUILD_INSTALL_PATH \
    --enable-optimizations \
    --with-lto \
    --with-ensurepip=install \
    --enable-shared 

make -j$NPROC
make install