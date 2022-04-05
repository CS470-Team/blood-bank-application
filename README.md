# Overview

How to run:
1. Install docker-compose
2. In the `milestone3` directory, run `docker-compose up --build` to build and run the containers.
   - (currently this just runs the database container)
   - Once it's up and running, it should be accessible at `localhost:3306` for things like mysql workbench.
3. When you're done, you can exit with Ctrl-C and run `docker-compose down -v --remove-orphans --rmi all` to bring the containers down and remove their artifacts (so they build fresh next time).