# include <stdio.h>

int main(){

	int x = 1;
	int y = 2;
	int z;

	z = z = (y > x) && (x < x);
	printf("%d\n", z);

	z = (x = x) && (y == y);
	printf("%d", z);

	return 0;
}
