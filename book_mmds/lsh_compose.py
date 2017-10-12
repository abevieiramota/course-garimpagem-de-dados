import re

def a(f, n):
    
    return lambda x: f(x)**n

def o(f, n):
    
    return lambda x: 1 - (1 - f(x))**n

fun_def = r'[ao]\d+'
re_extract_fun = re.compile(fun_def)
re_def_funs = re.compile(r'({})*'.format(fun_def))
def compose(funs):
    
    if not re_def_funs.match(funs):
        
        raise Exception("funs deve ser sequência de (o|a) seguida de um inteiro. Ex: o4a4 -> OR 4 AND 4")
    
    f = lambda x: x
    
    nfuns = 1
    
    for fun in re_extract_fun.findall(funs):
        
        fname = fun[0]
        n = int(fun[1:])
        nfuns *= n
        
        if fname == 'o':
            
            f = o(f, n)
        elif fname == 'a':
            
            f = a(f, n)
            
    return nfuns, f