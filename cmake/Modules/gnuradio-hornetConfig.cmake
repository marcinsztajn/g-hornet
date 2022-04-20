find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_HORNET gnuradio-hornet)

FIND_PATH(
    GR_HORNET_INCLUDE_DIRS
    NAMES gnuradio/hornet/api.h
    HINTS $ENV{HORNET_DIR}/include
        ${PC_HORNET_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_HORNET_LIBRARIES
    NAMES gnuradio-hornet
    HINTS $ENV{HORNET_DIR}/lib
        ${PC_HORNET_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-hornetTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_HORNET DEFAULT_MSG GR_HORNET_LIBRARIES GR_HORNET_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_HORNET_LIBRARIES GR_HORNET_INCLUDE_DIRS)
