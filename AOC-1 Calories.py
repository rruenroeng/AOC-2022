sample_input = """1000
2000 
3000

4000

5000
6000

7000
8000
9000

10000"""

def find_the_most_calories():
    file1 = open('elf_calories.txt', 'r')
    lines = file1.readlines()
    
    #elves_string = sample_input
    elves_lines = lines#elves_string.splitlines()
    
    
    curr = 0
    elves_capacities = []
    for line in elves_lines:
        if line != '\n':
            curr += int(line)
        else:
            elves_capacities.append(curr)
            curr = 0
    elves_capacities.sort()
    print(elves_capacities[-1]+elves_capacities[-2]+elves_capacities[-3])

def main():
    find_the_most_calories()

if __name__ == "__main__":
    main()