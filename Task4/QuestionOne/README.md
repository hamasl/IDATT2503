# Assembly hello world
## Task
Program prints out Hello World three times to stderr
and returns with error code 1, as requested by the task.
## Requirements
* nasm
* binutils

## Compile and run
Compile by using (make):
```
make
```
Or manually by using:
```
nasm -f elf64 main.s
ld main.o -o main
./main
```