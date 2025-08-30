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
  static char result[9];


  if ((strlen(str1) == 8 && strlen(str2) == 8) && (isBinary(str1) && isBinary(str2)))
  {
    int temp = 0;
    // principal code
    for (int i = 0; i < 8; i++) {
      // case 1 -> 1 + 1 +1
      if (str1[i] == '1' && str2[i] == '1' && temp == 1) {
        temp = 1;
        result[8 - i - 1] = '1';
      }
      // case 2 -> 0 + 1 + 1
      else if ((str1[i] == '0' && str2[i] == '1' && temp == 1) || (str1[i] == '1' && str2[i] == '0' && temp == 1)) {
        temp = 1;
        result[8 - i - 1] = '0';
      }
      // case 3 -> 0 + 0 + 1
      else if ((str1[i] == '0' && str2[i] == '1' && temp == 0) || (str1[i] == '1' && str2[i] == '0' && temp == 0)) {
        temp = 0;
        result[8 - i - 1] = '1';
      }
      else if (str1[i] == '0' && str2[i] == '0' && temp == 1) {
        temp = 0;
        result[8 - i - 1] = '1';
      }
      else if (str1[i] == '0' && str2[i] == '0' && temp == 0) {
        temp = 0;
        result[8 - i - 1] = '0';
      }
      else if (str1[i] == '1' && str2[i] == '1' && temp == 0) {
        temp = 1;
        result[8 - i - 1] = '0';
      }
    }
    result[8] = '\0';
    return atoi(result);
  }
  else
  {
    printf("Error: the numbers must be 8 bits long and binary\n");
    return -1;
  }
}

int subtractbinary(int number, int number2, int c) {
  char str[9];
  sprintf(str, "%08d", number2); // conversion
  
  if (c == 1) {
    for (int i = 0; i < 8; i++) {
      if (str[i] == '1')
        str[i] = '0';
      else if (str[i] == '0')
        str[i] = '1';
    }
    int inverted = atoi(str);
    return sumBinary(number, inverted, false);
  }

  else if (c == 2) {
    char newstr[9];
    sprintf(newstr, "%08d", number2);
    
    for (int i = 0; i < 8; i++) {
      if (newstr[i] == '1')
        newstr[i] = '0';
      else if (newstr[i] == '0')
        newstr[i] = '1';
    }
    
    int inverted = atoi(newstr);
    int with_one = sumBinary(inverted, 1, false);
    return sumBinary(number, with_one, false);
  }
  return -1;
}

int tobase(int number, int base) {
  // variables
  int rest[32];
  int j = 0;
  static char result[33];

  if (number == 0) {
    strcpy(result, "0");
    return atoi(result);
  }

  // picking the rest of the division
  while (number > 0) {
    rest[j] = number % base;
    number /= base;
    j++;
  }
  
  // building the number in the target base
  for (int i = 0; i < j; i++) {
    int digit = rest[j - 1 - i];
    if (digit < 10) {
      result[i] = '0' + digit;
    } else {
      result[i] = 'A' + digit - 10;
    }
  }
  result[j] = '\0';
  return atoi(result);
}

int toBinary(int number) {
  // variables
  int rest[32];
  int j = 0;
  static char result[33];

  if (number == 0) {
    strcpy(result, "0");
    return atoi(result);
  }

  // picking the rest of the division by 2
  while (number > 0) {
    rest[j] = number % 2;
    number /= 2;
    j++;
  }
  
  // building the binary number
  for (int i = 0; i < j; i++) {
    result[i] = rest[j - 1 - i] + '0';
  }
  result[j] = '\0';
  return atoi(result);
}

int convertBase(int number, int base, int baseto) {
  if (baseto == 2) // binary
  {
    return toBinary(number);
  } else if (baseto == 10) // to decimal
  {
    int decimal = 0;
    int power = 1;
    
    while (number > 0) {
      int digit = number % 10;
      decimal += digit * power;
      power *= base;
      number /= 10;
    }
    return decimal;
  } else if (base == 10) // decimal to other base
  {
    return tobase(number, baseto);
  }
  else if (baseto == 16) // to hexadecimal
  {
    return tobase(number, baseto);
  } 
  else {
    // For other base conversions, use intermediate decimal
    int decimal = 0;
    int power = 1;
    
    while (number > 0) {
      int digit = number % 10;
      decimal += digit * power;
      power *= base;
      number /= 10;
    }
    
    return tobase(decimal, baseto);
  }
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