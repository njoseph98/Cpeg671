#include <stdio.h>
#include <stdlib.h>

//takes two chars and adds them together
void add (char *x, char *y){
    printf("Question 1\n");
    int firstNum=atoi(x);
    int secondNum=atoi(y);
    int sum=firstNum+secondNum;
    printf("%d\n", sum);
}
void question2(){
    printf("Question 2\n");
    int x=3;
    int *y;
    y = &x;
    printf("%d\n", x );
    printf("%p\n", y );
    printf("%p\n", &x );
    printf("%p\n", &y );
    printf("%d\n", *y );
    
}
void question3(){
    printf("Question 3\n");
    int arr[3]={42,1337, 0};
    int *i;
    for (i=arr; i<arr+3;i++){
        printf("%d\n", *i);
    }

}
void question4(){
    
    printf("Question 4\n");
  
    int arr[3]={97,98,99};
    int n=sizeof(arr)/ sizeof(int);
    int l=sizeof(int)/sizeof(char);
    
    
    //Integer printing
    for (int i=0;i<n;i++){
        printf("%d\n", arr[i]);
    }
    char *charArray = (char*) arr;
    //char printing
    for(int i=0;i<3*n;i++){
		printf("%s\n", (charArray) + i);
    }
	
}

int main(int argc, char ** argv){
    //Question 1
    
    char *x= argv[1];
    char *y = argv[2];
    add(x,y);
    
    //Question 2
    question2();
    //Question 3
    question3();
    //Question 4
    question4();
    return 0;
}