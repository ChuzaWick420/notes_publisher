# Conditional Operator

```c
int max = (a > b) ? a : b; // (1)!
```

1. The `#!c (a > b)` is evaluated first, if it results into _non zero_, the expression is evaluated to be `#!c a`, otherwise it is evaluated to be `#!c b`.