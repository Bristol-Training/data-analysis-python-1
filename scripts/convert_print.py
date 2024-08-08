def ounces_to_grams(weight):
    if weight < 0:
        print("Cannot convert negative mass")
    
    new_weight = weight * 28.3495
    return new_weight
