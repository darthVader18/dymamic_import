import types

filename = "file1.py"
with open(filename) as fp:
    code1 = compile(fp.read(), filename, "exec")
config_module = types.ModuleType("<file1>")
exec (code1, config_module.__dict__)
config_module.name = ""

filename = "file2.py"
with open(filename) as fp:
    code = compile(fp.read(), filename, "exec")
config_module = types.ModuleType("<file2>")
exec (code, config_module.__dict__)
config_module.prog1(1, 2)
