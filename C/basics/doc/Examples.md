# 📁 Examples C - Programming

## [Example 1](../Examples/01_Example.c)

Προσπαθήστε να βρείτε την εκτύπωση του προγράμματος, προτού το μεταγλωττίσετε και το τρέξετε!

```c
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
```

## [Example 2](../Examples/02_Example.c)

- Μεταγλωττίστε, εκτελέστε και μελετήστε το παρακάτω πρόγραμμα που δείχνει την 1η χρήση της εντολής if
- Πόσες συγκρίσεις θα γίνουν κατά την εκτέλεση του προγράμματος;

```c
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
```

## [Example 3](../Examples/03_Example.c)

- Μεταγλωττίστε, εκτελέστε και μελετήστε το παρακάτω πρόγραμμα που δείχνει την 2η χρήση της εντολής if
- Πόσες συγκρίσεις θα γίνουν κατά την εκτέλεση του προγράμματος;

```c
# include <stdio.h>

int main(){
  int x;

  printf("Enter an integer: ");
  scanf("%d", &x);

  if (x%2 == 0)
    printf("The number is even.");
  else
    printf("The number is odd.");

  return 0;
}
```

## [Example 4](../Examples/04_Example.c)

Εύρεση μέγιστου αριθμού I.

```c
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
```

## [Example 5](../Examples/05_Example.c)

Εύρεση μέγιστου αριθμού II.

```c
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

```
