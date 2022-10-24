# RECIPES 

This is website for all who want to get recipes from around the world and who love cooking. People can add their own recipes, edit and delete them when needed.


## Demo
A live demo can be found [here](https://recipes-m.herokuapp.com/).

## UX

### User stories

As a visitor of the Recipes website, I expect to search for recipes from different cuisines, view them and can register to add my own recipes. 
When I need to return to the website, I expect to login to website then I can see my recipes. Also I can search recipes, edit and delete my own recipes.

I can register or login to the website.

![Register](https://recipes-m.herokuapp.com/recipes/images/register.jpg "Register")

![Login](https://recipes-m.herokuapp.com/recipes/images/login.jpg "Login")

And also I can add and edit my recipes.

![Add Recipe](https://recipes-m.herokuapp.com/recipes/images/add_recipe.jpg "Add Recipe")

![Edit Recipe](https://recipes-m.herokuapp.com/recipes/images/edit_recipe.jpg "Edit Recipe")

I can see all recipes list.

![Recipe List](https://recipes-m.herokuapp.com/recipes/images/recipe_list.jpg "Recipe List")

I can see any recipe's full information.

![Full Recipe](https://recipes-m.herokuapp.com/recipes/images/full_recipe.jpg "Full Recipe")



### Strategy
My aim for the website design was in the easiest way possible to login, to add, edit, delete and search recipes while trying to make a website for user-friendly page.

### Scope
For cooking lovers and users, I wanted to provide them to see, search recipes and add, edit, delete recipes to create their recipe inventory.

### Structure
For all users, they can search and see all recipes even if they do not add them. And also they can add their own recipes and store them on website to check later or to edit or delete them. The website is easy to use as users can navigate all around the site using navbar.

### Skeleton
#### Wireframes

[Main Page](https://recipes-m.herokuapp.com/recipes/wireframes/recipes.png)

[Register](https://recipes-m.herokuapp.com/recipes/wireframes/register.png)

[Log In](https://recipes-m.herokuapp.com/recipes/wireframes/login.png)

[My Recipes](https://recipes-m.herokuapp.com/recipes/wireframes/my_recipes.png)

[Full Recipe](https://recipes-m.herokuapp.com/recipes/wireframes/full_recipe.png)

[Add Recipe](https://recipes-m.herokuapp.com/recipes/wireframes/add_recipe.png)

[Edit Recipe](https://recipes-m.herokuapp.com/recipes/wireframes/edit_recipe.png)

[Manage Cuisines](https://recipes-m.herokuapp.com/recipes/wireframes/cuisine_list.png)

[Add Cuisines](https://recipes-m.herokuapp.com/recipes/wireframes/add_cuisine.png)

### Surface

The orange color was used to design the page.

### Technology

1. HTML
2. CSS
3. Materialize (1.0.0)
4. Python 3
5. MongoDB Atlas
6. PostgreSQL


### Features
This website was designed for several pages. For first time users, they can find register section on the main page. After registration, Recipe list is shown and the user can also access New Recipe and My Recipe section. Under My Recipe page, the user can edit and delete their own recipe. Every delete button on every recipe card has a defensive programming modal built. When the user wants to delete a recipe, a modal pop up appears and asking the user to confirm if they want to delete or not. The admin can only add, edit and delete cuisines to the website. When admin deletes a cuisine, any recipe under this cuisine will delete automatically because of the relation in the databases between cuisine and recipes. The site was build for mobile friendly using Materialize features. 


### Testing
When you look at this website can find information about the recipes.

All navigation links have been tested all over the website.

All forms and their validation have been tested. If you do not fill the form, you will be notified because the "required" attribute was added to each fields of the form. 

This website was tested on different browsers and mobile devices to make sure everything is working correctly. On mobile devices, the page was looking responsive and all sections was shown in the middle.

HMTL and CSS codes were tested on W3C Validation Service and both tests were passed.

You can find the links to the test results here:

[HTML Test Result Link](#)

[CSS Test Result Link](#)

You can find the screenshoots here:

[HTML Test Result](https://recipes-m.herokuapp.com/recipes/images/HTML.jpg)

[CSS Test Result](https://recipes-m.herokuapp.com/recipes/images/CSS.jpg)

During the self-testing, I have added a defensive programming then users can not delete recepies accidentally.

Also just admin can add, edit and delete cuisines. 


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