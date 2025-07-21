cmake_minimum_required(VERSION 3.31.8+)

include(ExternalProject)

# Versions
get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# Base URLs
set(GNU_MIRROR https://ftp.gnu.org/gnu)
set(GCC_BASE_URL ${GNU_MIRROR}/gcc/gcc-${VERSION})


ExternalProject_Add(gcc
  URL ${GCC_BASE_URL}/gcc-${VERSION}.tar.gz
  PREFIX gcc
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
    
  CONFIGURE_COMMAND 
      env ${LIBRARY_PATH_FLAGS}
      <SOURCE_DIR>/configure
      --prefix=<INSTALL_DIR>
      --enable-languages=c,c++,fortran
      --disable-multilib
      --enable-checking=release
      --enable-threads=posix
      --with-system-zlib
    
    BUILD_COMMAND make -j${REZ_BUILD_THREAD_COUNT}
    INSTALL_COMMAND make install-strip
    
    # Environment setup
    BUILD_IN_SOURCE 0
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] gcc-${VERSION} Install finished!\n\"
    )"
)