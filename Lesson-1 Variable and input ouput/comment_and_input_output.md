# Input & Output

## Comments

Comments are ignored by Python and are used to explain code.

### Single-line Comment
```python
# This is a comment
```

### Multi-line Comment
```python
"""
This is a
multi-line comment
"""
```

> 💡 Multi-line comments are commonly written using triple quotes (`'''` or `"""`).

---

## Input

`input()` is used to take input from the user.

### Syntax

```python
input()
```

### Store Input in a Variable

```python
name = input()
```

### Input with a Message

```python
name = input("Enter your name: ")
```

---

## Important

`input()` **always returns a string**.

```python
age = input("Enter age: ")

print(type(age))
# Output: <class 'str'>
```

Use type conversion when you need numbers.

```python
age = int(input("Enter age: "))
```

---

## Output

`print()` is used to display output.

```python
print("Hello World")
```

---

## Printing Variables

```python
name = "Shadab"
age = 20

print("My name is", name)
print("My age is", age)
```

---

## Formatted String (f-string)

Best way to print variables inside text.

### Syntax

```python
f"...{variable}..."
```

### Example

```python
name = "Shadab"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

✅ Easy to read.
✅ Preferred in modern Python.

---

## sep

Changes the separator between values.

```python
print("Python", "Java", "C++", sep=" | ")
```

Output

```
Python | Java | C++
```

### Is `sep` useful?

✅ Yes, but mostly for formatting output.

Examples:
- CSV data
- Logs
- Reports
- Custom output formatting

For everyday coding, you'll use it occasionally—not as often as `print()` or f-strings.

---

## end

By default, `print()` ends with a new line (`\n`).

Use `end=""` to change it.

```python
print("Hello", end=" ")
print("World")
```

Output

```
Hello World
```

---

## Common Mistakes

❌

```python
age = input()
print(age + 5)
```

✅

```python
age = int(input())
print(age + 5)
```

---

## Interview Nugget ⭐

- `input()` always returns a **string**.
- Prefer **f-strings** over string concatenation.
- `sep` changes the separator.
- `end` changes what `print()` adds at the end.

---

## 30-Second Revision

- `#` → Single-line comment
- `""" """` → Multi-line comment
- `input()` → Takes user input
- Input is always **string**
- `print()` → Displays output
- `f""` → Best way to print variables
- `sep` → Change separator
- `end` → Change line ending