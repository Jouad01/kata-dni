# Kata DNI

#### **Kata for practice the SOLID principles as SRP, OCP and LSP**

- **Single Responsibility Principle (SRP)** defens a class only have a motive to change.

- **Open/Closed Principle (OCP)** defense that  pieces of software has to be open to extension and closed to modification.

- **Liskov Substitution Principle (LSP)** defens the objects can be change for instances of his object type without changing behaviour of the programm.

Write a program that given a DNI number return the NIF letter. The letter in DNI number its calculated by the following algorithm:

* Get the remaining by dividing the ID number by 23
* The resulting number aims to the position in the follow table:



| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22 |      
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---|
| T   | R   | W   | A   | G   | M   | Y   | F   | P   | D   | X   | B   | N   | J   | Z   | S   | Q   | V   | H   | L   | C   | K   | K  |




- **'I', 'Ñ', 'O' and 'U' are no used letter.** 
- **'I' and 'O' letter are not used because of the possibility of generate confusion with other characters as 1, l and .**