from os import listdir
from os.path import isfile
from subprocess import run

# File extensions.
FILE_EXTENSION = ".c"
OUTPUT_EXTENSION = ".out"
# Test case hyperparameters.
TEST_CASE_NUM = 5
TEST_CASE_DIR = "test_case"
TEST_CASE_FILES = "{A,B,C}.txt"
# Solution hyperparameters.
SOL_FILENAME = "sol"
SOL_EXPECTEDS = []


def build_solutions():
    # Compile solution C file.
    run(args=["gcc", SOL_FILENAME + FILE_EXTENSION, "-o", SOL_FILENAME + OUTPUT_EXTENSION])

    # Build a list of expected solutions.
    for i in range(1, TEST_CASE_NUM + 1):
        # Copy test cases to current working directory.
        run(args=["cp " + TEST_CASE_DIR + str(i) + "/" + TEST_CASE_FILES + " ./"], shell=True)

        # Execute solution .out file and store the result to SOL_EXPECTEDS.
        results = run("./" + SOL_FILENAME + OUTPUT_EXTENSION, capture_output=True, text=True)
        SOL_EXPECTEDS.append(results.stdout.strip())

    # Remove test cases and compiled output.
    clean(SOL_FILENAME)


def extract_filenames():
    # Extract all names of .c files, but without solution file, excluding extension.
    files = [entry for entry in listdir() if isfile(entry)]
    filenames = [file[:-len(FILE_EXTENSION)] for file in files if FILE_EXTENSION == file[-len(FILE_EXTENSION):]]
    filenames.remove(SOL_FILENAME)

    return filenames


def clean(filenames):
    # Remove test cases and compiled output.
    run(args=["rm ./" + TEST_CASE_FILES], shell=True)

    if type(filenames) is not list:
        filenames = [filenames]

    for filename in filenames:
        run(args=["rm", filename + OUTPUT_EXTENSION])


def score_files(filenames):
    # Score C files one by one.
    for filename in filenames:
        print("Start scoring '{}'.".format(filename))

        # Compile C file.
        run(args=["gcc", filename + FILE_EXTENSION, "-o", filename + OUTPUT_EXTENSION])

        for i in range(1, TEST_CASE_NUM + 1):
            # Copy test cases to current working directory.
            run(args=["cp " + TEST_CASE_DIR + str(i) + "/" + TEST_CASE_FILES + " ./"], shell=True)

            # Execute .out file.
            results = run("./" + filename + OUTPUT_EXTENSION, capture_output=True, text=True)
            received = results.stdout.strip()
            if SOL_EXPECTEDS[i - 1] == received:
                print("  Test case {}: correct.".format(i))
            else:
                print("  Test case {}: wrong.".format(i))
                print("    Expected:\n{}".format(SOL_EXPECTEDS[i - 1]))
                print("    Received:\n{}".format(received))

        print("End scoring '{}'.\n\n".format(filename))


if __name__ == "__main__":
    build_solutions()
    filenames = extract_filenames()
    score_files(filenames)
    clean(filenames)
