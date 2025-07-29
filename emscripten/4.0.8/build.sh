VERSION=$(basename "$(dirname "$0")")

GIT_URL=https://github.com/emscripten-core/emsdk.git

if [ ! -d "$REZ_BUILD_INSTALL_PATH/.git" ]; then
    echo "Cloning emsdk repository..."
    git clone $GIT_URL "$REZ_BUILD_INSTALL_PATH"
else
    echo "emsdk repository already exists in $REZ_BUILD_INSTALL_PATH"
fi

$REZ_BUILD_INSTALL_PATH/emsdk install $VERSION
$REZ_BUILD_INSTALL_PATH/emsdk activate $VERSION