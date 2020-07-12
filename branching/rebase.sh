#!/bin/bash
# display command line options

count=1
for param in "$@"; do
<<<<<<< HEAD

    echo "Next parameter: $param"
    count=$(( $count + 1 ))
>>>>>>> 6aa3dd2... git-rebase 2
done

echo "====="