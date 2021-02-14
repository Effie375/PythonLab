# include <stdio.h>

int main(){
    int num;
    int max;
    
    printf("Enter a num1: ");
    scanf("%d", &num);
    
    max = num;
    
    printf("Enter a num2: ");
    scanf("%d", &num);
    
    if (num > max){
        max = num;
    }
    
    printf("Enter a num3: ");
    scanf("%d", &num);
    
    if (num > max){
        max = num;
    }
    
    printf("The greater number is %d.", max);
    
    return 0;
}
