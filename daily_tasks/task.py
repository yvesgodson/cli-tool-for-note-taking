import datetime


# now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



class Tasks:

    def __init__(self,
        id : int,
        title : str,
        completed : bool,
        created_at : datetime):


        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = created_at 

    def to_dict(self):

        return {                                                       
          "id": self.id,                                             
          "title": self.title,                                       
          "completed": self.completed,                               
          "created_at": self.created_at
      }
    
