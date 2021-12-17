def print_paper(points):
    max_x = sorted([x for (x,y) in points], reverse=True)[0]
    max_y = sorted([y for (x,y) in points], reverse=True)[0]
    paper = [["." for _ in range(0,max_x+1)] for _ in range(0,max_y+1)]

    for x,y in points:
        paper[y][x]="#"

    print( "\n".join(["".join(row) for row in paper])+"\n" )

def read_in_data(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        index = lines.index("\n")
        points = [tuple([int(n) for n in point.split(",")]) for point in lines[:index]]
        folds = [tuple(fold.split(" ")[2].split("=")) for fold in lines[index+1:]]
        folds = [(axis,int(value.rstrip())) for (axis, value) in folds]
        return(points, folds)

def perform_fold(points,axis,value):
    new_points = []
    for point in points:
        if axis == "x":
            if point[0] < value:
                new_points.append(point)
            else:
                diff = point[0] - value
                new_points.append((value-diff,point[1])) 
        if axis == "y":
            if point[1] < value:
                new_points.append(point)
            else:
                diff = point[1]  - value
                new_points.append((point[0], value-diff)) 

    return list( dict.fromkeys(new_points) )


def day_thirteen_part_one(test=False):
    file_name = "data/day_13.txt" if not test else "data/day_13_test.txt"
    points, folds = read_in_data(file_name)

    for fold in folds:
        #print_paper(points)
        axis, value = fold
        points = perform_fold(points, axis, value)
        print(len(points))

    print_paper(points)

    return(len(points))

print(day_thirteen_part_one(False))