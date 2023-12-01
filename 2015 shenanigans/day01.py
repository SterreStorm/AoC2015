def main(filename):
    floor = 0
    with open(filename) as file:
        iteration = 0
        for line in file:
            for letter in line:
                floor += 1 if letter == "(" else -1
                iteration += 1
                if floor < 0:
                    print(iteration)
                    break
main("input/day01.txt")