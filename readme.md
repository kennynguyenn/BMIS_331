To run this scraper and convert it into usable data, follow the step below
1. require a key from scrapfly.io
2. setting up the environment
3. export SCRAPFLY_KEY=”scp-live-67e353be49f84d99950b68d8ae04782d” (that is mine api key)
4. export PATH="/Users/kenny/.local/bin:$PATH" (im using poetry instead of pip so this is to set path for poetry)
6. cd *file location*
7. poetry shell
8. poetry install --with dev (first time install necessary files)
9. python run.py

