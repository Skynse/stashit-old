from .utils.utils import get_date, debug, gen_files, create_folder
import os
import subprocess
from .termcolor import termcolor
import argparse
import pathlib


ignore = 'stashit-,'.split(',')

class Scanner:
    def __init__(self, path, date=get_date()):
        self.path = path
        self.date = date
                    
    def makefolder(self) -> None:
        if not os.path.exists(f'stashit-{self.date}'):
            create_folder()
            print(debug('createdir') % self.date)
        else:
            print('Section already exists so moving files instead')

    def move(self) -> None:
        can_run=False
        counter = -1
        with os.scandir(self.path) as p:
            for f in p:
                counter += 1
                if (not f.name[:8] in ignore) and (str(pathlib.Path.cwd()) != str(pathlib.Path.home())):
                    can_run = True
                    subprocess.run(['mv', f'{f.name}', 'stashit-'+self.date])
                    print('Moving', termcolor.colored(f.name, 'green'))
                else:
                    can_run = False
        if can_run == True: 
            print(f'Moved {counter} file(s)')
        else: print('Cannot run stashit in this directory')

def run():
    print(f'ignoring {[i for i in ignore]}')
    s = Scanner('.')
    s.makefolder()
    s.move()

if __name__ == "__main__":
    run()
