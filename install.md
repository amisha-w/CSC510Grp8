## Installing a Python distribution for Greeter

This document gives the instructions to install a Python distribution with all dependencies required by the [Greeter](https://github.com/amisha-w/CSC510Grp8).

Check if Python is installed
Run the following command to test if python is installed or not. [If not click here.](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)
  ```
  python --version
  ```
  If it is installed, You will see something like this:

  ```
  Python 3.10.6

  ```

## Download and Install Pip 

The PIP can be downloaded and installed using the command line by going through the following steps:
### Method 1: Using cURL in Python

Step 1: Open the cmd terminal

Step 2: In python, a curl is a tool for transferring data requests to and from a server. Use the following command to request:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

    python get-pip.py
    
### Method 2: Manually install PIP on Windows

Pip must be manually installed on Windows. You might need to use the correct version of the file from pypa.org if you’re using an earlier version of Python or pip. Get the file and save it to a folder on your PC.

Step 1: Download the get-pip.py (https://bootstrap.pypa.io/get-pip.py) file and store it in the same directory as python is installed.

Step 2: Change the current path of the directory in the command line to the path of the directory where the above file exists. 

Step 3: get-pip.py is a bootstrapping script that enables users to install pip in Python environments. Run the command given below:

```
python get-pip.py
```

Step 4: Now wait through the installation process. Voila! pip is now installed on your system.

## Verification of the installation process

One can easily verify if the pip has been installed correctly by performing a version check on the same. Just go to the command line and execute the following command:

```
pip -V
or
pip --version
```

## Advanced details

### Dependencies

The following libraries are required:

* atomicwrites==1.4.1
* attrs==22.1.0
* colorama==0.4.5
* iniconfig==1.1.1
* packaging==21.3
* pluggy==1.0.0
* py==1.11.0
* pyparsing==3.0.9
* pytest==7.1.2
* tomli==2.0.1

## 📀 Install now!
```bash
pip install -m requirements.txt
```
## Then run setup.py