from dataclasses import dataclass


@dataclass
class User:
    name: str
    lastname: str
    email: str
    gender: str
    phone: str
    birthday_year: str
    birthday_month: str
    birthday_day: str
    hobby: str
    subject: str
    picture: str
    address: str
    state: str
    city: str


user = User(name='Ruslan',
            lastname='Matygullin',
            email='ruslan@mail.ru',
            gender='Male',
            phone='9770001010',
            birthday_year='1992',
            birthday_month='February',
            birthday_day='21',
            hobby='Sports',
            subject='Biology',
            picture='rus.jpg',
            address='Ulyanovsk',
            state='NCR',
            city='Gurgaon'
            )