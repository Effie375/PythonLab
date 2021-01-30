# include <stdio.h>

int main(){
    int num1, num2, num3;

    printf("Enter a num1: ");
    scanf("%d", &num1);

    printf("Enter a num2: ");
    scanf("%d", &num2);

    printf("Enter a num3: ");
    scanf("%d", &num3);

    if (num1 > num2){
        if (num1 > num3){
            printf("The greater number is %d.", num1);
        }
        else{
            printf("The greater number is %d.", num3);
        }
    }
    else{
        if (num2 > num3){
            printf("The greater number is %d.", num2);
        }
        else{
            printf("The greater number is %d.", num3);
        }
    }

    return 0;
}
