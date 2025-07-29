VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://registrationcenter-download.intel.com/akdlm/IRC_NAS/2d607ce3-9aa8-492d-a97d-e473dc37be66"
TAR_FILE="intel-cpp-essentials-"$VERSION"_offline.sh"

if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

sh $TAR_FILE -a -s --eula accept --action install --install-dir $REZ_BUILD_INSTALL_PATH

if [ ! -f "$HOME/intel" ]; then
    rm -rf "$HOME/intel"
fi