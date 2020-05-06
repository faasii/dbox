# dbox
A Command-line Dropbox client 

#### Requiremnts
* sudo apt-get install python
* pip install dropbox
* pip install wheel - for termux if not installed

### usage 
* **python dbox.py list**           &nbsp;  &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp; &nbsp; &nbsp; ***#List all files of dropbox***
* **python dbox.py upload \<file name> \<dropbox filename>**    &nbsp; &nbsp; &nbsp; ***#Download file from dropbox***
* **python dbox.py download \<dropbox filename> \<filename>**  &nbsp; &nbsp; &nbsp; ***#Upload  file to  dropbox***
* **python dbox.py delete   \<dropbox filename>** &nbsp; &nbsp; &nbsp; ***#Delete file from dropbox***
* **python dbox.py link     \<dropbox file name>** &nbsp; &nbsp; &nbsp; ***#To Generate Shareble link***

#### sample usage
* python dbox.py upload photo.jpg myphoto.jpg
* python dbox.py download myphoto.jpg photo.jpg
* python dbox.py delete myphot.jpg

##### Other info
* you needs to generate Dropbox authentication token in order to use
* the tutorials of  dropbox access token generation is [here](http://99rabbits.com/get-dropbox-access-token/).
