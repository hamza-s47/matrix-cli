import sys
# from colorama import Fore, Back, Style, init
import utils.switch as method
from utils.tools import cli, idx_overflow
from utils.help import help_commands, help_keys

# mat1=[[1,2], [3,4]]
# mat2=[[6,9], [7,8]]
# vect=[1,2,4,3,7,5]
# n=3

args=sys.argv[1:]

if cli(args)[0] in ["--help", "-h"] and len(cli(args))==1:
    for x in help_keys:
        print(help_commands[x])
elif cli(args)[0] in help_keys and cli(args)[1] in ["--help", "-h"] and len(cli(args))==2:
    print(help_commands[cli(args)[0]])
elif cli(args)[0] in help_keys and len(cli(args))<=7:
    if cli(args)[0] in ["d_type", "dimension", "length", "shape", "size", "summary"] and len(cli(args))==2:
        print(method.Inspect(cli(args)[0], cli(args)[1]))
    elif cli(args)[0] in ["flatten", "ravel", "sort", "transpose"] and 2<=len(cli(args))<=3:
        if len(cli(args))==3:
            print(method.Manip(cli(args)[0], cli(args)[1], cli(args)[2]))
        print(method.Manip(cli(args)[0], cli(args)[1]))
else:
    pass