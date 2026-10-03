# Web Mapping starter site

This repository is your Django web site for the semester. Everything you need
(Python, Django, and the GIS libraries) is already installed in your codespace.

## Start the web server
1. Open **Run and Debug** in the left toolbar (or press **F5**).
2. Choose **Django: Web Server** and click the green ▶ button.
3. Your site opens in a new browser tab. Keep that tab open and click the
   browser's **reload** button to see changes after you save a file.

To stop the server, click the red ■ square in the debug toolbar.

## Useful terminal commands
Open a terminal with **Terminal → New Terminal**, then:

| Task | Command |
| --- | --- |
| Create an admin user | `python manage.py createsuperuser` |
| Apply database changes | `python manage.py migrate` |
| Install a new package | add it to `requirements.txt`, then `pip install --user -r requirements.txt` |
| Run the tests | `python manage.py test` |

## Saving your work to GitHub
Open **Source Control** in the left toolbar, type a short message, click
**Commit**, then **Sync Changes**. Do this at the end of every class.

## Save your hours
Codespaces stop automatically after 30 idle minutes, but it is better to stop
yours when you finish: github.com/codespaces → **…** → **Stop codespace**.
