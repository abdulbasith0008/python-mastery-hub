#Write a program to fill in a letter template given below with name and date.
#letter = '''
#Dear <|Name|>,
#You are selected!
#<|Date|>
#''' 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

b=(letter.replace("<|Name|>","Shaik").replace("<|Date|>","21-03-2021") )
print(b)




