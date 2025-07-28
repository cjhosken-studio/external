VERSION=$(basename "$(dirname "$0")")

set -e
wget https://github.com/Kitware/CMake/releases/download/v$VERSION/cmake-$VERSION.tar.gz -O cmake_src.tar.gz
tar -xzf cmake_src.tar.gz
cd cmake-$VERSION
./bootstrap --prefix=$REZ_BUILD_INSTALL_PATH \
            --parallel=$NPROC \
            --system-curl \
            --no-qt-gui
make -j$NPROC
make install