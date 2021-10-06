import pytz
from datetime import datetime

def handle_input(inp, size):

    if inp.isnumeric():
        if not int(inp) in range(0, size):
            return False
        else:
            return True
    elif not inp.isnumeric():
        return False

if __name__ == '__main__':

    temp = ''
    options = []
    count = 0
    for i in pytz.all_timezones:
        
        if temp != i.split('/')[0]:
            temp = i.split('/')[0]
            options.append(temp)

            print('{}: {}'.format(count, temp))

            count = count + 1

    inp = input("Enter an option(number): ")
    size = len(options)

    while not handle_input(inp, size):
        inp = input("Please enter an available option(only number): ")
    
    inp = int(inp)
    inp = options[inp]

    retrieved_elements = list(filter(lambda x: inp in x, pytz.all_timezones))

    headerStr = ['timezone', 'current utc time', 'current local time']
    print('{} | {} | {}'.format(headerStr[0], headerStr[1], headerStr[2]))

    for i, ele in enumerate(retrieved_elements):
        tz = pytz.timezone(ele)

        ct = datetime.now(tz=tz)
        lt = tz.localize(datetime.now())
        
        print('==============================================================================================================================')
        print('{} | {} | {}'.format(ele, ct.isoformat(), lt))

        try:
            nextEle = retrieved_elements[i + 1]
        except IndexError:
            print('==============================================================================================================================')