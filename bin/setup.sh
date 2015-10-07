#!/bash/bin

#
# Setting-up dependencies.
#
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
