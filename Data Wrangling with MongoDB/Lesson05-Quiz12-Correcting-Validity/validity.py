"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f, open(output_good, "w") as gw_file, open(output_bad, "w") as bw_file:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        gw = csv.DictWriter(gw_file, delimiter=',', fieldnames=header)
        gw.writeheader()

        bw = csv.DictWriter(bw_file, delimiter=',', fieldnames=header)
        bw.writeheader()

        for line in reader:
            if line["URI"].find("dbpedia.org") != -1:
                try:
                    line["productionStartYear"] = line["productionStartYear"][:4]
                    line["productionStartYear"] = int(line["productionStartYear"])

                    if line["productionStartYear"]>= 1886 and line["productionStartYear"]<=2014:
                        gw.writerow(line)
                    else:
                        bw.writerow(line)
                except ValueError:
                    bw.writerow(line)

def test():
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()