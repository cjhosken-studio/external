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
    CONFIGURE_COMMAND python3 -m pip install PySide6==6.8.1 PyQt6==6.8.1
    
   BUILD_COMMAND <SOURCE_DIR>/configure
        -prefix <INSTALL_DIR>
        -release
        -opensource
        -confirm-license
        && make -Wno-dev -j
        
    INSTALL_COMMAND make install
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Qt-${VERSION} Install finished!\n\"
    )"
)