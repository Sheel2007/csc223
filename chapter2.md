## 2.8 Space & Time Complexity

- **Time Complexity**:
  - **Big O (Time)**: Describes the upper limit on the time taken by an algorithm to execute as a function of the input size.
    - Example: O(n<sup>2</sup>) represents an algorithm with a worst-case time complexity of n<sup>2</sup>.

- **Space Complexity**:
  - **Big O (Space)**: Represents the upper limit on the amount of memory used by an algorithm as a function of the input size.
    - Example: \( O(n) \) indicates that the algorithm's memory usage grows linearly with the input size.

These notations help analyze and compare the efficiency of algorithms in terms of time and space requirements.

## 2.9 Big O Notation

- **Definition**: Big O notation (O) signifies an upper limit for f(n), representing the maximum growth rate.
- **Examples**: Functions like n<sup>2</sup> and n<sup>3</sup> fall within O(n<sup>2</sup>), while n and n<sup>2.9</sup> are not within O(n<sup>3</sup>).
- **Usage**: Big O is used to describe the worst-case scenario in algorithms, outlining their upper performance bounds.

## 2.10 Omega Notation

- **Definition**: Omega notation (Ω) provides a tight lower bound for f(n), indicating the minimum performance level.
- **Examples**: Functions in Ω(n<sup>2</sup>) include n<sup>2</sup> and n<sup>3</sup>, while those not in Ω(n<sup>3</sup>) include n and n<sup>2.9</sup>.
- **Use Cases**: Omega describes best and worst-case performance bounds for algorithms, highlighting minimum performance expectations.

## 2.11 Theta Notation

Certainly, here are a few key points about Theta notation:

- Theta notation (θ(g(n))) provides a tight bound on the growth rate of a function.
- It signifies that a function grows at the same rate as another function within constant factors.
- Formally, f(n) in θ(g(n)) if there exist positive constants c<sub>1</sub>, c<sub>2</sub>, and n<sub>1</sub> such that 0 <= c<sub>1</sub> * g(n) <= f(n) <= c<sub>2</sub> * g(n) for all  n >= n<sub>0</sub>.
- Theta notation is used to describe functions where both the upper and lower bounds are asymptotically tight.
- It provides a more precise description of the growth rate compared to Big O or Big Omega notation alone.

## 2.12 Other Useful Notations

### Little O Notation

Little O notation is a way to describe how fast a function grows compared to another function. When we say 

f(n) ∈ o(g(n)), it means that f(n) grows much slower than g(n).

### Ex: 2.8

For example, if we have f(n)=n<sup>2</sup> and g(n)=n<sup>3</sup>, then
f(n) is in o(g(n)) because n<sup>2</sup> grows much slower than. But if we have f(n)=n<sup>3</sup>, then it's not in o(g(n)) because it grows at the same rate as g(n).

In simple terms, if f(n) is in o(g(n)), it means that f(n) is "smaller" than g(n) in terms of how quickly it grows as n gets really large.

### Little Omega Notation

Little Omega notation (ω(g(n))) indicates that a function grows faster than another function, without requiring a tight bound, using the symbol ω. It differs from other notations like Big O, Big Omega, and Theta by focusing on lower bounds and not requiring tightness or specific constants.


### Ex: 2.9

Show that 50n<sup>3</sup> / 100 ≠ ω(n<sup>3</sup>).

Given: 0 ≤ cg(n) < h(n) , for any constant c > 0
Plug in n<sup>3</sup>: 0 ≤ cn<sup>3</sup> < 50n<sup>3</sup>/ 100
Then divide by n<sup>3</sup>: 

0 ≤ c < 50/100

Therefore c does not work for all values (remember should by any value where greater than 0).