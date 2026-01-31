def print_file_on_screen(my_filename):
    fr = open(my_filename, "r")
    text = fr.read()
    print(text)
    fr.close() 

print_file_on_screen("grattisfil.txt") 