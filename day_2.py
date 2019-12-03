#Micha den Heijer

import random
def transfer(one, two, atoms, i):
    if one == two:
        return atoms
    if ("a" in [one, two]) and ("b" in [one, two]):
        to = "c"
    if ("b" in [one, two]) and ("c" in [one, two]):
        to = "a"
    if ("c" in [one, two]) and ("a" in [one, two]):
        to = "b"

    trs = i

    atoms[one] -= trs
    atoms[two] -= trs
    atoms[to] += trs

    return atoms

def total(atoms):
    return atoms["a"] + atoms["b"] + atoms["c"]

def is_one(atoms):
    if atoms["a"] == 0 and atoms["b"] == 0:
        return True
    elif atoms["b"] == 0 and atoms["c"] == 0:
        return True
    elif atoms["c"] == 0 and atoms["a"] == 0:
        return True
    else:
        return False

global high_score
high_score = 0
while True:
    atoms = {
      "a": 91,
      "b": 25,
      "c": 4
    }
    global new_atoms
    new_atoms = atoms
    while not is_one(new_atoms):
        i = random.randint(1, 9)
        if i < 4:
            new_atoms = transfer("a", "b",  new_atoms, random.randint(0, min([atoms["a"], atoms["b"]])))
        elif i < 7:
            new_atoms = transfer("c", "b",  new_atoms, random.randint(0, min([atoms["b"], atoms["c"]])))
        else:
            new_atoms = transfer("a", "c",  new_atoms, random.randint(0, min([atoms["a"], atoms["c"]])))
        if is_one(new_atoms) and total(new_atoms) > high_score:
            high_score = total(new_atoms)
            print("The answer is: " + str(high_score))


