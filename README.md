# Indiegogetter #
Find new products in Indiegogo using this webapp!

For this project I decided to use Python and the Flask framework, because those are the ones I have the most experience with when it comes to building webapps. Python (like Ruby) has some nice tools to make and handle APIs calls like urllib and simplejson.
Flask also has a library called Jinja2 for html templates, that let's you handle data on the front end very easily.

## Instructions ##
* First make sure you're using python 2.7.10, Macs' already have python installed but just in case go [here] (https://www.python.org/downloads/mac-osx/) and find the 2.7.10 version and select the Mac Installer.

* Go to your terminal once you have installed python and type `python`, you should see the following:
  ![python image](/python_repl.png)

* Now let's install pip using easy_install and type in your password:
  `sudo easy_install pip`

* For this project you'll need a few libraries, to install them follow these steps: 
 
  1. For **Flask** follow the instructions on their [website] (http://flask.pocoo.org/docs/0.10/installation/)
  2. For **urllib2** on your terminal type `pip install urllib2`.
  3. For **simplejson** on your terminal type `pip install simplejson`.

*Now that you have the python libraries we're going to use, there is a css library Bootstrap and a js library called Jquery we will use. I incorporated them using Bootstrap CDN by including the css style sheet in the head tag of the hml file:

![boostrap](/bootstrap_cdn.png)

and the bootstrap js and jquery files at the end of the body tag:

![jquery](/jquery_bootstrap.png)

*Now, make sure you're in the root directory and just run this command `python run.py`
*Finally go to [http://localhost:5000/](http://localhost:5000/)

Now you can pick, contribute and help build better products!

# Views #
## Home ##
![home](/home_view.png)

## Search ##
![search](/searching.png)
