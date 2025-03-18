#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>
#include <unistd.h>

bool flag[2] = {false, false}; // Indicates if process wants to enter critical section
int turn = 0;                  // Indicates whose turn it is to enter critical section

void *process0(void *arg)
{
    while (1)
    {
        flag[0] = true;
        turn = 1;
        while (flag[1] && turn == 1)
        {
        } // Wait if process 1 wants to enter

        // Critical section
        printf("Process 0 is in the critical section.\n");
        sleep(1);
        printf("Process 0 is leaving the critical section.\n");

        flag[0] = false; // Exit critical section

        // Remainder section
        printf("Process 0 is in the remainder section.\n");
        sleep(1);
    }
}

void *process1(void *arg)
{
    while (1)
    {
        flag[1] = true;
        turn = 0;
        while (flag[0] && turn == 0)
        {
        } // Wait if process 0 wants to enter

        // Critical section
        printf("Process 1 is in the critical section.\n");
        sleep(1);
        printf("Process 1 is leaving the critical section.\n");

        flag[1] = false; // Exit critical section

        // Remainder section
        printf("Process 1 is in the remainder section.\n");
        sleep(1);
    }
}

int main()
{
    pthread_t t0, t1;

    // Create threads representing process 0 and process 1
    pthread_create(&t0, NULL, process0, NULL);
    pthread_create(&t1, NULL, process1, NULL);

    // Wait for threads to finish
    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    return 0;
}
