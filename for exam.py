def display_menu():
    print("Phonebook menu")
    print("1.Add contact")
    print("2.update contact")
    print("3.delete contact")
    print("4.search contact")
    print("5.display all contact")
    print("6. exit")
def add_contact(phonebook):
    name=input("enter contact name:")
    if name in phonebook:
        print(f"{name} already exit")
    else:
        phone=int(input("Enter the phone number"))
        phonebook[name]=phone

def phonebookapp():
  phonebook={}
  while True:
      display_menu()
      choice=input("any")
      if choice=='1':
          add_contact(phonebook)

phonebookapp()          
