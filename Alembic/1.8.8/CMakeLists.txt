cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Alembic
    URL https://github.com/alembic/alembic/archive/refs/tags/${VERSION}.tar.gz
    PREFIX alembic
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DALEMBIC_SHARED_LIBS=ON

        -DUSE_TESTS=OFF

        -DUSE_HDF5=OFF

        -DUSE_PYALEMBIC=OFF
        -DPYALEMBIC_PYTHON_MAJOR=3
        -DALEMBIC_DEBUG_WARNINGS_AS_ERRORS=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Alembic-${VERSION} Install finished!\n\"
    )"
)