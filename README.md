# ProcessTown
MuddyTown


Overview
This python code takes in a file named MiniTown.dat and displays the file in a standard format and paving plan format. Its objective is to find the minimum cost to pave a street using Prim’s algorithm.


Standard Format
        The standard format for displaying, reading, and writing town data
                “<Town_Name>”
                <Paving Cost>, “<Building>”, “<Building>”
                <Paving Cost>, “<Building>”, “<Building>”
                <Paving Cost>, “<Building>”, “<Building>”


Paving Plan Format
        The format for reading and writing paving plans
                “<Plan_Name>”
                “<Building_Address>”, “<Building_Address>”
                “<Building_Address>”, “<Building_Address>”


How to Run the Program
Unfortunately, I didn’t get everything done so I have two files for muddytown one that is more functional but cannot be used via command line which is named muddytown.py and another that is my work in progress of switching my code to work via command line which is named commandMT.py.


The muddytown.py will take in a file named MiniTown.dat and display it in standard and paving plan format. Unfortunately it doesn’t display the lowest cost unless you run primAlg function and then change line 120 to map = read_map() to show the that paving plan and the cost to make it. I also forgot to hard code the paving cost into the file so instead of printing the cost in the new file it shows the minimum cost via console instead.
To run creat_town function you will need to attach the following file named StreetNameCleaner.txt so it pulls up a list of Denver streets that it can randomize into the function. Create_town function takes in two parameters the number of buildings you want and the number of streets. I tested it with 34 buildings and 50 streets but that can be changed.


To see a visual representation of the graph you’ll need to import networkx as nx.


I somehow messed up my commanMT.py and it may not be functioning anymore which is frustrating
