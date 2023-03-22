def read_courses() -> list:
    """
    Reads comp courses list.
    """
    f = open("data/comp_courses.txt")
    courses = []
    for line in f:
        courses.append(line.strip())
    f.close()
    return courses

def get_user_courselist(v_courses: list) -> list:
    """
    Repeatedly prompt user to enter courses to add to a list.
    """
    prompt = "Enter a course to add, Enter to stop: "
    course = input(prompt)
    courses = []
    while course != "":
        if course in v_courses:
            courses.append(course)
        else:
            print(f"Sorry, {course} is not a real course")
        course = input(prompt)
    
    return courses

def write_user_courselist(filename: str, courses: list) -> None:
    """
    Writes the contents of courses to filename.
    """
    f = open(filename, "w")
    for course in courses:
        f.write(course + "\n")
    f.close()

def main() -> None:
    valid = read_courses()
    courses = get_user_courselist(valid)
    write_user_courselist("data/user_courses.txt", courses)

main()
