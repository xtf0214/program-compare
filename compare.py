from ProgramCompare import *


def setData(data: TextIOWrapper, id=1):
    writeln = lambda *args: print(*args, file=data)
    #########


std = r''
cmp = r''
compare = ProgramCompare(setData, std, cmp)

# ######## make data or brute test
scores = open('scores.txt', 'w')
for id in range(1, 6):
    scores.write(f"test{id} 1 #{id}#\n")
    compare.makeData(id)
    compare.compare(id, display_data_when_correct=False,
                    display_input=False, display_output=True)
scores.close()

# find the first error
# compare.lower_bound(1, 1e8)

print(GREEN + 'finish!' + CLEAR)
