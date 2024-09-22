#include <stdio.h>
#include <conio.h>
#include <dos.h>
#include <time.h>

void main() 
{
    int cs = 0, pro = 0;
    double run = 5.0;
    char key = 'a';
    time_t t1, t2;

    clrscr();
    printf("Press a key (except q) to enter a process: ");
    printf("\nPress q at any time to exit\n");

    t1 = time(NULL) - 5;  

    while (key != 'q') 
    {
        if (kbhit()) 
        {
            key = getch();
            if (key != 'q') 
            {
                if (cs != 0) 
                {
                    t2 = time(NULL);
                    if (difftime(t2, t1) > run) 
                    {
                        printf("Process %d ", pro - 1);
                        printf("exited critical section.\n");
                        cs = 0;
                    }
                }
                
                if (cs == 0) 
                {
                    printf("Process %d ", pro);
                    printf("entered critical section.\n");
                    cs = 1;
                    pro++;
                    t1 = time(NULL);
                } 
                else 
                {
                    printf("Error: Another process is currently executing!\n");
                }
            }
        }
    }
}
