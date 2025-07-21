cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    MaterialX
    URL https://github.com/AcademySoftwareFoundation/MaterialX/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX materialx
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DMATERIALX_BUILD_PYTHON=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] MaterialX-${VERSION} Install finished!\n\"
    )"
)