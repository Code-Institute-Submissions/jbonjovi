<img src="media/responsive-1.png" alt="homepage">
<img src="media/responsive-2.png" alt="shop">
<img src="media/responsive-3.png" alt="bonjovi">
<img src="media/responsive-4.png" alt="contact">
<img src="media/responsive-5.png" alt="blog">

## Bonjovi
This site is dedicated to the Band's fans and offers them the ability to access their music, most updated articles
and above all the ability to purchase their merchandise.
The site color has been chosen in line with the latest album called '2020' which gives a strong impact as it is mainly 
black however the grey/red used throughout the site is reflecting the logo palette.


## Site Structure
The menu of the site is quite simple with a navigation focused first on the band's social media and fans account.
It gives the fans the ability to reach out to their favourite band but also getting info on their tour dates, listen to their
music, purchase their merchandise by categories, and be part of the jbj xp. 

The top navigation provides:
--links to the band's official social media accounts
--the users' account: provides the ability to login to an existing account, create an account by registering, upon registration, it
offers a link to their profile and the option to logout, and if the user is a super user there is a product management link added
to either add a new product, edit, update or delete an existing one.
--view of their current shopping bag.

# The menu is as follow:
The navigation is very easy
--A new feature has been added to the site: a Blog 
--Home -- the logo also brings you back to the homepage
--JBJ Boutique -- offers a dropdown by category
--bonjovi -- gives information on the band next tour appereances
--Contact us -- provides the user with a large selection of the band's albums and ability to either buy or stream them


As a user I want to surf this site and be able to get back to the homepage easily. Both the Home menu item and the logo brings me back to the homepage.

As a user if I want to purchase some merchandise I would like a simple navigation through the menu to the shop. 
The menu currently offers a one click to all items or provides a select by merchandise category option.
The JBJ Boutique is the ecommerce part of the site where users/visitors can see all the items displayed by categories.
Upon surfing on this page, the users can sort the products as well as make a search to find their favourite items.

As a user by clicking on the Bonjovi page I would like to see what the band is about, if any tour is scheduled and if there is some news on their coming tour.
As this is a band, it is important to have the option to listen to their album. as a user I would like to navigate through the bonjovi page and 
have the album displayed and when choosing to buy or stream not only being redirected to a different page but the page opens up in a new window.

As a user I would want to navigate to the Contact page to be able to gte in touch and send a mail to the band whether to request info, check on the tour dates or enquire about a specific merchandise.

## User stories
As a user I would like to feel close to the band, I would want a site that is easy to use, easy to navigate and gets me to sign up
and eventually purchase some items.
For that reason, the use of impactful images of the band is important. I am happy seeing the band and having the ability to 
be part of the jbj experience gives a sense of closeness to them.
As a user being able to register by providing a simple email and password to the 'fan club' is bringing me closer to the band. 
When navigation through the boutique, being able to see the products by category helps me as a user filter what I am looking for, and if 
I am interested in the cheapest product for example I can use the sort out option provided. 
Once the product selected, the toast message gives me an indication that it has been added to my basket which is a nice update to have as it also provides me with the 
option to either checkout ie purchase or continue shopping.
As a user if I want to checkout and find out on the page that I can benefit from free delivery it will entice me to purchase some more,
which I can do by choosing the go back to shopping option.
As a user it is also important for me to know that the purchases are secure. So after purchasing, an order number is displayed and a confirmation email will be sent.
If as a user I have an account, my order history will be displayed in my profile as a nice reminder and also to avoid purchasing the same products or simply as a folow up if 
there are delivery issues.
As a user having the option to purchase without registering is great. 
However any fan would want to register and have a profile so as a user I am happy to find that option on display on the top navigation.
When looking at the music page, as a user it shows me what are the latest albums but giving the option to buy or stream enhance my will to listen to the track without worrying about
the legality of it.
As a user making a purchase and receiving a confirmation email is important.

As a superuser, it is important for me to know that I am the only person whom can be in charge of the Boutique's product management.
Once logged in as a superuser, I will be interested in adding a product, editing an existing one, updating and deleting if products are out of stock.
and also making sure all the images load properly before logging out safely.

