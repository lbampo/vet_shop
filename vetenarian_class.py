from human_class import *
from appointment_class import *
class Vetenarian(Human):

    def __init__(self, h_name, phone, email, specialization):
        super().__init__(h_name, phone, email)
        self.specialization = specialization
        self.appointment_list = []

    def add_appointment(self, disease, date, pet, vetanarian, price):
        self.appointment_list.append(Appointment(disease, date, pet, vetanarian, price))

    def list_appointment(self):
        count = 0
        for appointment in self.appointment_list:
            print(f"Pet Name: {appointment.pet} \n"
                  f"Disease: {appointment.disease} \n"
                  f"Date: {appointment.date} \n"
                  f"Vet: {appointment.vet} \n"
                  f"Price: {appointment.price} \n \n")

            count += 1


