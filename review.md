# Review Questions

## Question 33

Show that n<sup>2</sup> + 50n = O(n<sup>2</sup>)

$0 ≤ n^2 + 50n ≤ cn^2$

$0 ≤ n^2(1+50/n) ≤ cn^2$

$0 ≤ 1+50/n ≤ c$ (Divide by n^2)

$1+50/n$ is greatest when $n=1$, meaning $c=2$. Therefore:

$0 ≤ 1+50/n ≤ 2$

$0 ≤ \frac{1}{n_0}(n_0+50) ≤ 2$

$0 ≤ n_0+50 ≤ 2n_0$

$0 ≤ 50 ≤ n_0$

Hence, $0 ≤ n^2 + 50n ≤ cn^2 \ ∀\ n ≥ n_0$ where $n_0=50,c=2$.


## Question 34

Show that n<sup>2</sup> + n<sup>2</sup> + n<sup>2</sup> = 3n<sup>2</sup> = O(n<sup>2</sup>)

$0 ≤ 3n^2 ≤ cn^3$

$0 ≤ 3/n ≤ c$ (Divide by n^3)

$3/n$ is greatest when $n=1$, meaning $c=3$. Therefore:

$0 ≤ 3/n ≤ 3$

$0 ≤ 3 ≤ 3n$

$0 ≤ 1 ≤ n$

Hence, $0 ≤ 3n^2 ≤ cn^3 \ ∀\ n ≥ n_0$ where $n_0=1,c=2$.

## Question 35

Prove that n<sup>3</sup> ≠ O(n<sup>2</sup>)

$0 ≤ n^3 ≤ cn^2$

$0 ≤ n ≤ c$

$n$ is not bounded by a constant. Therefore, $n^3 ≠ O(n^2)$.

# Multiple Choice

## Question 10

O(1) - Constant time  
O(n) - Linear time
O(n log n) - Loglinear Complexity  
O(n<sup>2</sup>) - Quadratic time