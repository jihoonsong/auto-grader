# Auto Grader

This is a python script file for auto-grading assignments. I hope this would make my teaching assistant life easier :p

## How it works

<p align="center">
  <img src="https://github.com/jihoonsong/auto-grader/blob/master/example.png" alt="example.png">
</p>

## How to use

    .
    ├── auto_grader.py           # A auto_grader.py.
    ├── sol.c                    # A solution file which can produce solutions.
    ├── student1.c               # A student's source file.
    ├── student2.c               # A student's source file.
    ...
    ├── studentn.c               # A student's source file.
    ├── test_case1/              # 1st test case. Put all files you need to run the 1st test case under here.
    ├── test_case2/              # 2nd test case. Put all files you need to run the 2nd test case under here.
    ...
    └── test_casen/              # nth test case. Put all files you need to run the nth test case under here.

> - Put auto_grader.py, solution file, and all student's source file in the same directory.
> - Put all test cases in each test_case folder.
> - You can change the name of the solution file. Note that you have to reflect that change on auto_grader.py.

Note that you need to modify this script according to your assignment to grade.

## Note

- This just directly compares output strings, so it fails if their format is different. Thus, it's better to manually check the expected output and the received output when the test case fails.

- Though this is not perfect, it helps you a lot to skim through all source files if they produce the expected result.

- You can modify this script to produce a .csv file.

## License

This project is licensed under the MIT License.
See [LICENSE.md](LICENSE.md) for details.
