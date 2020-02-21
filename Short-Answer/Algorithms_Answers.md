#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
a)  a = 0  ..... O(1) 
    while (a < n * n * n): ...... O(1)
      a = a + n * n ......  O(1)
For all of the three lines , the Big O  is constant regardless of the input size the runtime will not grow

```


b)
```
b)  sum = 0 ... O(1)
    for i in range(n): ....  O(n) * O(1) 
      j = 1     ............ O(1)
      while j < n: ......... O(n) * O(n)
        j *= 2   ........... O(1)
        sum += 1 ..........  O(1)

Ignore all the constants, we have O(n) * O(1) + O(n) * O(n)
then we have O(n^2) (loop inside of a loop)
```

c)


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II


