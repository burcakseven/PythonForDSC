import numpy as np
def slice_me(family: list, start: int, end: int) -> list:
    n_family = np.array(family)
    print(f"My shape is : {n_family.shape}")
    n_family =  n_family[start:end]
    print(f"My new shape is : {n_family.shape}")
    return n_family.tolist()