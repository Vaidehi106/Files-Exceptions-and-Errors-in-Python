user=input("enter text to write to the file:")

with open('output.txt','w') as file:
   file.write(user)
print('data successfully written to output.txt')

additional_user=input('enter additional text to append:')
with open('output.txt','a') as file:
  file.write('\n' + additional_user)
print('data successfully appended')

print('final content of output.txt:')
with open('output.txt','r') as file:
   for line in file:
       print(line,end='')
