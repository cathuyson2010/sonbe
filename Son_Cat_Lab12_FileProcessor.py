import shutil
import os
import csv

class FileProcessor:
    @staticmethod
    def merge(file1_path, file2_path, result_path):
        try:
            with open(file1_path, 'r', encoding= 'utf-8') as file1, open(file2_path, 'r', encoding= 'utf-8') as file2, open(result_path, 'w', encoding= 'utf-8') as result_file:
                result_file.write(file1.read())
                result_file.write('\n')
                result_file.write(file2.read())
        except Exception as e:
            print(f'Error merging files: {e}')

    @staticmethod
    def copy(file1_path, num_copies):
        try:
            for i in range(1, num_copies + 1):
                shutil.copy(file1_path, f'{file1_path}_{i}')
        except Exception as e:
            print(f'Error copying file: {e}')

    @staticmethod
    def convert_to_csv(text_file_path, csv_file_path):
        try:
            with open(text_file_path, 'r') as text_file, open (csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for line in text_file:
                    csv_writer.writerow([line.strip()])
        except Exception as e:
            print(f'Error converting to CSV: {e}')

    @staticmethod
    def file_statistics(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                words = sum(len(line.split()) for line in lines)
                print(f'Number of lines: {len(lines)}')
                print(f'Number of words: {words}')
        except Exception as e:
            print(f'Error calculating file statistics: {e}')

