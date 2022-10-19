try:
    import sys, math, time, re, os
    from Grade import Grade
except Exception as import_error:
    print("The python program has installed incorrectly. Ensure 'Grade.py' is in the same file directory")
    input("Enter to continue...")
    quit()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - PURPOSE OF PROGRAM -
# this program can be used to store topic papers / mock papers results digitally, it automatically saves your results
# and you can remove and add papers at any time. you can also get your average grade for specific subjects with the
# predicted grade option in first menu.
# future update will include GUI aswell as further OOP structure (currently not much can be done in OOP for this program except storing the paper info)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



try:
    def verify_files(): # this function determines whether the necessary data exists or not and creates the file if not
        if os.path.exists('data/saved_papers.data') is False:
            if os.path.exists('data/') is False:
                os.mkdir("data/")
            open('data/saved_papers.data', 'x')

    def customize_papers(list): # this function allows you to add, remove or delete all papers.
        choice_1 = input("'0' to add a paper, '1' to remove a paper, '2' to delete all papers (cannot be undone): ")
        if '0' in choice_1:
            add_paper(list)
        elif '1' in choice_1:
            remove_paper(list)
        elif '2' in choice_1:
            choice_2 = input("Are you sure you want to delete all papers? this action cannot be undone. (y/n): ")
            if choice_2 == "y":
                delete_all(list)
            else:
                main()

    def remove_paper(list): # removes a specific paper of user's choice
        choice_4 = input("Enter the name of paper you wish to delete: ")
        for i in range(len(list) - 1):
            if list[i].get_paper_name() == choice_4:
                list.remove(list[i])
                store_papers(list)
                break

    def delete_all(list): # resets the entire program, clears list and data file
        list.clear()
        store_papers(list)
        print("All papers successfully deleted.")

    def store_papers(list_to_store): # function's purpose is to save the papers in the file in correct format to be read from
        save_papers = open('data/saved_papers.data', 'w')
        save_papers.write("")
        for i in range(len(list_to_store)):
            save_papers.write(list_to_store[i].get_subject() + ',')
            save_papers.write(list_to_store[i].get_paper_name() + ',')
            save_papers.write(list_to_store[i].get_grade() + '\n')
        save_papers.close()

    def list_papers(list): # puts the information from data file into the object list which can then be modified at start-up
        verify_files()
        read_papers = open('data/saved_papers.data')
        for line in read_papers:
            if line == "\n":
                continue
            temp = re.split(',', line)
            list.append(Grade(temp[0],temp[1],temp[2]))
        read_papers.close()

    def output_papers(list): # outputs the papers and their results to the user
        if len(list) == 0:
            print("No papers to output. Add a paper first.")
        for i in range(len(list)):
            print("- - - - - - - - - - - - - - - - - -") # separates the different papers
            print(f"\nSUBJECT: {list[i].get_subject()}\nPAPER NAME: {list[i].get_paper_name()}\nGRADE: {list[i].get_grade()}\n ")

    def quit(): # exits the program
        print("\nThanks for using!")
        time.sleep(2)
        sys.exit()

    def add_paper(list): # adds the paper and result to list and then stores it to the data file for future use
        subject = input("Enter name of subject: ").upper()
        topic = input("Enter name of topic: ")
        grade = input("Enter grade recieved (0 if U/X): ")
        try:
            int(grade)
        except Exception:
            print("Invalid grade. Please retry")
            add_paper(list)
        if int(grade) > 9 or int(grade) < 0:
            print("Invalid grade. Please retry")
            add_paper(list)
        list.append(Grade(subject,topic,grade))
        store_papers(list)
        print(f"{subject} {topic} paper with grade {grade} added successfully.")

    def get_average_grade(list, subject): # gets a mean average of a specific subject's grades and returns it to the user
        sum_of_grades = 0
        counter = 0
        for i in range(len(list)):
            if list[i].get_subject().upper() == subject.upper():
                counter += 1
                sum_of_grades += int(list[i].get_grade())
        if counter == 0:
            return "Subject not found."
        result = sum_of_grades / counter
        rounded_result = round(result)
        if rounded_result > result:
            suffix = "-"
        elif rounded_result < result:
            suffix = "+"
        else:
            suffix = ""
        average_grade = str(rounded_result) + suffix
        return f"Your average grade for {subject} is {average_grade}"

    def main(): # main body of program, main menu

        choice_0 = input("'0' to customize papers, '1' to view papers or '2' to get predicted grade: ")
        if "0" in choice_0:
            customize_papers(list_of_grades)
        elif "1" in choice_0:
            output_papers(list_of_grades)
        elif "2" in choice_0:
            print(get_average_grade(list_of_grades, input("Enter subject: ")))
        elif "quit" in choice_0:
            quit()
        else:
            print("No option selected, try again.")
        main()

    if __name__ == "__main__":
        list_of_grades = []
        list_papers(list_of_grades)
        main()

except KeyboardInterrupt as x: # for people who use CTRL+C to exit programs
    quit()