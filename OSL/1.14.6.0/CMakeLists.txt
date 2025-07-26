cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(pugixml_VERSION 1.9)

ExternalProject_Add(
    pugixml
    URL https://github.com/zeux/pugixml/archive/refs/tags/v${pugixml_VERSION}.tar.gz
    PREFIX pugixml
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=OFF
)

ExternalProject_Add(
    OSL
    DEPENDS pugixml
    URL https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX osl
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=OFF
        -Dpugixml_DIR=<INSTALL_DIR>
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OSL-${VERSION} Install finished!\n\"
    )"
)