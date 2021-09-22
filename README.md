# shopify_backend_challenge
Backend challenge project for Shopify application

Make sure you have xterm, python, pip, and npm installed

cd into the main directory if needed and run the following:

>source env/bin/activate

>pip install -r requirements.txt

then, give the run command execute permissions:

>sudo chmod u+x run.sh

you should be good to go! just run 

>./run.sh 

and xterm will open, a few deps will be installed (because I didn't have time to write a real deploy) and you're good to go!

I started this at like noon on 9/20, so this isn't how I'd like to do deployment, but navigate to localhost:8080 to check out the app

# using the app
## create a new user
create a new user by clicking the create user button and filling out the form

## log in
log in by entering your log in creds into the log in form

## uploading pictures
just click on the plus icon, pick a photo, and click the upload button

## viewing other users accounts
i probably could have implemented a search, but just go to localhost:8080/home/[username] to view other users uploaded pictures