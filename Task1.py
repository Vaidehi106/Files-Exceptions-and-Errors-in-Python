try:
    file1=open('sample.txt','r')
    print('reading file content:')
    for line in file1:
        print(line, end='')
    file1.close()
except FileNotFoundError:
    print('error: file not found!')
except Exception as e:
    print(f'an unexpected error occurred:{e}')




