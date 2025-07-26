cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(GIT_LFS_VERSION 3.7.0)

ExternalProject_Add(
    git
    URL https://github.com/git/git/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX git
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND 
        autoreconf -i <SOURCE_DIR> &&
        <SOURCE_DIR>/configure
        --prefix=<INSTALL_DIR>
        --with-curl
        --with-openssl
        --with-expat
        --with-zlib

    BUILD_COMMAND make -j ${nproc} all
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND make install
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] git-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)