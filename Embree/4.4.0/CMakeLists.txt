cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Embree
    URL https://github.com/RenderKit/embree/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX embree
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DBUILD_SHARED_LIBS=ON

)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Embree-${VERSION} Install finished!\n\"
    )"
)