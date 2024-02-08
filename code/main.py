'''
--------------------------------------------------------------
FILE:
    code/main.py

DEGREE-CLASSIFIER:
    Main module to run the classifier through CLI.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    08/02/2024
--------------------------------------------------------------
'''


from academic_module import AcademicModule
from degree_classifier import DegreeClassifier
from os import system


class MainCLI:
    '''
    -------------------------
    MainCLI class utilizing DegreeClassifier through CLI.
    -------------------------
    '''
    FILE_PATH = '../data/academic_module_grades.csv'
    FHEQ_MAP = {
        4: 'Y1',
        5: 'Y2',
        6: 'Y3'
    }
    OPTS = [
        ('a', 'show all module marks up-to-date.'),
        ('b', 'calculate averages per each academic year.'),
        ('c', 'current full-degree average.'),
        ('i', 'input a new academic record.'),
        ('l', 'clear screen.'),
        ('q', 'quit the program.')
    ]

    def __init__(self: 'MainCLI') -> None:
        '''
        Initialize the CLI runner with its data loader and degree classifier.
        '''
        self.degree_classifier = DegreeClassifier(file_path=self.FILE_PATH)
    
    def get_all_marks(self: 'MainCLI') -> None:
        '''
        Show all (atomic) academic module grades.
        '''
        for ac_mod in self.degree_classifier.ac_modules:
            print(ac_mod)

    def get_year_avg(self: 'MainCLI') -> None:
        '''
        Show averages per academic year calling the DegreeClassifier instance.
        '''
        year_avgs = self.degree_classifier.calc_year_avg()
        line_sep = '\n' + (30 * '-')
        for (avg, fheq) in year_avgs:
            print(f'{line_sep}\n{self.FHEQ_MAP[fheq]} Average: {avg:.1f}%{line_sep}')
    
    def get_degree_avg(self: 'MainCLI') -> None:
        '''
        Show (current) full-degree average calling the DegreeClassifier instance.
        '''
        avg = self.degree_classifier.calc_degree_avg()
        line_sep = '\n' + (30 * '-')
        print(f'{line_sep}\nDEGREE AVERAGE: {avg:.1f}%{line_sep}')

    def add_academic_module(self: 'MainCLI') -> None:
        '''
        Create a new AcademicModule based on CLI input. DegreeClassifier saves it in CSV.
        '''
        try:
            print('Enter the details of a new Academic Module.')
            while True:
                code = input('Code: ')
                if not code:
                    system('clear')
                    print('Code is required. Please try again.')
                    continue
                name = input('Name: ')
                if not name:
                    system('clear')
                    print('Name is required. Please try again.')
                    continue
                credits = int(input('Credits: '))
                if credits < 0:
                    system('clear')
                    print('Credits must be a positive integer. Please try again.')
                    continue
                fheq = int(input('FHEQ Level: '))
                if fheq <= 0:
                    system('clear')
                    print('FHEQ Level must be a positive integer. Please try again.')
                    continue
                grade = int(input('Grade: '))
                if grade < 0 or grade > 100:
                    system('clear')
                    print('Grade must be in range 0-100. Please try again.')
                    continue
                # If valid inputs, then create an object and store it in data file.
                ac_mod = AcademicModule(
                    code=code,
                    name=name,
                    credits=credits,
                    fheq=fheq,
                    grade=grade
                )
                if self.degree_classifier.add_csv_record(new_ac_mod=ac_mod):
                    system('clear')
                    print(f'\nSUCCESS! New Academic Module created:\n{ac_mod}')
                break
        except KeyboardInterrupt:
            print('\nQuitting the sub-program...')
            self.run()

    def run(self: 'MainCLI') -> None:
        '''
        Main method to run the degree tool through CLI.
        '''
        try:
            while True:
                print('\nDEGREE CLASSIFIER -- OPTIONS:'+''.join(
                    [f'\n\t{opt} --> {i}' for (opt, i) in self.OPTS]
                ))
                opt = input('\nSelect your option: ').strip().lower()
                if opt == 'a':
                    system('clear')
                    self.get_all_marks()
                if opt == 'b':
                    system('clear')
                    self.get_year_avg()
                if opt == 'c':
                    system('clear')
                    self.get_degree_avg()
                if opt == 'i':
                    system('clear')
                    self.add_academic_module()
                    # Update CSV data.
                    self.degree_classifier.read_csv()
                if opt == 'l':
                    system('clear')
                elif opt == 'q':
                    system('clear')
                    print('\nQuitting the program...')
                    break
        except KeyboardInterrupt:
            print('\nQuitting the program...')


if __name__ == '__main__':
    cli = MainCLI()
    cli.run()
