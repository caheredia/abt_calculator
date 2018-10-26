with open("medical.txt", "r") as file:
    file_lines = file.readlines()

# set word counters
and_count = 0
but_count = 0
lines = [line.replace(',', '').replace('\'', '').replace('.', '').lower().split()
         for line in file_lines]

words = [word for line in lines for word in line]
print('No more than 2.6%')
print('\n')
print('AND index: {:.2%}'.format(words.count('and') / len(words)))
# NARRATIVE INDEX =  (BUT/AND)  X  100
print('\n')
print('Boring texts usually score under 10, average is in the teens, \nabove average is 20’s, powerful is 30’s, and 40 or over is incredibly rare')
print('\n')
print('Narrative index: {:.2%}'.format(words.count('but') / words.count('and')))
