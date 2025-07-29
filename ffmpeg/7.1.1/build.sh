VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://github.com/FFmpeg/FFmpeg/archive/refs/tags"
TAR_FILE="n$VERSION.tar.gz"
SOURCE_DIR="FFmpeg-n$VERSION"

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
echo "Configuring ffmpeg..."
./configure \
    --prefix=$REZ_BUILD_INSTALL_PATH \
    --disable-x86asm


# Build and install
echo "Building ffmpeg..."
make -j$(nproc)
make install

echo -e "\n[REZ] ffmpeg $VERSION Install finished!\n"