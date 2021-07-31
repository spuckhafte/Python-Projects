values = input('\n> ')
# input example: 1, 0.5, 0.25 or 1, 1/2, 1/4
# Minimum 2 values of the infinte GP are required for the Sum

sequence = values.split(',')

series=[]

ratio = []

def operate(sequence, series):

    for i in sequence:

        if "/" in i:

            k = i.split('/')

            x=float(k[0])

            y=float(k[1])

            series.append(float(x/y))

            continue

        else:

            series.append(float(i))

            continue

        

def check_sequence(series):

    r=[]

    max_index = len(series)-1

    i=0

    while i<max_index:

        common_ratio = float(series[i+1]/series[i])

        r.append(common_ratio)

        i+=1

        continue

    

    k=0

    for j in r:

        check = r[0]

        if j==check:

            k+=1

            continue

        else:

            break

    

    if k==len(r):

        ratio.append(r[0])

        return 0

    else:

        return 1

    

def summation(series, sequence):

    r=ratio[0]

    if check_sequence(series) == 0 and r<1 and r>-1:

        a = series[0]

        sum_gs = a/(1-r)

        sequence.append('...')

        out = ' + '.join(sequence)

        print(f"\n{out} = {round(sum_gs, 4)}")

        

    elif r>=1 or r<=-1:

        print('The series is Divergent')

    

    else:

        print("The series is not geometrical")

try:  

      

    operate(sequence, series)

    

    check_sequence(series)

    

    summation(series,sequence)

    

except:

    print("\nUnexpected Error")
