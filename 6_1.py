from collections import UserDict

#Base class for all record fields
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

#Class for storing contact name (required field)   
class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name can't be empty")
        super().__init__(value)

#Class for storing phone number with validation
class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

#Class for storing contact information
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value
                return
        raise ValueError("Phone number not found")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"

#Class for storing and managing records  
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    
#Test
if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book)

    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")

    book.delete("Jane")
    print(book)