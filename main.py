import os

PATH = os.path.expanduser("~\\Desktop\\takeout")


def main():
    files = get_files(PATH)
    extensions = get_extensions(files)

    for extension in extensions:
        os.mkdir(f"{PATH}\\{extension}")
        for file in files:
            os.replace(f"{PATH}\\{file}", f"{PATH}\\{extension}\\{file}")


def get_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(f"{path}\\{file}"):
            files.append(file)
    return files


def get_extensions(files):
    extensions = set()
    for file in files:
        extensions.add(file.split(".")[-1])
    return extensions


if __name__ == "__main__":
    main()
