#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

bool isBinary(const char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] != '0' && str[i] != '1') {
            return false;
        }
    }
    return true;
}

int sumBinary(int number, int number2, bool c2)
{
  // conversion and format
  char str1[9];
  sprintf(str1, "%08d", number);
  char str2[9];
  sprintf(str2, "%08d", number2);
  char result[9];


  if ((sizeof(str1) == 8 && sizeof(str2) == 8) && (isBinary(str1) && isBinary(str2)))
  {
    int temp = 0;
    // principal code
    for (int i = 0; i < sizeof(str1); i++) {
      // case 1 -> 1 + 1 +1
      if (str1[i] == '1' && str2[i] == '1' && temp == 1) {
        temp = 1;
        result[8 - i] = '1';
      }
      // case 2 -> 0 + 1 + 1
      else if ((str1[i] == '0' && str2[i] == '1' && temp == 1) || (str1[i] == '1' && str2[i] == '0' && temp == 1)) {
        temp = 1;
        result[8 - i] = '0';
      }
      // case 3 -> 0 + 0 + 1
      else if ((str1[i] == '0' && str2[i] == '1' && temp == 0) || (str1[i] == '1' && str2[i] == '0' && temp == 0)) {
        temp = 0;
        result[8 - i] = '1';
      }
    }
    return result;
  }
  else
  {
    raise("Error: the numbers must be 8 bits long and binary");
  }
}

int subtractbinary(int number, int number2, int c) {
  char str[20];
  sprintf(str, "%d", number2); // conversion
  if (c == 1) {
    for (int i = 0; i < sizeof(str); i++) {
      if (str[i] == '1')
        str[i] = '0';
      else if (str[i] == '0')
        str[i] = '1';
    }
    // return sumBinary(number, (int)str, false); // RETURN  
  }

  else if (c == 2) {
    char newstr[20];
    // CONTINUE HERE
    for (int i = 0; i < sizeof(str); i++) {
      if (str[i] == '1')
        str[i] = '0';
      else if (str[i] == '0')
        str[i] = '1';
    }
    // newstr = sumBinary(number, 1, true);
    // return sumBinary(number, (int)newstr, false);
  }
}

int tobase(int number, int base) {
  // variables
  int rest[8];
  int j = 0;
  char result[20];

  // picking the rest of the division by 2
  while (number > base) {
    // rest
    rest[j] = number % base;
    // division
    number /= base;
    j++;
    if (number == 1) {
      rest[j] += number;
    }
  }
  // building the binary number
  for (int i = 0; i < sizeof(rest); i++) {
    result[i] = (char)rest[sizeof(rest) - i];
  }
  return result;
}

int toBinary(int number) {
  // variables
  int rest[8];
  int j = 0;
  char result[20];

  // picking the rest of the division by 2
  while (number > 2) {
    // rest
    rest[j] = number % 2;
    // division
    number /= 2;
    j++;
    if (number == 1) {
      rest[j] += number;
    }
  }
  // building the binary number
  for (int i = 0; i < sizeof(rest); i++) {
    result[i] = (char)rest[sizeof(rest) - i];
  }
  return result;
}

int convertBase(int number, int base, int baseto) {
  char str[20]; // buffer

  // convert int to string
  sprintf(str, "%d", number);

  int result = 0;

  if (baseto == 2) // binary
  {
    return toBinary(number);
  } else if (baseto == 10) // decimal
  {
    for (int i = 0; i < sizeof(number); i++) {
      result += (char)((int)str[i] * base ^ sizeof(number) - i - 1); // CHANGE THIS
    }
  } else if (base == 10) // decimal to other base
  {
    return tobase(number, baseto);
  }
  else if (baseto == 16)
  {
    char hexadecimal[20];
    result = tobase(number, baseto);
    sprintf(hexadecimal, "%x", result);
    result = (int)hexadecimal;
    return result; // RETURN
  } 
  else {
    for (int i = 0; i < sizeof(number); i++) {
      result += (char)((int)str[i] * base ^ sizeof(number) - i - 1); // CHANGE THIS
    }
    return result;
  }
  return result;
}

/* 
---
---
---
  This is the program space to test the functions and to make programs
---
---
---
*/

// HERE IS WHERE THE PROGRAM STARTS
int main(void)
{
  printf("CODE STARTED\n");
  printf("Hello, my friends!!!!\n");
  return 0; 
}