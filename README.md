[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4UhIVYWz)
# Laboratory 7

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. modules
     2. classes and objects
     3. file input/output
     4. exception handling
1. Run and test a Python program.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/aadi1720/lab07-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab07-username
     ```
     
## Program Instructions
Title: Creating a Simple Banking System

**Files required:** (NOTE: Create the file names as specified)
1. bank_system.py(main file)
2. bank_exceptions.py**

**Instructions**
1. Create a Python program that simulates a basic banking system. The system should include the following:

   a. A `BankAccount` class that has the following attributes and methods:
      - Attributes: `account_number`, `account_holder`, `balance`
      - Methods: `deposit(amount)`, `withdraw(amount)`, `get_balance()`

   b. Use a separate Python module for the custom exception classes. Import this module into your main program.
      
   c. Implement the `BankAccount` class to raise exceptions for the following scenarios:
      - Trying to withdraw more money than the available balance should raise an `InsufficientFundsError` (a custom exception).
      - Depositing or withdrawing a negative amount should raise a `NegativeAmountError` (a custom exception).

   d. Create a custom exception class `InsufficientFundsError` and `NegativeAmountError` for handling the exceptions in part c.

2. In the main program:
   a. Create two instances of the `BankAccount` class with following attributes:
          101, "Alice", 1000
          102, "Bob", 500

   b. Demonstrate the deposit and withdraw functionality for each account, making sure to handle exceptions where necessary using `try` and `except`.
   c. After each transaction, display the current balance of the account.

3. The program should run in a loop, allowing the user to perform multiple transactions until they choose to exit.

4. Implement a module named `bank_exceptions` to define and store the custom exception classes.

5. Make sure to test your program thoroughly by simulating various scenarios, including depositing negative amounts, withdrawing more than the available balance, and normal transactions.

6. Add comments and docstrings to explain the purpose and usage of classes, methods, and exceptions.

Your program should showcase your understanding of classes, objects, try and except for exception handling, and the use of modules in Python.

**Expected Output:**
```
1: Successful Deposit

User selects option 1 (Deposit).
User enters the deposit amount: $500.
Expected Output:
$500.0 deposited successfully. New balance: $1500.0

2: Successful Withdrawal

User selects option 2 (Withdraw).
User enters the withdrawal amount: $300.
Expected Output:
$300.0 withdrawn successfully. New balance: $1200.0

3: Insufficient Funds

User selects option 2 (Withdraw).
User enters the withdrawal amount: $1500 (more than the balance).
Expected Output:
Insufficient funds. You tried to withdraw $1500, but your balance is only $1200.0.

4: Negative Deposit Amount

User selects option 1 (Deposit).
User enters the deposit amount: -$200 (negative).
Expected Output:
Amount cannot be negative: $-200.0

5: Checking Balance

User selects option 3 (Check Balance).
Expected Output:
Account balance for Alice: $1200.0

6: Invalid Option

User selects an invalid option (e.g., 5).
Expected Output:
Invalid choice. Please select a valid option.

7: Exiting the Program

User selects option 4 (Exit).
Expected Output:
Exiting the program. Goodbye!
```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:

```
bank_system.py
bank_exceptions.py

```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|10|bank_system.py file submitted and meets the program requirements |
|10|bank_exceptions.py file submitted and meets the program requirements |
|30|unit test passes|

