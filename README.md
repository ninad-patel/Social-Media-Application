# Social Media Application

Project Overview:-

It is a news application which display news articles from news api on which a user can interact with the news article as well as other people on this social networking platform. It also allows users to connect, share news updates, and engage with each other’s point of view in a dynamic and interactive environment. It is developed using html and css for front-end and python and flask framework for back-end. All the features and functionality of the website are as follows:

1. First of all, login page appears because home page appear only if the user is logged in.
2. Once user is logged in, home page appears with news updates on which they can interact to the news article by liking, commenting and sharing that particular news to their friends and connections who are connected with them through this platform.
3. Users can messsage personally with each other and talk about a particular news.
4. Log out button is there to log out which redirect to the login page.

How all these functionality works?
1. When the program is run on localhost, user needs to login or create an account if it is a new user.
2. When a user signup on signup.html page, /signup route's method store that data into the mysql database.
3. When a user login on the login.html page, /login route's method checks the username and password. If user username and password matches with the data in the database, user is logged in and session is started.
4. Once the user is logged in, app / route's method fetch the live news using fetch_live_news function with the help of news api and then display them on the page.
5. When user interact with the article, like, comment and shares are count using their respective columns in the database.
6. When a user clicks logout, /logout route's method clear the session using session.clear() method. This will logout the user and redirect to the login page again.
