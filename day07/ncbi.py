import ncbi_log

def main() :
    termx, retmaxx = ncbi_log.command_line()
    results_number_asked, results_number_founded, IDList, formatted_time, termx = ncbi_log.search_ncbi(termx,retmaxx)
    ncbi_log.save_data(IDList)
    ncbi_log.save_to_seraches_csv(results_number_asked, results_number_founded, formatted_time, termx)

main()