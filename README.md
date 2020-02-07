# Artwork Style Prediction

## TODO ##
refactor code, write tests, fix dependencies

## Up and Running ##
### setup env ###
```
virtualenv demo
cd demo
source bin/activate
```

### package installation ###
`pip3 install tensorflow==1.14 keras==2.2.5 tensorflow-estimator==1.14 pandas numpy sklearn h5py pyyaml pillow flask flask-restful`

### prep. project ###
1. Copy demo/app.py and demo/model.py from this repo to your project
2. Download model, and use suitable model by updating its path in variable "PATH_MODEL"
https://drive.google.com/drive/folders/1eiPCR6eX00oJn0Fl1vxtZncpxddRNOsn?usp=sharing

### run flask ###
```
export FLASK_APP=app.py
export FLASK_ENV=development
python3 app.py
```