## Wireframes
Please find my wireframes in the media folder under New Project.pdf

## Features
**Branded design and easy navigation:** the jbj boutique is easy to navigate to, the products are displayed in cards where all details ie price are
available, when a user click on the product image, it brings them to an individual product detail page they can select the size when appropriate, the quantities and 
more importantly they can add it to their bag. A choice of size is given to any apparel products and the quantity can also be selected
**User-focused order functionality:** Once the user select the product he/she wants to purchase and they want to complete their order, by clicking on secure checkout on either the toast message 
or the actual checkout page, it directs them to a secure checkout where they are asked to fill up their order details ie name, email, address before submitting their card details.
**Social media:** as we are in difficult time it is important to give the users the ability to stay connected with the band in all means especially through their active social media platforms.
**Music buying and streaming:** With all the legality involved around music, it is important to provide the user with the right channels.
**Blog:** I have created a blog that shows posts with images, only a designated superuser can add, update or delete the posts
**Contact us:**By inputting the name, emails and writing a message every user can get in touch with the site admin.
**Login in with Facebook:**Option to login with the social media platform Facebook is available when trying to Login
**register:**the menu offers a register option with authentication: email confirmation.
**profile:**user profile is set up and running if a user wants its details to be saved onto the db. Once revisiting the ;profile page, the user is 
offered with an order history, any profile can be updated at any time.

## Features for the future
**Youtube livestream:** with what is happening today, most gatherings such as concerts have been cancelled, a user will definetly enjoy the band's future live streaming online through youtube
**Tour dates:** as soon as the concerts are back on, add the ability to purchase/book tickets online

## technologies used
**HTML** 
**CSS**
**Javascript/jquery** 
**Python** 
**Github and gitpod**
**Fontawesome** 
**Django**
**Heroku**
**Stripe**
**AWS**

## tools used
**Wireframes** to create the wireframes
**W£C HTML Validator** to proof html files
**PEP8 validator** to proof python files
**Autoprefixed** to check css code

# Heroku deployment
Once the jbj site was set I have deployed with Heroku.

**deployment steps:**
First create a new app on heroku site by clicking new and create new app, I gave it the next available but close to my gitpod project name: jbonjovi.
then I chose europe as a region. On the resources tab, I provisioned a new Postgres database.
then installed dj_database_url, and psycopg2 in gitpod so to be able to use the postgres with accordingly pip3 install dj_database_url and pip3 install psycopg2-binary
then I froze the requirements with pip3 freeze > requirements.txt
To set up the new database I imported dj_database_url, commented out the default configuration and replaced the default database with a call to dj_database_url.parse, adding the url databse data from heroku
After that I ran the migrations with Python 3 manage.py migrate.
Followed by loading the fixtures, first categories python3 manage.py load data categories, then products with  python3 manage.py loaddata products
After that I have created with python3 manage.py create superuser.
Before commiting these changes I have uncommented the database default config.
At this stage I have added a piece of code on the app settings so that I can open my app either with heroku or on localhost.
The next step, I installed gunicorn with pip3 install gunicorn, created a Procfile and disabled collectstatic as I want this to be stored in S3 service from AWS.
this required to add the hostname into the app settings.py
I then initialised heroku remote in gitpod, logged in heroku through gitpod and pushed the code.
After that I realised my secret keys were bare so created a env.py and stored my secret keys in there and also added the secret keys in settings tab reveal var in heroku too.
My next step was to set up the automatic deployment on the heroku site simply by linking my repository through heroku and chosing the automatic deploy otpion offered on the page.

PS: STEPS TO SET UP AN ENV.PY:
    --Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
    --If you don't have one already, create a file named .gitignore  in the root directory of your project.
    --Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text to it: env.py 
    --At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” underneath you can assign your environment variables using the following syntax: 
    --os.environ["Variable Name Here"] = "Value of Variable Goes Here" 
    --Example: os.environ["SECRET_KEY"] = "ohsosecret" 
    --Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project or settings.py file for Django project. Add this under your other imports at the top of the file. 
    import os
    if os.path.exists("env.py"):
    import env 

