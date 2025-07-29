VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://gcc.gnu.org/pub/gcc/infrastructure"
TAR_FILE="mpc-1.2.1.tar.gz"
SOURCE_DIR="mpc-$VERSION"

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

echo $MPFR_ROOT

./configure --prefix=$REZ_BUILD_INSTALL_PATH --with-gmp=$GMP_ROOT --with-mpfr=$MPFR_ROOT

make -j$NPROC
make install