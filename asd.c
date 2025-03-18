#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>
#include <unistd.h>

bool turn = true; 
void *process0(void *arg)
{
    while (1)
    {
        
        while (!turn)
            ;

   
        printf("Process 0 is in the critical section.\n");
        sleep(1); 
        printf("Process 0 is leaving the critical section.\n");

        
        turn = false;

       
        printf("Process 0 is in the remainder section.\n");
        sleep(1); 
    }
}

void *process1(void *arg)
{
    while (1)
    {
        // Wait for Process 1's turn
        while (turn)
            ;

   
        printf("Process 1 is in the critical section.\n");
        sleep(1); 
        printf("Process 1 is leaving the critical section.\n");

        turn = true;

        printf("Process 1 is in the remainder section.\n");
        sleep(1); 
    }
}

int main()
{
    pthread_t t0, t1;


    pthread_create(&t0, NULL, process0, NULL);
    pthread_create(&t1, NULL, process1, NULL);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    return 0;
}