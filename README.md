1. sort the array in ascending order. 
2. Start from the least (left) and also from the largest (right)
3. Add the two numbers to get the total and  compare the total to the sum given
4. If the total is smaller than the sum given we move the  to second least number 
   (ie move from left to right)
 5.Add the two numbers to get th the total and  compare the total to the sum given
  6.If the total is larger than the sum given we move the to the next second largest number 
   (ie move from right ot left )
   7. We do this repeatedly .
    8. Once we get the total that is equal to the sum it stops there.
 

----------------------------------------
Pseudo code : 
 
expected output is indices.
1. Use iterations (for loop) and a condition statement.
2. Start form the first index (0) and add it to the next one (index 1) and compare it to the sum given. 
3. If it they do not add up the loop should go to the next index and do the same thing until it finds a pair of the first index the other that add up to the sum
 1st for loop--(Takes first index and iterates the remaining numbers until it gets the sum)
 2nd for loop --- Adds the remaining indexes (other than the 1st index) : ie takes index 1 and adds to index 2 and the remaining indices until the two add up to the sum given.
prints out the result
   
4. has 2 nested loops and quadratic running time: O(n2
{{{A function with a quadratic time complexity has a growth rate of n^2}}





