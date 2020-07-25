import mutagen

''' Input sequences, from the game 
    Exitus-1 MUST be defined
    If insufficient mutagens have been found, 
    this script will not find a solution
'''

print('''\n #1 : Input your sequences in the dictionary below: ''')

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

print('*** Run with your input values:\n')
mutagen.find_sequence(input_mutagens, maximum_mutagens = 7)

print('''\n #2 : Example from underrail wiki
         https://www.underrail.com/wiki/index.php?title=Mutagen_Puzzle ''')

input_mutagens = {'Exitus-1': 'GG WQ GP L7 H2 S2 AZ AX CS CN AP W1',
                  'Echo-1': 'AA S2 AZ VM H2 -AP -AX -BL',
                  'Echo-2': '',
                  'Echo-3': '',
                  'Echo-4': '',
                  'Helicon-1': '',
                  'Helicon-2': '',
                  'Helicon-3': '',
                  'Io-1': 'GP S2 GG AP W1 -DW -PQ',
                  'Io-2': 'L7 H2 WQ AX -CS -W1',
                  'Io-3': 'GG WQ GP AX -VM -AA',
                  'Ovid-1': '',
                  'Ovid-2': '',
                  'Ovid-3': '',
                  'Solis-1': '',
                  'Solis-2': 'CS CN GP AP WQ AX'}

print('\n*** Run with values from wiki example:\n')
mutagen.find_sequence(input_mutagens, maximum_mutagens = 7)

print('\n*** Manually adding sequence used in wiki:\n')
m =  mutagen.Mutagen(input_mutagens['Io-3'])
print('Io-3    :', m+m)
m += mutagen.Mutagen(input_mutagens['Io-2'])
print('Io-2    :', m)
m += mutagen.Mutagen(input_mutagens['Io-1'])
print('Io-1    :', m)
m += mutagen.Mutagen(input_mutagens['Echo-1'])
print('Echo-1  :', m)
m += mutagen.Mutagen(input_mutagens['Io-2'])
print('Io-2    :', m)
m += mutagen.Mutagen(input_mutagens['Io-3'])
print('Io-3    :', m)
m += mutagen.Mutagen(input_mutagens['Solis-2'])
print('Solis-2 :', m)
m += mutagen.Mutagen(input_mutagens['Io-1'])
print('Io-1    :', m)


print('''\n #3 : Example from a playthrough ''')

input_mutagens = {'Exitus-1': 'YJ NZ C9 PY PS GU MO XW H8 XQ NI E8 I4',
                  'Echo-1': 'I2 I4 NI NP',
                  'Echo-2': 'MO I4 IA -RZ -GU',
                  'Echo-3': 'NZ XW S6 C9 -XQ -PS -H8',
                  'Echo-4': '',
                  'Helicon-1': 'IA I4 E8 RZ XW PS -NI',
                  'Helicon-2': 'PS NP RZ XP C9 YJ -XW',
                  'Helicon-3': 'YJ PS S6 NI -GU -NP',
                  'Io-1': 'S6 C9 GU H8 -IA -ZV',
                  'Io-2': 'YJ RZ NZ I2 C9 -XP -PY -E8 -ZV',
                  'Io-3': 'YJ E8 MO NI NZ I4 -XP -RZ -ZV -I2',
                  'Ovid-1': 'PY PS S6',
                  'Ovid-2': 'GU MO RZ PY XP -I2 -S6',
                  'Ovid-3': 'H8 E8 ZV XW -RZ -PS -NZ -GU',
                  'Solis-1': '',
                  'Solis-2': 'XW PY H8 XQ NI'}

print('\n*** Run with values from a playthrough:\n')
mutagen.find_sequence(input_mutagens, maximum_mutagens = 7)

