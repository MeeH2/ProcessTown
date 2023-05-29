# ProcessTown
Muddy Town - Path Paving Optimization

Muddy Town is a Python project for optimizing the path paving process in a hypothetical town. Given a number of buildings and streets, the project generates a town, and implements Prim's Algorithm to find the minimum cost to pave all the streets in the town.

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

Features

Reads map data from a specified file.
Writes map data and paving plans to specified files.
Generates a random town with a given number of buildings and streets.
Implements Prim's Algorithm to find the minimum cost of paving all the streets in the town.
Visualizes the generated map using the NetworkX library.
Installation

You'll need to have Python installed on your machine (3.6 or later recommended).

Clone the repository to your local machine.
Run pip install -r requirements.txt to install necessary packages.
Usage

To run the program, you'll use python muddytown.py with different command line arguments:

-r <mapfile>: Read the map from <mapfile>
-w <mapfile>: Write the map to <mapfile>
-wp <mapfile>: Write the paving plan to <mapfile>
-t <buildings> <streets>: Generate a town with <buildings> buildings and <streets> streets
-p: Execute Prim's Algorithm on the current map
-v: Visualize the map using NetworkX
Examples:

css
Copy code
python muddytown.py -r MiniTown.dat
python muddytown.py -w MiniTown.dat
python muddytown.py -wp PavingPlan.dat
python muddytown.py -t 34 50
python muddytown.py -p
python muddytown.py -v
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

MIT
