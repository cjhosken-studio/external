cmake_minimum_required(VERSION 3.31.7)

include(ExternalProject)

# Versions
get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(LINUX_HEADERS_VERSION 6.8.5)

# 3. Linux headers
ExternalProject_Add(linux-headers
  URL https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-${LINUX_HEADERS_VERSION}.tar.xz
  PREFIX linux-headers
  INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
  CONFIGURE_COMMAND make defconfig && make INSTALL_DIR_PATH=<INSTALL_DIR>/include
  BUILD_IN_SOURCE 1
  BUILD_COMMAND  ""
)

# 4. glibc
ExternalProject_Add(glibc
  DEPENDS linux-headers
  URL https://ftp.gnu.org/gnu/glibc/glibc-${VERSION}.tar.gz
  PREFIX glibc
  INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
  CONFIGURE_COMMAND 
    <SOURCE_DIR>/configure 
    --prefix=<INSTALL_DIR> 
    --with-headers=<INSTALL_DIR>/include
    --enabled-shared
    --disable-werror

  BUILD_COMMAND make -j${nproc}
  INSTALL_COMMAND make install DESTDIR=<INSTALL_DIR>
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] glibc-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)