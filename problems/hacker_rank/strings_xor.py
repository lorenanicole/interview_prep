# import pytest
import calendar
import datetime
'''
1. Define how you want to represent your inputs and 
   outputs (ProgramConfig, Transfer).
2. Write a function that given a ProgramConfig, outputs 
   an array of Transfer as defined by the PaymentConfig.
'''
class Transfer:
  def __init__(self, date, amount):
    self.date = date
    self.amount = amount
  
  def __repr__(self):
    return f'Transfer({self.date}, {self.amount})'

def generate_transfers(programConfig):
  dates, transfers = [], []
  initial_date = programConfig['start_date'].split('-')
  
  initial_date = [int(val) for val in initial_date]
  initial_date = datetime.datetime(initial_date[0], initial_date[1], initial_date[2])
  
  dates.append(initial_date)
  num_transfers = programConfig['num_transfers']
  amount = programConfig['amount']

  if programConfig['cadence'] == 'weekly':
    weekly_delta = datetime.timedelta(days=7)
    for indx in range(num_transfers - 1): 
      new_date = dates[-1] + weekly_delta
      dates.append(new_date)
    
  elif programConfig['cadence'] == 'monthly' and calendar.monthrange(initial_date.year, initial_date.month)[1] == initial_date.day:
    date = dates[-1]
    for indx in range(num_transfers - 1):
      date = dates[-1]

      if date.month == 12:
        days_in_month = calendar.monthrange(date.year + 1, 1)
        date = date.replace(month=1, day=days_in_month[1])
      else:
        days_in_month = calendar.monthrange(date.year, date.month + 1)
        date = date.replace(month=date.month+1, day=days_in_month[1])

      dates.append(date)
  else:
    date = dates[-1]    
    for indx in range(num_transfers - 1):
      if date.month == 12:
        date.replace(month=1)
      else:
        date = date.replace(month=date.month+1)
      dates.append(date)
      
    for date in dates:
      new_date = date.strftime("%Y-%m-%d")
      transfers.append(Transfer(new_date, amount))
    # print(transfers)
    return transfers
    

'''
3. Write tests for your function. Please include testing 
for edge cases outside of the basic examples we have 
provided!
'''

# generate_transfers({'cadence': "weekly", 'start_date': '2024-05-30', 'num_transfers': 3, 'amount': 50.00 })

# def test_example_pass():
#   test_data_one =  { 'cadence': "monthly", 'start_date': '2024-01-25', 'num_transfers': 4, 'amount': 50.00 }
#   test_data_two = {'cadence': "weekly", 'start_date': '2024-05-30', 'num_transfers': 3, 'amount': 50.00 }
#   test_data_three = { 'cadence': "monthly", 'start_date': '2023-01-31', 'num_transfers': 4, 'amount': 50.00 }

#   tests = [test_data_one, test_date_two, test_data_three]

#   for test in tests:
#     resp = generate_transfers
  
#   assert len(resp) == len([Transfer('2024-01-25', 50.0), Transfer('2024-02-25', 50.0), Transfer('2024-03-25', 50.0), Transfer('2024-04-25', 50.0)])
# [Transfer('2024-05-30', 50.00), Transfer('2024-06-06', 50.00), Transfer('2024-06-13', 50.00)] 

# def test_example_fail():
#   print("fail")
#   assert 3 == 2

# pytest.main(["main.py"])

resp = generate_transfers({'cadence': "weekly", 'start_date': '2024-05-30', 'num_transfers': 3, 'amount': 50.00 })
print(resp)