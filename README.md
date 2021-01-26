# Unit testing challenge

This is an exercise for **unit testing** in Python. 
Simple `assert` expressions are used, as well as the `unittest` and the `pytest` modules.

A basic script is provided by the instructors, on which the tests are implemented. 
The unaltered script can be found in _original.py_. 

Full instructions for the challenge can be read [here](https://github.com/becodeorg/ANT-Theano-2-27/blob/main/2.python/2.python_advanced/11.unittest/03.challenge.ipynb).

The code contains a simple summation function that has to be tested on a large amount of integers. 
Further, there are some functions that interact with a (fake) database.
Here, mock objects are explored. 


## How to run all tests
* To run the tests that use the **Unittest** module, you can run 
  ```
  python -m unittest testing_with_unittest
  ```
  Because the addition test takes a long time, you might want to execute the tests separately:
  ```
  python -m unittest testing_with_unittest.TestAddition 
  python -m unittest testing_with_unittest.TestDatabase 
  ```
* The tests with **PyTest** can be executed by running

## More detailed explanation
### Unittest
### PyTest