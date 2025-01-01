class Ecommerce:
    def __init__(self, name, email,phoneNumber,finalPrice):
        self.customer_name=name
        self.customer_email=email
        self.customer_phonenumber=phoneNumber
        self.final_price=finalPrice

    def display(self):
        print(f'Customer Name: {self.customer_name}, and final invoice amount is: {self.final_price}')

customer1=Ecommerce("Umesh","abc@abc.com",1234567890,1000)
customer1.display()

customer2=Ecommerce("Selenium","def@gmail.com",8888888888,2000)
customer2.display()

