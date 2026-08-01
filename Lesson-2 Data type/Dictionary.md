# Dictionaries

## What is a Dictionary?

A **dictionary** stores data in **key-value pairs**.

```python
student = {
    "name": "Steve",
    "age": 32
}
```

---

## Properties

- Stores data as **key : value** pairs.
- Keys must be **unique**.
- Keys must be **immutable** (e.g., `int`, `str`, `tuple`).
- Values can be of any data type.
- Dictionaries are **mutable** (you can add, update, or delete items).

---

# Creating a Dictionary

Using `{}`

```python
student = {
    "name": "Steve",
    "age": 32
}
```

---

## Using `dict()` Constructor

```python
student = dict(
    name="Steve",
    age=32,
    country="India"
)

print(student)
```

Output

```python
{'name': 'Steve', 'age': 32, 'country': 'India'}
```

> **Note:** When using `dict()`, keys are written like variable names.
>
> ```python
> dict(True="Ram")   # ❌ Invalid
> ```
>
> `True` is a Python keyword, so it cannot be used as a keyword argument.

---

# Why does this happen?

```python
d = {
    1: "Sam",
    2: "Steve",
    True: "Ram"
}

print(d)
```

Output

```python
{1: 'Ram', 2: 'Steve'}
```

### Why?

In Python,

```python
1 == True
```

returns

```python
True
```

Python treats `1` and `True` as the **same key** because they are equal.

So when it sees:

```python
True: "Ram"
```

it **updates the value of key `1`** instead of creating a new key.

> **Remember:** If two keys are equal, the latest value replaces the previous one.

---

# Accessing Elements

Use the key to get its value.

```python
student = {
    "name": "Steve",
    "age": 45
}

print(student["name"])
```

Output

```
Steve
```

---

# Dictionary Methods

## keys()

Returns all keys.

```python
student = {
    "name": "Steve",
    "age": 45
}

print(student.keys())
```

Output

```python
dict_keys(['name', 'age'])
```

---

## values()

Returns all values.

```python
print(student.values())
```

Output

```python
dict_values(['Steve', 45])
```

---

## items()

Returns all key-value pairs as tuples.

```python
print(student.items())
```

Output

```python
dict_items([
    ('name', 'Steve'),
    ('age', 45)
])
```

---

# Adding Elements

Add a new key-value pair.

```python
student = {
    "name": "Steve",
    "age": 32
}

student["country"] = "India"
```

---

# update()

Adds or updates values from another dictionary.

```python
student = {
    "name": "Steve"
}

student.update({
    "age": 32,
    "country": "India"
})

print(student)
```

Output

```python
{
    'name': 'Steve',
    'age': 32,
    'country': 'India'
}
```

---

# Removing Elements

## pop()

Removes an item using its key.

```python
student.pop("age")
```

---

## popitem()

Removes the **last inserted** key-value pair.

```python
student.popitem()
```

---

## del

Deletes a specific key.

```python
del student["country"]
```

Delete the entire dictionary.

```python
del student
```

---

## clear()

Removes all key-value pairs.

```python
student.clear()
```

Output

```python
{}
```

---

# Methods You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `keys()`
- `values()`
- `items()`
- `update()`
- `pop()`

⭐⭐⭐ Good to Know

- `popitem()`
- `clear()`
- `del`

---

# Interview Notes ⭐

- Dictionary stores **key-value pairs**.
- Keys must be **unique** and **immutable**.
- Values can be duplicated.
- Dictionaries are **mutable**.
- `1` and `True` are treated as the same key.
- `update()` adds new keys and updates existing ones.
- `items()` returns key-value pairs as tuples.

---

# 30-Second Revision

- `{key: value}`
- Keys → Unique & Immutable
- Values → Any datatype
- Mutable
- `keys()` → All keys
- `values()` → All values
- `items()` → Key-value tuples
- `update()` → Add/Update
- `pop()` → Remove by key
- `popitem()` → Remove last pair
- `clear()` → Empty dictionary