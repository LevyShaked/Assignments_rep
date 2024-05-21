import A5_BUS_LOG

total_lines0 = 2
total_words0 = 7
total_character0 = 16
counter0 = {'t': 16}
filename1 = "tester_1_for_A5.txt"
filename2 = "tester_2_for_A5.txt"

def test_1_A5():
    counter, total_character, total_lines, total_words = A5_BUS_LOG.cahracters_counter(filename1) 
    assert(total_character == total_character0)
    assert(total_lines == total_lines0)
    assert(total_words == total_words0)

def test_2_A5():
    counter, total_character, total_lines, total_words = A5_BUS_LOG.cahracters_counter(filename2) 
    assert(counter == counter0)
    assert(total_character == total_character0)
    assert(total_lines == total_lines0)
    assert(total_words == total_words0)