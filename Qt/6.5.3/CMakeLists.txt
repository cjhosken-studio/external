cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

string(REGEX REPLACE "^([0-9]+\\.[0-9]+).*" "\\1" VERSION_MAJOR_MINOR ${VERSION})

ExternalProject_Add(
    Qt
    URL https://download.qt.io/official_releases/qt/${VERSION_MAJOR_MINOR}/${VERSION}/single/qt-everywhere-src-${VERSION}.tar.xz
    PREFIX qt
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=17
        -DBUILD_SHARED_LIBS=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Qt-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)