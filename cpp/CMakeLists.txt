cmake_minimum_required(VERSION 3.20)
project(LeetCode_CPP)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

set(CMAKE_CXX_STANDARD 20)

# Download Catch2 header automatically if not present
include(FetchContent)
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v2.13.10 # Stable v2 is header-only
)
FetchContent_MakeAvailable(Catch2)

# Target for Add Two Numbers
add_executable(test_l00002 test_l00002.cpp)
target_link_libraries(test_l00002 Catch2::Catch2)

# New Target for Median of Two Sorted Arrays
add_executable(test_l00004 test_l00004.cpp)
target_link_libraries(test_l00004 Catch2::Catch2)
