VERSION=$(basename "$(dirname "$0")")

git clone https://github.com/emscripten-core/emsdk.git $REZ_BUILD_INSTALL_PATH
$REZ_BUILD_INSTALL_PATH/emsdk install $VERSION
$REZ_BUILD_INSTALL_PATH/emsdk activate $VERSION
