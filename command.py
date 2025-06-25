from __future__ import annotations

from tasks import task
from typing import Any

def sort_expressions(expr: list[Expression]) -> tuple[ tuple, dict[str, Any] ]:
    args = []
    kwargs: dict[str, Any] = {}
    
    for e in expr:
        value = e.get()
        if e.name != None:
            kwargs[e.name] = value
        else:
            args.append(value)
    
    return (tuple(args), kwargs)


class Expression:
    def __init__(self, value: Any, name: str | None = None):
        self.value = value
        self.name = name
    
    def get(self):
        return self.value

class ExclamationExpression(Expression):
    """ !(...) """
    def __init__(self, evalstring):
        self.evalstring = evalstring
    
    def get(self):
        return eval(self.evalstring)

class CommandExpression(Expression):
    def __init__(self, name: str, exprs: list[Expression]):
        self.name = name
        self.exprs = exprs

    def get(self):
        # search for command & call it
        if self.name in commands:
            cmd = commands[self.name]
            expr = cmd(self.exprs)
            return expr.get()
        else:
            err = f"No command named {self.name} found"
            raise Exception( err )
            
commands: dict[str, Command] = {}
class Command:
    """ /name arg1 arg2 ... argn """
    def __init__(
        self,
        name: str,
        target: task.Callable,
        descr: str = "Empty description"
    ):
        self.name = name
        self.descr = descr
        self.target = target
    
    def __call__(self, expr: list[Expression]) -> Expression:
        args, kwargs = sort_expressions(expr)
        return Expression(self.target(*args, **kwargs))
    

def parse_query_to_blocks(query: str) -> list[ tuple[str,str] ]:
    blocks: list[tuple[str, str]] = []
    
    nowdoing = None
    curblock = ""
    
    bro = 0
    brc = 0
    
    cbro = 0
    cbrc = 0
    
    sbro = 0
    sbrc = 0
    
    for c in query + " ":
        if c=='\n': continue
        
        if c==' ':
            if nowdoing==None:
                continue
            
            if nowdoing in ['/', 'Lit']:
                blocks.append( (curblock, nowdoing) )
                nowdoing = None
                curblock = ""
                continue
        
        curblock += c
          
        match nowdoing:
            case None:
                match (c):
                    case '/':
                        nowdoing = '/'
                        curblock = "/"
                    
                    case '!':
                        nowdoing = '!'
                        curblock = "!"
                        bro = 0
                        brc = 0
                    
                    case '{':
                        nowdoing = '{'
                        curblock = "{"
                        cbro = 1
                        cbrc = 0
                    
                    case '[':
                        nowdoing = '['
                        curblock = "["
                        sbro = 1
                        sbrc = 0
                    
                    case '"':
                        nowdoing = '"'
                        curblock = '"'
                    
                    case _:
                        nowdoing = 'Lit'
                        # curblock = ""
            
            case '/':
                pass
            
            case '!':
                if c=='(': bro += 1
                elif c==')': brc += 1
                
                if bro==brc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    continue
            
            case '{':
                if c=='{': cbro += 1
                elif c=='}': cbrc += 1
                
                if cbro==cbrc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    continue
            
            case '[':
                if c=='[': sbro += 1
                elif c==']': sbrc += 1
                
                if sbro==sbrc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    continue
            
            case '"':
                if c=='"':
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    continue
    
    if len(blocks)==0:
        raise Exception(f"No blocks was found in command. Check for closure of {nowdoing}")          
    
    valid = False
    if blocks[0][1] == '/':
        valid = True
    elif len(blocks)==1 and blocks[0][1] == '!':
        valid = True
    elif len(blocks)==1 and blocks[0][1] == '{':
        valid = True
        subquery = blocks[0][0] [1:-1]
        blocks = parse_query_to_blocks(subquery)
    
    if not valid:
        raise Exception("Unknown syntax")
    
    return blocks

