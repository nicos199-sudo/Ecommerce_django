from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')

        #validation

        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'password'  : password
        }
        error_message = None

        
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password)

        error_message = self.validateCustomer(customer)
        
        #saving
        if not error_message:
            customer.password = make_password(customer.password)

        
            customer.register()
            return redirect('home')
        else:
            
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;

        if (not customer.first_name):
            error_message = 'first name required'
        elif len(customer.first_name) < 4:
            error_message = 'first name must be 4 char long or more'

        elif not customer.last_name:
            error_message = 'last name required'

        elif len(customer.last_name) < 4:
            error_message = 'last name must be 4 char long or more'


        elif len(customer.email) < 4:
            error_message = 'email must be 4 char long or more'
    
        elif len(customer.password) < 10:
            error_message = 'password must be 10 char long or more'


        elif customer.isExists():
            error_message = 'This email is already used!!'

        return error_message
