# C Bit Mask Maker
## Description
This is a simple Python script for creating and saving bitmasks for C. The program prompts you to select which bits you would like to set and at which positions (multiple bits can be added at once). Very little error-handling is done here, but hopefully the prompts will make it clear exactly how to format your inputs. Chances are this is the one and only commit for this project, but I may add more features later (new languages, edit old bitmasks).

## Compatibility and Dependencies
I wrote this for personal use, so currently, it is tested on Linux (though MacOS may be compatible...). It is dependent on Python and pipx, so ensure these are installed.

## Installation
The installer uses pyinstaller to create a binary in the system. You can download and run the installer using the following commands:
```
git clone https://www.github.com/stephen-daq/maskmaker.git/
cd maskmaker
chmod +x install
./install
```
or, if you like a one-time copy paste like me,
```
git clone https://www.github.com/stephen-daq/maskmaker.git/; cd maskmaker; chmod +x install; ./install
```
