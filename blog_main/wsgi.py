"""Compatibility wrapper for wsgi.

Delegates to `kiran_kumar_blog.wsgi` to keep any references to
`blog_main.wsgi` functional.
"""

import os

# Ensure the DJANGO settings env points to the new package
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiran_kumar_blog.settings')

from kiran_kumar_blog.wsgi import application  # re-export

