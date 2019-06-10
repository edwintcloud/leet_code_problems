# 735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Example 1:
```
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```

## Example 2:
```
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
```

## Example 3:
```
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
```

## Example 4:
```
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
```

## Note:
- The length of asteroids will be at most 10000.
- Each asteroid will be a non-zero integer in the range [-1000, 1000]..

## Communication Steps
* What do you still need to clarify about: inputs, outputs, etc?
    1. How should I handle an empty list as input?
* What are some reasonable assumptions about each?
    1. The length of asteroids will be at most 10000. 
    2. Each asteroid will be a non-zero integer in the range [-1000, 1000].
    3. An empty list should return an empty list.
* Assuming your assumptions are good, what are some good examples to test your finished algorithm against?
    1. Input: [-2, -1, 1, 2]  
       Output: [-2, -1, 1, 2]
    2. Input: [10, 2, -5]  
       Output: [10]
    3. Input: [5, 10, -5]  
       Output: [5, 10]
* Psuedocode
    1. initialize an empty list we will use as a stack
    2. iterate through the list of asteroids
    3. while there are asteroids in the stack and the current asteroid is less than 0 and the top item (last appended item) is greater than 0, loop - otherwise add the asteroid to the top of the stack
    4. each iteration, check if the absolute value of the current asteroid is less than the top item in the stack and break from the loop, or pop the top item from the stack and break if the absolute value of the current asteroid is equal to the item popped, otherwise continue the loop
    5. return stack