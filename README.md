River annotations wraps starsky to generate line level annotation lists for an image that starsky has ingested.
A resolver must be configured in settings.py to produce a projection height and width, canvas URI, image URI (which
the starsky instance in use must have ingested) and a base URI for the generated annotations whcih should include a
{{line_number}} placeholder.

to install dependencies:
pip install -r requirements.txt

