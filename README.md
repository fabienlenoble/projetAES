# projetAES
## Goal
This project is a 30 hours project during which we chose to inject data in the ELK (Elastic Logstash Kibana) stack and analyze it.
Once this is done, we anonymize it and try to evaluate how good we did by putting the new data through the same ELK stack.
We found a dataset of New York taxi trips from 2013 which will be what we will be working on at first.

## Start
Add your data to tripData2013 in folders such as trip_data_1.csv which will contain the trip_data_1.csv file itself

Run ```python generalize.py <input filepath>``` to anonymize the data

Run ```python modify_csv.py <input_filepath> <output_filepath>``` to modify to reformat the date fields in two separate dates in your csv file

Run ```python read_first_lines.py <input filepath> <x>``` to read the first x lines of the file given in the command line