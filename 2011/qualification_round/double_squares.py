from math import sqrt, floor


def is_square(num):
    num = sqrt(num)
    return num - floor(num) == 0


def main():
    r_file = open("double_squares.txt", "r")
    w_file = open("output.txt", "a")
    cases = int(r_file.readline())

    for i in range(1, cases+1):
        cnt = 0
        num = int(r_file.readline())

        num1 = 0
        num2 = num - num1
        if is_square(num2):
            cnt += 1

        j = 1
        while (j < floor(sqrt(num))+1) and num2 > num1:
            num1 = j**2
            num2 = num - num1
        
            if is_square(num2) and num2 > num1:
                cnt += 1

            j += 1
    
        w_file.write('Case #{}: {}\n'.format(i,cnt))
    r_file.close()
    w_file.close()


if __name__ == '__main__':
    main()
