VERSION=$(basename "$(dirname "$0")")

# Unix-like build commands (Linux/macOS)
wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tar.xz

tar -xf Python-$VERSION.tar.xz

cd Python-$VERSION

./configure --prefix=$REZ_BUILD_INSTALL_PATH \ 
--enable-optimizations \ 
--with-lto \ 
--with-ensurepip=install \ 
--enable-shared 

make -j$NPROC
make install

#{root}/bin/python3 -m pip install numpy==1.26.4