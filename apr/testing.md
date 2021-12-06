# Program testing

## How are the tests organized?
Each test X is composed of 3 files:

+ `Xprop.md`: briefly explains the purpose of the test

+ `Xtest.txt`: contains the input to be provided for the test

+ `Xtestresult.txt`: contains the output of the test

## How to verify the testing?
Tests result were obtained running the following

    cat testing/Xtest.txt | python3 apr.py > testing/Xtestresult.txt

one can verify these are in fact the results by running the same command in a Unix like system or manually.