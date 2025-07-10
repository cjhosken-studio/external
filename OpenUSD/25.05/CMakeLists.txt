cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    USD
    URL https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX ${CMAKE_BINARY_DIR}/usd
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DBUILD_SHARED_LIBS=ON

        -DPXR_ENABLE_PYTHON_SUPPORT=ON
        -DPXR_PY_UNDEFINED_DYNAMIC_LOOKUP=ON

        -DPython3_ROOT=${Python_ROOT}

        -DOpenSubdiv_DIR=${OpenSubdiv_ROOT}
        -DOPENSUBDIV_INCLUDE_DIR=${OpenSubdiv_INCLUDE_DIR}

        -DOIIO_LOCATION=LIBRARIES=$ENV{OpenImageIO_ROOT}/lib64
        -DOIIO_INCLUDE_DIR=$ENV{OpenImageIO_ROOT}/include

        -DPXR_ENABLE_PTEX_SUPPORT=OFF
        -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON
        -DPXR_BUILD_OPENCOLORIO_PLUGIN=OFF
        -DPXR_BUILD_EMBREE_PLUGIN=OFF
        -DPXR_ENABLE_MATERIALX_SUPPORT=OFF
        
        -DPXR_ENABLE_GL_SUPPORT=ON
        -DPXR_ENABLE_VULKAN_SUPPORT=OFF

        -DPXR_BUILD_ALEMBIC_PLUGIN=OFF
        -DPXR_ENABLE_HDF5_SUPPORT=OFF

        -DPXR_BUILD_PRMAN_PLUGIN=OFF

        -DPXR_BUILD_DOCUMENTATION=OFF
        -DPXR_BUILD_EXAMPLES=OFF
        -DPXR_BUILD_TESTS=OFF
        -DPXR_BUILD_TUTORIALS=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenUSD-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)