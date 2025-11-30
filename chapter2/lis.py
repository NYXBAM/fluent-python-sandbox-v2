


# without match/case 

def evaluate(exp: Expression, env: Environment) -> Any:
    if isinstance(exp, Symbol):
        return env[exp]
    
    elif exp[0] == 'if':
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda':
        (_, params, *body) = exp
        return Procedure(params, body, env)
    elif exp[0] == 'define':
        (_, name, value_exp) = exp 
        env[name] = evaluate(value_exp, env)
        
        
# with match/case

def evaluate(exp: Expression, env: Environment) -> Any:
    match exp:
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*params], *body] if body:
            return Procedure(params, body, env)
        
        case ['define', Symbol() as name, value_exp]:
            env[name] = evaluate(value_exp, env)
            
        case _:
            raise SyntaxError(lispstr(exp))