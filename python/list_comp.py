#
#
# people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]
#
# for x in people:
#     for y in x:
#         y
#
# x = [y for x in people for y in x]
# print(x)

# def check_cc(cc):
#     c1 = cc.split()
#     check_digit = int(c1[-1])
#     c2 = c1[:-1]
#     c2.reverse()
#     c3 = [int(c2[x])*2 if x%2==0 else int(c2[x]) for x in range(len(c2))]
#     c4 = [x-9 if x > 9 else x for x in c3]
#     c5 = sum(c4)
#     return int(str(c5)[-1]) == check_digit
#
# print(check_cc('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'))
# print(check_cc('4 5 7 5 8 6 8 9 9 8 5 5'))

def check_cc(cc):
    split = cc.split()
    last_10 = split[-10:]
    last_10.reverse()
    doubled = [str(int(last_10[x])*2) if x%2==0 else str(int(last_10[x])) for x in range(len(last_10))]
    added = [int(x[0]) + int(x[1]) if len(x) > 1 else int(x) for x in doubled]
    total = sum(added)
    times_nine = total * 9
    calc = int(str(times_nine)[-1]) + total
    if calc % 10 == 0:
        print('Valid!')
    else:
        print('Not Valid!')
check_cc('4 4 7 3 0 5 6 6 1 0 8 5 3 7 5 8')
