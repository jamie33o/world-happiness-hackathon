# **Positive Affirmations Journal** 🌈

![amIresponsive](/docs/screenshoots/responsive.png)

Welcome to the *Positive Affirmations Journal* - your new best friend for fostering positivity, mindfulness, and personal growth. Our platform is designed to be an oasis of motivation, allowing you to create, manage, and reflect upon personal affirmations in a supportive environment. Let's embark on this journey to a more positive you!

## Goal

### Problem statement
Many individuals struggle with self-doubt, low self-esteem, and negative self-talk, which can impact their mental well-being and overall quality of life. Traditional methods of affirmations, such as writing them down or repeating them to oneself, may not resonate with everyone or may be easily forgotten in daily routines.

### Objective
The objective of the Affirmative website is to provide a user-friendly platform where individuals can easily record and listen to their affirmations. By utilizing technology, the website aims to make affirmations more accessible and impactful for users, empowering them to cultivate a positive mindset and boost their self-confidence.

### Target Audience

- Individuals seeking to improve their self-esteem and mental well-being.
- Those interested in practicing positive affirmations as a form of self-care and personal development
- Therapists, counselors, and coaches who recommend affirmations as part of their practice
- Anyone looking for a convenient and customizable way to incorporate affirmations into their daily routine

### Benefits
- Convenience: The website offers a convenient platform for recording affirmations anytime, anywhere, using a computer or mobile device.
- Repetition: By allowing users to easily listen to their recorded affirmations repeatedly, the website reinforces positive messaging and helps ingrained them into the subconscious mind.
- Mental Well-being: Regular practice of affirmations has been shown to improve self-esteem, reduce stress, and promote a positive outlook on life, contributing to overall mental well-being.

## Features

### **Seamless Account Management** 🔐
- **Create Your Space**: Easily sign up for a personal account.
- **Secure Access**: Log in/out with ease and recover your password if forgotten.

### **Affirmations Central** 💖
- **Voice Your Positivity**: Record and playback your affirmations.
- **Your Affirmations, Your Way**: Create, update, delete, and store affirmations.

### **Customize Your Experience** 🌟
- **Visual Delight**: Customize background images to inspire.
- **A Joy to Use**: Navigate through a user-friendly interface designed for enjoyment.

### **Connect and Share** 🤝
- **Personal Touch**: Manage your information with ease.
- **Discover and Explore**: Navigate the home page for a seamless experience.
- **group affirmations** : Write affirmations and share to your friends or Family

## Deployment

### Heroku Deployment

The project was deployed using [Heroku](https://id.heroku.com/login).

After account setup, deployment steps are as follows:

1. Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
2. App name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
3. Navigate to the settings tab and click **Reveal config vars**  and add the config vars necessary for the project:
 `CLOUDINARY_URL`(insert your own Cloudinary API key here )                        
 `DATABASE_URL`           (insert your own ElephantSQL database URL ) 
 `DISABLE_COLLECTSTATIC`  1 (temporary) 
 `SECRET_KEY`             (random secret key )                                  
 
Also make sure you create Procfile and requirements.txt file.

4. Navigate to the **Deploy** section by clicking the "Deploy" tab in the navbar, Select **GitHub** as the deployment method and click **Connect to GitHub**.
5. Find the repository wehich you want to deploy and click on **connect**.
6. Find button **Deploy Branch** at the bottom of page.
7. After clicking **Deploy Branch** button it will take few minutes to deploy site and you will have ability to view it  clicking on **view** button.

The project is deployed and can be accessed at [https://affirm-app-057148428853.herokuapp.com/](https://affirm-app-057148428853.herokuapp.com/).

###  ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To set up a database, please follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on **Create New Instance**.
3. Enter a name for the instance.(project name)
4. Select **Tiny Turtle (Free)** free plan.
5. The "Tags" field can be left blank.
6. Click **Select Region**.
7. Select a data center near you.
8. Click **Review**, make sure that all details are correct and then click "Create instance".
9. Once created, click on the new database name, where you can view the database URL and Password.

## Criteria
In this section, we will briefly discuss how our team addressed the applicable criteria:

-  Creative use of CSS frameworks  Bootstrap to create an engaging and user-friendly design.
-  Well-executed project with effective planning using GitHub Projects and a detailed README.md.
-  Project demonstrates responsiveness, accessibility, and thorough testing.
-  Emphasizing collaborative effort and the quality of code produced.

# **Technologies used**

* Python
  * The packages installed for the is project can be found in [the requirements.txt](requirements.txt)
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL
  * Used for the database during development and in deployment.
* HTML
  * HTML was the base language used to layout the skeleton of all templates.
* CSS
  * Custom CSS used to style the page and make the appearance look a little more unique.
* Javascript
  * We have used inline JavaScript to automatically hide displayed messages after a few seconds.
* Bootstrap 5.0.1
  * Used to style HTML and CSS

# Credits

* [GitHub](https://github.com/) was used to store my repository.
* Responsive screenshot made using [amiresponsive.com](https://ui.dev/amiresponsive)
* [coolers.co](https://coolors.co/603f3f-a0acca-e4b67c-de9f13-000000) was used to generate color scheme.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Images:
  * for all images used for site  taken from [pexels.com](https://www.pexels.com/) 
* General references:
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)
    * [Bootstrap Documentation](https://getbootstrap.com/)





