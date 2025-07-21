cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenUSD
    URL https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX usd
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    
    # Pre-build steps
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND python3 -m pip install PyOpenGL PyOpenGL_accelerate Jinja2
    
    # Install Python dependencies
    BUILD_COMMAND 
        mkdir -p build &&
        cd build &&
        cmake 
            -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
            -DCMAKE_BUILD_TYPE=Release
            -DBUILD_SHARED_LIBS=ON
            
            -DPXR_ENABLE_PYTHON_SUPPORT=ON
            -DPXR_USE_PYTHON3=ON
            -DPYTHON_ROOT=$ENV{Python_ROOT}
            -DPXR_PY_UNDEFINED_DYNAMIC_LOOKUP=ON
            -DPYOPENGL_AVAILABLE=ON

            -DPXR_ENABLE_MATERIALX_SUPPORT=ON
            -DPXR_ENABLE_PTEX_SUPPORT=ON

            -DPTEX_INCLUDE_DIR=$ENV{Ptex_INCLUDE_DIR}
            -DPTEX_LIBRARY=$ENV{Ptex_LIBRARY_DIR}

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
            ..
    
    INSTALL_COMMAND 
        cd build &&
        make install -j$(nproc)
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenUSD-${VERSION} Install finished!\n\"
    )"
)