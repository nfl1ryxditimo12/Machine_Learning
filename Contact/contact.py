class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name :", self.name)
        print("Phone Number :", self.phone)
        print("Email :", self.email)
        print("Address :", self.addr)


def set_contact():
    name = input("Name : ")
    phone = input("Phone Number : ")
    email = input("Email : ")
    addr = input("Address : ")
    contact = Contact(name, phone, email, addr)

    return contact


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("선택 : ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone + '\n')
        f.write(contact.email + '\n')
        f.write(contact.addr + '\n')
    f.close()


def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readline()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip('\n')
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        addr = lines[4 * i + 3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()


def run():
    contact_list = []
    load_contact(contact_list)

    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        elif menu == 2:
            print_contact(contact_list)

        elif menu == 3:
            name = input("삭제할 이름 : ")
            delete_contact(contact_list, name)

        elif menu == 4:
            store_contact(contact_list)
            break


run()
