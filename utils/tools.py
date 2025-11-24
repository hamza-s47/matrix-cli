import json
# class CustomTools:
    
#     def _safe_execution(func):
#         def errorHandling(self, *args, **kwargs):
#             try:
#                 return func(self, *args, **kwargs)
#             except Exception as e:
#                 return f"Error while executing {func.__name__}"

# CLI Converter
def cli(cliArr):
    parsed = []
    for x in cliArr:
        try:
            if x.startswith('[') and x.endswith(']'):
                parsed.append(json.loads(x))
            elif '.' in x:
                parsed.append(float(x))
            else:
                parsed.append(int(x))
        except ValueError:
            parsed.append(x)
            
    return parsed

# Array to Dict
# def idx_overflow(arr):
#     d={}
#     for val,i in arr:
#         d[str(i)]=val
#     return


# Help Commands
def help_msg(key):
    return f"Use '{key} --help' or '{key} -h' to see the help message\nDon't use spaces inside arrays when writing commands, they get split and cause errors"