# WishList API

Simple REST API for managing a wishlist, developed with Flask.

## Technologies

* Python

* Flask

* SQLAlchemy

* Flask-Migrate

* Pydantic

* Spectree

* SQLite

## Structure

```text
controllers/  → Routes and endpoints

models/       → Database models

schemas/      → Data validation and serialization

migrations/   → Database migrations

factory.py    → Application Factory

config.py     → Configuration

main.py       → Application entry point
```

## How to Run

Clone the repository:

```
git clone https://github.com/GustavoMBM/WishListAPI.git
cd WishListAPI
```

Create and activate a virtual environment:

```
python -m venv venv
```

Windows:

```
venv\Scripts\activate
```

Linux/macOS:

```
source venv/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

Apply the migrations:

```
flask --app factory:create_app db upgrade
```

Run the application:

```
python main.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

## Troubleshooting

### `ensurepip is not available`

On some Debian/Ubuntu installations, the `venv` package may not be installed.

If the following command fails:

```
python -m venv venv
```

install the package corresponding to the installed Python version:

```
sudo apt install python3-venv
```

For example, if the system specifically requests `python3.12-venv`:

```
sudo apt install python3.12-venv
```

After installing it, remove the incomplete environment and create it again:

```
rm -rf venv
python -m venv venv
source venv/bin/activate
```

Alternatively, `virtualenv` can be used:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### `Could not locate a Flask application`

If the following command is used:

```
flask db upgrade
```

Flask may not automatically detect the application because the project uses an Application Factory instead of the conventional `app.py` or `wsgi.py` entry point.

Use:

```
flask --app factory:create_app db upgrade
```

This explicitly tells Flask to use the `create_app` factory defined in `factory.py`.

After applying the migrations, the application can be started normally:

```
python main.py
```

## Endpoints

| Method | Endpoint             | Description |
| ------ | -------------------- | ----------- |
| POST   | `/api/wishlist`      | Create item |
| GET    | `/api/wishlist`      | List items  |
| GET    | `/api/wishlist/<id>` | Get item    |
| PUT    | `/api/wishlist/<id>` | Update item |
| DELETE | `/api/wishlist/<id>` | Delete item |

## Documentation

The API documentation is available at:

```
http://127.0.0.1:5000/docs/swagger
```

or

```
http://127.0.0.1:5000/docs/redoc
```
