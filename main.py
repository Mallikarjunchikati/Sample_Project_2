pos = -1
def find(countries,n):
    i = 0
    while i < len(countries):
        if countries[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

countries = ['MA','VA','KA','WS','OH','GA']
n = 'VA'
if find(countries,n):
    print("True",pos)
else:
    print("False")