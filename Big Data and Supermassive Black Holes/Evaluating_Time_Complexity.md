## Speeding the current program

* The current complexity is O(nm), where n and m are number of galaxies in respective catalogues.

* We can speed up the current program by lessening the number of searches by maintaining a boundary.

```
sort cat_2 by dec

for source_A in cat_1:
    for source_B in cat_2:
        if (dec_A - radius) < dec_B < (dec_A + radius):
            offset < angular_distance(A, B)
            if offset < radius:
                if offset smallest seen so far:
                    best_match = (A, B, offset)
        elif (dec_A - radius) > dec_B:
            break out of loop
```

* Ways to speed up a program:
    - Use a faster programming language, like C;
    - Incorporate better data structures;
    - Include specialised routines;
    - Streamline the code
    - Improve time complexity of core algorithm