created_name_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=created_name_file)  # or out_file.write(name)
created_name_file.close()

recieved_name_file = open("name.txt", "r")
recieved_name = recieved_name_file.read()
print("Your name is {}".format(recieved_name))

recieved_number_file = open("number.txt", "r")
first_number = int(recieved_number_file.readline())
second_number = int(recieved_number_file.readline())
recieved_number_file.close()
print(first_number + second_number)

recieved_numbers_file = open("numbers.txt", "r")
total = 0
for line in recieved_numbers_file:
    numbers = int(line)
    total += numbers
print(total)
recieved_numbers_file.close()
