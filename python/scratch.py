# name = input('What is your name? ')
# # txt = open('../hello.txt', 'a')
# # txt.write('Hello {}!\n'.format(name))
# # txt.close()
#
# with open('../hello.txt', 'a') as txt:
#     txt.write('Hello {}!\n'.format(name))
#
# with open('hello.txt', 'r') as txt:
#     lines = txt.readlines()
#     for l in lines:
#         if 'Sheri' in l:
# #             print(l)
# import json
#
# with open('cities.json', 'r') as j:
#     data = json.loads(j.read())
#
#     for i in data:
#         print(i['city'])



def read_file(file, n):
    with open(file, 'r') as r:
        lines = r.readlines()
        for line in lines[:n]:
            print(line)
bacon = 'tmp.txt'
read_file(bacon, 5)
