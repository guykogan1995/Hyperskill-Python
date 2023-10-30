import math
import argparse
import sys

parser = argparse.ArgumentParser(description="This program is a loan calculator")
parser.add_argument("--type", choices=["diff", "annuity"], help="You need to choose an option")
parser.add_argument("--principal", default=0.0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0.0)
parser.add_argument("--payment", default=0)
args = parser.parse_args()
sum = 0
if (args.type != "diff" and args.type != "annuity" and args.type != "") or \
        ((args.type == "diff" or args.type == "annuity") and len(sys.argv) < 5) or \
        (float(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0 or \
            int(args.payment) < 0):
    print("Incorrect parameters")
    exit(-1)
if args.type == "diff" and float(args.principal) > 0 and int(args.periods) > 0\
        and float(args.interest) > 0:
    i = float(args.interest) / 1200
    for m in range(int(args.periods)):
        first_part = float(args.principal) / int(args.periods)
        second_part = float(args.principal) - (float(args.principal) * (m + 1 - 1)) / int(args.periods)
        calculation = math.ceil(first_part + i * second_part)
        sum += calculation
        print("Month " + str(m + 1) + ": payment is " + str(calculation))
    print("\nOverpayment = " + str(int(sum - float(args.principal))))
elif args.type == "annuity" and float(args.principal) > 0 and int(args.periods) > 0\
        and float(args.interest) > 0:
    i = float(args.interest) / 1200
    inside_func_of_monthly_payments = math.ceil(float(args.principal) * (i * math.pow((1 + i), int(args.periods))) / (
            math.pow((i + 1), int(args.periods)) - 1))
    print("You annuity payment = " + str(inside_func_of_monthly_payments) + "!")
    print("Overpayment = " + str(int(inside_func_of_monthly_payments * int(args.periods) - float(args.principal))))
elif args.type == "annuity" and int(args.payment) > 0 and int(args.periods) > 0\
        and float(args.interest) > 0:
    i = float(args.interest) / 1200
    inside_func_of_loan_principal = int(args.payment) / ((i * math.pow(1+i, int(args.periods))) / (
            math.pow(i+1, int(args.periods)) - 1))
    print("Your loan principal = " + str(math.floor(inside_func_of_loan_principal))
          + "!\nOverpayment = " + str((int(args.periods) * int(args.payment)) -
                                      math.floor(inside_func_of_loan_principal)))
elif args.type == "annuity" and float(args.principal) > 0 and int(args.payment) > 0\
        and float(args.interest) > 0:
    i = float(args.interest) / 1200
    inside_func_of_n = int(args.payment) / (int(args.payment) - i * float(args.principal))
    number_of_payments = math.ceil(math.log(inside_func_of_n, i + 1))
    if number_of_payments % 12 == 0:
        print("It will take " + str(number_of_payments//12) + " years to repay this loan!\nOverpayment = " +
              str(number_of_payments * int(args.payment) - int(args.principal)))
    else:
        print("It will take " + str(number_of_payments//12) + " years and " + str(number_of_payments % 12) +
              " months to repay this loan!\nOverpayment = " +
              str(number_of_payments * int(args.payment) - float(args.principal)))
