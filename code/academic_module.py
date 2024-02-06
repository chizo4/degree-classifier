'''
--------------------------------------------------------------
FILE:
    code/academic_module.py

DEGREE-CLASSIFIER:
    AcademicModule data class that is instantiated from a single 
    data record read from the (CSV) data file.

AUTHOR:
    Filip J. Cierkosz

VERSION:
    06/02/2024
--------------------------------------------------------------
'''

from dataclasses import dataclass

@dataclass
class AcademicModule:
    '''
    -------------------------
    AcademicModule data class storing data from a single 
    data record (i.e. 1 row in CSV).

        Parameters:
        -------------------------
        code (str)    : Module code.
        name (str)    : Module name.
        credits (int) : Module's credits (e.g., 10, 20).
        fheq (int)    : Framework for Higher Education Qualifications (FHEQ) Level.
    -------------------------
    '''
    code: str
    name: str
    credits: int
    fheq: int
    grade: int

    def __str__(self: 'AcademicModule') -> str:
        '''
        String representation of a data record.

            Return:
            -------------------------
            (str) : Formatted string representation of a record.
        '''
        line_sep = '\n' + (35 * '-')
        data_str = f'\n{self.code}: {self.name}\n\tGrade: {self.grade}%\n\tCredits: {self.credits}\n\tFHEQ Level: {self.fheq}'
        return line_sep + data_str + line_sep
