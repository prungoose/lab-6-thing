#eric reichard
def encode(string):
    encoded = []
    for i in string:
        digit = int(i) + 3
        if digit >= 10:
            digit -= 10
        encoded.append(str(digit))
    return ''.join(encoded)

def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        op = int(input('Please enter an option: '))
        if op == 1:
            password = input('Please enter your password to encode: ')
            encodedpass = encode(password)
            print('Your password has been encoded and stored!\n')
            continue
        if op == 2:
            print(f'The encoded password is {encodedpass}, and the original password is {password}.\n')
            continue
        if op == 3:
            exit()

if __name__ == '__main__':
    main()