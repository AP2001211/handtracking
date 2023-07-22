def sumSubsets(sets, n, target):
    # Create the new array with size
    # equal to array set[] to create
    # binary array as per n(decimal number)
    x = [0] * len(sets);
    j = len(sets) - 1;
    count = 0

    # Convert the array into binary array
    while (n > 0):
        x[j] = n % 2;
        n = n // 2;
        j -= 1;

    sum = 0;

    # Calculate the sum of this subset
    for i in range(len(sets)):
        if (x[i] == 1):
            sum += sets[i];

    # Check whether sum is equal to target
    # if it is equal, then print the subset
    if (sum == target):
        count = count + 1
    return count



# Function to find the subsets with sum K
def findSubsets(arr, K):
    # Calculate the total no. of subsets
    x = pow(2, len(arr));
    sum = 0

    # Run loop till total no. of subsets
    # and call the function for each subset
    for i in range(1, x):
        sum = sum + sumSubsets(arr, i, K);
    print(sum)


if __name__ == "__main__":
    arr = [5, 10, 12, 13, 15, 18];
    K = 30;
    findSubsets(arr, K);