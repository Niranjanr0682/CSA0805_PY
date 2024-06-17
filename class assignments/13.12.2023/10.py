# Write a program that takes user input for a number and handles exceptions if
# the input is not a valid number.

# user_input = input("Enter an integer number: ")
#
# try:
#     number = int(user_input)
# except ValueError:
#     print("Invalid input. Please enter a valid integer number.")
# else:
#     print(f"You entered {number}.")
# finally:
#     print("bye")

def findMaxProfit(projects):
    # Sort projects by end time
    projects.sort(key=lambda x: x[1])

    # Initialize an array to store maximum profit for each employee
    n = len(projects)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        proj_type, start, end, profit = projects[i - 1]

        if proj_type == 0:
            # Bonus request
            dp[i] = max(dp[i], dp[start - 1] + profit)
        else:
            # Project
            dp[i] = max(dp[i], dp[start - 1] + profit, dp[i - 1])

    return dp[n]

def main():
    num_projects = int(input("Enter the number of projects: "))
    projects = []

    for _ in range(num_projects):
        proj_type, start, end, profit = map(int, input().split())
        projects.append((proj_type, start, end, profit))

    print("The maximum profit is:", findMaxProfit(projects))

if __name__ == "__main__":
    main()
