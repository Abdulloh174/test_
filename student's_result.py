import os, random
os.system('cls')


class Results:
    def __init__(self, student):
        self.filename = 'exam_results.txt'
        self.student = student

    def the_best(self):
        the_best_name = ''
        the_highest_point = 0

        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if '-' in line and '/' in line:
                    name, score = line.split('/')
                    if int(score) > the_highest_point:
                        name = name.strip()
                        score = int(score.split('/')[0].strip())
                        the_highest_point = score
                        the_best_name = name
        if the_best_name:
            return f"The best student is {the_best_name}, who has gotten {the_highest_point} points."
        else:
            return "No valid student data found in the file."

    def surpass(self):
        best_student = ''
        highest_score = 0
        student_score = None
        aim = ''
        
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                if '-' in line and '/' in line:
                    name, score = line.split('-')
                    name = name.strip()
                    score = int(score.split('/')[0].strip())  
                    
                    if score > highest_score:
                        highest_score = score
                        best_student = name
                    

                    if name == self.student:
                        student_score = score
            
            if student_score == None:
                aim = f"Student {self.student} not found in the list."

            elif student_score < highest_score:
                aim = f"You need to work {highest_score - student_score} points better than {best_student} (Who has got the the most points)."

            elif student_score == highest_score:
                aim = f"{self.student.title()} Listen !!! You are tied with {best_student}. Study their strategy to surpass them."

            else:
                aim = f"{self.student}, don't worry, you are ahead of {best_student} by {student_score - highest_score} points."
        
        return aim
    
    def pass_the_exam(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()

            student_found = False

            for line in lines:
                if '-' in line and '/' in line:
                    name, score  = line.split('-')
                    name = name.strip()
                    score = int(score.split("/")[0].strip())

                    if name == self.student:
                        student_found = True


                        if score > 20:
                            return f"{self.student}, be grateful ALHAMDULLIH your efforts are paid off with excelent results ({score-20} times better), repeat!!!"
                        
                        elif score > 20:
                            return f"{self.student}, Excelent, Perfect, But I want you to always remember reaching to the top of the mauntain is much easier than maintaining the balance"
                        
                        elif score < 20:
                            return f"{self.student} it's more likely to be your fault, because if you had seek opportunity you'd definitely be able to pass the exam, but chech if something went wrong"
                        
                        else:
                            return f"{self.student} you could barely pass the exam"
                        
        if not student_found:
            return f"{self.student} is not in the list"
        
    def groups_from_file(self):
        participants = []
        try:
            with open('exam_results.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        if not line in participants:
                            participants.append(line)
            random.shuffle(participants)
            grouped = [participants[i:i+2] for i in range(0, len(participants), 2)]
            for i, group in enumerate(grouped, start=1):
                print(f"{i} Group: {', '.join(group)}")
                        

        except Exception as e:
            print(f"Error reading file: {e}")


a = Results("Charlie")

# print(a.the_best())

# print(a.surpass())

# print(a.pass_the_exam())

print(a.groups_from_file())


