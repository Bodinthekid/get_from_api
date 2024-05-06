import requests
import json
import csv

file_name = "..\\dados\\data.json"
output_file1 = "..\\dados\\all_data.csv"
output_file2 = "..\\dados\\olhao_data.csv"

url = "https://api.ipma.pt/open-data/observation/meteorology/stations/observations.json"  # Substitua pelo URL real da API
response = requests.get(url)

if response.status_code == 200:
    api_data_json = response.json()  # Converte a resposta para formato JSON
    #print(api_data_json)
else:
    print(f"Error to get API. Status code: {response.status_code}")

with open(file_name, "w") as file:
    json.dump(api_data_json, file, indent=4)

def get_data_api():
    with open(file_name, 'r') as file:
        try:
            data = json.load(file) 

            with open(output_file1, 'w', newline='') as csvfile:

                writer1 = csv.writer(csvfile)
                header = ["Date", "ID", "intensidadeVentoKM", "temperatura", "radiacao", "idDireccVento", "precAcumulada", "intensidadeVento", "humidade", "pressao"]  # Adicione os nomes das colunas conforme necessário
                writer1.writerow(header)
                
                with open(output_file2, 'w', newline='') as csvfile2:
                    writer2 = csv.writer(csvfile2)
                    writer2.writerow(header)

                    for date, value in data.items():
                        for id, value2 in value.items():
                            #row = [date]  # Start a new row with the date
                            #row.append(id)  # Add the ID to the row
                            row = [date, id]
                            if value2:
                                for key, value3 in value2.items():
                                    row.append(value3)  # Add the value to the row
                                writer1.writerow(row)  # Write the row to the CSV file
                                if id == "1210881":
                                    writer2.writerow(row)
        except json.JSONDecodeError as e:
            print("Error loading JSON data:", e)
    return
       
