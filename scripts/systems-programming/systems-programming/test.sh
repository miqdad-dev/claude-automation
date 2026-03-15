#!/bin/bash

make
echo "Hello, world!" > test.txt
./main test.txt copy.txt
diff test.txt copy.txt
if [ $? -eq 0 ]; then
    echo "Test passed."
else
    echo "Test failed."
fi
rm test.txt copy.txt
make clean