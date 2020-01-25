# Question 3 (14 points)

Implement a program that can parse and compute the result of parenthesized, fully-bracketed, binary infix arithmetic expressions (e.g. ((1+2)*(3/0.5)) ) on double-precision floating point numbers, using +, *, -, /, and parentheses, where ‘+’ indicates addition, ‘-’ indicates subtraction, ‘*’ indicates multiplication and ‘/’ indicates floating-point division. Order of operations should not be a concern.

Implementation of the arithmetic operators +, *, - and / should each be handled in a program in a different language than the one handling the input.

Input will be a single line of text using the digit characters, a period for a decimal point, leading ‘-’ minus signs to indicate a negative number, opening and closing parentheses, ‘(‘ and ‘)’, and the operators ‘+’, ‘-’, ‘*’ and ‘/’. Output should be a decimal representation of the resulting floating point number on a line on its own.

Some points will be awarded for implementing a correct parsing of the expression, rather than using an off-the-shelf solution.

*Note:* Repeated serialization and deserialization of floating point numbers to and from decimal representation can introduce errors, so we will tolerate outputs that are within 10% of the true value of directly computing from the input expression.