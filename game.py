## Mak3 an 8 x 8 grid filled with "~" and print it 
'''
Step 1) Define main(), make a list with 8 squiggles and print it 
'''



def main():
    grid=[]
    squiggles=["~", "~", "~", "~", "~", "~", "~", "~"]
    for squiggle in range(8):
        grid.append(squiggles)
    print(grid)
main()

