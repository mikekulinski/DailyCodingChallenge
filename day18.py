def max_k_subarray(array, k):
    current_three = array[:k]
    
    print("[")
    for i in range(k,len(array)):
        print(max(current_three))
        current_three = current_three[1:] + [array[i]]

    print(max(current_three))
    print("]")

if __name__ == "__main__":
    print(max_k_subarray([10, 5, 2, 7, 8, 7], 3))