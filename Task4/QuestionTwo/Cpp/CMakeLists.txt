cmake_minimum_required(VERSION 3.20)
project(Task4Question2Cpp)

set(CMAKE_CXX_STANDARD 20)
set(GCC_COVERAGE_COMPILE_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${CMAKE_COVERAGE_COMPILE_FLAGS}")

add_executable(QTwoCpp main.cpp)