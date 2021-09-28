#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    char input[32];
    char password[]="thatwaseasy";
    printf ("Enter the password: \n");
    scanf ("%s", input);
    for (int i=0;i<11;i++){
        if (input[i]!=password[i]-32){
            printf("Incorrect : (\n");
            return 1;
        }

    }
    printf("Correct!\n");
    return 1;
}