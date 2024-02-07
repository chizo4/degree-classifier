'''
--------------------------------------------------------------
FILE:
    code/data_handler.py

DEGREE-CLASSIFIER:
    DataHandler class serving various functionalities for CSV data.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    07/02/2024
--------------------------------------------------------------
'''

from academic_module import AcademicModule
from csv import DictReader, DictWriter
import os

class DataHandler:
    '''
    -------------------------
    DataHandler class handling CSV data processing.
    -------------------------
    '''

    def __init__(self: 'DataHandler', file_path: str) -> None:
        '''
        Initialize the class providing the (CSV) file name.

            Parameters:
            -------------------------
            file_path (str) : Path to the CSV data file.
        '''
        self.file = file_path
        self.ac_modules = []

    def read_csv(self: 'DataHandler') -> bool:
        '''
        Read a CSV file with columns: code, name, credits, fheq, grade.

            Return:
            -------------------------
            (bool) : Indication of a successful operation.
        '''
        i = 0
        try:
            with open(self.file, newline='', encoding='utf-8') as csv_file:
                csv_reader = DictReader(csv_file)
                for row in csv_reader:
                    i += 1
                    # Ensure the fields are correctly assigned.
                    code = row['code']
                    name = row['name']
                    credits = int(row['credits'])
                    fheq = int(row['fheq'])
                    grade = int(row['grade'])
                    # If a valid record, then assign a dataclass instance.
                    if code and name and credits and fheq and grade:
                        am = AcademicModule(
                            code=code,
                            name=name,
                            credits=credits,
                            fheq=fheq,
                            grade=grade
                        )
                        self.ac_modules.append(am)
                    else:
                        print(f'WARNING: Invalid record skipped in row {i} in {self.file}.')
                return True
        except FileNotFoundError:
            print(f'ERROR: File {self.file} not found.')
        except Exception as e:
            print(f'ERROR: {e}')
        return False

    def add_csv_record(self: 'DataHandler', new_am: 'AcademicModule') -> bool:
        '''
        Add a new data record into the data file (CSV).

            Parameters:
            -------------------------
            new_am (AcademicModule) : An instance of a new AcademicModule record. 

            Return:
            -------------------------
            (bool) : Indication of a successful operation.
        '''
        exist_file = os.path.isfile(self.file)
        try:
            with open(self.file, mode='a', newline='', encoding='utf-8') as csv_file:
                writer = DictWriter(
                    csv_file, 
                    fieldnames=['code', 'name', 'credits', 'fheq', 'grade']
                )
                if not exist_file:
                    writer.writeheader()
                writer.writerow(new_am.__dict__)
            return True
        except FileNotFoundError:
            print(f'ERROR: File {self.file} not found.')
        except Exception as e:
            print(f'ERROR: {e}')
        return False

    def input_academic_module(self: 'DataHandler') -> None:
        '''
        Create a new AcademicModule based on the CLI input. Then, save it in CSV.
        '''
        print('Enter the details of a new Academic Module.')
        while True:
            code = input('Code: ')
            if not code:
                os.system('clear')
                print('Code is required. Please try again.')
                continue
            name = input('Name: ')
            if not name:
                os.system('clear')
                print('Name is required. Please try again.')
                continue
            credits = int(input('Credits: '))
            if credits < 0:
                os.system('clear')
                print('Credits must be a positive integer. Please try again.')
                continue
            fheq = int(input('FHEQ Level: '))
            if fheq <= 0:
                os.system('clear')
                print('FHEQ Level must be a positive integer. Please try again.')
                continue
            grade = int(input('Grade: '))
            if grade < 0 or grade > 100:
                os.system('clear')
                print('Grade must be in range 0-100. Please try again.')
                continue
            # If valid inputs, then create an object and store it in data file.
            am = AcademicModule(
                code=code,
                name=name,
                credits=credits,
                fheq=fheq,
                grade=grade
            )
            if self.add_csv_record(new_am=am):
                os.system('clear')
                print(f'\nSUCCESS! New Academic Module created:\n{am}')
            break
