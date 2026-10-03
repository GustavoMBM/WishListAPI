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

```bash
git clone https://github.com/GustavoMBM/WishListAPI.git
cd WishListAPI
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
flask db upgrade
```

Run the application:

```bash
python main.py
```

The API will be available at:

```text
http://127.0.0.1:5000
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

```text
http://127.0.0.1:5000/docs/swagger
```

or

```text
http://127.0.0.1:5000/docs/redoc
```
