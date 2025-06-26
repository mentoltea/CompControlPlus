import command
from command import Expression, CommandUsageError, NewCommand
from typing import Any


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
    "/? CommandName"
)
def DescribeCommand(*args, **kwargs) -> str:
    if (len(args) == 0):
        raise CommandUsageError("Needs at least 1 command to describe")
    
    name = args[0]
    res = ""
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

query = "/? ?"
res = command.evaluate_blocks(command.parse_query_to_blocks(query))
print(res.get())