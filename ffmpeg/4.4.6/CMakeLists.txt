cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    FFmpeg
    URL https://github.com/FFmpeg/FFmpeg/archive/refs/tags/n${VERSION}.tar.gz
    PREFIX ffmpeg
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND 
        chmod +x <SOURCE_DIR> &&
        <SOURCE_DIR>/configure
        --prefix=<INSTALL_DIR>
        --disable-x86asm

    BUILD_COMMAND make -j ${nproc}
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] FFmpeg-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)