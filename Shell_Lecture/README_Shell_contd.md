
# Advanced Topics


## 📌 Introduction to Z Shell Scripting

So far, we have explored executing commands in the shell. However, in many scenarios, we need to perform a series of commands and utilize control flow expressions like conditionals or loops. This is where **Z Shell (Zsh) scripting** comes in.

Zsh scripts allow users to automate tasks, execute commands in sequence, and implement logic such as loops and conditionals. Unlike general-purpose programming languages, Zsh scripting is specifically designed for command-line operations, making it well-optimized for tasks such as creating pipelines, handling files, and processing input/output.

---

## 📜 Variables in Zsh

Variables in Zsh are assigned using the `=` operator, but note that there should be no spaces around the `=` sign.

```bash
foo=bar   # Assign 'bar' to variable 'foo'
echo "$foo"  # Outputs: bar
echo '$foo'  # Outputs: $foo (literal string, no substitution)
```

```bash
echo "Value is $foo" # Outputs: Value is bar
echo 'Value is $foo' # Outputs: Value is $foo
```

### 📝 Variable Expansion

- **Single Quotes (`'`)**: Treats everything literally, does not expand variables.
- **Double Quotes (`"`)**: Expands variables and special characters.

---

## 🔄 Control Flow in Zsh

### 🔁 Loops (`for`, `while`)
Zsh loops allow iteration over lists and condition-based execution.

```bash
for file in *.txt; do
    echo "Processing $file"
done
```

### Loops in Shell Scripts
```bash
for i in {1..5}; do
  echo "Iteration $i"
done
```

```bash
for i in $(seq 1 5); do
    echo hello
done
```

```bash
while [[ condition ]]; do
    # commands
    break  # exits the loop
    continue  # skips iteration
    sleep 1  # waits 1 second

done
```

####  📝 Exercises

1️⃣ Create a loop that prints "Zsh is awesome!" five times.

2️⃣ Modify the loop to print the current iteration number.

3️⃣ Find and list all .sh files in the current directory using a for loop.


### ✅ Conditional Statements (`if`)
Zsh supports conditionals using `if`, `case`, and `test` expressions.

```bash
if [[ "$foo" == "bar" ]]; then
    echo "foo is bar"
else
    echo "foo is not bar"
fi
```

```bash
if [ -f "file.txt" ]; then
  echo "File exists."
else
  echo "File does not exist."
fi
```

**Example: 🔍 Testing File Types**

To only print directories:
```bash
for f in $(ls); do
    if test -d "$f"; then
        echo "dir $f"
    fi
done
```

Additional information to above:
```bash
if CONDITION; then BODY; fi
```
- `CONDITION` is a command, if it returns exit status `0 (success)`, then `BODY` is run.

- Can also include `else` or `elif` for additional conditions.

- `test` is another program that provides various checks and comparisons, exiting with `0` if they’re true `($?)`.

- Try `man test` for more details.

- `test` can also be invoked with brackets: `[ -d "$f" ]`.

---

## Argument Splitting

Zsh splits arguments by whitespace and this is not always the desired behavior.

If a file contains spaces (e.g., `My Documents`), `for f in $(ls)` expands incorrectly:
```bash
for f in $(ls)  # Expands to: for f in My Documents
```
Same issue applies to `test -d $f`; if `$f` contains spaces, `test` will error!

This leads to incorrect parsing, testing each word separately. Biggest **source of bugs in shell scripts**!

## 🛠 Fixing Argument Splitting Issues

To avoid incorrect splitting:
**quote all use of variables that you don’t want split**!

- `for f in "My Documents"` would work correctly :)

*Warning!*

Using `for f in "$(ls)"` might seem like a solution, but it introduces more problems. The command substitution `$(ls)` replaces itself with a single string containing all filenames, separated by newlines (The command substitution `$(ls)` executes `ls`, capturing its output as a single string). However, if a filename contains a space, it will still be split incorrectly.


**To avoid incorrect splitting**:

```bash
for f in *; do
    if [ -d "$f" ]; then
        echo "dir $f"
    fi
done
```

✅ Globbing as a Solution

Zsh understands patterns for file searching:

- `*` → Any string of characters

- `?` → Any single character

- `{a,b,c}` → Any of these characters

**Examples**:

```bash
for f in *; do  # All files in this directory
    echo "$f"
done

for f in a*; do  # All files starting with "a"
    echo "$f"
done

for f in foo/*.txt; do  # All .txt files in "foo" directory
    echo "$f"
done

for f in foo/*/p??.txt; do  # Three-letter .txt files starting with "p" in subdirectories of foo
    echo "$f"
done

```

