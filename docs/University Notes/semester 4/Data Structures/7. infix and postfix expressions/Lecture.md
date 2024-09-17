---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

consider this pseudocode:

```
Stack s;
while (not end of inputs) {
	e = get next input;
	if (e is an operand) {
		s.push(e);
	}
	else {
		op2 = s.pop();
		op1 = s.pop();
		value = result of operator applied on op2 and op1
		s.push(value);
	}
}
finalresult = s.pop();
```

Consider an example: 4 + 3 * 2.  
The expression is in _infix_ form.  
Converting it to #postfix form, we get: 4 3 2 * +.  
Now apply the pseudocode on this input: `4 3 2 * +`

In the beginning, the stack is empty  
![[Pasted image 20240425123016.png]]  
Since the first `input` is `4` which isn't an `operator`, it is pushed on the `stack`.  
![[Pasted image 20240425123429.png]]  
Same for `3` and `2` .  
![[Pasted image 20240425123610.png]]  
Next input is `*` operator, the `operands` are `poped` out of the `stack`, `*` operator is applied onto them and the result is pushed back into the `stack`.  
![[Pasted image 20240425124435.png]]  
Next input is `+`, same thing will happen.  
![[Pasted image 20240425124855.png]]  
In the end when inputs are finished,  
![[Pasted image 20240425125150.png]]

# Conversion from Infix to Postfix
We have an algorithm which changes the #infix form in string, to #postfix form.

```
Stack s;
while( not end of input ) {
	
	c = next input character;
	
	if( c is an operand )
		add c to postfix string;
	
	else {
		
		while( !s.empty() && prcd(s.top(),c) ){
			op = s.pop();
			add op to the postfix string;
		}
		
		if (s.empty() || e != ')')
			s.push( c );
		
		else
			s.pop(); //discard the '('
    }
}

//cleanup in the end
while( !s.empty() ) {
    op = s.pop();
    add op to postfix string;
}
```

This algorithm is language independent.  
Where `prcd()` is `precedence` determinant function which takes 2 arguments as inputs and returns `true` if precedence of `1st` argument is higher than or equal to `2nd` one.

Additional things to consider:

```
prcd('(', ')'); //false
prcd(op, ')'); //true if op != '(', false if op != ')'
prcd(op, '('); //false
```

These are self defined such that `(` forces the `operands` to be pushed on the stack and when `)` is encountered, the `while` loop is processed.

Let us understand it using an example:  
A + B * C  
![[Pasted image 20240425183851.png]]  
Since `A` is an `operand`, it is added to `postfix` form.  
![[Pasted image 20240425184132.png]]  
Since the stack was empty, the `while` loop is skipped and `operator` is pushed on the stack.  
![[Pasted image 20240425184502.png]]  
Since the next input (`B`) is an `operand`, it is written in the #postfix string.  
![[Pasted image 20240608120208.png]]  
Next input character is `*` which is an `operator`.  
Since the #stack is not empty, the #while-loop condition is checked.  
condition:

```cpp
while (!s.empty() && prcd(s.top(), c))
```

Because the `prcd()` function returns `false`, the loop is skipped again.  
The next statement is checked.

```cpp
if (s.empty() || e != ')')
	s.push( c );
```

Since `*` is not `)`, it is pushed.  
![[Pasted image 20240608121020.png]]  
Next input (`C`) being an `operand` is written in the #postfix string.  
![[Pasted image 20240608121233.png]]  
Since there are not inputs left.

```cpp
else
	s.pop(); //discard the '('
```

![[Pasted image 20240608121526.png]]  
Same thing happens again  
![[Pasted image 20240608121553.png]]
