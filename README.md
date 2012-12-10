RenrenRecipies
==============

# What is this

Tools for hacking RenRen(Chinese social network like Facebook) API with OAuth and without OAuth

# How to use it 

This tool needs **requests** package:

`sudo pip install requests`

1.    First, clone the source code on your local machine.

      `git clone https://github.com/stephenLee/RenrenRecipies.git`


2.    `python renren.py -h`

     usage: renren.py [-h] user password

     Friends collections command line tool for Renren

     positional arguments:
     
     user        your Renren username
     
     password    your Renren password

    optional arguments:
    
    -h, --help  show this help message and exit
    
    `python renren.py user password` will create a json file called friends.json about your Renren friends.
    
3.  using **d3.js** visualizing friends. At the project dir, type:

    `python -m SimpleHTTPServer`
    
    open your browser, at the 127.0.0.1:8000 address.
    


Hope this helpful for you!


