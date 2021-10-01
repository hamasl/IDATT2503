cmake_minimum_required(VERSION 3.20)

project(Task5)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

add_library(string_editor INTERFACE)
target_include_directories(string_editor INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(main main.c)
target_link_libraries(main string_editor)

enable_testing()
add_subdirectory(tests)