To store the static files, I have created a AWS account, and on the S3 service created a new bucket and opened its access to the public, added a few settings on static website hosting, then
on permissions tab where I pasted in a coors configuration then on the bucket policy tab the type being s3 bucket policy and the action getobject, added the ARN clicked on statement and generate policy which I copied into the bucket policy editor.
To allow access to all I added /* at the end of my resource key.
Onto the IAM service, to create a new user. I created a group first then created a policy which is a generic one from json import managed policy.
I had to copy the ARN from the bucket again.
then click review policy give it a name and click create policy.
The last step is to create a user bonjovi-staticfiles-user with programmatic access and add it to our group. once saved a .csv is generated that I have saved as it holds all secret keys to add into my heroku settings reveal var.
Following this I had to install pip3 install boto3 and pip3 install django-storages and added the corresponding settings in gitpod: AWS_STORAGE_BUCKET_NAME and  AWS_S3_REGION_NAME then remove the disable collectstatic variable add the new secret keys into my env.py, write the 
corresponding code into the settings.py and run python3 manage.py collectstatic.
A quick look at the s3 site and I could see my static files uploaded. For the media files I have created a media folder into s3 right where my static folder is and added the products images from there.
To finalise the deployment I verified and confirmed my superuser email through the heroku admin platform and added the heroku url to stripe as well as the stripe keys into my heroku var.

**testing deployment:**
If the above deployment is a success than my app will open successfully which it did.
The next step is regarding to the webhooks which I tested by going on the stripe send webhook test and it was successfully
Now onto the order. While ordering a random project and filling all the details required at checked out, checking stripe message: success.
My app is now deployed properly.

# Manual testing
I have manually tested my site continuously through firefox, chrome on tablet and phone huawei and samsung
On logo click the user was directed successfully to the homepage
On any of the menu clicked, the user was directed successfully to its corresponding page
On the account options the user had options as to either register or login. If the user was a superuser then the account was showing an etra 2 options in the dropdown: the profile as well as the product management
when the user is a returning customer than his profile was successfully added.
All social links are opening in a new page as well as all the album buy or stream music button links.
I have manually tested all screen resolutions using the inspect on chrome browser with successfull results.

Testing product management:
I have logged in as a superuser and filled the add products fields before adding the product with an image first then without an image and
the none image has automatically being picked which is a success.
going onto the same added product, as a superuser I was able to modify the description and update it successfully. 
Also when I put a wrong amount in the price tab, a toast message appeared asking me to review it. Which is working.
Then I decided to delete the newly added product and it got processed with no issue.

Testing register:
Once register the required details, a confirmation email is sent, as soon as clicked I am able to sign in.
Upon sign in I was able to go to the boutique add products to my shopping cart and checkout using the generic credit card.
a toast message accompanied me all the way: when adding a product, when checking out, I also was able to set a profile
and once done when I logged back in the profile held a history of my previous orders.

Testing links:
every link opens, every social links open in a new page

Testing sign in:
Tried to sign in as a super user and a random user and both are successful

Testing link on the album tracks:
The link open in a new page on all screen size

Testing the site responsiveness:
http://ami.responsivedesign.is/

# Automated testing
Whenever an issue arised ie an error not clear to resolved I would add a print statement to parts of my codes which became very handy as to point to what went wrong.

**W3C CSS Validator**
2 errors popped: .dropdown-menu: Value Error : background-color none is not a background-color value : none and none is not a background-clip value : none
which I removed from the original file.
I have chosen to ignore the warning as it is relating to the color for the allauth section.

**W3C HTML Validator**
Most of the errors displayed are from the use of the jinja templates and I have been advised to ignore them

**PEP8**
settings.py: the line too long 'problem' can't be resolved as when I did it broke my register an account link. I have been advised to leave it like that.
the Product has no object member error from pylint is also to be ignore

# Bugs

# Credit and media
The content of articles has been copied from the online official interviews article provided by the corresponding magazines
The images are also from the official images site

# Acknowledgement
Thanks to my family for allowing me to follow my dreams
Thank you to all of the Code Institute Tutors whom have thoroughly helped
Thank you to my mentor for giving me good spirit
Thank you assessors for your time


