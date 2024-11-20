### 1. **RTOS Techniques**
The implementation incorporates various RTOS-related techniques, such as:

#### **1.1 Priority Inversion and Inheritance**
- **Priority Inversion**: A lower-priority task might block a higher-priority task due to resource contention (e.g., shared lock).
  
- **Priority Inheritance Protocol**: Implemented in the `execute_task()` method of `RTScheduler`. When acquiring a lock (`mutex`), the protocol temporarily raises the priority of the locking task, preventing higher-priority tasks from being starved

#### **1.2 Locking Mechanisms**
- **Thread-safe Locks**: The `threading.Lock()` ensures tasks are added and executed safely in the `task_queue`.
  
- This prevents race conditions when accessing shared data, such as the task queue or logging structures.

#### **1.3 Priority Ceiling Protocol**
- the `execute_task()` function prevents blocking by using a **pre-defined ceiling priority** when scheduling and executing tasks under lock.

---

### 2. **Scheduling Algorithms**
- Implements three common **real-time scheduling algorithms**:

#### **2.1 Earliest Deadline First (EDF)**
- Tasks are prioritized by their deadlines. The task with the earliest deadline is executed first.

#### **2.2 Rate Monotonic Scheduling (RMS)**
- Tasks with shorter periods (higher frequency) are given higher priority.

#### **2.3 Deadline Monotonic Scheduling (DMS)**
- Tasks are prioritized solely by their deadlines, regardless of when they are added.

---

### 3. **SchedulerAPI Class**
The `SchedulerAPI` class provides a centralized interface to manage and switch between schedulers dynamically:
- **Purpose**:
  - Acts as a container for different schedulers (`EDF`, `RMS`, `DMS`).
  - Supports dynamic scheduler switching at runtime.
- **Key Methods**:
  - `add_scheduler(name, scheduler)`: Adds schedulers to the API.
  - `switch_scheduler(name)`: Switches to a specific scheduler.

---

### 4. **`manage_scheduling()` Function**
This function implements dynamic scheduler switching based on system performance metrics (e.g., CPU utilization, task wait time, missed deadlines):
- **Key Metrics**:
  - **CPU Utilization**: Simulates real-time CPU usage.
  - **Task Wait Time**: Simulates average task wait time.
  - **Missed Deadlines**: Tracks cumulative missed deadlines from all schedulers.
- **Decision Logic**:
  - Switch to EDF for high missed deadlines or task wait times.
  - Switch to RMS for high CPU utilization or queue size.
  - Default to DMS otherwise.
- **Execution**:
  - Logs decisions and metrics periodically.
  - Executes the chosen scheduler’s tasks.

---


### 5. **Flow of Execution**

1. **Initialization**:
   - Create scheduler instances (`EDF`, `RMS`, `DMS`) and add them to the `SchedulerAPI`.
   - Define tasks and their parameters.

2. **Task Addition**:
   - Add tasks to the appropriate scheduler.

3. **Dynamic Scheduler Switching**:
   - The `manage_scheduling()` function evaluates real-time metrics periodically (every second) and switches between schedulers as needed.

4. **Task Execution**:
   - The selected scheduler executes tasks in priority order, handling locks and deadlines.

5. **Logging and Monitoring**:
   - Logs CPU utilization, missed deadlines, and task executions for analysis and visualization.

6. **Visualization**:
   - Uses `panel` and `hvplot` to display real-time metrics and task execution progress.

---

### 6. **Core Logic**
- Tasks are managed using a **priority queue** to ensure high-priority tasks are executed first.
- Each scheduler overrides the `add_task` method to define its unique priority calculation logic.
- Dynamic switching between schedulers ensures optimal task handling based on real-time system conditions.

---

### 7. **RTOS Techniques**
- **Priority Inversion Mitigation**: Handled using locks and priority inheritance.
- **Dynamic Scheduler Switching**: Ensures adaptability to changing conditions.
- **Preemptive Scheduling**: Implicitly managed via dynamic priority queues.
