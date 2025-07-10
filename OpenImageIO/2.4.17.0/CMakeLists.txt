cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenImageIO
    URL https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX openimageio
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON

        -DUSE_PYTHON=OFF
        -DUSE_QT=OFF
        -DUSE_OPENGL=ON

        -DPTEX_DIR=$ENV{Ptex_ROOT}

        -DOIIO_BUILD_TOOLS=ON
        -DENABLE_toolname=ON
        -DENABLE_formatname=ON

        -DOIIO_BUILD_TESTS=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenImageIO-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)