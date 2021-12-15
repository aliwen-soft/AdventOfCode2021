
def print_octos(octos):
    string = "".join([ " ".join(["*" if o==0 else str(o) for o in row])+"\n" for row in octos])
    print(string)

def read_in_octopuses(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        energy_levels = [[int(n) for n in line.rstrip()] for line in lines]
        return energy_levels

def increment(octopuses):
    return [[o+1 for o in line] for line in octopuses]

def increment_surrounding(octos,x,y):
    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if i>=0 and j>=0 and i<10 and j<10 and not(i==x and j==y) and octos[i][j] != 0:
               # print(i,j,"increment to",octos[i][j] + 1,"from",x,y)
                octos[i][j] = octos[i][j] + 1
                if (octos[i][j]>9):
                    octos[i][j] = 0
                    octos = increment_surrounding(octos,i,j)
    return octos

def light(octos):
    light = False
    for i in range(0,10):
        for j in range(0,10):
            octo = octos[i][j]
            if octo > 9:
                octos[i][j] = 0
                light = True
              #  print(i,j,"flashed")
                octos = increment_surrounding(octos,i,j)
    return(light,octos)

def count_zeros(octos):
    return sum([sum([1 for l in line if l == 0]) for line in octos])

def day_eleven_part_one(test = False):
    file_name = "data/day_eleven.txt" if not test else "data/day_eleven_test.txt"
    octos = read_in_octopuses(file_name)
    zeros = 0
    days = 100
    for _ in range(0,days):
        print_octos(octos)
        octos = increment(octos)
        repeat = True
        while repeat:
            repeat, octos = light(octos)
        zeros = zeros + count_zeros(octos)
    return(zeros)


print(day_eleven_part_one(False))
