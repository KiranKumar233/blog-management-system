"""Compatibility settings shim.

If any code still imports `blog_main.settings`, re-export the values from
the new `kiran_kumar_blog.settings` module so both names work during the
transition.
"""

from kiran_kumar_blog.settings import *  # noqa: F401,F403
