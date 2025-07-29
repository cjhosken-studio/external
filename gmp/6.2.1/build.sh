VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://gcc.gnu.org/pub/gcc/infrastructure"
TAR_FILE="gmp-6.2.1.tar.bz2"
SOURCE_DIR="gmp-$VERSION"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Extracting $TAR_FILE..."
    tar -xvjf $TAR_FILE
else
    echo "Source directory $SOURCE_DIR already exists, skipping extraction."
fi

cd $SOURCE_DIR

./configure --prefix=$REZ_BUILD_INSTALL_PATH

make -j$NPROC
make install