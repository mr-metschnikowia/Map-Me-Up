# Programme: Map Me Up!

interest = input('Please provide array of obtained fragments separated by spaces no commas:')
interest = interest.split()
reference = input('Please provide reference sequence:')

score = 0

function = {'AGGC' : 'codes for pure gold', 'GGGG' : 'tumour suppressor gene'}

for i in range(len(interest)):
    y = interest[i]
    for i in range(len(reference)):
        a = len(y)
        x = reference[i : i + a]
        if x in interest:
            print(x)
            score += 1
            try:
                print(function[x])
            except KeyError:
                print('Unknown functionality!')

if score == 0:
    print('No map this time bud!')
