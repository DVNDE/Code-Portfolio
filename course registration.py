# Function to prompt the user for course codes
def get_course_codes():
    # Ask the user for the number of courses
    num_courses = int(input("Enter the number of courses you have registered for: "))
    
    # Initialize an empty list to store course codes
    course_codes = []
    
    # Loop to get each course code from the user
    for i in range(num_courses):
        course_code = input(f"Enter the code for course {i + 1}: ")
        course_codes.append(course_code)
    
    # Display the course codes
    print("\nYou have registered for the following courses:")
    for code in course_codes:
        print(code)

# Call the function to execute the program
get_course_codes()

