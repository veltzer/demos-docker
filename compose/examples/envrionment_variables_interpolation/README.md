This example explores how to use environment variables in docker-compose.

test this with:
    $ docker-compose config

conclusions
* You can only have one environment block per service in a docker-compose.yml file.
* You can declare variables in two syntaxes ":" and "=". Both work. 
* The quotation works differently and is better in the ":" way
