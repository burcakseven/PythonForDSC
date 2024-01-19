import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        n_height = np.array(height, dtype = float)
        n_weight = np.array(weight, dtype = float)

        if n_height.shape != n_weight.shape:
            raise ValueError("Sizes are not equal.")
    except ValueError as v:
        print(v)
        exit(1)

    n_bmi = n_weight / (n_height ** 2)
    return n_bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [one_bmi > limit for one_bmi in bmi]
