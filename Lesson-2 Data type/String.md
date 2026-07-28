# Strings

## What is a String?

A **string** is a sequence (group) of characters used to store text.

```python
name = "Shadab"
```

---

## Important: Strings are Immutable ⭐

Once a string is created, **it cannot be modified**. Any operation that changes a string creates a **new string** instead.

### Why are strings immutable?

- ✅ Safer when multiple parts of a program use the same string (concurrency).
- ✅ Saves memory by allowing Python to reuse identical strings.

Example:

```python
s = "shadab"

s[0] = "b"      # ❌ Error
```

---

# Creating Strings

Using single quotes

```python
name = 'Shadab'
```

Using double quotes

```python
name = "Shadab"
```

Using triple quotes (multi-line strings)

```python
message = '''
Hello
Welcome to Python
'''
```

> `'` and `"` are generally used for single-line strings, while `'''` or `"""` are used for multi-line strings.

---

# Indexing

Each character has an index.

```python
name = "Shadab"

print(name[0])
```

Output

```
S
```

If the index is out of range, Python raises an **IndexError**.

```python
print(name[12])
```

```
IndexError: string index out of range
```

---

## Index Range

### Positive Index

```
0 → length - 1
```

### Negative Index

```
-length → -1
```

Example:

```python
name = "Python"

print(name[-1])
```

Output

```
n
```

---

# String Concatenation

Join strings using `+`.

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output

```
Hello World
```

---

# Length of a String

Use `len()`.

```python
name = "Shadab"

print(len(name))
```

---

# Slicing

Syntax

```python
string[start:end]
```

- Start → Included ✅
- End → Excluded ❌

Example

```python
name = "Shadab"

print(name[1:4])
```

Output

```
had
```

---

## Slice Shortcuts

From a specific index to the end

```python
name[2:]
```

From the beginning to a specific index

```python
name[:4]
```

Negative slicing also works.

```python
name[-4:-1]
```

---

# Common String Methods

## upper()

Converts all characters to uppercase.

```python
name.upper()
```

---

## lower()

Converts all characters to lowercase.

```python
name.lower()
```

---

## capitalize()

Capitalizes only the first letter.

```python
name.capitalize()
```

---

## strip()

Removes leading and trailing spaces.

```python
name.strip()
```

---

## replace()

Replaces one substring with another.

```python
text = "I like Python"

print(text.replace("Python", "Java"))
```

Output

```
I like Java
```

Replace only a specific number of occurrences.

```python
text = "Hi Hi Hi"

print(text.replace("Hi", "Hello", 2))
```

Output

```
Hello Hello Hi
```

---

# Escape Characters

| Escape Character | Meaning |
|------------------|---------|
| `\n` | New line |
| `\t` | Tab space |
| `\'` | Single quote |

Example:

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

# Interview Notes ⭐

- Strings are **immutable**.
- Index starts from **0**.
- Maximum positive index = `length - 1`.
- Negative indexing starts from `-1`.
- Slicing includes the **start** index but excludes the **end** index.
- `replace()` returns a **new string**; it does not modify the original.

---

# Methods You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `len()`
- `upper()`
- `lower()`
- `strip()`
- `replace()`

⭐⭐⭐ Good to Know

- `capitalize()`

---

# 30-Second Revision

- String = Sequence of characters
- Immutable
- `'`, `"`, `''' '''`
- Positive & Negative Indexing
- `len()` → Length
- `+` → Concatenation
- `[start:end]` → Slicing
- `upper()`, `lower()`, `capitalize()`
- `strip()` → Remove extra spaces
- `replace(old, new, count)` → Replace text
- `\n`, `\t`, `\'` → Escape characters