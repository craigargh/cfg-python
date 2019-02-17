# Setup

This part of the guide will explain how to install the software required for the course. It will show you how to install:

- Python 3
- Git
- PyCharm Community Edition

I'll also show you how to create a new PyCharm project and test that everything is installed OK.

## Python 3

Python is frequently updated. Some older versions of Python, such as version 2.7, are no longer supported. Even if you already have a version of Python installed you should follow these instructions to install an up to date version of Python.

In a web browser go to [https://www.python.org/downloads/](https://www.python.org/downloads/)

Click on the button that says `Download Python 3` (the number on the button might say something like 3.7.2 instead).

The installer for Python should now download. Once the download is complete, open the installer. Tick the `Add Python 3.7 to PATH` box and click `Install Now`.

## Git

Git is a tool that is used by developers to share and collaborate when writing programs. You will need to install git for sesison 5 and your group project. 

To install Git, open your web browser and go to [https://git-scm.com/download/](https://git-scm.com/download/). Select your operating system and click on the download link for 64-bit.

Once the installer has download, open it and follow the instructions

## PyCharm

When writing Python programs there are a lot of programs you can use. Some developers like to use text editors like Sublime Text or Atom, others prefer powerful (yet complicated) editors like Vim or Emacs. For this course you will be writing and running your Python programs with PyCharm.

PyCharm is an editor that is designed specifically for Python. It comes with lots of built-in tools that help you work with Python (for example it can highlight typos in your code).

To install PyCharm, go to [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)

There are two versions of PyCharm. You will be using the free Community Edition for this course. Click the `Download` button under the Community Edition. The installer should now download.

Once the installer has downloaded, run it and follow the instructions to install PyCharm.


## Creating a PyCharm Project and Testing the Installations

So that you're prepared for the first session, we're going to create a new PyCharm project and check that Python has installed correctly.

> If you have any problems, double check that you've followed the installation instructions correctly. After doing this if there are still issues with the installation make sure you tell the instructors when at the very start of the first session and they should be able to help you.

Open PyCharm. You should see a window like the one below:

![](/home/craig/Documents/workspace/cfg-python/course_handbook
/images/pycharm_landing.png)

Click on the `Create New Project` button. 

On the next screen in the `Location:` field name your project `cfg-python`. You need to do one more thing before clicking `Create`.

You also need to make sure you're project will use the correct version of Python. Click on the `Project Interpreter: New Virtual Environment` dropdown to see more option for your project.

In the `Base interpreter` field click the drop-down and select `Python 3.7`. 

![](/home/craig/Documents/workspace/cfg-python/course_handbook
/images/new_project.png)

Click `Create` to start your project.

PyCharm will now create the project. You may need to wait a while depending on the speed of your computer. There might be a progress bar at the bottom-right of the PyCharm window, which you can follow the progress.

Once the new project is ready, it's time to check that Python is working correctly. We'll use a tool called the *terminal*.

On the menu bar at the top of the screen click on `View > Tool Windows > Terminal`.

You should see the terminal panel pop-up at the bottom of the window.

In that window type `python --version` and press enter to check which version of Python you are using. The output should look similar to this:

```bash
Python 3.7.2
```

> If you the output says you are using Python 2.7 or earlier you will need to check two things. First check that you downloaded and installed Python in the step earlier. If you definitely did this you may have selected the wrong option when creating your project. Go to `File > New Project` and follow the Creating a PyCharm Project instructions above

Next type `git --version` and press enter to check that Git is installed. The output should look something like this


```bash
git version 2.17.1
```


This is just to check the installation is OK, the version of Git is not important here.

You should now be ready for the first session. Remember, if you have any trouble with the setup instructions let your instructors know at the very start of the first session.

I hope you enjoy the course!
