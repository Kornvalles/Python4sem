# A
filename = './airtravel.csv'

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines() 
    for line in content[:len(content)-1]:
        print(line.strip().split(','))

print_file_content(filename)

# B
output_file = "./file.txt"
tuplelist = ("mikkel", "hvordan gaar det", "det gaar skam meget godt")

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_obj:
        for line in lst:
            file_obj.write(line + "\n")

write_list_to_file(output_file, tuplelist)

# a
def write_list_to_file_strings(output_file, *strings):
    with open(output_file, 'w') as file_obj:
        for string in strings:
            file_obj.write(string + "\n")
write_list_to_file_strings(output_file, "hey", "hvordan", "gaar", "det", "idag?")

# C
def read_csv(input_file):
    with open(input_file) as file_obj:
        for line in file_obj:
            print(line)

read_csv(filename)