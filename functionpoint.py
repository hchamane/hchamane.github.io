"""Enhanced Software Project Analysis Tool"""

# Constants for FPA
DELIVERED_PROJECT = 3
ONGOING_PROJECT = 1
FAILED_PROJECT = 0

def calculate_functionality_points(delivered, ongoing, fail):
    """
    Calculates the total functionality points based on project results.
    """
    return (delivered * DELIVERED_PROJECT) + (ongoing * ONGOING_PROJECT) + (fail * FAILED_PROJECT)

def analyse_project_size(points):
    """
    Determines project size based on functionality points.
    """
    if points >= 50:
        return "Large project"
    elif points >= 40:
        return "Medium project"
    elif points >= 30:
        return "Small project"
    else:
        return "Very small project"

def identify_optimisation_areas(points):
    """
    Suggests areas for optimisation based on functionality points.
    """
    if points >= 50:
        return "Consider optimising resource allocation and scalability."
    elif points >= 40:
        return "Focus on improving efficiency and code quality."
    elif points >= 30:
        return "Look for opportunities to streamline processes."
    else:
        return "Explore ways to reduce complexity."

def analyse_development_performance(points):
    """
    Evaluates development performance based on functionality points.
    """
    if points >= 50:
        return "Excellent performance!"
    elif points >= 40:
        return "Good performance."
    elif points >= 30:
        return "Moderate performance."
    else:
        return "Room for improvement."

def main():
    """
    The main function to validate and calculate the team's performance
    """
    teamname = input("Enter the Name of your team: ")
    delivered = int(input("Enter the number of projects your team delivered: "))
    ongoing = int(input("Enter the number of projects your team is working on: "))
    fail = int(input("Enter the number of projects your team failed to deliver: "))

    # Validate input (assuming a maximum of 40 matches)
    if delivered + ongoing + fail > 20:
        print("Error: You entered too many matches. Please enter valid numbers.")
        return

    # Calculate total functionality points
    totalpoints = calculate_functionality_points(delivered, ongoing, fail)

    # Output results
    print(f"\nTeam: {teamname}")
    print(f"Functionality Points: {totalpoints}")
    print(f"Project Size: {analyse_project_size(totalpoints)}")
    print(f"Optimisation Areas: {identify_optimisation_areas(totalpoints)}")
    print(f"Development Performance: {analyse_development_performance(totalpoints)}")


if __name__ == "__main__":
    main()
