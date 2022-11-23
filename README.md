# RECIPES 

This is website for all who want to get recipes from around the world and who love cooking. People can add their own recipes, edit and delete them when needed.


## Demo
A live demo can be found [here](https://recipes-m.herokuapp.com/).

## UX

### User stories

As a visitor of the Recipes website, I expect to search for recipes from different cuisines, view them and can register to add my own recipes. 
When I need to return to the website, I expect to login to website then I can see my recipes. Also I can search recipes, edit and delete my own recipes.

I can register or login to the website.

![Register](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/register.jpg "Register")

![Login](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/login.jpg "Login")

And also I can add and edit my recipes.

![Add Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/add_recipe.jpg "Add Recipe")

![Edit Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/edit_recipe.jpg "Edit Recipe")

I can see all recipes list.

![Recipe List](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/recipe_list.jpg "Recipe List")

I can see any recipe's full information.

![Full Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/full_recipe.jpg "Full Recipe")



### Strategy
My aim for the website design was in the easiest way possible to login, to add, edit, delete and search recipes while trying to make a website for user-friendly page.

### Scope
For cooking lovers and users, I wanted to provide them to see, search recipes and add, edit, delete recipes to create their recipe inventory.

### Structure
For all users, they can search and see all recipes even if they do not add them. And also they can add their own recipes and store them on website to check later or to edit or delete them. The website is easy to use as users can navigate all around the site using navbar.

### Skeleton
#### Wireframes

[Main Page](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/recipes.png)

[Register](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/register.png)

[Log In](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/login.png)

[My Recipes](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/my_recipes.png)

[Full Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/full_recipe.png)

[Add Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/add_recipe.png)

[Edit Recipe](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/edit_recipe.png)

[Manage Cuisines](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/cuisine_list.png)

[Add Cuisines](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/wireframes/add_cuisine.png)

### Surface

The orange color was used to design the page.

### Technology

1. HTML
2. CSS
3. Materialize (1.0.0)
4. Python 3
5. MongoDB Atlas
6. PostgreSQL


### Database Schema
![Database Schema](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/db_schema.jpg "Database Schema")

Database divided into three sections: Cuisine, users and recipes. Postgresql database was used for "cuisine" and "users" tables and MongoDB database was used for the "recipes" collection. There is a relationship on "cuisine_name" data between these databases.



### Features
This website was designed for several pages. For first time users, they can find register section on the main page. After registration, Recipe list is shown and the user can also access New Recipe and My Recipe section. Under My Recipe page, the user can edit and delete their own recipe. Every delete button on every recipe card has a defensive programming modal built. When the user wants to delete a recipe, a modal pop up appears and asking the user to confirm if they want to delete or not. The admin can only add, edit and delete cuisines to the website. When admin deletes a cuisine, any recipe under this cuisine will delete automatically because of the relation in the databases between cuisine and recipes. The site was build for mobile friendly using Materialize features. 


### Testing
When you look at this website you can find information about the recipes.

All navigation links have been tested all over the website.

All forms and their validation have been tested. If you do not fill the form, you will be notified because the "required" attribute was added to each fields of the form.

#### Lighthouse

Lighthouse chrome extension was used to determine the website’s performance, accessibility, best practices, and SEO for index, myrecipe and fullrecipe pages. All test results were passed.

##### Home Page

![Home Page](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/lighthouse.jpg "Home")

##### My Recipe Page

![My Recipe Page](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/lighthouse_myrecipe.jpg "My Recipe Page")

##### Full Recipe Page

![Full Recipe Page](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/lighthouse_fullrecipe.jpg "Full Recipe Page")

This website was tested on different browsers and mobile devices to make sure everything is working correctly. 

Manual testing of all elements and functionality on every page
Browsers tested:
* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari

No errors were found on the above browsers.

Devices tested:
* IPhone 12
* IPhone 11
* IPhone 7
* Samsung Tablet S6
* Samsung S20 Plus
* Samsung Galaxy S10
* Samsung A52

No errors were found when testing on the above devices.

**---**

| Page  | Section   | Action    | Expected Performance  | Result |
| ----- | --------- | --------- | --------------------- | ------ |
| Home Page  | Tab at top of page    | On a desktop go to https://recipes-m.herokuapp.com/get_recipes    | The Home Page displays; there is a recipe list.   | Pass |
| | Navigation Bar  | The name "Recipes" displays on the left hand side    | The name "Recipes” in the correct position   | Pass |
| | | Confirm 3 navigation links display, which include: Home, Log In and Register    | 3 navigation links display   | Pass |
| | | Click each navigation link    | The correct corresponding page displays   | Pass |
| | Responsiveness  | Go to Dev Tools and confirm the page displays correctly when you reduce and expand the margins    | The correct page displays   | Pass |
| | | Change the pixels to 992px    | The hamburger menu displays  | Pass |
| | | Click the hamburger menu    | The Name of the website and 3 links display being which include: Home, Log In and Register  | Pass |
| Recipe List/Home Page  | Main    | On a desktop go to https://recipes-m.herokuapp.com/get_recipes    | The Recipe List Page displays with a search bar and a reset and search links above the recipe list   | Pass |
| | | Type “Chicken” in the search bar    | The recipe “Easy Chicken Parmesan” displays  | Pass |
| | | Confirm the recipes display on the page    | The recipe displays with a photo of the recipe, the name of the recipe, the name of the cuisine, who created the recipe, the prep time, the cook time, serves and a link to “View Full Recipe” button  | Pass |
| | | Click View Full Recipe    | The image of the recipe, the name of the recipe, the ingredients and instructions display  | Pass |
| Log In Page  | Main    | On a desktop go to https://recipes-m.herokuapp.com/login     | The Log In Page displays   | Pass |
| | | There is a prompt for Username and Password    | The prompts display  | Pass |
| | | Click the Log In link    | A prompt displays on the Username to ask you to complete the field  | Pass |
| | | Type a Username and click Log In    | A prompt displays on the Password to ask you to complete the field  | Pass |
| | | There is a link underneath the Log In button to Register Account    | The Register Account link displays  | Pass |
| | | Click the Register Account link    | The Register page displays  | Pass |
| | | The title Register displays   | The title displays  | Pass |
| | | There is a prompt for Username and Password   | The prompts display  | Pass |
| | | Click the Register button   | A prompt displays on the Username to ask you to complete the field  | Pass |
| | | Type a Username and click Log In   | A prompt displays on the Password asking you to complete the field  | Pass |
| | | There is a link underneath the Register button to Log In   | Clicking the link displays the Log In page  | Pass |
| Register Page  | Main    | Enter a Username and Password and click Register     | You are taken to the Profile page and “Registration Successful” displays   | Pass |
| | | Click the Log Out button   | You are taken to the Login page and “You have been logged out” displays  | Pass |
| Log In Page  | Main    | Enter a Username and Password that you registered with    | You are taken to the Profile page and “Welcome, 'username' ” displays   | Pass |
| Add Recipe Page  | Main    | Click the New Recipe link    | The Add Recipe Page displays   | Pass |
|  | Main    | The Add Recipe form displays    | The sections to complete are Choose Cuisine, Recipe Name, Preparation time, Cooking Time, Serves (which is number only), Ingredients, Instructions and there is a part to Add an Image URL and all fields are mandatory   | Pass |
| | | Click Add Recipe   | The Recipe List page displays with a message stating the “Recipe Successfully Added” on the top of the page  | Pass |
| My Recipes Page  | Main    | Click the My Recipes link    | The My Recipe List page that was added displays with an edit and delete button   | Pass |
| | | Click the Edit button   | The Edit Recipe page displays with all the fields populated  | Pass |
| | | Go to the bottom of the page and click Cancel   | The Recipe List page displays  | Pass |
| | | Go back to the My Recipes page   | The My Recipe List page displays  | Pass |
| | | Click the Edit button   | The Edit Recipe page displays with all the fields populated  | Pass |
| | | Make a change to the recipe and click Edit Recipe   | The Recipe List page displays and the change has been saved, you may have to click View Full Recipe to see some changes, all depends on where you made the change, A flash message stating the “Recipe Successfully” Updated displays  | Pass |
| | | Click My Recipes and delete the recipe that you created   | The pop-up message “Do you really want to delete this recipe?” displays and click Yes. Then Recipe List page display with a message stating the “Recipe Successfully Deleted”  | Pass |
| | | Click My Recipes   | The recipe has been deleted  | Pass |

**---**

#### W3C Validation 

HMTL and CSS codes were tested on W3C Validation Service and both tests were passed but there is an error related to Materialize CSS file on CSS results.

You can find the links to the test results here:

[HTML Test Result Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipes-m.herokuapp.com%2F)

[CSS Test Result Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frecipes-m.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

You can find the screenshoots here:

[HTML Test Result](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/HTML.jpg)

[CSS Test Result](https://raw.githubusercontent.com/ayhanuzumcu/milestone-project-3/main/recipes/images/CSS.jpg)

During the self-testing, I have added a defensive programming then users can not delete recepies accidentally.

Also just admin can add, edit and delete cuisines. 

#### Bugs/Fixes

**Images on the recipe and my recipe pages**

**Issue**: I had an issue with the quality of the images as they appeared stretched.
* **FIX**: I added an outer div before the picture frame div. And I added outer class for the outer div and frame class for the picture frame div and I added height to 300px and width to 250px for the outer div in the css file.



### Deployment
#### To Heroku
Heroku is used to deploy this project. To do this, follow these steps:
1. In GitPod CLI create requirements.txt file and Procfile.
2. Go to Heroku and login. Create new app, add a name and choose region.
3. Install postgres.
4. Insert relevant information under "Config Vars" like IP, PORT, SECRET_KEY, DATABASE_URL.
5. Navigate to the Deploy tab and select GitHub. Search for your repo and click connect.
6. Select "Enable Automatic Deploys"
7. Click "Deploy Branch"
8. Click "Open App" to see the website.


## Credits

### Content
Materialize was used to create the design with responsiveness and styling of the website. Stack Overflow and W3C Schools websites were used to provide some source of codes relating to HTML and CSS. Also I followed the Task Manager Walk Through Project from Code Institute for doing this project.

### Media

Recipes and photos have been taken from:

[My Food Book](https://www.myfoodbook.com.au)

[Delish](https://www.delish.com)

[Eating Well](https://www.eatingwell.com) 

[The Spruce Eats](https://www.thespruceeats.com)

[BBC Recipes](https://www.bbc.co.uk/food/recipes)

All icons were taken from [Font Awesome](https://www.fontawesome.com/) website.