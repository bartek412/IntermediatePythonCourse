files_to_process = [
    "math_sin_square.py",
    "math_square_root.py"
    ]
for path in files_to_process:
    print(path)
    with open(path) as f:
        source = f.read()
        exec(source)
    print('-'*30)

