# Session One

## Git & .gitignore

### What is .gitignore?

.gitignore is a file that tells git which files to ignore. It is a plain text file that contains a list of files and directories that git should ignore. It is a very useful file to have in your project directory.

### How to use .gitignore?

Create a file called .gitignore in the root directory of your project. Add the files and directories that you want git to ignore to this file. For example, if you want to ignore all files with the extension .pyc, you can add the following line to the .gitignore file:

```.gitignore
*.pyc
```

You can also ignore directories by adding the directory name to the .gitignore file:

```.gitignore
venv  # also, venv/ or venv/*
```

You can keep some specific files from being ignored by adding an exclamation mark (!) before the file name:

```.gitignore
*.pyc
!main.pyc
```

## Venv and Virtual Environments

### What is a virtual environment?

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

### How to create a virtual environment?

To create a virtual environment, you need to install the `virtualenv` package. You can do this by running the following command:

```bash
pip install virtualenv
```

Once you have installed the virtualenv package, you can create a virtual environment by running the following command:

```bash
virtualenv venv
```

This will create a directory called venv in your current directory. You can specify a different directory by running the following command:

```bash
virtualenv <directory_name>
```

You can also use the -p flag to specify the Python interpreter to use. For example, if you want to use Python 3.6, you can run the following command:

```bash
virtualenv -p python3.6 venv
```

You can create a virtual environment using the `venv` module that comes with Python 3.3 and above. To create a virtual environment using the venv module, you need to run the following command:

```bash
python3 -m venv venv
```

In Windows, you need to run the following command:

```bash
py -m venv venv
```

**\[!] Note:** The `venv` module is rather slow, prone to failure, and is not recommended for production use. It is recommended to use the `virtualenv` package instead.

### How to activate a virtual environment?

To activate a virtual environment, you need to run the following command:

```bash
source venv/bin/activate
```

In Windows, you need to run the following command:

```bash
venv\Scripts\activate
```

### How to deactivate a virtual environment?

To deactivate a virtual environment, you need to run the following command:

```bash
deactivate
```

## Linked Lists

### What is a linked list?

A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty, then the head is a null reference.

### How to create a linked list?

Refer to the [Linked list implementation](linked_list.py) file.

### Complexity analysis

| Operation | Complexity | Arrays Complexity |
| --------- | ---------- | ----------------- |
| Access    | O(n)       | O(1)              |
| Search    | O(n)       | O(n)              |
| Insertion | O(1)       | O(n)              |
| Deletion  | O(1)       | O(n)              |

**\[!] Note:** The complexity of the linked list operations is O(n) because we need to traverse the list to find the element. In the case of arrays, the complexity is O(1) because we can directly access the element using the index (pointer arithmetic).

## Databases

### What is a database?

A database is an organized collection of data. It is used to store, manage and retrieve large amounts of data efficiently.

### Why do we need databases?

Databases are used to store data in a structured format. They are used to store data that is used by multiple applications. They are also used to store data that is used by multiple users.

### Serialize and Deserialize

Serialization is the process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file. Its main purpose is to save the state of an object in order to be able to recreate it when needed. The reverse process is called deserialization.

Strategy | Pros | Cons
---------|------|-----
JSON | Human readable, Easy to Produce | Not secure, Wasteful
CSV | Easy to read and write | Not secure, Wasteful
Protocol Buffers | Fast and efficient | Hard to read and write
