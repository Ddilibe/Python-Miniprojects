class Student:
    # [assignment] Skeleton class. Add your code here
    """
        Name: A string 
        Age: An integer 
        Tracks: A list of strings
        Score: A float    
    """
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.tracks = kwargs['tracks']
        self.score = kwargs['score']
        pass
        
    def change_name(self, name):
        """ Method to change students name. It accepts a new name as an argument."""
        self.name = name

    def change_age(self, age):
        """ Method to change students' age. It accepts a new age as an argument. It ensures age remains an integer."""
        self.age = age
        
    def add_track(self, track):
        """ Method to add a new item to students tracks. It accepts a new track as an argument."""
        self.tracks.append(track)
        
    def get_score(self,):
        """ Method to return student’s score."""
        print(self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
