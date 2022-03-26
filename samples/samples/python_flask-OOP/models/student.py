class Student:
    def __init__(self, name: str, student_id: str, term: int = 1):
        """
        Constructor for the student class.
        name:str Cannot be empty
        Student_id: str, starts with A0 and 7 numbers
        term: int (typically 1-4)
        """
        if name == None or type(name) != str:
            raise ValueError
        if type(term) != int:
            raise ValueError
        if type(student_id) != str:
            raise ValueError
        if "A0" not in student_id:
            raise ValueError
        if not student_id[1:-1].isnumeric() or len(student_id) != 9:
            raise ValueError
        self.name = name
        self.student_id = student_id
        self.term = term

    def to_dict(self):
        return {"name": self.name, "student_id": self.student_id, "term": self.term}
