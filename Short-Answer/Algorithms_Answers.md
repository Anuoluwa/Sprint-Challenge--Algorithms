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
      while j < n: ......... O(logn) * O(n)
        j *= 2   ........... O(1)
        sum += 1 ..........  O(1)

Ignore all the constants, we have O(n) * O(1) + O(n) * O(nlogn)
then we have O(n^2) (loop inside of a loop)
```

c)


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Linear time O(n)

## Exercise II


1. def check_floor(numbers of floor=n):
2. get the middle of n ==> n/2 , I have both left hand side and right hand side
3. for lhs and rhs drop the egg in the highest floor, is broken, 
 a. we get the middle of the lhs, lhs/2 or lhs
4. we continue until we have the highest floor where the egg is not broken, then 
5. check the value of that floor let say x, then 
the value of f : x + 1


