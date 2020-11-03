#include <stdio.h>  // FILE, printf
#include <limits.h> // CHAR_BIT

int main()
{
  FILE *f;
  char c;
  int i;
  int j;

  j = 1;
  i = 0;
  c = 0;
  f = fopen("ascii_uart.raw", "r");
  if (f)
  {
    // Read each char of FILE
    while ((c = fgetc(f)) != EOF)
    {
      // Read each bit of char
      for (i = 0; i < CHAR_BIT; i++)
      {
        if (j == 10)
        {
          printf("\n");
          j = 1;
        }
        if (j > 1 && j < 10)
        {
          printf("%d", (c >> i) & 1);
        }
        j++;
      }
    }
    // printf("\n");
  }

  return 0;
}
