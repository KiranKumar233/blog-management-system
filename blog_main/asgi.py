"""Compatibility wrapper.

This module keeps the old package name `blog_main` importable while delegating
to the new `kiran_kumar_blog` project package. It exists to avoid breakage
if any external code or tooling still imports `blog_main.asgi`.
"""

import os

# Delegate settings to the new project package
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiran_kumar_blog.settings')

from kiran_kumar_blog.asgi import application  # re-export the ASGI application

