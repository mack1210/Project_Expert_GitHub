//compile shortcut c + a + c
//running shortcut c + a + r
//compile .\a.exe.
//output : gcc ex.c -o main.exe     ex.c를 gcc 컴파일러를 이용하여 main.exe로 output한다
//compile : gcc -c ex.c -> ex.o가 생겨남 o means object
//실행파일 만들기 : gcc ex.o -o exe_from_obj.exe
#include <stdio.h>
#include <math.h>

void main(){
    printf("Hello World!\n");
    int a = 3;
    int b = 7;
    int result = pow(a, b);
    printf("%d\n\n", result);
}