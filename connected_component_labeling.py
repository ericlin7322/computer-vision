import numpy as np

def labeling(image) :
    size = image.shape 
    m = size[0]  # rows
    n = size[1]  # columns

    label = np.ones([m,n])
    new = 0
    link = []

    # first pass
    for row in range(m):
        for column in range(n):
            if image[row,column] == [0] :
                label[row, column] = 0
            # object
            else : # check neighbor label
                current_neighbor = [label[row-1,column],label[row,column-1]]

                if (row == 0):
                    current_neighbor = [0, current_neighbor[1]]
                elif column == 0:
                    current_neighbor = [current_neighbor[0], 0]

                # current is new label
                if current_neighbor == [0,0]:
                    new= new + 1
                    label[row, column] = new

                # neighbor got label
                else :
                    # only one neighbor labeling => choose the large one (the only label)
                    if np.min(current_neighbor) == 0 or current_neighbor[0] == current_neighbor[1] :
                        label[row,column] = np.max(current_neighbor)

                    else:
                        label[row,column] = np.min(current_neighbor)

                        if len(link) == 0:
                            link.append(current_neighbor)
                        else:
                            check = 0
                            last = -1
                            for k in range(len(link)) :
                                tmp = set(link[k]).intersection(set(current_neighbor))
                                if len(tmp) != 0 :
                                    if check != 0:
                                        link[last] = set(link[last]).union(set(link[k]))
                                        link[k] = link[k].intersection(set([0]))
                                    else:
                                        link[k] = set(link[k]).union(set(current_neighbor))
                                        last = k
                                    check = check + 1
                            if check == 0:
                                link.append(set(current_neighbor))
    id = len(link)
    ti = 0
    while ti < id:
        if (len(link[ti]) == 0):
            del link[ti]
            id-=1
        else:
            ti+=1

    # second pass
    for row in range(m):
        for column in range(n):
            for x in range(id):
                if (label[row, column] in link[x]) and label[row, column] !=0 :
                    label[row, column] = min(link[x])

    for row in range(m):
        for column in range(n):
            for x in range(id):
                if (label[row, column] == min(link[x])):
                    label[row, column] = x+1
    return label,image,id
