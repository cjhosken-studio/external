VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://gcc.gnu.org/pub/gcc/infrastructure"
TAR_FILE="mpfr-$VERSION.tar.bz2"
SOURCE_DIR="mpfr-$VERSION"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

if [ ! -d "$SOURCE_DIR" ]; then
    tar -xvjf "$TAR_FILE"
else
    echo "Source directory $SOURCE_DIR already exists, skipping extraction."
fi

cd $SOURCE_DIR

./configure --prefix=$REZ_BUILD_INSTALL_PATH \
    --with-gmp=$GMP_ROOT

make -j$NPROC
make install