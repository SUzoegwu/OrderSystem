# Changelog

## [Unreleased]
- Add logic to substitute item for a desired item if the course was not included in the order. Currently only drink can be substituted with Water if drink is not included
- Ability to store env variables needed for ordering system in a database and connect to the database via database connection.

## [1.1] 27 March 2022
### ADDED
- Ability to dynamically customize courses that are mandated to be ordered with the meal
- Ability to add courses to the order such as if you want to include appetizers

## [1.0] 26 March 2022
### ADDED
- Initial release of OrderSystem
- Ability to store your menu in environment variables and order using this package. Currently menu can have main, side, course and dessert. Every order needs to have a Main and Side order