# Overview

This is the home of our CS470 semester project. The goal was to produce a database model that could form the foundation for a blood bank management system, managing the data of hospitals, blood banks, and clients.

This README is a brief overview, for more information see our Milestone 3 document.

- Abdirahman Ahmed, Joseph Granado, Reece McMillin, Harjot Singh, and Sam Straub.

## Directory Structure

- `database`
   - `python`: This directory houses the data model along with a model-specific fake data generation script.
      - `queries`
         - `create`: This directory contains several files designed to create tables, views, and stored procedures. The primary focus here is on `create_tables.sql`.
         - `delete`: This directory contains one script used to clean up tables to help facilitate rapid iteration during development.
         - `insert`: This directory contains primarily auto-generated queries to satisfy a requirement for data insertion scripts to be SQL rather than the result of a transaction within a Python program.
         - `update`: This directory contains `add_foreign_keys.sql`, which serves to add foreign key constraints. This is done in an atomic transaction with foreign key checks disabled to avoid failure on circular dependencies, a requirement for the project.

# Running

How to run:
1. Install docker-compose
2. In the `milestone3` directory, run `docker-compose up --build` to build and run the containers.
   - (currently this just runs the database container)
   - Once it's up and running, it should be accessible at `localhost:3306` for tools like mysql workbench.
3. When you're done, you can exit with Ctrl-C and run `docker-compose down -v --remove-orphans --rmi all` to bring the containers down and remove their artifacts (so they build fresh next time).

> **NOTE**
> 
> If you have MySQL installed, running `python/monolith.sql` should build the entire database at once. We use Docker in this instance because we also put some effort into building a backend for the app which had to be scrapped due to a new set of requirements for the final deliverables.
