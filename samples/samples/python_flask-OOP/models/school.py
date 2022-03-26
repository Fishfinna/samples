from .student import Student
import json


class School:
    def __init__(self, name):
        """Constructor for the"""
        self.name = name
        with open("data/school.json") as fp:
            data = json.load(fp)
            self.students = []
            for person in data:
                self.students.append(Student(**person))

    def get_by_id(self, student_id):
        matching_ids = [i for i in self.students if i.student_id == student_id]
        if len(matching_ids) <= 0:
            return None
        else:
            matching_ids = matching_ids[0]
        return matching_ids

    def get_by_name(self, name):
        matching_names = [i for i in self.students if i.name == name]
        return matching_names

    def add(self, instance: Student):
        if type(instance) != Student:
            self.students.append(Student(**instance))
        else:
            self.students.append(instance)

    def delete(self, student_id):
        data_removed = False
        to_remove = self.get_by_id(student_id)
        if to_remove != None:
            data_removed = True
            self.students = [
                i for i in self.students if i.student_id != to_remove.student_id
            ]
        return data_removed

    def save(self):
        to_save = []
        for student in self.students:
            to_save.append(student.to_dict())
        # opens the json for writtng
        with open("data/school.json", "w") as file:
            json.dump(to_save, file)

    def __len__(self):
        return len(self.students)
