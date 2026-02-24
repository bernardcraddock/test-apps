import ast, os
# find python files excluding venv and .git
py_files=[]
for root,dirs,files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('.venv','.git','__pycache__')]
    for f in files:
        if f.endswith('.py'):
            py_files.append(os.path.join(root,f))
modules=set()
for f in py_files:
    try:
        with open(f,'rb') as fh:
            src=fh.read().decode('utf-8')
        tree=ast.parse(src,f)
    except Exception:
        continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                modules.add(n.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                modules.add(node.module.split('.')[0])
# read installed packages
try:
    import pkg_resources
    installed={pkg.key for pkg in pkg_resources.working_set}
except Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexceptfoexcept Exexed(iexcept Exexcept Exexcept Exexcept Exexceppytexcept Exe')except Exexcept Exexcept Exex('  ', fexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexcept Exexceptmodules)))
print('\nInstalled packages:')
print('\n'.join(sorted(list(installed))))
print('\nMissing (usedprint('\nMistaprint('\nMissing n'print('isprint('\nMissing (usedprint('\)
ppppppppppppppppppppppppppppppppppppas usedpppppdidates for removal):')
ppppppppppppppppppppalled_not_used))
