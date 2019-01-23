# The-Perfect-Cushion-Store
CS 341 - Software Design IV - Software Engineering Group Project. Ecommerce Web Site.
An Ecommerce Web Site built to the specifications of the client/Professor. Developed in Python using Django. 
Other languages and technologies used include JavaScript, HTML, CSS, Bootstrap, jQuery, Stripe, and Canva. 
Stripe API was removed in final version of project. Client/Professor required users' addresses to be stored and auto populated. 
Stripe API does not allow for auto-populating fields and requires users to enter all information each time at check out.

Click [here](http://ethanlor.pythonanywhere.com/shop/) to visit the live web site.

![Alt text](https://github.com/lor-ethan/The-Perfect-Cushion-Store/blob/master/Cushion%20Store.png)

For Project Memebers:

Git clone the The-Perfect-Cushion-Store project.

Make sure you are running the current environment in the Anaconda Navigator Python 3.6 and open terminal that is running that ennvironment. 
Or open terminal and have a virtual environment activated. Change directory into the `The-Perfect-Cushion-Store/perfectcusions` folder to 
run the required pip command.

Run this command to install all required packages for project to run
```
pip install -r requirements.txt
```

This command will start the django server to run the website.
```
python mangage.py runserver
```
Go to the http://127.0.0.1:8000 or  http://localhost:8000 to see the current website

-- TODO For Documentation
- include dummy admins and registered users - Completed
- include dummy credit cards provided by stripe - Completed

--TODO for project
- need to redirect when they just put in http://127.0.0.1:8000 to http://127.0.0.1:8000/shop - Completed

### Dummy Credit Cards
### No longer using Stripe in final application version!
Provided by [Stripe](https://stripe.com/docs/testing)

|NUMBER          |BRAND        |
|----------------|-------------|
|4242-4242-4242-4242|Visa      |
|4000-0566-5566-5556|	Visa (debit)|
|5555-5555-5555-4444|	Mastercard|
|2223-0031-2200-3222|	Mastercard (2-series)|
|5200-8282-8282-8210|	Mastercard (debit)|
|5105-1051-0510-5100|	Mastercard (prepaid)|
|3782-822463-10005|	American Express|
|3714-496353-98431|	American Express|
|6011-1111-1111-1117|	Discover|
|6011-0009-9013-9424|	Discover|
|3056-9309-0259-04|	Diners Club|
|3852-0000-0232-37|	Diners Club|
|3566-0020-2036-0505|	JCB|
|6200-0000-0000-0005|	UnionPay|

