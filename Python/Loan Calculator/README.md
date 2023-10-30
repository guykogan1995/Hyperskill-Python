# Loan Calculator Readme

## Description

This Python script is a versatile loan calculator that helps you calculate various parameters related to loans. You can use this script to:

- Calculate annuity payments (fixed monthly payments) based on the principal, number of periods, and interest rate.
- Determine the loan principal based on the annuity payment, number of periods, and interest rate.
- Find out the number of periods (loan term) required to repay the loan based on the principal, annuity payment, and interest rate.

The script accepts command-line arguments to specify the type of calculation and provide the required loan details. It then validates the input and performs the requested calculation, displaying the results and the overpayment amount (the total amount paid beyond the loan principal).

## Usage

To use the loan calculator, follow these steps:

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Use the script with the following command-line arguments to perform the desired calculation:

   - `--type`: Choose the type of calculation (options: "diff" for differential, "annuity" for annuity).
   - `--principal`: Specify the loan principal amount.
   - `--periods`: Set the number of periods (loan term).
   - `--interest`: Define the annual interest rate.
   - `--payment`: Provide the monthly payment amount (for annuity calculation).

   For example, to calculate annuity payments, you can use a command like this:

   ```bash
   python loan_calculator.py --type=annuity --principal=1000 --periods=10 --interest=10
   ```

4. The script will perform the calculation and display the results, including the calculated value and overpayment amount.

## Example

Here's an example of how to use the script:

```bash
python loan_calculator.py --type=annuity --principal=1000 --periods=10 --interest=10
```

This command would calculate and display the annuity payment for a $1000 loan with a 10% interest rate over 10 months.


Happy loan calculations!