# `#!cpp Printf` Conversions Table

## Table

| Argument Character | Argument Type  | Printed as                                                                                                                                                                     |
| ------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `d`, `i`           | `#!cpp int`    | decimal number.                                                                                                                                                                |
| `o`                | `#!cpp int`    | unsigned octal number (without a leading zero).                                                                                                                                |
| `x`, `X`           | `#!cpp int`    | unsigned hexadecimal number (without a leading `0x` or `0X`), using `abcdef` or `ABCDEF` for 10, …, 15.                                                                      |
| `u`                | `#!cpp int`    | unsigned decimal number.                                                                                                                                                       |
| `c`                | `#!cpp int`    | single character.                                                                                                                                                              |
| `s`                | `#!cpp char *` | print characters from the string until a `\0` or the number of characters given by the precision.                                                                              |
| `f`                | `#!cpp double` | `[-]m.dddddd`, where the number of `d`'s is given by the precision (default 6).                                                                                                |
| `e`, `E`           | `#!cpp double` | `[-]m.dddddde±xx` or `[-]m.ddddddE±xx`, where the number of `d`'s is given by the precision (default 6).                                                                       |
| `g`, `G`           | `#!cpp double` | use `%e` or `%E` if the exponent is less than `-4` or greater than or equal to the precision; otherwise use `%f`. Trailing zeros and a trailing decimal point are not printed. |
| `p`                | `#!cpp void *` | pointer (implementation-dependent representation).                                                                                                                             |
| `%`                | no argument    | print a `%`.                                                                                                                                                                   |

## Optional Arguments

Following are the optional arguments you can use.

- `Field Width` (the minimum amount of character space required inside `stdout`).
	- Example: `#!cpp %11s` makes a `field width` of `11` characters.
- `Left Justification Flag`
	- Example: `#!cpp %-10s`. If the `string`[^1] to be printed is smaller than the `field width` required, the characters will be left justified instead of being right justified by default.
- `Precision`
	- Example: `#!cpp %.4s` allows `4` characters (in case of `strings`[^1]) or `4` digits after the decimal point in `#!cpp float` values to be printed.

```cpp
#include <stdio.h>

int main () {

    const char* test = "hello world";

    printf(":%s:\n", test); // (1)!;
    printf(":%10s:\n", test); // (2)!;
    printf(":%.10s:\n", test); // (3)!;
    printf(":%-10s:\n", test); // (4)!;
    printf(":%.15s:\n", test); // (5)!;
    printf(":%-15s:\n", test); // (6)!;
    printf(":%15.10s:\n", test); // (7)!;
    printf(":%-15.10s:\n", test); // (8)!;

     return 0;
}

```

1. Prints `:hello world:`.
2. Prints `:hello world:`. The field width `10` was too small to fit in the `string`[^1] so some padding was needed.
3. Prints `:hello worl:`. `String`[^1] is only printed with `10` characters.
4. Prints `:hello world:`. There is no extra padding, therefore justification is irrelevant.
5. Prints `:hello world:`. More characters are allowed but `string`[^1] contains characters less than `15` in count.
6. Prints `:hello world    :`. Minimum `field width` is `15`, creating some padding around the `string`.[^1] Then the `string`[^1] is left justified.
7. Prints `:     hello worl:`. Minimum `field width` is `15`, creating some padding around the `string`.[^1] But only `10` characters are allowed due to precision.
8. Prints `:hello worl     :`. Minimum `field width` is `15`, creating some padding around the `string`.[^1] But only `10` characters are allowed due to precision and the `string`[^1] is left justified.

## References

1. Read more about [[C_string_literals|strings]].