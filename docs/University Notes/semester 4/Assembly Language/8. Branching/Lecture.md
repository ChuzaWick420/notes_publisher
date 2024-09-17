---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Comparison and Conditions
The `cmp` operation subtracts `source` from `destination`.

```asm
cmp destination, source  ;destination - source
```

We need `flags` like `borrow` (in case the `source` is bigger in comparison), `sign`, `zero` and `overflow` flags etc to check relationship between `destination` and the `source`.

There can be `signed` or `unsigned` numbers.  
For the `signed`, we need `JG` and `JL`.  
For the `unsigned`, we need `JA` and `JB`.

Imagine we are comparing `-2`(`65534`) and `2`.

```asm
cmp -2, 2
```

 If we use `JA`, the jump will be taken.  
 If we use `JG`, the jump will not be taken.

| DEST = SRC   | ZF = 1             | When the source is subtracted from the destination and both are equal the result is zero and therefore the zero flag is set. This works for both signed and unsigned numbers.                                                                                                                                                      |
| ------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDEST < USRC | CF = 1             | When an unsigned source is subtracted from an unsigned destination and the destination is smaller, a borrow is needed which sets the carry flag.                                                                                                                                                                                   |
| UDEST £ USRC | ZF = 1 OR CF = 1   | If the zero flag is set, it means that the source and destination are equal and if the carry flag is set it means a borrow was needed in the subtraction and therefore the destination is smaller.                                                                                                                                 |
| UDEST ³ USRC | CF = 0             | When an unsigned source is subtracted from an unsigned destination no borrow will be needed either when the operands are equal or when the destination is greater than the source.                                                                                                                                                 |
| UDEST > USRC | ZF = 0 AND CF = 0  | The unsigned source and destination are not equal if the zero flag is not set and the destination is not smaller since no borrow was taken. Therefore the destination is greater than the source.                                                                                                                                  |
| SDEST < SSRC | SF ¹ OF            | When a signed source is subtracted from a signed destination and the answer is negative with no overflow than the destination is smaller than the source. If however there is an overflow meaning that the sign has changed unexpectedly, the meanings are reversed and a positive number signals that the destination is smaller. |
| SDEST £ SSRC | ZF = 1 OR SF ¹ OF  | If the zero flag is set, it means that the source and destination are equal and if the sign and overflow flags differ it means that the destination is smaller as described above.                                                                                                                                                 |
| SDEST ³ SSRC | SF = OF            | When a signed source is subtracted from a signed destination and the answer is positive with no overflow than the destination is greater than the source. When an overflow is there signaling that sign has changed unexpectedly, we interpret a negative answer as the signal that the destination is greater.                    |
| SDEST > SSRC | ZF = 0 AND SF = OF | If the zero flag is not set, it means that the signed operands are not equal and if the sign and overflow match in addition to this it means that the destination is greater than the source.                                                                                                                                      |

# Conditional Jumps

| JC<br><br>JB<br><br>JNAE  | Jump if carry<br><br>Jump if below<br><br>Jump if not above or equal     | CF = 1             | This jump is taken if the last arithmetic operation generated a carry or required a borrow. After a CMP it is taken if the unsigned source is smaller than the unsigned destination.               |
| ------------------------- | ------------------------------------------------------------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JNC<br><br>JNB<br><br>JAE | Jump if not carry<br><br>Jump if not below<br><br>Jump if above or equal | CF = 0             | This jump is taken if the last arithmetic operation did not generated a carry or required a borrow. After a CMP it is taken if the unsigned source is larger or equal to the unsigned destination. |
| JE<br><br>JZ              | Jump if equal<br><br>Jump if zero                                        | ZF = 1             | This jump is taken if the last arithmetic operation produced a zero in its destination. After a CMP it is taken if both operands were equal.                                                       |
| JNE<br><br>JNZ            | Jump if not equal<br><br>Jump if not zero                                | ZF = 0             | This jump is taken if the last arithmetic operation did not produced a zero in its destination. After a CMP it is taken if both operands were different.                                           |
| JA<br><br>JNBE            | Jump if above<br><br>Jump if not below or equal                          | ZF = 0 AND CF = 0  | This jump is taken after a CMP if the unsigned source is larger than the unsigned destination.                                                                                                     |
| JNA<br><br>JBE            | Jump if not above<br><br>Jump if not below or equal                      | ZF = 1 OR CF = 1   | This jump is taken after a CMP if the unsigned source is smaller than or equal to the unsigned destination.                                                                                        |
| JL<br><br>JNGE            | Jump if less<br><br>Jump if not greater or equal                         | SF ¹ OF            | This jump is taken after a CMP if the signed source is smaller than the signed destination.                                                                                                        |
| JNL<br><br>JGE            | Jump if not less<br><br>Jump if greater or equal                         | SF = OF            | This jump is taken after a CMP if the signed source is larger than or equal to the signed destination.                                                                                             |
| JG<br><br>JNLE            | Jump if greater<br><br>Jump if not less or equal                         | ZF = 0 AND SF = OF | This jump is taken after a CMP if the signed source is larger than the signed destination.                                                                                                         |
| JNG<br><br>JLE            | Jump if not greater<br><br>Jump if less or equal                         | ZF = 1 OR SF ¹ OF  | This jump is taken after a CMP if the signed source is smaller than or equal to the signed destination.                                                                                            |
| JO                        | Jump if overflow.                                                        | OF = 1             | This jump is taken if the last arithmetic operation changed the sign unexpectedly.                                                                                                                 |
| JNO                       | Jump if not overflow                                                     | OF = 0             | This jump is taken if the last arithmetic operation did not change the sign unexpectedly.                                                                                                          |
| JS                        | Jump if sign                                                             | SF = 1             | This jump is taken if the last arithmetic operation produced a negative number in its destination.                                                                                                 |
| JNS                       | Jump if not sign                                                         | SF = 0             | This jump is taken if the last arithmetic operation produced a positive number in its destination.                                                                                                 |
| JP<br><br>JPE             | Jump if parity<br><br>Jump if even parity                                | PF = 1             | This jump is taken if the last arithmetic operation produced a number in its destination that has even parity.                                                                                     |
| JNP<br><br>JPO            | Jump if not parity<br><br>Jump if odd parity                             | PF = 0             | This jump is taken if the last arithmetic operation produced a number in its destination that has odd parity.                                                                                      |
| JCXZ                      | Jump if CX is zero                                                       | CX = 0             | This jump is taken if the CX register is zero.                                                                                                                                                     |
