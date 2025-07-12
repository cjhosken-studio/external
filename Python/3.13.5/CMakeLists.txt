cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Python
    URL https://github.com/python/cpython/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX python
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND
        <SOURCE_DIR>/configure
        --enable-optimizations --with-lto
        --with-pydebug
        --with-ensurepip=install
        --prefix=<INSTALL_DIR>
    BUILD_COMMAND make -j ${nproc}
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
)

# Add post-install step for Python packages
ExternalProject_Add_Step(Python upgrade_pip
    COMMAND <INSTALL_DIR>/bin/pip3 install --upgrade pip
    DEPENDEES install
    COMMENT "Upgrading pip..."
)

ExternalProject_Add_Step(Python install_packages
    COMMAND <INSTALL_DIR>/bin/pip3 install PySide6==6.8.1 PyQt6==6.8.1 PyOpenGL==3.1.9 numpy==1.26.4
    DEPENDEES upgrade_pip
    COMMENT "Installing Python packages..."
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Python-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)