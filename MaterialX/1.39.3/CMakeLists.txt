cmake_minimum_required(VERSION 4.0.3)

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
        -DCMAKE_CXX_STANDARD=17
        -DBUILD_SHARED_LIBS=ON

        -DMATERIALX_BUILD_PYTHON=ON
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] MaterialX-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)