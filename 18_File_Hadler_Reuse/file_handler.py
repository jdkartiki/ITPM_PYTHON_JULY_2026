def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()