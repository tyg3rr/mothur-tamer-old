MothurTamer.py and SequenceTamer.py are designed to be used on a linux machine (Mac).
Both codes take a .fasta, .qual, and .xlsx file. You should download the fasta and qual file off
of the finch server. The xlsx file should have your well positions in 
the first column and the name of your samples in the second column. You also want to have Python3 installed.

To easily install Python3, into your terminal copy and paste this:

ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

This installs homebrew. Brew may ask you to do install a couple things, just do what it tells you.
After you have brew installed, type this:

brew install python3

Whoohoo! Now you have python3. Next, you need to install the openpyxl module for python3. To do this, type: 

python3 -m easy_install openpyxl

Done!


SequenceTamer.py changes the names of your samples for you.
MothurTamer.py does what SequenceTamer.py does, as well as runs your sequences through Mothur.

Make sure that the python code is in the same directory as your files, and also make sure that Mothur
is in your path. 

In terminal, to run a script, type ./example.py
You may also just type ./e*.py if example.py is the only script that starts with an 'e'.
You may need to make the .py files executable; to do this, type 

chmod -x name.py

Questions? Email Lily at jensenl7@msu.edu
