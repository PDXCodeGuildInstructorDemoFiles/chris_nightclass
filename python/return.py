import os

def cls():
    q = input('Press any key to continue.')
    os.system('cls' if os.name=='nt' else 'clear')


def pagetext(text):
    with open(text,'r') as f:
        lines = f.read().split()
        new_str = []
        new_line = ''

        for i in lines:
            if len(i) + 1 + len(new_line) < 41:
                new_line += i + ' '
            else:
                new_str.append(new_line)
                new_line = ''
        else:
            new_str.append(new_line)

        new_text = '\n'.join(new_str)
        with open('tmp.txt', 'w') as x:
            x.write(new_text)

        with open('tmp.txt', 'r') as output:
            time = 0
            printed = ''
            for line in output:
                if time < 7:
                    printed += line# + '\n'
                    time += 1
                else:
                    printed += line
                    print(printed)
                    printed = ''
                    cls()
                    time = 0
            else:
                print(printed)
                print('')
                cls()

pagetext('text.txt')
