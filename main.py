
print('Enter the number of species for the calculation:')
species_number = int(input('> '))

N = 0
listn = []


for i in range(1, species_number):
    print('enter the number of organisms in species ' + str(i))
    n = int(input('> '))
    N =+ n
    appenditem = int((n*n) - n)
    listn.append(appenditem)

print('Sum of n(n-1):')
print(sum(listn))
print('\nN(N-1):')
print((N*N)-N)

print('')
print('')
print('The diversity index:')
diversity_index = (sum(listn))/((N*N)-N)

print(str(diversity_index))