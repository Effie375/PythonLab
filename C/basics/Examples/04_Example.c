# include <stdio.h>

int main(){
    int num1, num2, num3;
    int max;
    
    printf("Enter a num1: ");
    scanf("%d", &num1);
    
    printf("Enter a num2: ");
    scanf("%d", &num2);
    
    printf("Enter a num3: ");
    scanf("%d", &num3);
    
    max = num1;
    
    if (num2 > max){
        max = num2;
    }
    if(num3 > max){
        max = num3;
    }

    printf("The greater number is %d.", max);
    
    return 0;
}

