import os
import sys
from csv import reader, writer


try:
    if len(sys.argv) == 3:
        # Open as readable file
        with open(sys.argv[1], 'r') as source:
            csv_reader = reader(source)
            raw_data = list(csv_reader)

        # Open as truncated writable file
        with open(sys.argv[1], 'w+', newline='') as source:
            csv_writer = writer(source)
            for line in raw_data:
                csv_writer.writerow(line[0].split('|'))

        # Rename file
        os.rename(sys.argv[1], sys.argv[2])

    else:
        raise Exception
except:
    print(f'\nUse this instruction: python fix_csv.py <source_file> <dest_file>')
else:
    print('\nExecution completed')
