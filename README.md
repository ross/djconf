Example environment-base django config.

usage:

    export ENV=dev
    ./manage.py runserver

All secrets (usernames, passwords, api keys and secrets) should live in
creds.py which should not be checked in to your repo. (it is here for demo
purposes.)
