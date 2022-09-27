#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
 
int main()
{
 
  int var;
  int check = 0x10203040;
  char buf[40];
 
  fgets(buf,45,stdin);
 
  printf("\n[buf]: %s\n", buf);
  printf("[check] %p\n", check);
 
  if ((check != 0x10203040) && (check != 0xf4c3b00c))
    printf ("\nClooosse!\n");
 
  if (check == 0xf4c3b00c)
   {
     printf("Yeah!! You win!\n");
     setreuid(geteuid(), geteuid());
     system("/bin/bash");
     printf("Byee!\n");
   }
   return 0;
}

