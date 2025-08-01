# Instructions

| Instruction | Description                                                                                                                                             |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `mov x,y`   | $x \leftarrow y$                                                                                                                                        |
| `and x,y`   | $x \leftarrow x \land y$                                                                                                                                |
| `or x,y`    | $x \leftarrow x \lor y$                                                                                                                                 |
| `xor x,y`   | $x \leftarrow x \oplus y$                                                                                                                               |
| `add x,y`   | $x \leftarrow x + y$                                                                                                                                    |
| `sub x,y`   | $x \leftarrow x - y$                                                                                                                                    |
| `inc x`     | $x \leftarrow x + 1$                                                                                                                                    |
| `dec x`     | $x \leftarrow x - 1$                                                                                                                                    |
| `syscall n` | Invoke operating system routine $n$                                                                                                                     |
| `db`        | A [pseudo-instruction](http://www.nasm.us/xdoc/2.11.02/html/nasmdoc3.html#section-3.2) that declares bytes that will be in memory when the program runs |
