import ast, os

# find python files excluding venv and .git
py_files = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".venv", ".git", "__pycache__")]
    for f in files:
        if f.endswith(".py"):
            py_files.append(os.path.join(root, f))
modules = set()
for f in py_files:
    try:
        with open(f, "rb") as fh:
            src = fh.read().decode("utf-8")
        tree = ast.parse(src, f)
    except Exception:
        continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                modules.add(n.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                modules.add(node.module.split(".")[0])
# read installed packages
try:
    import pkg_resources

    installed = {pkg.key for pkg in pkg_resources.working_set}
except Exception:
    installed = set()
# filter to standard library and installed
stdlib = {
    "os",
    "sys",
    "ast",
    "json",
    "re",
    "datetime",
    "collections",
    "itertools",
    "functools",
    "math",
    "random",
    "subprocess",
    "pathlib",
    "typing",
    "unittest",
    "pytest",
}
used_non_stdlib = modules - stdlib
missing = used_non_stdlib - installed
installed_not_used = installed - modules
print("\nUsed modules (non-stdlib):")
print("\n".join(sorted(list(used_non_stdlib))))
print("\nInstalled packages:")
print("\n".join(sorted(list(installed))))
print("\nMissing (used but not installed):")
print("\n".join(sorted(list(missing))))
print("\nInstalled but not used (candidates for removal):")
print("\n".join(sorted(list(installed_not_used))))
