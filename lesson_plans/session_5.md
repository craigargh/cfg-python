# Session Title: Files, Pip and APIs

Session No: ???
 
## Learning Objectives:

By the end of this session students will be able to:

- Write programs that read and write to files
- Explain the purpose of the pip package manager
- Gather data using web APIs


## Session Outline

Please do not change the intro and closing blocks - feel free to add more session blocks as you see fit.


## Intro & Framing

This session focuses on working with files and making requests to Web APIs. 

In the first part of this session, students will learn how to read and write data to text files. They will also learn how to read and write to csv files, which is particularly relevant for students that want to learn more about data science.

The second part of this session focuses on making requests to Web APIs. Students are introduced to the pip package manager, which is used to install third-party packages from PyPI. They will use the requests module to make requests to the Pokemon API, a free API that provides stats about different Pokemon.

This session intentionally covers less content than the previous sessions. This is so that you can either:
- Cover any content that you missed from previous sessions
- Start team projects early

## Block 1: Reading and Writing Files

5 minutes

This block covers reading and writing files with Python. When demonstrating the code to students make sure you draw attention to the following:
- The `with` and `as` keywords
- The file permissions argument for the `open()` function ('r' for read and 'w+' for write)
- Using the `open()` function in the `with` block automatically closes the file at the end of the block

### Relevant Exercise(s):

Exercise 5.1: 10 minutes
- Students will create a todo list program that allows users to add items to a file
- Steps are provided to help the students
- Students should manually create a `todo.txt` in the same directory as their program before running the program
- Make sure you also create the `todo.txt` file before running the solution

## Block 2: Working With CSV Files

5 minutes

This section builds on the previous one to show students how to read and write csv files. CSV is a format for spreadsheets. If students are interested in data science or want to know how to automate part of their job, they might find this particularly useful.

### Relevant Exercise(s):

Exercise 5.2: 10 minutes
- 

## Block 3: Pip Package Manager

5 minutes

This block introduces students to the pip package manager. The Pip package manager is used to help install third-party packages so that they can be used in Python prorgams. Having access to a wide variety of packages is one of the reasons that Python is so popular. Third-party packages mean that programmers can reuse code that someone else has written to do a specific task, meaning that they don't have to write it themselves.

### Relevant Exercise(s):

N/A

## Block 4: ??? 

10 minutes

This final block introduces students to the requests library. The requests library allows your Python code to communicate with external Web APIs. Web APIs can be used to retrieve data from specific places on the internet.

To practice interacing with Web APIs, students will write a short program to get information from the Pokemon API. The Pokemon API stores data about every Pokemon in the Pokemon series of games. It is designed for teaching beginners and does not require authentication. You may need to explain what Pokemon are to students.

It is important for students to understand how to use the requests package as it is the most used Python package outside of the standard library.

Some students using Macs may have an error about when using the requests library. This might be because their version of OpenSSL is out of date. They can fix this by installing a newer version of OpenSSL

### Relevant Exercise(s):

Exercise 5.3: 10 minutes
- Students will use the Pokemon API and requests library to retrieve data about a specific Pokemon
- Students should refer back to the example code
- Extension: Print the names of all of a specific Pokemon's moves
- The API urls can be viewed in Firefox to make the JSON responses easier to read


## Recap & Closing
How can you get the learners to articulate what they learned today, celebrate what they achieved and inform them what they need to do as homework?

Recap questions:
- ???


## Homework Tasks

Learning Task: 
Which exercise will help all students recap what they have learnt and prepare for the next session?

???


Extended Learning Task:
Which exercise will help students push their learning from today a step further?

???

## Guide for Instructors 

General comments
-
