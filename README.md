# CPSC 450
## Sequence Mining Using the 2-jump Algorithm 

Utilizing a paper published in 2011, we are directing our efforts towards finding patterns that might help identify genes related to oculocutaneous albinism type-7.

## Installation

This project was made with Python version 3.9.0. First, install Python, along with pip. Next install the Kivy library ver. 2.0.0. This can be done by running `python.exe` with the command line arguments: `python -m pip install https://github.com/kivy/kivy/archive/master.zip`. This will install the latest version of Kivy and all of its dependencies. Next, extract the zip contents, or clone the repository to complete installation.

## Running

To run the program, simply execute `python.exe` with the path to [main.py](src/main.py) as the only argument.

## Operating the GUI

The GUI is made of three components ordered from left to right of the application: The file select button, the pattern searcher, and the frequent sequence miner. 

### File Select

Simply press the button on the left titled *select file*. This will open a file browser dialog, with a default path of the current working directory. To select a file, navigate through the browser and double click the desired file. This will cause the program to attempt a parse of the file into a string of dna sequences. If successful, the string will be displayed in the other two compontents.

Currently we have provided one file containing the LRMDA gene string, in [the src/data](src/data) folder with the name [dataset_1.txt](src/data/dataset_1.txt).

### Pattern Searcher

To operate the pattern searcher component, once you have loaded a data set to examine, press the button labelled *search*. This will cause the program to highlight any matching patterns within the string, and will display the number of occurrences, and the indices within the string in which they were found, at the bottom of the application.

### Frequent Sequence Miner

Finally, the frequent sequence miner component can be operated by entering a desired sequence length to search for in the appropriately labeled box, and a minimum support threshold in the other. These values default to 1 and 0 respectively. Once the desired values have been inputted and the desired data set is loaded, press the button labelled *mine* to commence the mining process. Upon completion, frequent sequences of the data set with a support above or equal to the minimum threshold will be displayed.

## Relevant Source Code

Our implementation of the two-jump algorithm can be found in [src/TwoJump.py](src/TwoJump.py). Our own algorithm for frequent sequence mining can be found in [src/dna_tree.py](src/dna_tree.py). Finally, the source for the GUI implementation can be found in [src/dna_viewer.py](dna_viewer.py), along with the accompanying `.kv` files ([1](src/PatternSearchWidget.kv)[2](src/SequenceMinerWidget.kv)[3](src/SidebarWidget.kv)).