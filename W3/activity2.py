print('please, rating from 1–10 on the following:')

loan_large = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

should_loan = False

if loan_large >= 5:
    if credit_history >= 7 and income >= 7:
        should_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit_history < 4:
      should_loan = False
    else: 
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else: 
            should_loan = False


if should_loan:
    print('Decision: yes')
else:
    print('Decision: no')
