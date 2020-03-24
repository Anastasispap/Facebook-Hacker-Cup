def main():
    r_file = open('billboards.txt', 'r')
    w_file = open('billboards_output.txt', 'a')

    cases = int(r_file.readline())
    for i in range(1, cases+1):
        info = [x for x in r_file.readline().split()]
        width = int(info[0])
        height = int(info[1])

        font_size = 1
        for size in range(1, 1+max(width, height)):
            text = info[2:]
            cols, rows = width // size, height // size

            rem_cols = cols
            text.reverse()
            while text and rows > 0:
                word = text[-1:][0]
                if len(word) < rem_cols:
                    rem_cols = rem_cols - len(word)-1
                    text.pop()
                elif len(word) == rem_cols:
                    rows = rows - 1
                    text.pop()
                    rem_cols = cols - 1
                else:
                    rows = rows - 1
                    rem_cols = cols
                if len(text) == 0 and rows > 0:
                    font_size = size

        w_file.write('Case #{}: {}\n'.format(i, font_size))



if __name__ == '__main__':
    main()