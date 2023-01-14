
def fuct(array,key,matches):
    for x in array:
        if key in x:
            matches= matches+1
        if matches == 2:
            return matches
    return matches

def assgin(allreviewer,allpaperkeywords,assignedreview):
        num_rev = 0
        matches = 0
        for x in allreviewer:
            if num_rev<=3:
                for y in allreviewer[x]["key"]:
                    matches = fuct(allpaperkeywords,y,matches)
                    if matches==2:
                        assignedreview.append(x)
                        num_rev = num_rev+1
                        matches = 0
                        break
        return assignedreview