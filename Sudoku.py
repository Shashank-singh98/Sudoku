from utils import *

# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    a=list(grid)
    list1=['A1','A2','A3','A4','A5','A6','A7','A8','A9',
         'B1','B2','B3','B4','B5','B6','B7','B8','B9',
         'C1','C2','C3','C4','C5','C6','C7','C8','C9',
         'D1','D2','D3','D4','D5','D6','D7','D8','D9',
         'E1','E2','E3','E4','E5','E6','E7','E8','E9',
         'F1','F2','F3','F4','F5','F6','F7','F8','F9',
         'G1','G2','G3','G4','G5','G6','G7','G8','G9',
         'H1','H2','H3','H4','H5','H6','H7','H8','H9',
         'I1','I2','I3','I4','I5','I6','I7','I8','I9'
         ]
    c=dict(list(zip(list1,a)))
    return c
grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    a=list(grid)
    for i,j in enumerate(a):
        if j=='.':
            a[i]='123456789'
            b=a
        
    list1=['A1','A2','A3','A4','A5','A6','A7','A8','A9',
         'B1','B2','B3','B4','B5','B6','B7','B8','B9',
         'C1','C2','C3','C4','C5','C6','C7','C8','C9',
         'D1','D2','D3','D4','D5','D6','D7','D8','D9',
         'E1','E2','E3','E4','E5','E6','E7','E8','E9',
         'F1','F2','F3','F4','F5','F6','F7','F8','F9',
         'G1','G2','G3','G4','G5','G6','G7','G8','G9',
         'H1','H2','H3','H4','H5','H6','H7','H8','H9',
         'I1','I2','I3','I4','I5','I6','I7','I8','I9'
         ]
    c=dict(list(zip(list1,a)))
    return c
grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    new1=[]
    for x in values.keys():
        if len(values[x]) ==1:
            new1.append(x)
    for i in new1:
        y=values[i]
        near_peers=peers[i]
        for remove_peer in near_peers:
            values[remove_peer]=values[remove_peer].replace(y,'')
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    for units in unitlist:
        for x in '123456789':
            d=[]
            for i in units:
                if x in values[i]:
                    d.append(i)
            if len(d)==1:
                values[d[0]]=x
            
    return values
def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values=eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values=only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values=reduce_puzzle(values)
    if values==False:
        return False
    if all(len(values[v])==1 for v in boxes ):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    k,v=min((len(values[v]),v) for v in boxes if len(values[v])>1 )
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[v]:
        new_s=values.copy()
        new_s[v]=value
        attempt=search(new_s)
        if(attempt):
            return attempt
    # If you're stuck, see the solution.py tab!
    x=[]
def assign_value(values,key,value):
    values[key]=value
    if len(value)==1:
        x.append(values.copy())
    return values
def naked_twins(values):
    for units in unitlist:
        peer_keys=[(values[key],key) for key in units if len(values.values())==2]
        if len(peer_keys)==2:
            v1=peer_keys[0]
            v2=peer_keys[1]
            if v1[0]==v2[0]:
                for i in units:
                    if len(values[i])>2:
                        near=v1[0][0]
                        far=v2[0][1]
                        assign_value(values,i,values[i].replace(near,''))
                        assign_value(values,i,values[i].replace(far,''))
    return values