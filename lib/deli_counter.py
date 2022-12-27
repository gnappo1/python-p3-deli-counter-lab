def line(line):
    (print("The line is currently empty.")) if len(line) < 1 else print("The line is currently: " + " ".join([f"{line.index(name) + 1}. {name}" for name in line]))
    
def take_a_number(line, person):
    line.append(person)
    print(f"Welcome, {person}. You are number {len(line)} in line.")

def now_serving(line):
    print("There is nobody waiting to be served!") if len(line) < 1 else print(f"Currently serving {line.pop(0)}.")