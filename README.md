# Indiegogetter #
Find new products in  Indiegogo using this webapp!

For this project I decided to use Python and the Flask framework, becauseeb those are the ones I have the most experience with building webapps.Python also has some nice tools to make and handle APIs calls like urllib and simplejson.


## Instructions ##
* First make sure you're using python 2.7.10, Macs already have python installed but just in case go [here] (https://www.python.org/downloads/mac-osx/) and find the 2.7.10 version and select the Mac Installer.
* Go to the command line and type `python`, you should see the following:
  ![python image](/python_repl.png)
* Now let's install pip using easy_install and type in your password:
  `sudo easy_install pip`
* For this project you'll need a few libraries, to install them follow these steps: 
  1. For *Flask* follow the instructions on their [website] (http://flask.pocoo.org/docs/0.10/installation/)
  2. For *urllib2* on your terminal type `pip install urllib2`
  3. For *simplejson* on your terminal type `pip install simplejson`
*Now that you have the python libraries, there is a css library Bootstrap and a js library called Jquery on the header of the html file. I incorporate them using Bootstrap CDN by including the css style sheet in the head tag of the hml file:
![boostrap](/bootstrap_cdn.png)
and the bootstrap js file and jquery at the end of the body tag:
![jquery](/jquery_bootstrap.png)

*Finally make sure you're in the root directory and just run this command:
  `python run.py`
And go to [http://localhost:5000/](http://localhost:5000/)

And donate,contribute and build!
