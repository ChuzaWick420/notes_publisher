# Bitwise Operators

In `C`, there are 6 bitwise operators.  
Let's assume 2 `variables`.

```c
int a = 6;
int b = 2;
```

## `AND`

```c
int c = a & b;    // (1)! 
```

1. Performs logical `AND` between `2`(`10`) and `6`(`110`), hence the result is `2`(`10`).

## `OR`

```c
int c = a | b;    // (1)! 
```

1. Performs logical `OR` between `2`(`010`) and `6`(`110`), hence the result is `6`(`110`).

## `XOR`

```c
int c = a ^ b;    // (1)!
```

1. Performs logical `XOR` between `2`(`010`) and `6`(`110`), hence the result is `4`(`100`).

## Left Shift

```c
int c = a << 2;    // (1)!
```

1. Shifts the value of `a`(which is `2`, `10` in `binary`) towards left side by `2` `bits`. Hence the result is `8`(`1000`). After the shifting, the vacated `bits` are `0`.

## Right Shift

```c
int c = a >> 1;  // (1)!
```

1. Shifts the value of `a`(which is `2`, `10` in `binary`) towards right side by `1` `bit`. Hence the result is `1`(`1`). After the shifting, the vacated `bits` are `0`.

## One's Complement

```c
int c = ~a;    // (1)!
```

1. Flips the `bits` of `a` (`2` = `00000000000000000000000000000010` to `11111111111111111111111111111101` which is `-3` in `binary`).