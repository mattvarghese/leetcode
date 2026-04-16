cmake_minimum_required(VERSION 3.20)
project(LeetCode_CPP)

set(CMAKE_CXX_STANDARD 20)

# Download Catch2 header automatically if not present
include(FetchContent)
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v2.13.10 # Stable v2 is header-only
)
FetchContent_MakeAvailable(Catch2)

add_executable(run_tests test_l00002.cpp)
target_link_libraries(run_tests Catch2::Catch2)
