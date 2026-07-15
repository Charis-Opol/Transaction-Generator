import os
os.chdir(r"C:\Users\chari\Desktop\Transaction Generator")
import config
config.NUM_BORROWERS = 5
import transaction_generator as tg

g = tg.TransactionGenerator()
df = g.generate()
print('rows', len(df))
print(df[['borrower_id','loan_amount','monthly_income']].head().to_string(index=False))
