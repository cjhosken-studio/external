VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://ftp.gnu.org/gnu/gcc/gcc-$VERSION"
TAR_FILE="gcc-$VERSION.tar.gz"
SOURCE_DIR="gcc-$VERSION"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Extracting $TAR_FILE..."
    tar -xf $TAR_FILE
else
    echo "Source directory $SOURCE_DIR already exists, skipping extraction."
fi

cd $SOURCE_DIR

# Configure
echo "Configuring gcc..."
./configure \
    --prefix=$REZ_BUILD_INSTALL_PATH \
    --enable-languages=c,c++,fortran \
    --disable-multilib \
    --with-mpc=$MPC_ROOT \
    --with-gmp=$GMP_ROOT \
    --with-mpfr=$MPFR_ROOT


# Build and install
echo "Building gcc..."
make -j$(nproc)
make install-strip

echo -e "\n[REZ] gcc $VERSION Install finished!\n"
