<!--
![Lines of code](https://img.shields.io/tokei/lines/github/Effie375/TPTE_PLR)
![GitHub issues](https://img.shields.io/github/issues-raw/Effie375/TPTE_PLR)
![GitHub](https://img.shields.io/github/license/Effie375/TPTE_PLR)
[![Gitter](https://badges.gitter.im/ΤΠΤΕ-AEGEAN/community.svg)](https://gitter.im/ΤΠΤΕ-AEGEAN/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
-->
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FEffie375%2FTPTE_PLR&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Εισαγωγή στον Προγραμματισμό

Το μάθημα αυτό απευθύνεται σε φοιτητές ή φοιτήτριες που σπουδάζουν στο ΤΠΤΕ του Πανεπιστημίου ΑΙΓΑΙΟΥ  και αποτελεί το βασικό εισαγωγικό μάθημα στην Πληροφορική και ειδικά στον Προγραμματισμό. Περιλαμβάνει τόσο θεωρητικό όσο και εργαστηριακό μέρος. Η ύλη στοχεύει στην εξοικείωση με τις βασικές έννοιες του προγραμματισμού υπολογιστών, στη κατανόηση του τρόπου εκτέλεσης ενός προγράμματος και στην εκμάθηση της γλώσσας προγραμματισμού **Python**.

Σας συνιστώ να αφιερώνετε αρκετό χρόνο στην προσπάθεια επίλυσης των ασκήσεων που θα συναντήσετε στη συνέχεια. Αν, ωστόσο, έχετε κολλήσει και δεν μπορείτε να προχωρήσετε, μπορείτε να βρείτε τις λύσεις των περισσότερων ασκήσεων στο τέλος της κάθε άσκησης.

## Τι πρέπει να γνωρίζω

Τα παραδείγματα που γράφτηκαν αναπτύχθηκαν στην έκδοση **3.8.2** της Python και σε περιβάλλον **Windows**. Πιο γενικά, η Python μπορεί να χρησιμοποιηθεί για πολλούς σκοπούς και σε διάφορες περιοχές ενδιαφέροντος. Η Python έχει την δυνατότητα να τρέξει στις περισσότερες πλατφόρμες υλικού υπολογιστών και Λειτουργικών Συστημάτων (OS), όπως για παράδειγμα Windows, Linux και Mac. Διαθέτει πάρα πολλές βιβλιοθήκες που μπορούν να χρησιμοποιηθούν εύκολα και άμεσα. Μπορεί να δημιουργήσει και ένας προγραμματιστής δικές του βιβλιοθήκες, ώστε να τις χρησιμοποιεί κατάλληλα σε διαφορετικά προγράμματά του, αποφεύγοντας να γράφει, κάθε φορά, κώδικα από την αρχή. Τα προγράμματα σε Python είναι ευανάγνωστα και γράφονται γρηγορότερα σε σχέση με άλλες γλώσσες προγραμματισμού όπως οι C, C++ και Java.

## Γιατί επιλέξαμε να μάθουμε την γλώσσα Python

Η Python είναι μια εξαιρετικά αποδοτική γλώσσα. Αυτό σημαίνει ότι τα προγράμματα που θα γράψουμε στη συνέχεια θα μπορούν να κάνουν περισσότερα σε λιγότερες γραμμές κώδικα από άλλες γλώσσες προγραμματισμού.

Για παράδειγμα στη **Python** εαν θέλουμε να εμφανίσουμε στην οθόνη ένα κείμενο `Hello World!` θα γράψουμε:

```python
print("Hello World!")
```

Ενώ στη γλώσσα **C** θα πρέπει να γράψουμε:

```c
#include <stdio.h>

int main(){
    printf("Hello World!");
    return 0;
}
```

Η σύνταξη της Python μας βοηθάει να γράψουμε έναν "καθαρό" κώδικα. Ο κώδικας είναι σε πολύ μεγάλο βαθμό ευανάγνωστος, με εύκολη αποσφαλμάτωση και εύκολη επέκταση και ανάπτυξη σε σύγκριση με άλλες γλώσσες.

Έχουμε επιλέξει την Python για να μάθουμε προγραμματισμό διότι είναι:

- Γλώσσα ανοικτού κώδικα (διαθέσιμη στη διεύθυνση [http://python.org](http://python.org)).
- Γενικής χρήσης, υψηλού επιπέδου γλώσσα προγραμματισμού.
- Απλό συντακτικό, εξαιρετική αναγνωσιμότητα.
- Με σημαντικές δυνατότητες προς διάφορες κατευθύνσεις (ισχυρή γλώσσα προγραμματισμού).
- Κατάλληλη για αρχάριους και για έμπειρους προγραμματιστές.
- Αντικειμενοστραφής.
- Υπάρχουν αρκετά πακέτα υποστήριξης (βιβλιοθήκες).

## Μαθησιακά Αποτελέσματα

Μετά την ολοκλήρωση των μαθημάτων οι φοιτητές/τριες θα είναι σε θέση να:

- γνωρίζουν τις βασικές αρχές του διαδικασιακού, δομημένου προγραμματισμού και τον τρόπο εφαρμογής τους.
- κατανοούν τη σημασία της αλγοριθμικής λογικής και τον τρόπο εφαρμογής της στην επίλυση απλών και σύνθετων αλγοριθμικών προβλημάτων.
- κατανοούν το συντακτικό και τον τρόπο λειτουργίας των εντολών που χρησιμοποιούνται στη γλώσσα προγραμματισμού Python.
- γνωρίζουν το προγραμματιστικό περιβάλλον της Python, τον τρόπο συγγραφής διόρθωσης και εκτέλεσης προγραμμάτων.
- δημιουργούν προγράμματα με τη γλώσσα προγραμματισμού Python εφαρμόζοντας τις
αρχές του διαδικασιακού προγραμματισμού, για την υλοποίηση λύσεων σε αλγοριθμικά προβλήματα.

## Γενικές Ικανότητες

- Αναζήτηση, ανάλυση και σύνθεση δεδομένων και πληροφοριών, με τη χρήση και των απαραίτητων τεχνολογιών.
- Εργασία σε διεπιστημονικό περιβάλλον.
- Προαγωγή της ελεύθερης, δημιουργικής και επαγωγικής σκέψης.
- Μετάδοση και μεταφορά τεχνογνωσίας σε άλλα περιβάλλοντα.

Το μάθημα περιλαμβάνει τη διδασκαλία σε:

- γενικές αρχές σχεδίασης προγραμμάτων
- αλγόριθμοι
- λογικά διαγράμματα ροής
- τεχνικές σχεδιασμού αλγορίθμου
- επίλυση αλγοριθμικών προβλημάτων

Λέξεις κλειδιά:

- Μεταβλητές
- Σταθερές
- Εκφράσεις
- Βασικοί τύποι δεδομένων
- Προτάσεις
- Τελεστές
- Είσοδος/έξοδος δεδομένων
- Εντολές ελέγχου ροής
- Επαναλήψεις
- Λίστες
- Υποπρογράμματα

## Διαλέξεις

Εδώ περιλαμβάνονται τα βασικότερα σημεία που παρουσιάστηκαν κατά την διάρκεια των διαλέξεων του μαθήματος και ως εκ τούτου αποτελεί ένα βοήθημα μελέτης για την προετοιμασία των φοιτητών εν όψει της τελικής εξέτασης. Η εξεταστέα ύλη καλύπτεται πλήρως από το υλικό που περιλαμβάνεται εδώ.

- [1 Βασικές έννοιες](lectures/lecture_01.md)
- [2 Τύποι μεταβλητών - Απλές εντολές](lectures/lecture_02.md)
  - [2.1 Λυμένα Παραδείγματα](examples/examples_02.md)
- [3 Εντολή επιλογής](lectures/lecture_03.md)
  - [3.1 Λυμένα Παραδείγματα](examples/examples_03.md)
  - [3.2 Ασκήσεις](exercises/exercises_03.md)
- [4 Δομή πολλαπλής επιλογής / Μη-προκαθορισμένες επαναλήψεις - while](lectures/lecture_04.md)
  - [4.1 Λυμένα Παραδείγματα](examples/examples_04.md)
  - [4.2 Ασκήσεις](exercises/exercises_04.md)
- [5 Εισαγωγή στις Λίστες](lectures/lecture_05.md)
  - [5.1 Λυμένα Παραδείγματα](examples/examples_05.md)
  - [5.2 Ασκήσεις](exercises/exercises_05.md)
- [6 Δομή Επανάληψης - Η εντολή for](lectures/lecture_06.md)
  - [6.1 Λυμένα Παραδείγματα](examples/examples_06.md)
  - [6.2 Ασκήσεις](exercises/exercises_06.md)
- [7. Μονοδιάστατες Λίστες - Αναζήτηση - Ταξινόμηση](lectures/lecture_07.md)
  - [7.1 Λυμένα Παραδείγματα](examples/examples_07.md)
  - [7.2 Ασκήσεις](exercises/exercises_07.md)
- [8 Δομές Δεδομένων - Πολυδιάστατες Λίστες](lectures/lecture_08.md)
  - [8.1 Λυμένα Παραδείγματα](examples/examples_08.md)
  - [8.2 Ασκήσεις](exercises/exercises_08.md)
- [9 Υποπρογράμματα](lectures/lecture_09.md)
  - [9.1 Λυμένα Παραδείγματα](examples/examples_09.md)
  - [9.2 Ασκήσεις](exercises/exercises_09.md)

## Εργαστήρια

Τα εργαστήρια αφορούν στη πρακτική εφαρμογή όσων διδάσκονται στις διαλέξεις.

- [Εισαγωγή στην Python - Βασικές έννοιες](labs/lab_01.md)
- [Βασικές εντολές](labs/lab_02.md)
- [Εντολές επιλογής](labs/lab_03.md)
- [Εντολή επιλογής - επανάληψης](labs/lab_04.md)
- [Λίστες](labs/lab_05.md)
- [Δομή Επανάληψης - Η εντολή for 1](labs/lab_06.md)
- [Εντολή επανάληψης - Λίστες](labs/lab_07.md)
- [Αναζήτηση - Ταξινόμηση σε Λίστα](labs/lab_08.md)
- [Δομές Δεδομένων - Πολυδιάστατες Λίστες](labs/lab_09.md)
- [Υποπρογράμματα](labs/lab_10.md)

## Κουίζ

Στην ενότητα Κουίζ θα βρείτε τεστ πολλαπλής απάντησης με ερωτήσεις επάνω στις βασικές έννοιες που έχετε διδαχθεί. Είναι ένας τρόπος να καταλάβετε αν έχετε κατανοήσει πλήρως τις διαλέξεις. Αφιερώστε χρόνο για να τα κάνετε. Αν έχετε κάνει λάθη να τα επαναλάβετε όσες φορές χρειαστεί μέχρι να πάρετε ένα υψηλό ποσοστό! Αυτά τα Κουίζ, πέρα του ότι θα σας βοηθήσουν αφάνταστα για να κατανοήσετε ότι διδάσκεστε, θα αποτελέσουν τη βάση των περισσότερων ερωτήσεων στις εξέτάσεις, αλλά και σε μια πρόοδο που ίσως κληθείτε να δώσετε.

- [Βασικές έννοιες](https://forms.gle/KDL7dgS5xqitsSKb7)
- [Τύποι μεταβλητών - Απλές εντολές](https://forms.gle/DnMXaDK4GG7KDZo49)
- [Η εντολή επιλογής if - Λογικές παραστάσεις](https://forms.gle/RZUFRsUiPdPFRjkW9)
- [Η εντολή επανάληψης while](https://forms.gle/CbPtBfprGQ9LPgqg7)
- [Λίστες 1](https://forms.gle/tiiPPRpcML3BaRhYA)
- [Λίστες 2](https://forms.gle/4dxdY98kRxBN5JTa7)
- [Λίστες 3](https://forms.gle/JS7prqxCapoWE3vS9)
- [Η εντολή επανάληψης for 1](https://forms.gle/JWpCTGXkEqZ9kWCcA)
- [Η εντολή επανάληψης for 2](https://forms.gle/HSvRsCtJPXBA8EWm8)
- [Ταξινόμηση σε Λίστα](https://forms.gle/EW827grJZb1hkq9C7)
- [Υποπρογράμματα 1](https://forms.gle/zM7QFk66ZA9W376p7)
- [Υποπρογράμματα 2](https://forms.gle/TcerN71VjnGjbV6fA)

## Επιπλέον ασκήσεις για λύση και εξάσκηση

- [Μεταβλητές και εκχώρηση τιμής](more/docs/variables.md)
- [Η εντολή if](more/docs/if_exercises.md)
- [Η εντολή while](more/docs/while_exercises.md)

## Βιβλιογραφία

- [Εισαγωγή στον προγραμματισμό με την Python](http://aggelid.mysch.gr/pythonbook/INTRODUCTION_TO_COMPUTER_PROGRAMMING_WITH_PYTHON.pdf). (ΝΙΚΟΛΑΟΣ Α. ΑΓΓΕΛΙΔΑΚΗΣ).
- [Περίγραμμα μαθήματος](http://www.ct.aegean.gr/Home/Proptyxiako) από τα μαθήματα εξαμήνων του τμήματος ΤΠΤΕ (Α΄ Έτος 1ο Εξάμηνο).
- Διαλέξεις και εργαστήρια του κ. Καλλονιάτη και κ. Σίμου.
- [Βιβλίο Προγραμματισμoύ Υπολογιστών Γ ́Τάξης ΕΠΑ.Λ.](http://users.sch.gr/iliadisk/site/PDFs/24-0576-01_Programmatismos-Ypologiston_C-EPAL_BM.pdf)
- [Πληροφορική Α΄, Β΄, Γ΄ Γυμνασίου](http://ebooks.edu.gr/ebooks/v/html/8547/2759/Pliroforiki_A-B-G-Gymnasiou_html-empl/index.html)
- [Πληροφορική στο ΕΠΑ.Λ.](https://sites.google.com/view/pliroforikiepal/home)
- [Σταύρος Κομηνέας, Πανεπιστήμιο Κρήτης](http://users.tem.uoc.gr/~komineas/python-course/Lectures/index.html)
- [Strephonsays](https://el.strephonsays.com/difference-between-translator-and-interpreter-in-programming-language)
- [Εισαγωγή στον Προγραμματισμό - Στέφανος Ουγιάρογλου](https://people.iee.ihu.gr/~stoug/themata/aeppkef6.pdf)
- [Τμήμα Μηχανολόγων Μηχανικών / Ελληνικό Μεσογειακό Πανεπιστήμιο](https://mech.hmu.gr/proptyxiakes/katanomh-mathhmatwn-eksamhno/plhrophorikh/)
- [Repl.it / Αθανάσιος Μουρτζούκος](https://msc.cs.uowm.gr)
