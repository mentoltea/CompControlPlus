from . import command
from .command import Expression, CommandUsageError, NewCommand
from typing import Any

@NewCommand(
    "!", 
    "Eval", 
    "/! arg"
)
def ExplicitEval(*args, **kwargs) -> Any:
    if len(args) != 1:
        raise CommandUsageError("Needs exactly 1 argument to eval")
    estr = args[0]
    res = eval(estr)
    return res

@NewCommand(
    "!!", 
    "Exec", 
    "/!! arg"
)
def ExplicitExec(*args, **kwargs) -> Any:
    if len(args) < 1:
        raise CommandUsageError("Needs at least 1 argument to eval")
    estr = ""
    for arg in args:
        if (arg == ';'): estr +=  "\n"
        elif (arg[-1] == ';'):
            arg = arg[0:len(arg)-1]
            estr += str(arg) + "\n"
        else: estr += str(arg) + " "
        
    print(estr)
    res = exec(estr)
    return res

@NewCommand(
    "+", 
    "Adds two arguments", 
    "/+ Arg1 Arg2 [... ArgN]"
)
def AddArguments(*args, **kwargs) -> Any:
    if len(args) < 2:
        raise CommandUsageError("Needs at least 2 arguments to add")
    
    
    v1 = args[0]
        
    for i in range(1, len(args)):
        v2 = args[i]
        v1 = v1 + v2
    
    return v1

@NewCommand(
    "-", "Subtracts or negates", 
    "/- Arg" + "\n" 
    + "/- Arg1 Arg2"
)
def SubtractArguments(*args, **kwargs) -> Any:
    if (len(args) == 0):
        raise CommandUsageError("Needs at least 1 arguments to negate")
    
    if (len(args) == 1):
        v = args[0]
        return -v
    
    if len(args) == 2:
        v1 = args[0]
        v2 = args[1]
        return v1 - v2
    
    raise CommandUsageError(f"Too many arguments to subtract: {len(args)}")
    
@NewCommand(
    "?", "Returns the description of given command", 
    "/?" + "\n" +
    "/? CommandName"
)
def DescribeCommand(*args, **kwargs) -> str:
    res = ""
        
    if (len(args) == 0):
        res = "Command list:"
        for name in command.commands:
            cmd = command.commands[name]
            res += f"\n{cmd.name}"
        return res
    
    name = args[0]
    if name in command.commands:
        cmd = command.commands[name]
        res = ( ""
            + f"Name: {cmd.name}"       + "\n" + "\n"
            + f"Description:"           + "\n"
            + f"{cmd.descr}"            + "\n" + "\n"
            + f"Usage:"                 + "\n"
            + f"{cmd.usage}"           
        )
    else:
        res = f"No command named {name} found"
    
    return res

@NewCommand(
    "/str", "Tries to convert argument to string", 
    "/str arg"
)
def Stringify(*args, **kwargs) -> str:
    if (len(args) != 1):
        raise CommandUsageError("Needs exactly 1 arguments to convert")
    
    arg = args[0]
    res = str(arg)
    return res

@NewCommand(
    "/int", "Tries to convert argument to int", 
    "/int arg"
)
def Intify(*args, **kwargs) -> int:
    if (len(args) != 1):
        raise CommandUsageError("Needs exactly 1 arguments to convert")
    
    arg = args[0]
    res = int(arg)
    return res

@NewCommand(
    "/float", "Tries to convert argument to float", 
    "/float arg"
)
def Floatify(*args, **kwargs) -> float:
    if (len(args) != 1):
        raise CommandUsageError("Needs exactly 1 arguments to convert")
    
    arg = args[0]
    res = float(arg)
    return res
    