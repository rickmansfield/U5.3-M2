# Unit 5.3 M2 Queues and Stacks 
## [Video Link]()
## [CoLab Link](https://colab.research.google.com/drive/1eyRKNZI5CMlZXCdZQITCSwRebeXDyIms?usp=sharing)


Queues and Stacks
Stack is a LIFO Data Structure
Queue is a FIFO Data Structure
Queue is used when things don’t have to be processed immediately, but have to be processed in First In First Out order like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.

1. When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
2. When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.
3. In Operating systems:
    ```
     - Semaphores
     - FCFS ( first come first serve) scheduling, example: FIFO queue
     - Spooling in printers
     - Buffer for devices like keyboard
    ```
4. In Networks:
    ```
    - Queues in routers/ switches 
    - Mail Queues
    ```
5. Variations: ( Deque, Priority Queue, Doubly Ended Priority Queue )

Real life examples of stack are:

- To reverse a word. You push a given word to stack - letter by letter - and then pop letters from the stack.
- An "undo" mechanism in text editors; this operation is accomplished by keeping all text changes in a stack.Undo/Redo stacks in Excel or Word.
- Language processing :space for parameters and local variables is created internally using a stack.compiler's syntax check for matching braces is implemented by using stack.
- A stack of plates/books in a cupboard.
- Wearing/Removing Bangles.
- Support for recursion
- Activation records of method calls.