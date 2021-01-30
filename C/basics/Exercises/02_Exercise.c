# include <stdio.h>

int main(){
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);
    
    if (age < 18){
    	printf("Underage");
	} 
    else if (age <= 65){
    	printf("Adult");
	}
    else{
    	printf("Retired");
	}

    return 0;
}
