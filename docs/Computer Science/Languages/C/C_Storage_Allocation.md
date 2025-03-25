# Storage Allocation

## `#!cpp malloc()`

![[C_e_storage_allocation.svg]]  
`#!cpp malloc()` requests the `operating system` for some memory.  

- The red blocks represent memory which is not available for the program.  
- The `in use` memory is memory which is owned by `#!cpp malloc()`.
- The empty ones are part of a "free list" from which `#!cpp malloc()` will `#!cpp return`.

After calling `#!cpp malloc()`, a block from "free list" is unlinked and returned. If the returning block is too big then it is split and the residue remains linked within the "free list".  
After calling `#!cpp free()`, the block is linked back inside the "free list". If the block being freed is adjacent to any free block, they are joined together into one bigger block so that the memory doesn't become fragmented.

## Header

The `header` contains information such as 

- `Pointer`[^1] to the next free block.
- The size of the block.
- The storage itself.

To simply alignment, all blocks are multiples of header size.

```cpp
typdef long Align;

union header {
	struct {
		union header *ptr; // (1)!
		unsigned int size; // (2)!
	} s;
	Align x; // (3)!
};

typedef union header Header; 
```

1. `Pointer` to next block.
2. Size of the current block.
3. It is never used, it is only there to force alignment with the help of `unions`.[^2]

Also, `#!cpp malloc()` doesn't returns the block starting from `header` but rather the free storage inside that block.

```cpp
void *malloc(unsigned nbytes) {

    Header *p, *prevp;
    Header *morecore(unsigned);
    unsigned nunits;

    nunits = (nbytes + sizeof(Header) - 1) / sizeof(Header) + 1;

    if ((prevp = freep) == NULL) { // no free list yet
        base.s.ptr = freep = prevp = &base;
        base.s.size = 0;
    }

    for (p = prevp->s.ptr; ; prevp = p, p = p->s.ptr) {
        if (p->s.size >= nunits) { // big enough
            if (p->s.size == nunits) // exactly
                prevp->s.ptr = p->s.ptr;
            else { // allocate tail end
                p->s.size = nunits;
                p += p->s.size;
                p -> s.size = nunits;
            }

            freep = prevp;
            return (void*)(p + 1);
        }
        if (p == freep) // wrapped around free list
            if ((p = morecore(nunits)) == NULL)
                return NULL; // none left
    }

}
```

```cpp
#define NALLOC  1024   /* minimum #units to request */

/* morecore: ask system for more memory */
static Header *morecore(unsigned nu)
{
    char *cp, *sbrk(int);
    Header *up;

    if (nu < NALLOC)
        nu = NALLOC;
    cp = sbrk(nu * sizeof(Header));
    if (cp == (char *) -1)  /* no space at all */
        return NULL;
    up = (Header *) cp;
    up->s.size = nu;
    free((void *)(up+1));
    return freep;
}
```

```cpp
/* free: put block ap in free list */
void free(void *ap)
{
    Header *bp, *p;

    bp = (Header *)ap - 1;  /* point to block header */
    for (p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
        if (p >= p->s.ptr && (bp > p || bp < p->s.ptr))
            break;  /* freed block at start or end of arena */

    if (bp + bp->s.size == p->s.ptr) {  /* join to upper nbr */
        bp->s.size += p->s.ptr->s.size;
        bp->s.ptr = p->s.ptr->s.ptr;
    } else
        bp->s.ptr = p->s.ptr;

    if (p + p->s.size == bp) {  /* join to lower nbr */
        p->s.size += bp->s.size;
        p->s.ptr = bp->s.ptr;
    } else
        p->s.ptr = bp;

    freep = p;
}
```

Notice that `#!cpp srbk()` may return any pointer. By using a `cast`, we make sure that the code becomes independent of the underlying details which could vary from system to system.

## References

[^1]: Read more about [[C_Pointers|pointers]].
[^2]: Read more about [[C_union|unions]].