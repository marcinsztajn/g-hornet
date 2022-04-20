# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT hornet_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT hornet_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND hornet_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(hornet
   ../../..
   gr::hornet
   "${hornet_python_files}")

# copy in bindings .so file for use in QA test module
add_custom_target(
  copy_bindings_for_tests ALL
  COMMAND
    ${CMAKE_COMMAND} -E copy "${CMAKE_CURRENT_BINARY_DIR}/*.so"
    ${CMAKE_BINARY_DIR}/test_modules/gnuradio/hornet/
  DEPENDS hornet_python)

install(TARGETS hornet_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/hornet COMPONENT pythonapi)
