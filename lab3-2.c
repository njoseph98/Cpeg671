#include <stdio.h>
#include <stdlib.h>

int main(){
    int x=4;
    int z = 0;
    int y=0;
    if (x==1){
        z=1;
    }
    else if (x==4){
        z=2;
        
    }
    else{
        z=3;
    }
    for (int i=0; i<z;i++){
           y+=i;
    }
    return 0;
}