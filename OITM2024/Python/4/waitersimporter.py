### Data file importer - Waiters

def get_waiters(fname):
    import numpy as np
    with open(fname, "rt") as in_f:
        data = [int(item) for item in in_f.read()] 
    return np.array(data).reshape(180,20,20)

CONTSA = 1

def display_floor(floor):
    """
    20x20 floor expected
    """
    import matplotlib.pyplot as plt
    import numpy as np

    markers = {1:'>', 2:"<", 3: "v", 4: "^", 5: "s"}

    x = [[] for _ in range(5)]
    y = [[] for _ in range(5)]
    
    for i in range(20): 
        for j in range(20):
            if floor[i,j] == 0: 
                pass
            else:
                x[floor[i,j]-1].append(19-i)
                y[floor[i,j]-1].append(j)
    for i in range(5):
        plt.scatter(y[i], x[i], marker=markers.get(i+1, ";"), zorder=2)
        plt.grid(linestyle="--",alpha=0.5,zorder=1)
    plt.show()
    return    
