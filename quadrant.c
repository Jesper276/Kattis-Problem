#include <stdio.h>

int main()
{
    int x,y;
    scanf("%i %i",&x,&y);
    if(x > 0 && y > 0){
        printf("1");
    }
    else if(x < 0 && y < 0){
        printf("3");
    }
    else if(x > 0 && y < 0){
            printf("4");
    }else(printf("2"));

    return 0;
}