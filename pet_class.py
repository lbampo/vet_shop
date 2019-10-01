class Pet():

    def __init__(self, d_owner, d_name, d_breed, animal = 'dog'):
        self.d_owner = d_owner
        self.d_name = d_name
        self.d_breed = d_breed
        self.animal = animal


    def get_pet_info(self):
        return f"Name: {self.d_name} \n " \
               f"Breed:{self.d_breed} \n" \
               f"Animal: {self.animal} \n" \
               f"Owner: {self.d_owner} \n \n"


