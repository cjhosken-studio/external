VERSION=$(basename "$(dirname "$0")")

VERSION_PATCH="575.57.08"

SOURCE_URL="https://developer.download.nvidia.com/compute/cuda/$VERSION/local_installers"
TAR_FILE="cuda_"$VERSION"_"$VERSION_PATCH"_linux.run"
SOURCE_DIR="cmake-$VERSION"

echo $SOURCE_URL

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

sh $TAR_FILE --silent --toolkit --defaultroot=$REZ_BUILD_INSTALL_PATH --toolkitpath=$REZ_BUILD_INSTALL_PATH
