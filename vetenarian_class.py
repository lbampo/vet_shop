from human_class import *

class Vetenarian(Human):

    def __init__(self, h_name, phone, email, specialization):
        super().__init__(h_name, phone, email)
        self.specialization = specialization