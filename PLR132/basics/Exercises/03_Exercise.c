# include <stdio.h>

int main(){

    int num_1;
    int num_2;
    
    printf("Enter a num1: ");
    scanf("%d", &num_1);
    
    printf("Enter a num2: ");
    scanf("%d", &num_2);
    
    if (num_1 > num_2){
        printf("The greater number is: %d", num_1);
    }
    else //num_1 <= num_2{
        printf("The greater number is: %d", num_2);
    }
    
    return 0;
}
