import os

for i in range(0, 26):
    folder_name = f"day{i}"
    file_names = [f"day{i}_example1.txt", f"day{i}_example2.txt", f"day{i}_input1.txt", f"day{i}_input2.txt"]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for file_name in file_names:
        with open(os.path.join(folder_name, file_name), 'w') as file:
            file.write("")  # Creating an empty file
