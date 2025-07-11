cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    HDF5
    URL https://github.com/HDFGroup/hdf5/archive/refs/tags/hdf5_${VERSION}.tar.gz
    PREFIX hdf5
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] HDF5-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)