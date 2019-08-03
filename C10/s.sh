#!/bin/bash
for ((i=2;i>0;i++)) do
    echo $i
    python3 gengrid.py > grid
    diff -w <(python3 countsubgrids_slow.py < grid  ) <( python3 countsubgrids.py < grid ) || break
done
