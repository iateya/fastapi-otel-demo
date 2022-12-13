This is a poetry project. If poetry is installed run the following command to install the dependencies

`poetry install --sync`


Activate the virtual environment with:

`poetry shell`

To run the project
`python3 ./fastapi_otel_demo/main.py`

To test the app
`curl http://localhost:9000/hello`

The project contains 2 log config files 
* log-desktop.yaml --> redirects the logs to console formatted as JSON
* log-docker.yaml --> redirects the logs to a file as formatted lines. The log file is rotated at midnight.


Edit main.py to switch between the log config files. In a production setting this can be done via command arguments or environment variables.

The 2 files can actually be merged into one if needed and this way the application will write JSON logs to the console as well as line logs to the file.
