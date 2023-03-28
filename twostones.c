#include <stdio.h>

int N;

int main(){
    int N;
    scanf("%i",&N);
    if(N%2 == 0){
        printf("Bob");
    }else{
        printf("Alice");
    }
    return 0;
}