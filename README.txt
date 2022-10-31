This is a example package for showing distribution using pip and including a flask module.

The package includes:

molecule.py - a molecule mass calculator
mflask.py - a flask front-end for the calculator
templates - jinja templates folder for mflask
static - folder for static elements (just some css for jinja at the moment)
docs - an empty folder for docs, nothing there right now
tests - a sub-package holding the unittest tests 

TO SETUP the local development environment
    make sure you have a virtual environment installed
    run "pip install -e ." in the terminal to get setup.py to run and install the development environment
    run "python -m unittest discover" to run the tests from the command line.

TO RUN THE FLASK APPLICATION SERVER:
    with moleflask and flask installed you can run the moleflask app using the flask development server:
        $ FLASK_APP=moleflask.mflask.py flask run

NOTE THAT this is a pre-production server, and the development is not mature enough for a production server

TO RUN THE UNIT TESTS:
    unit tests are in the moleflask package "tests" sub-package (folder). Using test discovery mode:
        $ python3 -m unittest discover moleflask.tests
