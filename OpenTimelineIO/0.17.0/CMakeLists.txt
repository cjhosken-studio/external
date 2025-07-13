cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenTimelineIO
    URL https://github.com/AcademySoftwareFoundation/OpenTimelineIO/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX opentimelineio
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DOTIO_SHARED_LIBS=ON

        -DOTIO_IMATH_LIBS=$ENV{Imath_LIBRARY_DIR}
        -DOTIO_FIND_IMATH=OFF

        -DOTIO_PYTHON_INSTALL=OFF


)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenTimelineIO-${VERSION} Install finished!\n\"
    )"
)