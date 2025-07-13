cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX pybind11
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND python3 -m pip install pytest==8.4.1
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DCMAKE_BUILD_TYPE=Release
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Pybind11-${VERSION} Install finished!\n\"
    )"
)