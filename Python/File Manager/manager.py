import os
import shutil

os.chdir("./module/root_folder")
command = input("Input the command\n").lower()
while command != "exit":
    if command == "pwd":
        print(os.getcwd())
    elif "cd " in command:
        if command == "cd ..":
            os.chdir("../")
            print(os.getcwd().split(sep="\\")[-1])
        else:
            args = command.split()
            try:
                if "/" in args[1]:
                    os.chdir(args[1])
                else:
                    os.chdir("./" + args[1])
            except FileNotFoundError:
                print(args[1])
            print(os.getcwd())
    elif command in ["ls", "ls -l", "ls -lh"]:
        if command == "ls":
            files = os.listdir(os.getcwd())
            files = sorted(files, key=lambda x: "." in x)
            for file in files:
                print(file)
        elif command == "ls -l":
            files = os.listdir(os.getcwd())
            files = sorted(files, key=lambda x: "." in x)
            for file in files:
                if os.stat(file).st_size == 0:
                    print(file)
                else:
                    print(file, os.stat(file).st_size)
        else:
            files = os.listdir(os.getcwd())
            files = sorted(files, key=lambda x: "." in x)
            for file in files:
                if os.stat(file).st_size == 0:
                    print(file)
                else:
                    byte_count = os.stat(file).st_size
                    if byte_count / 1024 < 1:
                        print(file, str(byte_count) + "B")
                    elif byte_count / (1024 ** 2) < 1:
                        print(file, str(round(byte_count / 1024)) + "KB")
                    elif byte_count / (1024 ** 3) < 1:
                        print(file, str(round(byte_count / 1024 ** 2)) + "MB")
                    elif byte_count / (1024 ** 4) < 1:
                        print(file, str(round(byte_count / 1024 ** 3)) + "GB")
    elif "rm" in command:
        args = command.split()
        if len(args) == 1:
            print("Specify the file or directory")
        else:
            if os.path.exists(args[1]) or args[1][0] == ".":
                if "." in args[1] and len(args[1]) > 1 and args[1][0] != ".":
                    os.remove(args[1])
                elif "." in args[1] and len(args[1]) > 1 and args[1][0] == ".":
                    directory = os.listdir()
                    count = 0
                    for file in directory:
                        if args[1] in file:
                            count += 1
                            os.remove(file)
                    if count == 0:
                        print(f"File extension {args[1]} not found in this directory")
                else:
                    directory = os.listdir(args[1])
                    if len(directory) == 0:
                        os.rmdir(args[1])
                    else:
                        shutil.rmtree(args[1])
            else:
                print("No such file or directory")
    elif "mv" in command:
        args = command.split()
        if len(args) == 1:
            print("Specify the current name of the file or directory and the new location and/or name")
        elif len(args) == 4:
            print("The file or directory already exists")
        elif len(args) == 3:
            old_name = args[1]
            new_name = args[2]
            if not os.path.exists(old_name) and not old_name[0] == ".":
                print("No such file or directory")
            elif os.path.exists(new_name) and "." in new_name:
                print("The file or directory already exists")
            elif old_name[0] == "." and len(old_name) > 1:
                directory = os.listdir()
                count = 0
                for file in directory:
                    if old_name in file:
                        count += 1
                        try:
                            shutil.move(file, new_name)
                        except shutil.Error:
                            answer = ""
                            while answer not in ["y", "n"]:
                                answer = input(f"{file} already exists in this directory. Replace? (y/n)\n").lower()
                                if answer == "y":
                                    shutil.copy(file, new_name)
                                    os.remove(file)
                                if answer == "n":
                                    continue
                                else:
                                    answer = input(f"{file} already exists in this directory. Replace? (y/n)\n").lower()
                if count == 0:
                    print(f"File extension {old_name} not found in this directory")
            else:
                shutil.move(src=old_name, dst=new_name)
        else:
            print("Specify the current name of the file or directory and the new name")
    elif "mkdir" in command:
        args = command.split()
        if len(args) != 2:
            print("Specify the name of the directory to be made")
        elif os.path.exists(args[1]):
            print("The directory already exists")
        else:
            os.mkdir(args[1])
    elif "cp" in command:
        args = command.split()
        if len(args) > 3:
            print("Specify the current name of the file or directory and the new name")
        elif len(args) < 2:
            print("Specify the file")
        else:
            old_file = args[1]
            new_file = args[2]
            if not os.path.exists(old_file) and old_file[0] != ".":
                print("No such file or directory")
            elif os.path.exists(old_file) and new_file == ".":
                print(f"{old_file} already exists in this directory")
            elif os.path.exists(new_file) and new_file != ".." and not os.path.isdir(new_file):
                print(f"{new_file} already exists in this directory")
            elif old_file[0] == "." and len(old_file) > 1:
                directory = os.listdir()
                count = 0
                for file in directory:
                    if old_file in file:
                        count += 1
                        if os.path.exists(new_file + "/" + file):
                            answer = ""
                            while answer not in ["y", "n"]:
                                answer = input(f"{file} already exists in this directory. Replace? (y/n)").lower()
                                if answer == "y":
                                    shutil.copy(file, new_file)
                                elif answer == "n":
                                    continue
                                else:
                                    answer = input(f"{file} already exists in this directory. Replace? (y/n)").lower()
                        else:
                            shutil.copy(file, new_file)
                if count == 0:
                    print(f"File extension {old_file} not found in this directory")
            else:
                shutil.copy(old_file, new_file)
    else:
        print("Invalid command.")
    command = input()
