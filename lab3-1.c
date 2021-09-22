#include <stdio.h>
#include <stdlib.h>

//takes two chars and adds them together
int func1(int x, int y);
int func2(int x, int y);

int func1(int x, int y){
    int z=3*x+y;
    return (func2(z, 3));
}
int func2(int x, int y){
    return x-y;
}
int main(){
    int x=0;
    x=func1(6,4);
    return 0;
}