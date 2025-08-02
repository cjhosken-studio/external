VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://static.rust-lang.org/dist"
TAR_FILE="rust-$VERSION-x86_64-unknown-linux-gnu.tar.xz"
SOURCE_DIR="rust-$VERSION-x86_64-unknown-linux-gnu"

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
echo "Installing rust..."
./install.sh --prefix=$REZ_BUILD_INSTALL_PATH --disable-ldconfig

echo -e "\n[REZ] rust $VERSION Install finished!\n"
