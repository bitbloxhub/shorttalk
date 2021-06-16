# shorttalk
write short 50-character posts with shorttalk
## Requirements
to start, you need [python 3.8.5](https://www.python.org/) and [node-foreman](http://strongloop.github.io/node-foreman/)
## Running
first, run `python3.8.5 -m venv env/`, then run `./env/bin/pip install -r requirements.txt`.  
then, when you need to run it, run:  
```
# however you activate your virtualenv
nf start
```
but replace the line `# however you activate your virtualenv` with however you activate your virtualenv
## Scaling node-foreman
to scale node-foreman, replace `nf start` in the script above with `nf start -x access-port web=worker-number` and replace `access-port` with the port you will access the service on and replace `worker-number` with the number of server workers you want to start
## Deploying
here are the basic steps to prepare for deployment:
- set `DEBUG = False` in `shorttalk/settings.py`
- set up the email properly

if not on [heroku](https://www.heroku.com/), also:
- set up the database
