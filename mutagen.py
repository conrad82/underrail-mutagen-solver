import itertools
from functools import lru_cache

CACHE_MAXSIZE = int(1E7)

class Mutagen():

    def __init__(self, sequence, name=''):
        self.sequence = sequence
        self._hash = hash(sequence)
        self.name = name

    # @lru_cache(maxsize=CACHE_MAXSIZE)
    def __add__(self, mutagen2):
        ''' Note, addition immutable! '''

        if mutagen2.sequence == '':
            m =  self+self
            m.name = self.name
            return m
        if self.sequence == '':
            m =  mutagen2+mutagen2
            m.name = mutagen2.name
            return m
        
        new_sequence = []
        for code in self.sequence.split(' '):
            if code[0] != '-':
                new_sequence.append(code)

        for code in mutagen2.sequence.split(' '):
            if code[0] != '-':
                if code not in new_sequence:
                    new_sequence.append(code)
            if code[0] == '-':
                if code[1:] in new_sequence:
                    new_sequence.remove(code[1:])

        return Mutagen(' '.join(new_sequence), name=self.name+'+'+mutagen2.name)

    def __str__(self):
        return self.sequence

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self.sequence == other.sequence

    def analysis(self, mutagen2):
        print(f'Compare {self.name} to {mutagen2.name}:')
        print(self.sequence,     self.name)
        print(mutagen2.sequence, mutagen2.name)

        set_self = set(self.sequence.split(' '))
        set_2    = set(mutagen2.sequence.split(' '))
        print('Add      : ', set_2 - set_self)
        print('Remove   : ', set_self - set_2)
        print('In_place : ', set_self & set_2)


def find_sequence(input_mutagens, maximum_mutagens = 10):
    ''' Using input dictionary, determine the correct sequence to produce Exitus-1 '''

    if 'Exitus-1' not in input_mutagens.keys():
        print('Exitus-1 sequence not provided, not possible to solve')
        return None
    if input_mutagens['Exitus-1'] == '':
        print('Exitus-1 sequence not provided, not possible to solve')
        return None
    
    sequence = brute_force_sequence(input_mutagens, maximum_mutagens)
    return sequence

def parse_input_to_mutagen_list(input_mutagens):
    ''' Convert input dictionary to list of Mutagens '''
    mutagen_list = list()
    for k, v in input_mutagens.items():
        if v  == '':
            continue
        if k == 'Exitus-1':
            continue
        
        mutagen = Mutagen(v, name=k)
        mutagen_list.append(mutagen)

    return mutagen_list

def brute_force_sequence(input_mutagens, maximum_mutagens=10):
    ''' Tries all combinations of input mutagens until solution is found,
        or maximum mutagens is reached.
        Same mutagen can be used multiple times in the sequence.
    '''
    
    mutagens_list  = parse_input_to_mutagen_list(input_mutagens)
    empty_mutagen  = Mutagen('')
    solution       = input_mutagens['Exitus-1']
    counter        = 0

    for counter in range(maximum_mutagens):
        counter += 1
        print(f'Trying sequence of {counter} mutagens')
        for mutagen_sequence in itertools.product(mutagens_list, repeat=counter):
            new_mutagen = sum_mutagens(tuple(mutagen_sequence))
            
            if new_mutagen.sequence == solution:
                print('\nSolution found:', new_mutagen.name)
                new_mutagen.analysis(Mutagen(input_mutagens['Exitus-1'], name = 'Exitus-1'))
                return new_mutagen

    print('No solution found...')

@lru_cache(maxsize=CACHE_MAXSIZE)
def sum_mutagens(mutagen_sequence):
    ''' An attempt to speed up summation through caching '''
    if len(mutagen_sequence) == 1:
        return mutagen_sequence[0]
    
    return sum_mutagens(mutagen_sequence[:-1])+mutagen_sequence[-1]
