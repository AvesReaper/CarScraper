python -m venv .venv
source .venv/bin/activate (or) source .venv/bin/activate.fish



DEV NOTES:
- pip freeze > requirements-lock.txt => Use this to freeze the pkg versions once ur project is stable

- Phase1:
    - installed fastapi reqs
    - built and tested a simple fastAPI with 2 methods and explored the OpenAPI docs

- Phase2:
    - fastAPI -> SQLAlchemy -> PostgreSQL
    - DONE :
        PostgreSQL installation and testing
        SQLAlchemy configuration
        Database connection establishment
        loaded configuration  from .env
        first database model (Car)
        create tables 
        CRUD endpoints for cars
        Input validation with Pydantic
        Proper project organization
- Phase3:
    - created dockerfile and compose file for containerizing api and postgres services





INSTALLATION:
- WILL MAKE SURE TO BUILD A sh script based on the below steps.

STEPS:
PHASE 1:
- create venv, 
    python -m venv .venv
    source .venv/bin/activate (or) source .venv/bin/activate.fish
- pip install - requirements.txt
PHASE 2:
- installing postgresql
    sudo pacman -S postgresql
    psql --version
    sudo -iu postgres initdb -D /var/lib/postgres/data
    sudo systemctl enable postgresql
    sudo systemctl start postgresql
    sudo pacman -S dbeaver // OPTIONAL
- DB libs were added to requirements.txt
PHASE 3:
- installing Docker
    sudo pacman -S docker
    docker --version
    docker compose --version
    docker run hello-world
PHASE 4:
- installing playwright
    
