"""Async executor versions of file functions from the os module."""
import asyncio
from functools import partial, wraps
import os


def wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


stat = wrap(os.stat)
rename = wrap(os.rename)
replace = wrap(os.replace)
remove = wrap(os.remove)
mkdir = wrap(os.mkdir)
rmdir = wrap(os.rmdir)

if hasattr(os, "sendfile"):
    sendfile = wrap(os.sendfile)
