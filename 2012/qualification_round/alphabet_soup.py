
def main():
    r_file = open('alphabet_soup.txt', 'r')
    w_file = open('alphabet_soup_output.txt', 'a')

    letters = ['H', 'A', 'C', 'K', 'E', 'R', 'C', 'U', 'P']
    cases = int(r_file.readline())
    for i in range(1, cases+1):
        word = r_file.readline()
        counts = []
        for letter in letters:
            counts.append(word.count(letter))

        total_cnt = min(counts)
        w_file.write('Case #{}: {}\n'.format(i, total_cnt))

if __name__ == '__main__':
    main()