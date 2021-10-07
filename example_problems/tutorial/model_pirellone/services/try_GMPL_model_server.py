#!/usr/bin/env python3
import subprocess
import os
#import turingarena as ta

from sys import exit
import re
import random
from time import monotonic

from multilanguage import Env, Lang, TALcolors

import pirellone_lib as pl

# METADATA OF THIS TAL_SERVICE:
problem="pirellone"
service="validate_GMPL_model"
args_list = [
    ('goal',str),
    ('seed',str),
    ('lang',str),
]

ENV =Env(problem, service, args_list)
TAc =TALcolors(ENV)
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))

# START CODING YOUR SERVICE: 

def get_path_dir():
    """Creates a folder where to store the temporary files needed by the service and returns its fullpath. Our goal is that this should work whether the service is run in local or on a server."""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    tmp_directory = os.path.join(current_dir,"tmp97815")
    if not os.path.exists(tmp_directory):
        os.path.makedirs(tmp_directory)
    return tmp_directory

def
    tmp_dir = get_path_dir()

def get_solution_from_mod_and_dat_in(tmp_dir, with_output_file=True, output_style="subset"):
    """launches glpsol on the .mod and .dat files contained in tmp_dir. The output of glpsol is displayed on standard output. If with_output_file=True then the procedure expects a file 'output.txt' to be generated by glpsol in tmp_dir and its format to comply output_style. If not, the procedure warns the user and terminates the service. If 'output.txt' is valid then the solution is returned."""    
    try:
        subprocess.run([
            "glpsol", 
            "-m", os.path.join(tmp_dir,MOD_FILENAME), 
            "-d", os.path.join(tmp_dir,DAT_FILENAME)
        ], cwd=tmp_dir, timeout=30.0)        
    except subprocess.TimeoutExpired:
        print("Too much computing time! Deadline exceeded.")
        return None
    except subprocess.CalledProcessError as e: 
        print ("The call to glpsol on your .dat file returned error")
        return None
    except Exception as e:
        print ("Processing returned with error")
        print(f" error: {e}")
        return None

    if not with_output_file:
        return
    # here I read the result file ('output.txt') and return it
    output_file_fullname = os.path.join(tmp_dir, "output.txt")
    if not os.path.exists(output_file_fullname)
        print("... sembra che glpsol non sia riuscito a creare il file output.txt")
        print("""If you want to get your model validated, then from your .mod file you should create a file named 'output.txt' containing the final solution for your instance. Namely, if the puzzle has no solution, then the file named 'output.txt' should contain the string "NO SOLUTION". Nel caso in cui non sia possibile spegnere tutte le luci del Pirellone
con gli interruttori speciali, il file `output.txt` offre la stringa "NO SOLUTIONS". Altrimenti, il file `output.txt` deve contenere due linee per indicare
su quali interruttori deve agire il custode.

La prima linea contiene una sequenza di $M$ valori ($0$ oppure
$1$) separati da uno spazio.
L'$i$-esimo valore della sequenza indica se il custode deve
agire sull'interruttore dell'$i$-esima riga (valore = $1$)
oppure no (valore = $0$).

Analogamente, la seconda linea contiene una sequenza di $N$
valori ($0$ oppure $1$) separati da uno spazio, per rappresentare le
operazioni che il custode deve effettuare sugli interruttori di
colonna.  Il $j$-esimo valore della sequenza indica se il
custode deve agire sull'interruttore della $j$-esima colonna
oppure no.""")
        exit(0)
    try:
        with open(os.path.join(tmp_dir, "output.txt")) as output:
            actual_output_file = output.readlines()
            if len(actual_output_file)>2:
                print("The file 'output.txt' has more than 2 lines.")
                exit(0)                
            if "NO SOLUTION" in actual_output_file[0] or "NO SOLUTION" in actual_output_file[1]:
                return "NO SOLUTION"
            if output_style=="subset":
                actual_row_vals = tuple(map(int,actual_output_file[0].split()))
                actual_col_vals = tuple(map(int,actual_output_file[1].split()))
            else:
                if not re.match("^|[a-zA-Z][0-9]+$",actual_output_file[0]):
                    print("The first line of the 'output.txt' file generated by your model does not comply the regex '^|[a-zA-Z][0-9]+$'")
                    exit(0)
                if not re.match("^|[a-zA-Z][0-9]+$",actual_output_file[1]):
                    print("The second line of the 'output.txt' file generated by your model does not comply the regex '^|[a-zA-Z][0-9]+$'")
                    exit(0)
                actual_row_vals, actual_col_vals = 1000,1001
                    
    except os.error as e:
        print(f" error: {e}")
        exit(1)
    except (IndexError, ValueError) as e:
        print(f" {e}\nThe file output.txt is not compliant with the intended frmat:")
        print("Fornire spiegazioni su cosa debba essere contenuto in output.txt")
        exit(0)
    return (actual_row_vals, actual_col_vals)


def get_expected_result(input_pirellone):
    # read the expected result
    with open(output) as out:
        expected_output_file = out.readlines()
        expected_row_vals = tuple(map(int,expected_output_file[0].split()))
        expected_col_vals = tuple(map(int,expected_output_file[1].split()))
        expected_result = (expected_row_vals, expected_col_vals)
        
    result = evaluate_solution(os.path.join(os.getcwd(), ta.submission.source), input)

    
def are_equiv(result,expected_result):
    if result == expected_result:
        return True
    if result == "NO SOLUTION":
        return False
    if expected_result == "NO SOLUTION":
        return False
    if (tuple(1-v for v in result[0]),tuple(1-v for v in result[1])) == expected_result:
        return True

