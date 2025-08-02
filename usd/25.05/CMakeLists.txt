cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenUSD
    URL https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX usd
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    BUILD_IN_SOURCE 1
    CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
            -DCMAKE_BUILD_TYPE=Release
            -DBUILD_SHARED_LIBS=ON
            
            -DPXR_ENABLE_PYTHON_SUPPORT=ON
            -DPXR_USE_PYTHON3=ON
            -DPYTHON_ROOT=$ENV{PYTHON_ROOT}
            -DPYTHON_INCLUDE_DIRS=$ENV{PYTHON_INCLUDE_DIR}
            -DPYTHON_LIBRARIES=$ENV{PYTHON_LIBRARY_DIR}
            #-DPXR_PY_UNDEFINED_DYNAMIC_LOOKUP=ON

            -DTBB_ROOT_DIR=$ENV{oneAPI_ROOT}/../tbb/latest

            -DOCIO_INCLUDE_DIRS=$ENV{OpenColorIO_INCLUDE_DIR}
            -DOCIO_LIBRARIES=$ENV{OpenColorIO_LIBRARY_DIR}

            -DPXR_ENABLE_MATERIALX_SUPPORT=ON
            -DPXR_ENABLE_PTEX_SUPPORT=ON

            -DPTEX_INCLUDE_DIR=$ENV{PTEX_INCLUDE_DIR}
            -DPTEX_LIBRARY=$ENV{PTEX_LIBRARY_DIR}

            -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON
            -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON

            -DPXR_BUILD_ALEMBIC_PLUGIN=ON
            -DPXR_ENABLE_HDF5_SUPPORT=OFF
            -DPXR_BUILD_DRACO_PLUGIN=OFF

            -DALEMBIC_LIBRARY_DIR=$ENV{Alembic_LIBRARY_DIR}
            -DALEMBIC_INCLUDE_DIR=$ENV{Alembic_INCLUDE_DIR}

            -DPXR_ENABLE_METAL_SUPPORT=OFF

            -DPXR_BUILD_DOCUMENTATION=OFF
            -DPXR_BUILD_EXAMPLES=OFF
            -DPXR_BUILD_TESTS=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenUSD-${VERSION} Install finished!\n\"
    )"
)