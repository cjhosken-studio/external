cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Python
    URL https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tar.xz
    PREFIX python
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND
        <SOURCE_DIR>/configure
        --prefix=<INSTALL_DIR>
        --enable-optimizations
        --with-ensurepip=install
    BUILD_COMMAND make -j ${nproc}
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
)

# Add post-install step for Python packages
ExternalProject_Add_Step(Python install_packages
    COMMAND <INSTALL_DIR>/bin/pip3 install PySide6==6.8.3 PyOpenGL numpy pybind11 ninja2
    DEPENDEES install
    COMMENT "Installing Python packages: PySide6, PyOpenGL, numpy"
    LOG 1
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Python-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)