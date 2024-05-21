def cahracters_counter(filename) :
    total_lines = 0
    total_words = 0
    total_character = 0
    counter = {}
    with open(filename) as fh :
        for line in fh :
            line = line.rstrip()
            total_lines += 1
            words_list = line.split(' ')
            total_words += len(words_list)
            for ch in line :
                if ch == ' ' or ch == '  ' :
                    continue
                total_character += 1
                if ch not in counter :
                    counter[ch] = 1
                else :
                    counter[ch] += 1           
    return counter, total_character, total_lines, total_words