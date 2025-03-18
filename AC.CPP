#include <iostream>
#include <iomanip> // For formatting output
using namespace std;

// Structure to represent a process
struct Process
{
    char id;        // Process ID
    int arrival;    // Arrival time
    int burst;      // Burst time
    int waiting;    // Waiting time
    int turnaround; // Turnaround time
    bool completed; // Whether process is completed
};

// Function to calculate the response ratio
double calculateResponseRatio(int waitingTime, int burstTime)
{
    return (double)(waitingTime + burstTime) / burstTime;
}

// Function to find the next process to execute based on HRRN
int findNextProcess(Process proc[], int n, int currentTime)
{
    int index = -1;
    double maxRR = -1.0; // Max response ratio

    for (int i = 0; i < n; i++)
    {
        if (!proc[i].completed && proc[i].arrival <= currentTime)
        {
            int waitingTime = currentTime - proc[i].arrival;
            double rr = calculateResponseRatio(waitingTime, proc[i].burst);
            if (rr > maxRR)
            {
                maxRR = rr;
                index = i;
            }
        }
    }

    return index;
}

// Function to implement HRRN and calculate waiting and turnaround times
void HRRN(Process proc[], int n)
{
    int currentTime = 0;
    int completedProcesses = 0;

    // Loop until all processes are completed
    while (completedProcesses < n)
    {
        int index = findNextProcess(proc, n, currentTime);

        if (index != -1)
        {
            // Execute the process with the highest response ratio
            proc[index].waiting = currentTime - proc[index].arrival;
            proc[index].turnaround = proc[index].waiting + proc[index].burst;
            currentTime += proc[index].burst;
            proc[index].completed = true;
            completedProcesses++;
        }
        else
        {
            currentTime++;
        }
    }
}

// Function to calculate average waiting and turnaround times
void calculateAverageTimes(Process proc[], int n)
{
    int totalWaitingTime = 0, totalTurnaroundTime = 0;

    cout << "\nProcesses    Arrival Time    Burst Time    Waiting Time    Turnaround Time\n";
    for (int i = 0; i < n; i++)
    {
        totalWaitingTime += proc[i].waiting;
        totalTurnaroundTime += proc[i].turnaround;
        cout << "  " << proc[i].id << "\t\t" << proc[i].arrival << "\t\t" << proc[i].burst << "\t\t"
             << proc[i].waiting << "\t\t" << proc[i].turnaround << endl;
    }

    cout << fixed << setprecision(2);
    cout << "\nAverage waiting time = " << (double)totalWaitingTime / n << endl;
    cout << "Average turnaround time = " << (double)totalTurnaroundTime / n << endl;
}

// Driver code
int main()
{
    int n;

    cout << "Enter the number of processes: ";
    cin >> n;

    Process proc[n]; // Array of processes

    // Input for each process
    for (int i = 0; i < n; i++)
    {
        proc[i].id = 'A' + i; // Assign process ID starting from 'A'
        cout << "Enter arrival time for process " << proc[i].id << ": ";
        cin >> proc[i].arrival;
        cout << "Enter burst time for process " << proc[i].id << ": ";
        cin >> proc[i].burst;
        proc[i].waiting = 0;
        proc[i].turnaround = 0;
        proc[i].completed = false;
    }
    // Perform HRRN scheduling
    HRRN(proc, n);

    // Calculate and display average waiting and turnaround times
    calculateAverageTimes(proc, n);

    return 0;
}
