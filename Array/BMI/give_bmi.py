# weight / height^2
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("Lists not has same sizes.")
        if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
            raise ValueError("Elements in the lists must be of type int or float")
    except ValueError as v:
        print(v)
        exit(1)
    
    bmi_list = [(weight[i]/(height[i] ** 2)) for i in range(len(height))]
    print(len(height))
    return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [one_bmi > limit for one_bmi in bmi]
