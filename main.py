
with open("Input/Letters/starting_letter.txt") as letter:
    all_info = letter.read()
with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for char in name_list:
        stripped_name = char.strip()
        new_letter = all_info.replace("[name]" , stripped_name)
        # print(new_letter)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt" , "w") as send_letter:
            send_letter.write(new_letter)


    #   