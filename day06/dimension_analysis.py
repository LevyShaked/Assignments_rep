import dimension_log

def main() : 
    N_axis_vec, n_unique_vec, x, p = dimension_log.file_to_var()
    dimension = dimension_log.calculations(N_axis_vec, n_unique_vec)
    dimension_log.print_plot(dimension, x, p)
    
main()