# Project Title

**SpotifyDaily** is a simple scraping project written in python. It is integrated with google sheets. It scrapes the spotify chart and uploads the data to google spreadsheet using the `Google Drive API`.

---
# Getting Started
Before starting any further, I recommend you to go through this **README.md** file.
I also strongly recommend that you to read this on `github` or `PyCharm`.

---

# Setup and Installation

### You will need:
* python 3.5 or higher
* pip, a package manager for python
* git

The following process is tested in **Ubuntu 16.04**. However, you can always do a quick google search and install everything that is required.

### Installing python, pip and git 
Open terminal and enter the following commands.

    $ sudo apt-get update
    $ sudo apt-get install python3.5    # available on Ubuntu already
    $ sudo apt-get install python3-pip  # pip for python 3
    $ sudo apt-get install git
---

# Cloning the project onto your machine

Before cloning the project to your machine, create a separate directory for the project. You can name it anything you want, but try to make it relevant with the project.

    $ mkdir Spotify-Project
    $ cd Spotify-Project
    $ git clone https://github.com/sagunsh/SpotifyDaily.git

# Setting up Virtual Environment [Optional]
Although not mandatory, virtual environment is the recommended way to install all the python packages. And I happen to be a big fan of virtual environment.

If you are a windows user, you might want to look at [Hitchhiker's Guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Installing virtualenv

    $ sudo pip3 install virtualenv  # pip and pip2 for python2
    
Inside the project directory we just created (i.e. Spotify-Project), create a virtual environment.

    $ virtualenv venv

A new directory called venv will be created. 

### Activating venv
The virtual environemnt can be activated as:

    $ source venv/bin/activate

Once the virtual environment is activated, your terminal will appear something like this.

    (venv) $ 

### Installing package inside venv
We have created a requirements.txt file which contains information about all the packages to install. You can install all the packages for the project with a simple command as:

    (venv) $ cd SpotifyDaily
    (venv) $ pip install -r requirements.txt

In the future if you wish to modify the project, you may need some more packages. In such situations, add them to the requirements.txt file along with the version.
For example:
    
    my-package==2.0.4

If you skipped the virtual environment part, you can simply install all the dependencies with the following command:

    $ cd SpotifyDaily
    $ sudo pip3 install -r requirements.txt
