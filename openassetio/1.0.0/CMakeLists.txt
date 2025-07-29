cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(tomlplusplus_VERSION 3.2.0)
set(fmt_VERSION 9.1.0)
set(ada_VERSION 2.7.4)
set(PCRE2_VERSION 10.42)

ExternalProject_Add(
    fmt
    URL https://github.com/fmtlib/fmt/archive/refs/tags/${fmt_VERSION}.tar.gz
    PREFIX fmt
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
)

ExternalProject_Add(
    tomlplusplus
    DEPENDS fmt
    URL https://github.com/marzer/tomlplusplus/archive/refs/tags/v${tomlplusplus_VERSION}.tar.gz
    PREFIX tomlplusplus
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
)

ExternalProject_Add(
    ada
    DEPENDS tomlplusplus
    URL https://github.com/ada-url/ada/archive/refs/tags/v${ada_VERSION}.tar.gz
    PREFIX ada
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
)

ExternalProject_Add(
    PCRE2
    DEPENDS ada
    URL https://github.com/PCRE2Project/pcre2/archive/refs/tags/pcre2-${PCRE2_VERSION}.tar.gz
    PREFIX pcre2
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
)

ExternalProject_Add(
    OpenAssetIO
    DEPENDS PCRE2
    URL https://github.com/OpenAssetIO/OpenAssetIO/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX openassetio
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -Dtomlplusplus_DIR=<INSTALL_DIR>
        -Dfmt_DIR=<INSTALL_DIR>
        -Dada_DIR=<INSTALL_DIR>
        -DPCRE2_DIR=<INSTALL_DIR>

        -DOPENASSETIO_ENABLE_PYTHON=ON
        -DOPENASSETIO_ENABLE_TESTS=OFF
        -DOPENASSETIO_ENABLE_PYTHON_STUBGEN=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenAssetIO-${VERSION} Install finished!\n\"
    )"
)