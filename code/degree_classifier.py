'''
--------------------------------------------------------------
FILE:
    code/degree_classifier.py

DEGREE-CLASSIFIER:
    DegreeClassifier class serving various functionalities for 
    processing CSV data and calculating its stats.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    05/03/2024
--------------------------------------------------------------
'''


from academic_module import AcademicModule
from csv import DictReader, DictWriter
import os


class DegreeClassifier:
    '''
    -------------------------
    DegreeClassifier class handling CSV data processing and stats.
    -------------------------
    '''
    FILE_TXT = '../data/degree_average.txt'
    FHEQ_LEVELS = [
        4,    # Year 1.
        5,    # Year 2.
        6     # Year 3.
    ]

    def __init__(self: 'DegreeClassifier', file_path: str) -> None:
        '''
        Initialize the class providing the (CSV) file name.

            Parameters:
            -------------------------
            file_path (str) : Path to the CSV data file.
        '''
        self.file = file_path
        self.ac_modules = []
        # Read the CSV data file on initialization.
        self.read_csv()

    def read_csv(self: 'DegreeClassifier') -> bool:
        '''
        Read a CSV file with columns: code, name, credits, fheq, grade.

            Return:
            -------------------------
            (bool) : Indication of a successful operation.
        '''
        ac_mod_data = []
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
                        ac_mod = AcademicModule(
                            code=code,
                            name=name,
                            credits=credits,
                            fheq=fheq,
                            grade=grade
                        )
                        ac_mod_data.append(ac_mod)
                    else:
                        print(f'WARNING: Invalid record skipped in row {i} in {self.file}.')
                self.ac_modules = ac_mod_data
                return True
        except FileNotFoundError:
            print(f'ERROR: File {self.file} not found.')
        except Exception as e:
            print(f'ERROR: {e}')
        return False

    def add_csv_record(self: 'DegreeClassifier', new_ac_mod: 'AcademicModule') -> bool:
        '''
        Add a new data record into the data file (CSV).

            Parameters:
            -------------------------
            new_ac_mod (AcademicModule) : An instance of a new AcademicModule record. 

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
                writer.writerow(new_ac_mod.__dict__)
            return True
        except FileNotFoundError:
            print(f'ERROR: File {self.file} not found.')
        except Exception as e:
            print(f'ERROR: {e}')
        return False
    
    def calc_year_avg(self: 'DegreeClassifier') -> list:
        '''
        Calculate year-by-year averages based on FHEQ levels.

            Return:
            -------------------------
            (list) : Tuples of calculated year-by-year averages.
        '''
        try:
            if self.read_csv():
                year_avgs = []
                for fheq in self.FHEQ_LEVELS:
                    # Filter target modules by FHEQ.
                    ac_mods = [ac_mod for ac_mod in self.ac_modules if ac_mod.fheq == fheq]
                    # Calculate the target year average.
                    avg_sum = sum([ac_mod.grade * ac_mod.credits for ac_mod in ac_mods])
                    credit_sum = sum([ac_mod.credits for ac_mod in ac_mods])
                    year_avg = avg_sum / credit_sum
                    year_avgs.append((year_avg, fheq))
                return year_avgs
        except ZeroDivisionError:
            print('ERROR: Cannot calculate the average if there are no grades provided.')
        return []
 
    def calc_degree_avg(self: 'DegreeClassifier') -> float:
        '''
        Calculate the (current) full-degree average.

            Return:
            -------------------------
            (float) : Full-degree average.
        '''
        try:
            if self.read_csv():
                # Handle FHEQ Level 5.
                fheq5_ac_mods = [ac_mod for ac_mod in self.ac_modules if ac_mod.fheq == 5]
                avg_sum = sum([ac_mod.grade * ac_mod.credits for ac_mod in fheq5_ac_mods])
                credit_sum = sum([ac_mod.credits for ac_mod in fheq5_ac_mods])
                # Handle FHEQ Level 6.
                fheq6_ac_mods = [ac_mod for ac_mod in self.ac_modules if ac_mod.fheq == 6]
                avg_sum += sum([2 * ac_mod.grade * ac_mod.credits for ac_mod in fheq6_ac_mods])
                credit_sum += sum([2 * ac_mod.credits for ac_mod in fheq6_ac_mods])
                degree_avg = avg_sum / credit_sum
                if degree_avg > 0 and degree_avg <= 100:
                    self.save_degree_avg(degree_avg=degree_avg)
                return degree_avg
        except ZeroDivisionError:
            print('ERROR: Cannot calculate the average if there are no grades provided.')
        return None
    
    def save_degree_avg(self: 'DegreeClassifier', degree_avg: float) -> None:
        '''
        Save the (current) degree average in a TXT file.

            Parameters:
            -------------------------
            degree_avg (float) : Calculated degree average.
        '''
        with open(self.FILE_TXT, 'w') as file:
            file.write(f'DEGREE AVERAGE: {degree_avg}')
