# The script is in a python environment running python 3.8.0
 
- The input that should be entered and provide an example/example file.
    - datetime and sys are part of the standard python 3.8.0 library
    - Install croniter by running:
        pip install croniter
 
- To ensure that the command line program will run successfully under all reasonable circumstances
    - Run the unit test file by running this command in the terminal: python -m unittest test_next_cron_update.py
        - The test file will run 2 test:
            - 1st: The number of command line arguments
            - 2nd: Where the format of the input time is correct

- To run the program please run the command below in the (shell) terminal with python 3.8.0:
    - Windows/Linux: python next_cron_update.py 16:10 < crontab
        - Following the time format HH:MM
            - If entry is incorrect hints will be given within the terminal
