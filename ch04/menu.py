MENU = {'sandwich': 10, 'tea': 7, 'salad': 9} 

def restaurant():
    total = 0
    while True:
        order = input('please enter your order: ').strip()
        if not order:
            break
        if order in MENU:
            total += MENU[order]
            print(f'{order} costs {MENU[order]}, total is {total}')
        else:
            print(f'we are fresh out of {order} today')
    
    print(f'your total is {total}')

if __name__ == '__main__':
    restaurant()