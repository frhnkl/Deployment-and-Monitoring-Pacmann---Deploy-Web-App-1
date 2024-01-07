# Introduction and Background Problem
A boss of a company is angry at Twitter because it's so heavy. So he ordered his company to make a knock-off version of Twitter which is lighter, more intuitive, and easier to use. This is a simple Twitter-like app created using Flask for the backend and Vue for the front end. The app allows users to register an account, log in, send tweets, upload pictures, and like other tweets. It also includes a leaderboard to track the number of tweets each user has posted. Additionally, there is an admin login to manipulate tweets, such as deleting and editing, as well as deleting user accounts.
# Objective and Features
- User Registration: Users can create accounts with unique usernames and passwords.
- User Login: Registered users can log in securely.
- Posting Tweets: Users can post tweets with text and optional picture uploads.
- Leaderboard: A leaderboard displays the top users by the number of tweets posted.
- Admin Login: Administrators can manipulate tweets, delete tweets, and delete user accounts.

# User Flowchart
![Teks paragraf Anda (1)](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/93494521-2db0-4a6b-bf21-3acbf566b034)
This is the User flowchart. The user will start on the login page. if a User doesn't have an account, they can click on the registration page and once succeed in making an account, the user can go back to the login page and log in to their account. once on the home page, users can interact with each other by liking, tweeting, and uploading pictures. Users can also see leaderboards of who makes the most tweets. after interacting, user can log out of their account
# Admin Flowchart
![Teks paragraf Anda (2)](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/349d0f78-7ad4-4d88-8d28-15e65f15e45b)

For admin, Admin will be presented with a login page for admin. if the admin doesn't have an admin account, they can register and choose what role they want to have. after logging in, an admin can manipulate users and tweets by modifying or deleting them.

# Requirements and Technology Used
### backend
- Python
- Flask
- Flask-Admin
- Flask-Cors
- Flask-JWT-Extended
- Flask-Login
- Flask-SQLAlchemy
- psycopg2
- dotenv
- gunicorn
### frontend
- vue
- vue-router
- pinia
- axios
- datatables.net
- vue-sweetalert2
- tailwindcss

everything is available in both folders. requirement.txt for the backend and package.json for frontend
# User Guideline for Deployment
## Backend
- run flask-backend in the terminal and type
  ```cmd
  flask --app app run
  ```
  DB and backend side will be deployed with flask.
## Frontend
- run vue-frontend in the terminal and type
  ```cmd
  npm run dev
  ```
  Vue will be running and you can click on the localhost link to use it. Frontend and Backend will automatically integrated.
# User Journey Screenshots
- user will start their journey with registration
  ![regis](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/eaf69de6-eeef-4174-b227-b0a67d8ee4bc)
- if the registration succeeds, this message will appear
  ![regis complete](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/236d28e9-2b14-44ae-a208-4e8433d51b26)
- in case there are some error like the user already exists the email is not email type or the password is not matching. error pop-up will appear. in this case, this is a user already existing error.
  ![regis fail](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/21f3948c-45fb-4178-812e-57cc1c8d7a3e)
- after the user logs in, this home page will be presented
  ![twttr home](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/3ead41da-dc32-4e1e-af36-63b416689fd0)
- The user can see other tweets/posts from another user. This, for example, is a tweet that Sumartono tweeted.
  ![tweets from another user](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/35c22593-fa04-4991-b031-33939ef0d27d)
- Users can interact by simply tweeting or tweeting with pictures. For example, we logged in as juan1 and tweeted this. When tweeting succeeds, this message will appear.
  ![tweeting](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/e348ecfe-5c81-4dda-b812-dbdf737e1099)
- the result of said tweet can be seen in this picture
  ![juan tweet](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/28e5eac1-f68b-4628-86be-a6eadbf09168)
- user can also tweet with pictures by simply clicking on upload image which will redirect user to upload their image
  ![upload image](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/4fa40793-4336-462b-aefc-5ca9b69851f7)
- when an image is selected, the user can add words along with the picture
  ![upload pict](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/3f49b528-d146-4336-afd8-96abca2e0689)
- this is the result of the tweet with the picture that we tweeted
  ![uploaded pict](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/5fcaf777-74d7-4214-a9f5-0c7673653f28)
- Users can also see the leaderboards of users and how many tweets they tweeted. As we can see, we tweeted 2 tweets as juan1 and we can see it in the leaderboard
  ![leaderboard](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/eceef2dd-6205-408e-bfbb-6472435f07d4)
- after interacting, users can log out. when the log out succeeds, this message will appear
  ![logout](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/95af9abd-841c-42f8-b798-7fbd588f9bfc)
- there is also an admin panel feature for admin where an admin can manipulate users and tweets. this is the login page for the admin
  ![login form for admin](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/e8ba7b65-4c2b-46d8-bbb4-ac492aabe415)
- in admin panel, admin can see users and manipulate them with edit or delete users. we can see username, registered email, and hashed passwords
  ![admin panel with registered user](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/8823b786-4aed-4211-ab63-277b8e1512b0)
- admin can also see all tweets and manipulate it
  ![admin panel with tweets](https://github.com/frhnkl/Web-Arc-twttr-app/assets/125452431/a1b4b3a3-6801-4830-8ed5-b67c9742dcfe)




