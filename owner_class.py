from human_class import *

class Owner(Human):

    def __init__(self, h_name, phone, email, payment_details):
        super().__init__(h_name, phone, email)
        self.__payment_details = payment_details


