cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Vulkan
    URL https://sdk.lunarg.com/sdk/download/${VERSION}/linux/vulkansdk-linux-x86_64-${VERSION}.tar.xz
    PREFIX vulkan
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND
        COMMAND ${CMAKE_COMMAND} -E copy_directory <SOURCE_DIR> <INSTALL_DIR>
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Vulkan-${VERSION} Install finished!\n\"
    )"
)