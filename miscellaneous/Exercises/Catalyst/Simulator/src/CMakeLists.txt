cmake_minimum_required(VERSION 3.8)

set(CMAKE_CXX_STANDARD 11)

project(simulator)

add_executable(${CMAKE_PROJECT_NAME} main.cxx UtilsConduit.cxx Catalyst2Adaptor.cxx)

find_package(catalyst REQUIRED)
target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE catalyst::catalyst)

option(USE_MPI "Use MPI" OFF)
if (USE_MPI)
  find_package(MPI REQUIRED)
  target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${MPI_C_INCLUDE_PATH})
  target_link_libraries(${CMAKE_PROJECT_NAME} LINK_PRIVATE ${MPI_LIBRARIES})
  add_compile_definitions(USE_MPI=1)
endif()

