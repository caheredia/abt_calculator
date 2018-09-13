with open("medical.txt", "r") as file:
    file_lines = file.readlines()

# set word counters
and_count = 0
but_count = 0
lines = [line.replace(',', '').replace('\'', '').replace('.', '').lower().split()
         for line in file_lines]

words = [word for line in lines for word in line]

print('AND index: {:.2%}'.format(words.count('and') / len(words)))
# NARRATIVE INDEX =  (BUT/AND)  X  100
print('Narrative index: {:.2%}'.format(words.count('but') / words.count('and')))
