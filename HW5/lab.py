s = '''
PRICE LOCATION KIND CONDITION DECISION
high city townhouse excellent BUY
medium city townhouse OK BUY
medium city townhouse OK MAYBE
medium city house OK MAYBE
medium city condo OK BUY
high city condo OK NO
medium city condo poor NO
high city townhouse poor NO
medium city townhouse poor NO
medium city condo poor NO
medium city condo poor NO
high city condo poor MAYBE
low city townhouse good MAYBE
medium city condo good NO
high city townhouse good NO
medium city house good MAYBE
high city house good BUY
medium city house good BUY
medium city townhouse good NO
medium city townhouse NO
low city condo BUY
high city condo NO
'''

s = s.split(' ')
print(','.join(s))