**Important**: Always quote variables when using them in conditions!
```bash
if [ -d "$f" ]; then echo "Directory: $f"; fi
```

🚨 **More Whitespace Issues**

Whitespace issues don't stop with loops! Consider:
```bash
if [ $foo = "bar" ]; then
```

If `$foo` is empty, the condition expands to `[ = "bar" ]`, which is invalid.

Workarounds:

- Use `[ x$foo = "xbar" ]` (not ideal but works).

- Instead, prefer `[[` which is a built-in comparator:
```bash
if [[ $foo == "bar" ]]; then
    echo "Foo is bar"
fi
```

- `[[ ... ]]` provides better syntax handling (e.g., avoiding word splitting issues).

- Allows `&& (AND)` and `|| (OR)` instead of `-a` and `-o`.

✅ Numeric Comparators
```bash
if [[ $num -gt 10 ]]; then
    echo "Number is greater than 10"
fi
```
- `-gt` (greater than)
- `-lt` (less than)
- `-ge` (greater than or equal to)
- `-le` (less than or equal to)

---

### Exercises

1️⃣ Write a script that checks if a file exists and prints whether it is a file or directory (`file_path="/path/to/file"`).

2️⃣ Fix the following buggy script that fails when filenames have spaces.
(✅ Hint: Ensure correct argument splitting by quoting variables.)

3️⃣ Create a script that takes an argument and checks if it matches a specific string (e.g., "hello").


## ✨ Globbing in Zsh

Globbing allows for powerful pattern matching in Zsh, making it easier to work with multiple files and directories. This feature is essential for scripting and command-line efficiency.

🎯 Wildcards for Filename Expansion (as in the examples above)

- `*` → Any string of characters

- `?` → Any single character

- `{a,b,c}` → Any of these characters

```bash
echo *.txt  # List all .txt files
echo ??.sh  # Match two-character filenames ending in .sh
```

```bash
rm foo?  # Deletes foo1, foo2 (but not foo10)
rm foo*  # Deletes all files starting with "foo"
```

📦 Curly Braces {} for Expansion

Curly braces {} help expand common substrings in multiple commands automatically.

```bash
convert image.{png,jpg}  # Expands to: convert image.png image.jpg
cp /source/{file1,file2}.txt /destination/  # Expands into two copy commands
```

**More Examples**:
```bash
cp /path/to/project/{foo,bar,baz}.sh /newpath

# Expands to:
# cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

mv *{.py,.sh} folder  # Moves all .py and .sh files into 'folder'
```

### 🔗 Combining Globbing Techniques

Globbing can be used in combination with other commands to improve efficiency:
```bash
mkdir foo bar
touch foo/x bar/y

touch {foo,bar}/{a..h}
# Creates files: foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h

```

---

### Exercises on Globbing

1️⃣ List all .txt and .sh files in the current directory.

2️⃣ Write a script to move all .log files from the current directory to a logs folder.

3️⃣ Use globbing to create multiple files at once and then list them.

---

## 🔄 Command & Process Substitution

Command substitution allows you to store the output of a command into a variable or use it directly within another command.
Whenever you use `$( CMD )`, the shell first executes `CMD`, captures its output, and substitutes it in place.

✅ Examples:
```bash
for file in $(ls); do
    echo "Processing $file"
done
```
```bash
date_now=$(date)
echo "Current date: $date_now"
```

Process substitution is useful when a command expects file input instead of standard input. It executes `CMD`, writes its output to a temporary file, and substitutes `<( CMD )` with that file's name.

```bash
diff <(ls foo) <(ls bar)  # Compare file listings of two directories
```
```bash
# Process substitution
cat <(ls -l) <(date)
```

```bash
# Process substitution
cat <(ls)
cat <(ls) <(ls ..)
```

**Advanced Example**: Comparing Boot Logs

```bash
diff <(journalctl -b -1 | head -n20) <(journalctl -b -2 | head -n20)
```
- `journalctl` is a command-line utility used in Linux systems that utilize systemd for managing and querying the system log (journal). It provides a way to view, filter, and analyze system logs generated by `systemd-journald`.
- `journalctl -b -1 | head -n20` → Fetches the first 20 lines of the last boot log.
- `journalctl -b -2 | head -n20` → Fetches the first 20 lines of the boot log before that.
- `diff` then highlights the differences between these logs.

### Exercise

Write a script that counts the number of files in a directory using `$(ls | wc -l)` and prints the result.

---

## 🔹 Functions in Zsh
Zsh allows defining functions that can take arguments and execute blocks of code.

```bash
function greet() {
  echo "Hello, $1!"
}
# greet Alice
```

```bash
mcd () {
    mkdir -p "$1"
    cd "$1"
}
```

