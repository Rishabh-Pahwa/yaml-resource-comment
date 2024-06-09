import os


# COMMENT RESOURCES
def comment_resources(lines):
    in_resources_section = False
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("resources:"):
            in_resources_section = True
            continue
        if in_resources_section:
            if line.startswith("- ") or line.startswith("# - "):
                lines[i] = "  # " + lines[i].lstrip()
            elif not line:
                in_resources_section = False
    return lines


# UN-COMMENT RESOURCES
def uncomment_resources(lines):
    in_resources_section = False
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("resources:"):
            in_resources_section = True
            continue
        if in_resources_section:
            if line.startswith("# - "):
                L1 = lines[i].lstrip()
                lines[i] =  "  "+L1[2:]
            elif line.startswith("# # - "):
                lines[i] = "  " + lines[i][4:]
                # L1=lines[i].lstrip()
                # lines[i]= " "+L1[4:]
            elif not line:
                in_resources_section = False
    return lines


# READ FILE
def read_file(filename, option):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        if option == 1:
            lines = comment_resources(lines)
        elif option == 2:
            lines = uncomment_resources(lines)
        else:
            print("Invalid option")
            return

        with open(filename, "w") as f:
            f.writelines(lines)
        print(f"File {filename} updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# MAIN
def main():
    filename = input("Enter the path of the YAML file:   ").strip()
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        return

    try:
        option = int(
            input(
                "Select an action: \n   1.Comment resources \n   2.Uncomment resources \n"
            ).strip()
        )
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")
        return

    read_file(filename, option)


if __name__ == "__main__":
    main()
