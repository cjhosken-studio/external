cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenVDB
    URL https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX openvdb
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release

        -DUSE_ZLIB=OFF
        -DUSE_BLOSC=OFF

        -DOPENVDB_BUILD_DOCS=OFF

        -DOPENVDB_BUILD_PYTHON_MODULE=ON

        -DOPENVDB_BUILD_AX=OFF
        -DOPENVDB_BUILD_AX_BINARIES=OFF

        -DOPENVDB_BUILD_NANOVDB=OFF
        -DNANOVDB_BUILD_TOOLS=OFF

)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenVDB-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)