# Quesdtion 1 (Assembly hello world)
## Task
Program prints out "Hello World from Trondheim!" three times to stderr
and returns with error code 1, as requested by the task.
## Requirements
* nasm
* binutils

## Compile and run
Assuming that the starting point is in the QuestionOne folder.
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