# Loops

## Difference between Pre-tested loops and Post-tested loops

| Aspect                  | Pre-tested Loop (for, while, foreach) | Post-tested Loop (do-while)     |
|-------------------------|------------------------------------|--------------------------------------|
| **Condition Check**     | Condition checked before entering loop body  | Condition checked after executing loop body      |
| **Execution**           | Executes loop body if condition is true   | Executes loop body at least once before checking condition |



## Loops in Python

### Python has two types of loops - for loop and while loop

| Aspect               | For Loop in Python                       | While Loop in Python                         |
|----------------------|-----------------------------------------|----------------------------------------------|
| **Usage**            | Iterates over a known sequence           | Repeats a block of code until a condition becomes false |
| **Syntax**           | `for variable in iterable:`              | `while condition:`                           |
| **Condition Check**  | Implicitly checks condition based on the iterable | Explicitly checks a condition using a boolean expression |
| **Initialization**   | Iterable is specified in the loop        | Variables need to be initialized before the loop |
| **Control**          | Iterates through the iterable until completion | Executes as long as the condition remains true |
| **Number of Iterations** | Known in advance                     | Depends on when the condition becomes false  |
| **Increment/Decrement** | Automatic iteration through the iterable | Increment/decrement required inside the loop to control the condition |


