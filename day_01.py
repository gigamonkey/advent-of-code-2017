#!/usr/bin/env python3

def captcha(digits):
    return sum(i for i, j in zip(digits, digits[1:] + digits[:1]) if i == j)

if __name__ == '__main__':

    def check(input, expected):
        digits = [int(d) for d in input]
        if captcha(digits) == expected:
            print('{} ok!'.format(digits))
        else:
            print('Uh oh, {} => {}; expected'.format(digits, captcha(digits), expected))

    if False:
        check('1122', 3)
        check('1111', 4)
        check('1234', 0)
        check('91212129', 9)

    with open('day_01.txt') as f:
        digits = [int(c) for c in f.read() if c.isdigit()]
        print(captcha(digits))
