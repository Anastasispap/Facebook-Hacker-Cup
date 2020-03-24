
def main():
    r_file = open('studious_student.txt', 'r')
    w_file = open('studious_student_output.txt', 'a')

    cases = int(r_file.readline())
    for i in range(1, cases+1):
        info = [x for x in r_file.readline().split()]
        words = info[1:]
        words.sort()
        res_word = ''

        for word in words:
            res_word = ''.join((res_word, word))

        w_file.write('Case #{}: {}\n'.format(i, res_word))

if __name__ == '__main__':
    main()