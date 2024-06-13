import sys
import os
import shutil
import csv
from datetime import datetime

import requests
import certifi

from Bio import Entrez
from io import BytesIO

Entrez.email = "shakedlevy1.61@gmail.com"

def search_ncbi(termx,retmaxx):

    # Function to perform Entrez esearch
    def entrez_esearch(term, db="nucleotide", retmax=retmaxx):
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": db,
            "term": term,
            "retmax": retmax,
            "retmode": "xml",
            "idtype": "acc",
            "email": Entrez.email
        }

        response = requests.get(url, params=params, verify=certifi.where())

        if response.status_code == 200:
            # Convert the response content to a file-like object using io.BytesIO
            handle = BytesIO(response.content)
            record = Entrez.read(handle)
            handle.close()
            return record
        else:
            raise Exception(f"Error fetching data: {response.status_code}")

    record = entrez_esearch(termx)

    results_number_founded = record["Count"]
    results_number_asked = retmaxx
    IDList = record["IdList"]

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return(results_number_asked, results_number_founded, IDList, formatted_time, termx)

def save_data(IDList):
    counter = 0
    for id in IDList :
        counter += 1
        doc_id = str(id)

        # Define the URL for the efetch request
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={doc_id}&rettype=gb&retmode=text"

        # Make the request using requests library
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.text
            
            filename = f"ID_{doc_id}.data"
            print(f'File number = {counter}\n\
                  File name = {filename}')
            with open(filename, 'w') as fh:
                fh.write(data)

        else:
            print("Error fetching data:", response.status_code)
       
        folder_path = 'data_ncbi'

        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            os.remove(filename)            
        else:
            shutil.move(filename, folder_path)


def save_to_seraches_csv(results_number_asked, results_number_founded, formatted_time, termx):

    data_to_append = [formatted_time, termx, results_number_asked, results_number_founded]
    csv_file = 'searches.csv'
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_to_append)


def command_line():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} Term Number")
    termx = sys.argv[1]
    retmaxx = sys.argv[2]
    return(termx, retmaxx)