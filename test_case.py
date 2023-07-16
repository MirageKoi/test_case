# This is manual text var
# text = """The Tao gave birth to machine language.  Machine language gave birth
# to the assembler.
# The assembler gave birth to the compiler.  Now there are ten thousand
# languages.
# Each language has its purpose, however humble.  Each language
# expresses the Yin and Yang of software.  Each language has its place within
# the Tao.
# But do not program in COBOL if you can avoid it.
#         -- Geoffrey James, "The Tao of Programming" """


def find_unique_character(text: list) -> str:
    character_counts = {}

    for word in text:
        for char in word:
            if word.count(char) == 1 and char.isalpha():
                character_counts[char] = character_counts.get(char, 0)
                character_counts[char] += 1
                break

    try:
        result = [key for key, val in character_counts.items() if val == 1]
        return result[0]
    except IndexError:
        return "There are no unique character in the text"


def read_from_file() -> list:
    temp = []
    while True:
        path = input("Insert path to file: ")
        try:
            with open(path, "r") as file:
                for raw in file:
                    some = raw.strip().split()
                    temp.extend(some)
            return temp

        except FileNotFoundError:
            print("Incorect path name")


if __name__ == "__main__":
    result = find_unique_character(read_from_file())
    print(result)
