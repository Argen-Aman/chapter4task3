import re

number = input('Enter 8-digit number (separate them by two digits with "---", "-", "." or ":"):\n')
pattern = r'^\d{2}(?:(-|\.|:|---)\d{2}){3}$'

match = re.fullmatch(pattern, number) 
print('True' if match else 'False')
