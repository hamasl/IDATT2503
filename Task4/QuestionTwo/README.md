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
With cmake:
```
cd C
cmake .
make
./QTwoC
```
Without cmake:
```
cd C
gcc main.c -o QTwoC
./QTwoC
```
### C++
With cmake:
```
cd Cpp
cmake .
make
./QTwoCpp
```
Without cmake:
```
cd Cpp
g++ -std=c++2a main.cpp -o QTwoCpp
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