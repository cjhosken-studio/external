cmake_minimum_required(VERSION 3.15)

include(ExternalProject)

# Versions
get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(GMP_VERSION 6.2.0)
set(MPFR_VERSION 4.1.0)
set(MPC_VERSION 1.2.1)
set(ISL_VERSION 0.16.1)

# Base URLs
set(GNU_MIRROR https://ftp.gnu.org/gnu)
set(GCC_BASE_URL ${GNU_MIRROR}/gcc/gcc-${VERSION})
set(MPFR_BASE_URL https://www.mpfr.org/mpfr-${MPFR_VERSION})

# Dependency chain: GMP → MPFR → MPC → ISL → GCC

ExternalProject_Add(gmp
  URL ${GNU_MIRROR}/gmp/gmp-${GMP_VERSION}.tar.bz2
  PREFIX gmp
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
  CONFIGURE_COMMAND <SOURCE_DIR>/configure
    --prefix=<INSTALL_DIR>
    --enable-cxx
    --disable-shared
    --enable-static
  BUILD_IN_SOURCE 1
)

ExternalProject_Add(mpfr
  DEPENDS gmp
  URL ${MPFR_BASE_URL}/mpfr-${MPFR_VERSION}.tar.bz2
  PREFIX mpfr
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
  CONFIGURE_COMMAND <SOURCE_DIR>/configure
    --prefix=<INSTALL_DIR>
    --with-gmp=<INSTALL_DIR>
    --disable-shared
    --enable-static
  BUILD_IN_SOURCE 1
)

ExternalProject_Add(mpc
  DEPENDS mpfr
  URL ${GNU_MIRROR}/mpc/mpc-${MPC_VERSION}.tar.gz
  PREFIX mpc
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
  CONFIGURE_COMMAND <SOURCE_DIR>/configure
    --prefix=<INSTALL_DIR>
    --with-gmp=<INSTALL_DIR>
    --with-mpfr=<INSTALL_DIR>
    --disable-shared
    --enable-static
  BUILD_IN_SOURCE 1
)

ExternalProject_Add(isl
  DEPENDS gmp
  URL https://libisl.sourceforge.io/isl-${ISL_VERSION}.tar.bz2
  PREFIX isl
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
  CONFIGURE_COMMAND <SOURCE_DIR>/configure
    --prefix=<INSTALL_DIR>
    --with-gmp-prefix=<INSTALL_DIR>
    --disable-shared
    --enable-static
  BUILD_IN_SOURCE 1
)

# Main GCC build

ExternalProject_Add(gcc
  DEPENDS gmp mpfr mpc isl
  URL ${GCC_BASE_URL}/gcc-${VERSION}.tar.gz
  PREFIX gcc
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
    
  CONFIGURE_COMMAND 
      env ${LIBRARY_PATH_FLAGS}
      <SOURCE_DIR>/configure
      --prefix=<INSTALL_DIR>
      --enable-languages=c,c++,fortran
      --disable-multilib
      --with-gmp=<INSTALL_DIR>
      --with-mpfr=<INSTALL_DIR>
      --with-mpc=<INSTALL_DIR>
      --with-isl=<INSTALL_DIR>
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
        COMMAND echo \"\n[REZ] gcc-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)