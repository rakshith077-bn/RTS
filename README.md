# Real-Time Scheduler Framework
The Real-Time Scheduler Framework is designed to simulate real-time operating system (RTOS) behaviors, such as task prioritization, dynamic scheduler switching.

- Current commit supports **EDF**, **RMS**, and **DMS**, with dynamic switching.
- project works fine but present issues in execute_tasks(). 

## Why's
Managing concurrent tasks with strict timing constraints is a core challenge in real-time systems. This provides:
- A modular and extensible framework for implementing and testing scheduling strategies.
- Real-time monitoring and decision-making capabilities based on system metrics like CPU utilization and task deadlines.
- A visualization tool for analyzing scheduler performance and task execution in real time.

## **Features**
- Check `work_flow.md`: documents the RTOS techniques, algorithms implemented.

- Check `classDefined.md`: documents the program flow.

- **Dynamic Scheduler Switching:**
  - Switches schedulers based on real-time metrics like CPU utilization, task wait time, and missed deadlines.

- **Visualization:**
  - visualization achived with `panel` and `hvplot`.
 
## Present Issues
- **`execute_tasks()` Limitations:**
  - Tasks may experience delays under heavy loads which might be due to Python's Global Interpreter Lock (GIL).
  - Priority inheritance implementation might not cover edge cases where multiple high-priority tasks depend on the same lock.

## **Further updates:**
  - general fixes
  - enhanced decision-making logic for scheduler switching.
  - improved decision processing for scheduler switching and dynamic resource lock.