def parse_array_to_blocks(body: str) -> list[tuple[str,str]]:
    blocks: list[tuple[str, str]] = []
    
    nowdoing = None
    curblock = ""
    
    bro = 0
    brc = 0
    
    cbro = 0
    cbrc = 0
    
    sbro = 0
    sbrc = 0
    
    done = 0
    
    for c in body + ",":
        if c=='\n': continue
        
        if c==" ":
            if nowdoing in [None, 'Lit']:
                continue
        
        if c==',':  
            if nowdoing==None:
                if done==0:
                    raise Exception("Empty slot in array")
                if done>1:
                    raise Exception("Two expressions in one slot")
                done = 0
                continue
            
            if nowdoing == 'Lit':
                blocks.append( (curblock, nowdoing) )
                nowdoing = None
                curblock = ""
                done = 0
                continue
            
        
        curblock += c
          
        match nowdoing:
            case None:
                match (c):   
                    case '!':
                        nowdoing = '!'
                        curblock = "!"
                        bro = 0
                        brc = 0
                    
                    case '{':
                        nowdoing = '{'
                        curblock = "{"
                        cbro = 1
                        cbrc = 0
                    
                    case '[':
                        nowdoing = '['
                        curblock = "["
                        sbro = 1
                        sbrc = 0
                    
                    case '"':
                        nowdoing = '"'
                        curblock = '"'
                    
                    case _:
                        nowdoing = 'Lit'
                        # curblock = ""
            
            case '!':
                if c=='(': bro += 1
                elif c==')': brc += 1
                
                if bro==brc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    done += 1
                    continue
            
            case '{':
                if c=='{': cbro += 1
                elif c=='}': cbrc += 1
                
                if cbro==cbrc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    done += 1
                    continue
            
            case '[':
                if c=='[': sbro += 1
                elif c==']': sbrc += 1
                
                if sbro==sbrc:
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    done += 1
                    continue
            
            case '"':
                if c=='"':
                    blocks.append( (curblock, nowdoing) )
                    nowdoing = None
                    curblock = ""
                    done += 1
                    continue 
    
    return blocks

def evaluate_array_blocks(blocks: list[tuple[str,str]]) -> Expression:
    exprs: list[Expression] = []
    
    for (block_body, block_type) in blocks:
        match block_type:
            
            case '!':
                # !(...)
                if len(block_body) <= 3:
                    raise Exception("Empty exclamation expression")
                eval_body = block_body[2:-1]
                exprs.append( ExclamationExpression(eval_body) )
                
            case '{':
                if len(block_body) <= 2:
                    raise Exception("Empty subcommand")
                subcommand_body = block_body[1:-1]
                subcommand_blocks = parse_query_to_blocks(subcommand_body)
                expr = evaluate_blocks(subcommand_blocks)
                exprs.append( expr )
            
            case '[':
                if len(block_body) < 2:
                    raise Exception("Broken array")
                array_blocks = parse_array_to_blocks(block_body[1:-1])
                expr = evaluate_array_blocks(array_blocks)
                exprs.append(expr)
            
            case '"':
                if len(block_body) < 2:
                    raise Exception("Broken string")
                string_body = block_body[1:-1]
                exprs.append( Expression(string_body) )

            case 'Lit':
                try:
                    value = int(block_body)
                except:
                    try:
                        value = float(block_body)
                    except:
                        value = block_body
                exprs.append( Expression(value) )
            
            case _:
                raise Exception(f"Unknown block type: {block_type}")
    
    values: list[Any] = []
    for e in exprs:
        values.append( e.get() )
    
    return Expression(values)
       
def evaluate_blocks(blocks: list[tuple[str,str]]) -> Expression:
    if len(blocks)==1 and blocks[0][1] == '!':
        block_body = blocks[0][0]
        if len(block_body) <= 2:
            raise Exception("Empty exclamation expression")
        eval_body = block_body[2:-1]
        return ExclamationExpression(eval_body)
        
    elif blocks[0][1] == '/':
        command_name = blocks[0][0][1:]
        
        exprs: list[Expression] = []
        
        for i in range(1,len(blocks)):
            (block_body, block_type) = blocks[i]
            
            match block_type:
                case '/':
                    raise Exception("Cannot have multiple commands - use subcommand {} notation")
                
                case '!':
                    # !(...)
                    if len(block_body) <= 3:
                        raise Exception("Empty exclamation expression")
                    eval_body = block_body[2:-1]
                    exprs.append( ExclamationExpression(eval_body) )
                    
                case '{':
                    if len(block_body) <= 2:
                        raise Exception("Empty subcommand")
                    subcommand_body = block_body[1:-1]
                    subcommand_blocks = parse_query_to_blocks(subcommand_body)
                    expr = evaluate_blocks(subcommand_blocks)
                    exprs.append( expr )
                
                case '[':
                    if len(block_body) < 2:
                        raise Exception("Broken array")
                    array_blocks = parse_array_to_blocks(block_body[1:-1])
                    expr = evaluate_array_blocks(array_blocks)
                    exprs.append(expr)
                
                case '"':
                    if len(block_body) < 2:
                        raise Exception("Broken string")
                    string_body = block_body[1:-1]
                    exprs.append( Expression(string_body) )

                case 'Lit':
                    try:
                        value = int(block_body)
                    except:
                        try:
                            value = float(block_body)
                        except:
                            value = block_body
                    exprs.append( Expression(value) )
                
                case _:
                    raise Exception(f"Unknown block type: {block_type}")
        
        
        return CommandExpression(command_name, exprs)    
            
    else:
        raise Exception("Unknown expression type")


def func(*args, **kwargs):
    print(*args)

cA = Command("A", func)
commands["A"] = cA

cB = Command("B", func)
commands["B"] = cB


example_query = '/A "1 []" [1, !(str(1) + "1"), { /B }]'

blocks = parse_query_to_blocks(example_query)
result = evaluate_blocks(blocks)
print(result.get())