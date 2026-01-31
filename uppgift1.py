def create_file_from_string(my_filename, my_string):
    fw = open(my_filename, "w")
    fw.write(my_string)
    fw.close()


create_file_from_string("grattisfil.txt", "hurra")
