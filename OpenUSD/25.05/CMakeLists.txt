cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    USD
    URL https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX usd
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    BUILD_IN_SOURCE 1
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DBUILD_SHARED_LIBS=ON

        -DPXR_ENABLE_PYTHON_SUPPORT=ON
        -DPXR_PY_UNDEFINED_DYNAMIC_LOOKUP=ON

        -DPython3_ROOT=$ENV{Python_ROOT}
        -DPython3_EXECUTABLE=$ENV{Python_EXECUTABLE}

        -DOpenSubdiv_DIR=${OpenSubdiv_ROOT}
        -DOPENSUBDIV_INCLUDE_DIR=${OpenSubdiv_INCLUDE_DIR}

        -DOIIO_LOCATION=${OpenImageIO_ROOT}
        -DOIIO_LIBRARIES=${OpenImageIO_LIBRARY_DIR}
        -DOIIO_INCLUDE_DIRS=${OpenImageIO_INCLUDE_DIR}

        -DOCIO_INCLUDE_DIRS=${OpenColorIO_INCLUDE_DIR}
        -DOCIO_LIBRARIES=${OpenColorIO_LIBRARY_DIR}

        -DPTEX_INCLUDE_DIR=$ENV{Ptex_INCLUDE_DIR}
        -DPTEX_LIBRARY=$ENV{Ptex_LIBRARY_DIR}

        -DPXR_ENABLE_PTEX_SUPPORT=ON
        -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON
        -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON
        -DPXR_BUILD_EMBREE_PLUGIN=OFF
        -DPXR_ENABLE_MATERIALX_SUPPORT=ON
        
        -DPXR_ENABLE_GL_SUPPORT=ON
        -DPXR_ENABLE_VULKAN_SUPPORT=OFF

        # Don't support Alembic, only going with USD for file management.
        -DPXR_BUILD_ALEMBIC_PLUGIN=OFF
        -DPXR_ENABLE_HDF5_SUPPORT=OFF

        -DPXR_BUILD_PRMAN_PLUGIN=OFF

        -DPXR_BUILD_DOCUMENTATION=OFF
        -DPXR_BUILD_EXAMPLES=OFF
        -DPXR_BUILD_TESTS=OFF
        -DPXR_BUILD_TUTORIALS=OFF

        -DPXR_ENABLE_OSL_SUPPORT=OFF
        -DPXR_BUILD_IMAGING=ON
        -DPXR_BUILD_USE_IMAGING=ON
        -DPXR_BUILD_USDVIEW=ON
        -DPXR_BUILD_USDTOOLS=ON

)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenUSD-${VERSION} Install finished!\n\"
    )"
)