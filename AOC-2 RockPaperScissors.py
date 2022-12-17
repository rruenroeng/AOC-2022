sample_input = """A Y
B X
C Z"""

def play_RPS():
    file1 = open('RockPaperScissors.txt', 'r')
    lines = file1.readlines()
    
    # elves_string = sample_input
    # elves_lines = elves_string.splitlines()
    elves_lines = lines
    
    
    total_score = 0
    for line in elves_lines:
        line_arr = line.split()
        if line_arr[0] == 'A' and line_arr[1] == 'Y':
            # You win 
            total_score+=6
        elif line_arr[0] == 'B' and line_arr[1] == 'Z':
            # You win 
            total_score+=6
        elif line_arr[0] == 'C' and line_arr[1] == 'A':
            # You win 
            total_score+=6
        elif line_arr[0] == 'A' and line_arr[1] == 'X':
            # You draw 
            total_score+=3
        elif line_arr[0] == 'B' and line_arr[1] == 'Y':
            # You draw 
            total_score+=3
        elif line_arr[0] == 'C' and line_arr[1] == 'Z':
            # You draw 
            total_score+=3
        if line_arr[1] == 'X':
            total_score+=1
        if line_arr[1] == 'Y':
            total_score+=2
        if line_arr[1] == 'Z':
            total_score+=3
    print(total_score)

def main():
    play_RPS()

if __name__ == "__main__":
    main()