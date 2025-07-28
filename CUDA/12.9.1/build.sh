VERSION=$(basename "$(dirname "$0")")

INSTALLER="cuda_"$VERSION"_575.57.08_linux.run"

wget https://developer.download.nvidia.com/compute/cuda/$VERSION/local_installers/$INSTALLER
sh ./$INSTALLER --silent --toolkit --defaultroot=$REZ_BUILD_INSTALL_PATH --toolkitpath=$REZ_BUILD_INSTALL_PATH