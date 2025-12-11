"""Compatibility wrapper for URLs.

If code imports `blog_main.urls`, re-export the urlpatterns from
`kiran_kumar_blog.urls` so both names work during the transition.
"""

from kiran_kumar_blog.urls import urlpatterns as urlpatterns

