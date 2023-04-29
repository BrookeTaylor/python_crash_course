# Testing a Class

> "In this first part of this chapter, you wrote test for a single function. Now you'll write tests for a class. You'll use classes in many of your own programs, so it's helpful to be able to oprove that your classes work correctly. If you have passing tests for a class you're working on, you can be confident that improvements you make to the class won't accidentally break its current behavior."

## A Variety of Assertions

> So far, you've seen just one kind of assertion: a claim that a string has a specific value. When writing a test, you can make any claim that can be expressed as a conditional statement. If the condition is **True** as expected, your assumption about how that part of your program behaves will be confirmed; you can be confident that no errors exist. If the condition you assume is **True** is actually **False**, the test will fail and you'll know there's an issue to resolve. Table (below) shows some of the most useful kinds of assertions you can include in your initial tests.

| **Assertion**   | **Claim**   |
|-----------------|-----------------|
| assert a == b   | Assert that two values are equal |
| assert a != b   | Assert that two values are not equal |
| assert a    | Assert that a evaluates to **True** |
| assert not a    | Assert that a evaluates to **False** |
| assert *element* in *list*   | Assert that an element is in a list. |
| assert *element* not in *list*   | Assert that an element is not in a list. |

> These are just a few examples; anything that can be expressed as a conditional statement can be included in a test."

