#!/usr/bin/env python3

from sys import exit, stderr

from tabulate import tabulate

from multilanguage import Env, Lang, TALcolors
from TALfiles import TALfilesHelper

import RO_problems_lib as RO
from knapsack_lib import solver, check_instance_consistency

# METADATA OF THIS TAL_SERVICE:
args_list = [
    ('pwd',str),
    ('elementi','list_of_str'),
    ('pesi','list_of_int'),
    ('valori','list_of_int'),
    ('Knapsack_Capacity',int),
    ('elementi_proibiti','list_of_str'),
    ('elementi_obbligati','list_of_str'),
    ('instance_dict','yaml'),
    ('request_dict','yaml'),
    ('as_yaml',bool),
    ('recall_instance',bool),
    ('recall_request',bool),
    ('with_opening_message',bool),
    ('with_output_files',bool),
    ('esercizio',int),
    ('task',int),
]
instance_objects = ['elementi','pesi','valori','Knapsack_Capacity','elementi_proibiti','elementi_obbligati']
sol_objects_implemented = ['opt_sol','opt_val','DPtable_opt_val']

ENV =Env(args_list)
TAc =TALcolors(ENV, "None")
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"), print_opening_msg = 'now'if ENV['with_opening_message'] else 'never')
TALf = TALfilesHelper(TAc, ENV)

# START CODING YOUR SERVICE:

TOKEN_REQUIRED = True
RO.check_access_rights(ENV,TALf, require_pwd = True, TOKEN_REQUIRED = TOKEN_REQUIRED)
instance_dict = RO.dict_of_instance(instance_objects,args_list,ENV)
check_instance_consistency(instance_dict)
RO.check_request(ENV['request_dict'], sol_objects_implemented)

request_dict = ENV["request_dict"]
if len(request_dict) == 0:
    request_dict = { key:key for key in sol_objects_implemented }
print(f"request_dict={request_dict}", file=stderr)
    
call_data = {"instance":instance_dict,"request":request_dict}
call_data["oracle"] = solver(call_data)

RO.oracle_outputs(call_data,ENV)
if ENV.LOG_FILES != None:
    RO.oracle_logs(call_data,ENV,TALf)
if ENV["with_output_files"]:    
    RO.oracle_output_files(call_data,ENV,TALf)

