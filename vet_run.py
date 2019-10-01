from owner_class import *
from pet_class import *
from vetenarian_class import *
from appointment_class import  *

# Create owners

owner_1 = Owner('Abigail Ohora', '07584763456', 'a_Ohora@hotmail.com', 'Credit Card *****1977')
owner_2 = Owner('Carang Teng', '07897876456', 'teng@yahoo.co.uk', 'Cash')
owner_3 = Owner("Ulysses Harver", '02084857675', 'Uhar@outlook.co.uk', 'Cheque')
owner_4 = Owner('Montgomery Huggins', '07903854567', 'hugme@hotmail.com', 'Cash')
owner_5 = Owner('Breezy', '07415135919', 'breezy@yahoo.co.uk', 'Debit Card ******9033')

# Create Pets

pet_1 = Pet('Breezy', 'Kojo', 'doberman')
pet_2 = Pet('Ulysses Harver', 'Botamian', 'shitsu' )
pet_3 = Pet('Abigail Ohora', 'Dennis', 'Golden retriever')
pet_4 = Pet('Montgomery Huggins', "Badu", 'Pug')
pet_5 = Pet("Carang Teng", 'princess', 'chow chow')

pet_list = [pet_1, pet_2, pet_3, pet_4, pet_5]

# Create Vets

vet_1 = Vetenarian('Dr Russell Westbrook', '02083006421', 'westy@hotmail.com', 'Mouth Disease')
vet_2 = Vetenarian('Dr Dun Knoe', '02083006422', 'udunknoe@da-ting.com', "heart surgery")
vet_3 = Vetenarian("Dr Who Dis", '02083006424', 'diswho@ahaha.co.uk', "tail specialist" )
vet_4 = Vetenarian('Dr Yew CantseeMe', '02083006425', 'johncena@wwe.co.uk', "key hole surgery")

vet_list = [vet_1, vet_2, vet_3, vet_4]

vet_1.add_appointment('Broken nose', '02/10/2019', 'Kojo', 'Dr Russell Westbrook', '£32')
vet_3.add_appointment('Extreme case of flies', '02/10/2019', 'Botamian', 'Dr Who Dis', '£32')
vet_2.add_appointment('Heart Disease', '17/10/2019', 'Badu', 'Dr Dun Know', '£14')
vet_3.add_appointment('Tail wont wiggle anymore', '17/10/2019', 'Dennis', 'Dr Who Dis', '£650')
vet_4.add_appointment('Inflamed bladder', '04/11/2019', 'Princess', 'Dr Yew CantseeMe', '£32')



print('\n')

# #Appointment list for each vet


#Appointment list for each vet
for vet in range(len(vet_list)):
    print(f'Vet : {vet + 1}')
    vet_list[vet].list_appointment()


# Each appointment
# #Vet 1
# vet_1.list_appointment()
#
# #Vet 2
# vet_2.list_appointment()
#
# #Vet 3
# vet_3.list_appointment()
#
# #Vet 4
# vet_4.list_appointment()








#List pet snd owner details
#
# print('\n')
# for pet in range(len(pet_list)):
#     print(pet_list[pet].get_pet_info())
#
# print(pet_1.get_pet_info())
# print(pet_2.get_pet_info())
# print(pet_3.get_pet_info())
# print(pet_4.get_pet_info())
# print(pet_5.get_pet_info())








