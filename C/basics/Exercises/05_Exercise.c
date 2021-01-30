# include <stdio.h>

int main(){
	int num, hour, minutes, seconds, x;
	
	printf("Enter a number of seconds: ");
	scanf("%d", &num);
	
	hour = (num / 3600);
	x = (num % 3600);
	minutes = (x / 60);
	seconds = (x % 60);
	
	printf("\n%d seconds is %d hour, %d minutes and %d seconds.", num, hour, minutes, seconds);
	
	return 0;
}
