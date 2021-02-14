# include <stdio.h>

int main(){
    const int constant = 15;
    int variable;

    printf("Enter a number: ");
    scanf("%d", &variable);

    printf("The value of the variable is %d\n", variable);
    printf("The value of the constant is %d", constant);

    return 0;
}
