# underrail-mutagen-solver
Python script for solving mutagen sequence by brute force with caching.

# installation and use
copy files mutagen.py and solver.py to computer, and run solver.py with python3 intepreter.
To use it for a specific game, it is necessary to edit `solver.py`, all the sequences must be pasted into the variable `input_mutagens` between the `''`

```
input_mutagens = {'Exitus-1': '',
                  'Echo-1': '',
                  'Echo-2': '',
                  'Echo-3': '',
                  'Echo-4': '',
                  'Helicon-1': '',
                  'Helicon-2': '',
                  'Helicon-3': '',
                  'Io-1': '',
                  'Io-2': '',
                  'Io-3': '',
                  'Ovid-1': '',
                  'Ovid-2': '',
                  'Ovid-3': '',
                  'Solis-1': '',
                  'Solis-2': ''}
```
After you have entered all known sequences, running the script will output the shortest correct solution, if any exist. Note that the script does not need all mutagens to function. However, Exitus-1 must be defined.

### Maximum number of mutagens
By default the script stops after 7 mutagens. If this is not sufficient you must increase the `maximum_mutagens` function variable.
Be warned, this will take a long time to run!

Example with 10 mutagens: `mutagen.find_sequence(input_mutagens, maximum_mutagens = 10)`

# output
Below is the output of the script (from initial commit):

```
$ python3 solver.py

 #1 : Input your sequences in the dictionary below: 
*** Run with your input values:

Exitus-1 sequence not provided, not possible to solve

 #2 : Example from underrail wiki
         https://www.underrail.com/wiki/index.php?title=Mutagen_Puzzle 

*** Run with values from wiki example:

Trying sequence of 1 mutagens
Trying sequence of 2 mutagens
Trying sequence of 3 mutagens
Trying sequence of 4 mutagens
Trying sequence of 5 mutagens
Trying sequence of 6 mutagens

Solution found: Io-3+Io-2+Echo-1+Io-3+Solis-2+Io-1
Compare Io-3+Io-2+Echo-1+Io-3+Solis-2+Io-1 to Exitus-1:
GG WQ GP L7 H2 S2 AZ AX CS CN AP W1 Io-3+Io-2+Echo-1+Io-3+Solis-2+Io-1
GG WQ GP L7 H2 S2 AZ AX CS CN AP W1 Exitus-1
Add      :  set()
Remove   :  set()
In_place :  {'GP', 'AX', 'H2', 'W1', 'GG', 'AP', 'L7', 'AZ', 'WQ', 'CS', 'CN', 'S2'}

*** Manually adding sequence used in wiki:

Io-3    : GG WQ GP AX
Io-2    : GG WQ GP AX L7 H2
Io-1    : GG WQ GP AX L7 H2 S2 AP W1
Echo-1  : GG WQ GP L7 H2 S2 W1 AA AZ VM
Io-2    : GG WQ GP L7 H2 S2 AA AZ VM AX
Io-3    : GG WQ GP L7 H2 S2 AZ AX
Solis-2 : GG WQ GP L7 H2 S2 AZ AX CS CN AP
Io-1    : GG WQ GP L7 H2 S2 AZ AX CS CN AP W1

 #3 : Example from a playthrough 

*** Run with values from a playthrough:

Trying sequence of 1 mutagens
Trying sequence of 2 mutagens
Trying sequence of 3 mutagens
Trying sequence of 4 mutagens
Trying sequence of 5 mutagens

Solution found: Io-2+Ovid-1+Ovid-2+Solis-2+Io-3
Compare Io-2+Ovid-1+Ovid-2+Solis-2+Io-3 to Exitus-1:
YJ NZ C9 PY PS GU MO XW H8 XQ NI E8 I4 Io-2+Ovid-1+Ovid-2+Solis-2+Io-3
YJ NZ C9 PY PS GU MO XW H8 XQ NI E8 I4 Exitus-1
Add      :  set()
Remove   :  set()
In_place :  {'PS', 'I4', 'XQ', 'PY', 'GU', 'C9', 'NI', 'E8', 'XW', 'NZ', 'MO', 'H8', 'YJ'}
```
