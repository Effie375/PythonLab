# 📁 Exercises C - Programming

## [Exercise 1](../Exercises/01_Exercise.c)

Γράψτε ένα πρόγραμμα C το οποίο:

- Δηλώνει μια σταθερά με τιμή 15, με τη χρήση της const
- Δηλώνει μια ακέραια μεταβλητή
- Διαβάζει τη τιμή της ακέραιας μεταβλητής από το χρήστη
- Εκτυπώνει τις τιμές της σταθεράς και της μεταβλητής

```c
# include <stdio.h>

int main(){
  int variable;
  const int constant = 15;
    
  printf("Enter a number: ");
  scanf("%d", &variable);
    
  printf("The value of the variable is %d\n", variable);
  printf("The value of the constant is %d", constant);

  return 0;
}
```

## [Exercise 2](../Exercises/02_Exercise.c)

Γράψε ένα πρόγραμμα C το οποίο θα ελέγχει την ηλικία του και θα εκτυπώνει:

- Ανήλικος! Αν ο χρήστης είναι < 18
- Ενήλικος! Αν ο χρήστης ειναι μεταξύ 18 και 65
- Συνταξιούχος! Αν ο χρήστης > 65

```c
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
```

## [Exercise 3](../Exercises/03_Exercise.c)

Γράψτε ένα πρόγραμμα, το οποίο θα λαμβάνει από το χρήστη 2 ακέραιους αριθμούς και θα εκτυπώνει ποιος είναι ο μεγαλύτερος.

```c
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
  else // num_1 <= num_2{
    printf("The greater number is: %d", num_2);
  }
    
  return 0;
}

```

## [Exercise 4](../Exercises/04_Exercise.c)

Γράψτε ένα πρόγραμμα, το οποίο θα λαμβάνει από το χρήστη 3 ακέραιους αριθμούς και θα εκτυπώνει ποιος είναι ο μεγαλύτερος.

```c
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
```

## [Exercise 5](../Exercises/05_Exercise.c)

Να γράψετε ένα πρόγραμμα το οποίο:

- Θα δέχεται από το χρήστη έναν ακέραιο αριθμό, ο οποίος θα απεικονίζει δευτερόλεπτα,
- Έπειτα να υπολογίζεις πόσες ώρες, πόσα λεπτά και πόσα δευτερόλεπτα είναι ο αριθμός που έδωσε ο χρήστης. Π.χ. Είσοδος του χρήστη: 5000

- Ώρες: 1
- Λεπτά: 23
- Δευτερόλεπτα: 20

```c
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
```
