import json
import passwordmodule as pm
import random as rd


class Signup:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = None

    def is_valid_email(self):
        return '@' in self.email and self.email.endswith('.com')

    def is_valid_password(self):
        if pm.final_count(self.password):
            return True
        else:
            return False

    def id_generate(self):
        id_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&'
        self.id = ''.join(rd.choices(id_chars, k=10))
        return self.id

    def gen_json(self):
        user_data = {
            'name': self.name,
            'id': self.id_generate(),
            'email': self.email,
            'password': self.password
        }
        return user_data

    def file_open_write(self):
        with open("SmallProjects/credentials.txt", 'a') as file:
            json.dump(self.gen_json(), file)
            file.write('\n')

user_1 = Signup('Sagar Moktan','sagarmoktna@gmail.com','moktan@3')

