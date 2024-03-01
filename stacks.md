# 7.1 INTRODUCTION

Stack is an important data structure which stores its elements in an ordered manner. We will explain the concept of stacks using an analogy. You must have seen a pile of plates where one plate is placed on top of another. Now, when you want to remove a plate, you remove the topmost plate first. Hence, you can add and remove an element (i.e., a plate) only at/from one position which is the topmost position.

A stack is a linear data structure which uses the same principle, i.e., the elements in a stack are added and removed only from one end, which is called the **TOP**. Hence, a stack is called a LIFO (Last-In-First-Out) data structure, as the element that was inserted last is the first one to be taken out.

Now the question is where do we need stacks in computer science? The answer is in function calls. Consider an example, where we are executing function A. In the course of its execution, function A calls another function B. Function B in turn calls another function C, which calls function D.

When A calls B, A is pushed on top of the system stack. When the execution of B is complete, the system control will remove A from the stack and continue with its execution.

When C calls D, C is pushed on top of the system stack. When the execution of D is complete, the system control will remove C from the stack and continue with its execution.

When D calls E, D is pushed on top of the system stack. When the execution of E is complete, the system control will remove D from the stack and continue with its execution.

When B calls C, B is pushed on top of the system stack. When the execution of C is complete, the system control will remove B from the stack and continue with its execution.

In order to keep track of the returning point of each active function, a special stack called system stack or call stack is used. Whenever a function calls another function, the calling function is pushed onto the top of the stack. This is because after the called function gets executed, the control is passed back to the calling function.

Now when function E is executed, function D will be removed from the top of the stack and executed. Once function D gets completely executed, function C will be removed from the stack for execution. The whole procedure will be repeated until all the functions get executed.

The system stack ensures a proper execution order of functions. Therefore, stacks are frequently used in situations where the order of processing is very important, especially when the processing needs to be postponed until other conditions are fulfilled.

Stacks can be implemented using either arrays or linked lists.


# 7.2 ARRAY REPRESENTATION OF STACKS

In the computer’s memory, stacks can be represented as a linear array. Every stack has a variable called `TOP` associated with it, which is used to store the address of the topmost element of the stack. It is this position where the element will be added to or deleted from. There is another variable called `MAX`, which is used to store the maximum number of elements that the stack can hold. If `TOP = NULL`, then it indicates that the stack is empty and if `TOP = MAX – 1`, then the stack is full. (You must be wondering why we have written `MAX – 1`. It is because array indices start from 0.)

The stack in a linear array representation means that insertions and deletions are done at the topmost position of the array.


# 7.3 OPERATIONS ON A STACK

A stack supports three basic operations: push, pop, and peek. 

## 7.3.1 Push Operation

The push operation is used to insert an element into the stack. The new element is added at the topmost position of the stack. However, before inserting the value, we must first check if `TOP = MAX – 1`, because if that is the case, then the stack is full and no more insertions can be done. If an attempt is made to insert a value in a stack that is already full, an OVERFLOW message is printed.

## 7.3.2 Pop Operation

The pop operation is used to delete the topmost element from the stack. However, before deleting the value, we must first check if `TOP = NULL` because if that is the case, then it means the stack is empty and no more deletions can be done. If an attempt is made to delete a value from a stack that is already empty, an UNDERFLOW message is printed.

## 7.3.3 Peek Operation

Peek is an operation that returns the value of the topmost element of the stack without deleting it from the stack. However, the Peek operation first checks if the stack is empty, i.e., if `TOP = NULL`, then an appropriate message is printed, else...

**NIST**
- **stack (data structure)**
    - **Definition:** A collection of items in which only the most recently added item may be removed. The latest added item is at the top. Basic operations are push and pop. Often top and isEmpty are available, too. Also known as "last-in, first-out" or LIFO.
    - **Formal Definition:** The operations new(), push(v, S), top(S), and popoff(S) may be defined with axiomatic semantics as follows:
        - new() returns a stack
        - popoff(push(v, S)) = S
        - top(push(v, S)) = v
      where S is a stack and v is a value. The pop operation is a combination of top, to return the top value, and popoff, to remove the top value.
    - The predicate isEmpty(S) may be defined with the following additional axioms:
        - isEmpty(new()) = true
        - isEmpty(push(v, S)) = false
    - Also known as LIFO.
    - **Generalization (I am a kind of ...):** abstract data type.
    - **Specialization (... is a kind of me):** bounded stack, cactus stack.