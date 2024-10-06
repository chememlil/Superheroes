SUPERHEROES

This repository contains the code for a Flask API for tracking superheroes and their superpowers.

Project Overview
This API allows users to manage heroes and their powers. Users can view all heroes, get details for a specific hero, view all powers, get details for a specific power, update a power's description, and associate existing heroes and powers.

Setup
Clone this repository.
Create a virtual environment and activate it.
Install dependencies: pip install -r requirements.txt   
Configure your database connection (details not included in this repository for security reasons).
Run database migrations: flask db migrate and flask db upgrade.
(Optional) Seed your database with sample data: flask seed (seed file not included).
Functionality
The API provides the following functionalities:

Get all Heroes (GET /heroes): Retrieves a list of all heroes in JSON format.
Get a Hero by ID (GET /heroes/:id): Retrieves details for a specific hero, including associated powers, by their ID.
Get all Powers (GET /powers): Retrieves a list of all powers in JSON format.
Get a Power by ID (GET /powers/:id): Retrieves details for a specific power by its ID.
Update a Power (PATCH /powers/:id): Updates the description of an existing power.
Create a Hero Power Association (POST /hero_powers): Creates a new association between an existing hero and power.
Data Model
The API utilizes three models:

Hero: Represents a superhero with properties like name and super name.
Power: Represents a superpower with properties like name and description.
HeroPower: Represents an association between a Hero and a Power, including the strength level of the association (Strong, Weak, Average).
Validation
The API enforces validations on models:

HeroPower: strength must be one of "Strong", "Weak", or "Average".
Power: description must be present and at least 20 characters long.
Testing
You can use Postman or any other REST client to test the API endpoints. A sample Postman collection (challenge-2-superheroes.postman_collection.json) is provided in this repository for reference.

Contributing
Feel free to fork this repository and contribute improvements. Please ensure your code adheres to the existing style and includes proper tests.


