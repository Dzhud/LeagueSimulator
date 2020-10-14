
def generate_fixtures(teams):
    s = []
    n = len(teams)
    #create list from 0 to 19
    map = list(range(n))
    mid = n//2
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = teams[l1[j]]
            t2 = teams[l2[j]]
            if j==0 and i%2==1:
                #flip first match only, every other round
                #this is because first match always involves last team in list
                round.append((t2,t1))
            else:
                round.append((t1,t2))
        s.append(round)
        #rotate list by n/2, leaving last element at the end
        map = map[mid:-1] + map[:mid] + map[-1:]
    return s
