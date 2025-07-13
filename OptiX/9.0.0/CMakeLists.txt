cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OptiX
    URL https://github.com/NVIDIA/optix-dev/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX optix
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ${CMAKE_COMMAND} -E copy_directory
        "<SOURCE_DIR>"
        "$ENV{REZ_BUILD_INSTALL_PATH}"

)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OptiX-${VERSION} Install finished!\n\"
    )"
)