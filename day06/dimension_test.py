import dimension_log

def test_file_reader():
    N_axis_vec = []
    n_unique_vec = []
    dimension_log.file_reader("N_axis_test.csv",N_axis_vec)
    assert(len(N_axis_vec) > 0) # checking if the file_reader read and convert it to vector
    dimension_log.file_reader("n_unique_test.csv",n_unique_vec)
    assert(len(n_unique_vec) > 0) # checking if the file_reader read and convert it to vector
    
def test_calculations() :
    error = 0.05
    # known_dim = int(input("Enter the known dimension for the test (should be 1): "))
    known_dim = 1
    N_axis_vec = []
    n_unique_vec = []
    dimension_log.file_reader("N_axis_test.csv",N_axis_vec)
    dimension_log.file_reader("n_unique_test.csv",n_unique_vec)
    dimension = dimension_log.calculations(N_axis_vec, n_unique_vec)  
    assert(abs(known_dim-dimension) < error)