


def main():
    r_file = open('auction_sample_input.txt', 'r')
    w_file = open('auction_output.txt', 'a')

    cases = int(r_file.readline())
    for i in range(1, cases + 1):
        info = [int(x) for x in r_file.readline().split()]
        N = info[0]
        P1 = info[1]
        W1 = info[2]
        M = info[3]
        K = info[4]
        A = info[5]
        B = info[6]
        C = info[7]
        D = info[8]
        Pi_1 = P1
        Wi_1 = W1
        for j in range(2, N+1):
            P = ((A*Pi_1 + B) % M) + 1
            W = ((C*Wi_1 + D) % K) + 1
            Pi_1 = P
            Wi_1 = W

        w_file.write('Case #{}: {} {}')

if __name__ == '__main__':
    main()