In this example:
- `$1` represents the first argument passed to the function.
- `mkdir -p` ensures that the directory exists before attempting to `cd` into it.

Put everything into script, update shell and run script with the function:

```bash
nano mcd.sh
source mcd.sh
mcd test
```

---

## ⚙️ Special Variables in Zsh
Zsh has built-in variables for script execution and argument handling.

| Variable | Description |
|----------|-------------|
| `$0` | Name of the script |
| `$1` - `$9` | Positional parameters (arguments) |
| `$@` | All arguments as a list |
| `$#` | Number of arguments |
| `$?` | Exit status of the last command |
| `$$` | Process ID of the script |
| `!!` | Last executed command |
| `$_` | Last argument from the previous command |

Comprehensive list of variables is [here](https://tldp.org/LDP/abs/html/special-chars.html).

---

## 📌 Exit Codes and Operators
Zsh scripts rely on **exit codes**. Exit codes can be used to conditionally execute commands using `&&` (`and` operator) and `||` (`or` operator). Commands can also be separated within the same line using a semicolon `;`. The `true` program will always have a `0` return code and the `false` command will always have a `1` return code.

```bash
false || echo "Oops, fail"
# Executes echo because false returns non-zero

true && echo "Success"
# Executes echo because true returns 0

true || echo "Will not be printed"
#

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run

```

To chain multiple commands on the same line, use `;`:

```bash
true ; echo "This will always run"
false ; echo "This will always run"
```

---

## 🛠 Example: Zsh Script for File Processing
This script iterates over files, searches for "foobar", and adds a comment if it's not found.

```bash
#!/bin/zsh
echo "Starting program at $(date)"
echo "Running program $0 with $# arguments and PID $$"

for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    if [[ $? -ne 0 ]]; then
        echo "File $file does not contain 'foobar', adding it"
        echo "# foobar" >> "$file"
    fi
done
```

---

### Exercise 1)

> Write a bash script that processes a list of text files provided as arguments.
> For each file, the script should:

1. ✅ Check if the file contains the string `"TODO"`.
2. ✅ If the string is not found, append a line `# TODO` to the end of the file.
3. ✅ Log the actions taken, including timestamps and process information.

This exercise will help you understand **command substitution, loops, conditionals, exit statuses,** and **output redirection** in bash scripting.

---

### ⚡ Optional Challenge

**Modify the script to:**

- 🔢 Keep a count of how many files were processed.
- 📌 Report how many files had `"TODO"` added.
- 📜 Log all actions to a separate log file with timestamps.

💡 **Tip:** Use `grep`, `if` conditions, `echo`, `>>` (append operator), and `date` for logging! 🖥️

### Exercise 2)

Create a script called `slow_seq.sh` with the following contents and do `chmod +x slow_seq.sh` to make it executable.
```bash
   #! /usr/bin/env bash

for i in $(seq 1 10); do
  echo $i;
  sleep 1;
done
```

There is a way in which pipes (and process substitution) differ from using subshell execution, i.e. `$()`. Run the following commands and observe the differences:

```bash
./slow_seq.sh | grep -P "[3-6]"
grep -P "[3-6]" <(./slow_seq.sh)
echo $(./slow_seq.sh) | grep -P "[3-6]"
```

---

## Operators in Shell Scripts

Operators are fundamental components of Shell scripting. They allow us to perform arithmetic operations, comparisons, logical evaluations, file manipulations, and more. Understanding operators is essential for writing efficient and functional Shell scripts.

🔢 Arithmetic Operators

```bash
var1=10
var2=5
sum=$((var1 + var2))
echo "Sum: $sum"
```
🔍 Relational (Comparison) Operators

```bash
a=10
b=20
if [ "$a" -lt "$b" ]; then
  echo "$a is less than $b"
fi
```
🔄 Logical Operators

```bash
a=10
b=5
if [ "$a" -gt 0 ] && [ "$b" -gt 0 ]; then
  echo "Both numbers are positive"
fi
```

✏️ Assignment Operators

```bash
count=10
count+=5
echo "Count: $count"  # Output: Count: 15
```

🔤 String Operators

```bash
str1="Hello"
str2="World"

if [ "$str1" != "$str2" ]; then
  echo "Strings are different"
fi
```

## 📌 Summary

### Operator Types and Their Symbols

### 🔢 Arithmetic Operators
| Operator | Description |
|----------|------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus (Remainder) |
| `**` | Exponentiation |

### 🔗 Relational Operators
| Operator | Description |
|----------|------------|
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-gt` | Greater than |
| `-lt` | Less than |
| `-ge` | Greater than or equal to |
| `-le` | Less than or equal to |

### 🧠 Logical Operators
| Operator | Description |
|----------|------------|
| `&&` | Logical AND |
| `\|\|` | Logical OR |
| `!` | Logical NOT |

### 📝 Assignment Operators
| Operator | Description |
|----------|------------|
| `=` | Assignment |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |

### 🔧 Bitwise Operators
| Operator | Description |
|----------|------------|
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `<<` | Left shift |
| `>>` | Right shift |

### 📂 File Test Operators
| Operator | Description |
|----------|------------|
| `-e` | Check if file exists |
| `-f` | Check if it's a file |
| `-d` | Check if it's a directory |
| `-r` | Check if readable |
| `-w` | Check if writable |
| `-x` | Check if executable |

### 🔠 String Operators
| Operator | Description |
|----------|------------|
| `=` | String equality |
| `!=` | String inequality |
| `-z` | Check if string is empty |
| `-n` | Check if string is not empty |

---

### Exercises

1. **Arithmetic Operators:**
   - Write a bash script that takes two numbers as input and performs all arithmetic operations (`+`, `-`, `*`, `/`, `%`, `**`) on them.
   - Example:
     ```bash
     ./arithmetic.sh 10 5
     ```
     **Expected Output:**
     ```
     Addition: 15
     Subtraction: 5
     Multiplication: 50
     Division: 2
     Modulus: 0
     Exponentiation: 100000
     ```

2. **Relational Operators:**
   - Write a script that takes two numbers and compares them using `-eq`, `-ne`, `-gt`, `-lt`, `-ge`, and `-le`.
   - Example:
     ```bash
     ./compare.sh 10 5
     ```
     **Expected Output:**
     ```
     10 is greater than 5
     ```

---

## 🎯 Functions vs. Scripts in Zsh

Writing Zsh scripts can be tricky and unintuitive. There are tools like shellcheck that will help you find errors in your sh/Zsh scripts.

Note that scripts need not necessarily be written in bash to be called from the terminal. For instance, here’s a simple Python script that outputs its arguments in reversed order:

```bash
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```

The kernel knows to execute this script with a Python interpreter instead of a shell command because we included a `shebang` line at the top of the script. It is good practice to write `shebang` lines using the `env` command that will resolve to wherever the command lives in the system, increasing the portability of your scripts. To resolve the location, `env` will make use of the `PATH` environment variable. For this example, the shebang line would look like:

```bash
#!/usr/bin/env python
```

### Exercises

Create a Python script that reverses its command-line arguments and can be executed directly from the terminal without explicitly invoking the Python interpreter.
Since Python is installed using `pyenv`, the interpreter's location is not the default, and you need to determine the correct path for the shebang (`#!`) line.

---

🔍 Finding the Python Interpreter Path

To find the correct Python path for the shebang line, run:

```bash
which python
```

The output should be a path within your `.pyenv` directory, such as:
```bash
/home/yourusername/.pyenv/shims/python
```

## 🔹 Key Differences Between Shell Functions and Scripts

Some differences between shell functions and scripts that you should keep in mind are:

- Functions have to be in the same language as the shell, while scripts can be written in any language. This is why including a `shebang` for scripts is important.

- Functions are loaded once when their definition is read. Scripts are loaded every time they are executed. This makes functions slightly faster to load, but whenever you change them you will have to reload their definition.

- Functions are executed in the current shell environment, whereas scripts execute in their own process. Thus, functions can modify environment variables (e.g., change your current directory), whereas scripts can’t. Scripts will be passed by value environment variables that have been exported using export.

As with any programming language, functions are a powerful construct to achieve modularity, code reuse, and clarity of shell code. Often, shell scripts will include their own function definitions.

---


## 🚀 Best Practices in Zsh Scripting
✅ Use `#!/usr/bin/env zsh`
To improve script portability, use the following shebang:

```bash
#!/usr/bin/env zsh
```

✅ Debugging with `set`
Enable debugging and error handling using:

```bash
set -e  # Exit on first error
set -x  # Print each command before executing it
```

✅ Use `shellcheck` to Lint Scripts
[`shellcheck`](https://www.shellcheck.net/) helps identify syntax errors in Zsh scripts.

```bash
shellcheck my_script.zsh
```

## 🎯 Summary
- Zsh scripting automates command-line tasks and enhances efficiency.
- Zsh scripts use variables, control structures, and functions to perform complex operations.
- Proper use of globbing, substitution, and debugging ensures robust scripting.

🚀 **Happy Z Shell Scripting!** 🚀

---

## 📚 Additional Resources

- [Command Line Challenges](https://cmdchallenge.com/)
- [Linux Shell Scripting](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/)
- [Learn Shell Process Substitution](https://www.learnshell.org/en/Process_Substitution)

---
