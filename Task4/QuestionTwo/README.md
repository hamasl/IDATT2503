# Question 2 (C, C++ and Rust)
## Task
Make a program (in each of C, C++ and Rust) that converts every ionstance of &, <, > to &amp, &lt and &gt.

## Requirements
### C
* gcc
* CMake (recomended) VERSION 3.20
### C++
* g++ (with c++20 compatability)
* CMake (recomended) VERSION 3.20
### Rust
* rustc
* Make (recommended)

## Compiling and running
Assuming that the starting point is in the QuestionTwo folder.
### C
With make:
```
cd C
cmake .
make
./QTwoC
```
Without make:
```
cd C
gcc main.c -O QTwoC
./QTwoC
```
### C++
With make:
```
cd Cpp
cmake .
make
./QTwoCpp
```
Without make:
```
cd Cpp
g++ -std=c++20 main.cpp -O QTwoCpp
./QTwoCpp
```
### Rust
With make:
```
cd Rust
make
```
Without make:
```
cd Rust
rustc main.rs
./main
```