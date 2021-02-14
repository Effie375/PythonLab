# include <stdio.h>

int main(){
	int x;
	int y;
	
	printf("Enter an integer for x: ");
	scanf("%d", &x);

	printf("Enter an integer for y: ");
	scanf("%d", &y);
	
	if (x < y)
		printf("\n %d < %d", x, y);
		
	if (x <= y)
		printf("\n %d <= %d", x, y);
		
	if (x == y)
		printf("\n %d == %d", x, y);
		
	if (x > y)
		printf("\n %d > %d", x, y);
		
	if (x >= y)
		printf("\n %d >= %d", x, y);
		
	return 0;
}
