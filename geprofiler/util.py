import codecs
import importlib
import json
import os
import shlex
import subprocess
import sys
import warnings
from typing import IO

from geprofiler.vendor.decorator import decorator


def object_with_import_path(import_path):
    if "." not in import_path:
        raise ValueError("Can't import '%s', it is not a valid import path" % import_path)
    module_path, object_name = import_path.rsplit(".", 1)

    module = importlib.import_module(module_path)
    return getattr(module, object_name)


def truncate(string: str, max_length: int):
    if len(string) > max_length:
        return string[0 : max_length - 3] + "..."
    return string


@decorator
def deprecated(func, *args, **kwargs):
    """Marks a function as deprecated."""
    warnings.warn(
        f"{func} is deprecated and should no longer be used.",
        DeprecationWarning,
        stacklevel=3,
    )
    return func(*args, **kwargs)


def deprecated_option(option_name, message=""):
    """Marks an option as deprecated."""

    def caller(func, *args, **kwargs):
        if option_name in kwargs:
            warnings.warn(
                f"{option_name} is deprecated. {message}",
                DeprecationWarning,
                stacklevel=3,
            )

        return func(*args, **kwargs)

    return decorator(caller)


def file_supports_color(file_obj: IO) -> bool:
    """
    Returns True if the running system's terminal supports color.

    Borrowed from Django
    https://github.com/django/django/blob/master/django/core/management/color.py
    """
    plat = sys.platform
    supported_platform = plat != "Pocket PC" and (plat != "win32" or "ANSICON" in os.environ)

    is_a_tty = file_is_a_tty(file_obj)

    return supported_platform and is_a_tty


def file_supports_unicode(file_obj: IO) -> bool:
    encoding = getattr(file_obj, "encoding", None)
    if not encoding:
        return False

    codec_info = codecs.lookup(encoding)

    return "utf" in codec_info.name


def file_is_a_tty(file_obj: IO) -> bool:
    return hasattr(file_obj, "isatty") and file_obj.isatty()


# functions for parsing curl command
def add_header_to_curl(curl, header):
    return f"{curl} -H '{header}'"

async def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))