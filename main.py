#!python3

# /// pyproject
# [project]
# name = "name"
# version = "version"
# description = "description"
# readme = {file = "README.txt", content-type = "text/markdown"}
# requires-python = ">=3.11"
#
# dependencies = [
#    "importlib_metadata",
#    "pygments",
#    "typing-extensions",
#    "markdown-it-py",
#    "mdurl",
#    "zipp",
#    "linkify-it-py",
#    "mdit-py-plugins",
#    "uc-micro-py",
#    "rich",
#    "textual",
# ]
# ///


if 0:
    import pygbag.aio as asyncio
else:
    import asyncio

import sys

import argparse

import textual

from noteri import Noteri


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default="./", nargs="?", help="Path to file or directory to open")
    args = parser.parse_args()

    app = Noteri(args.path)

    loop = asyncio.get_event_loop()
    try:
        if sys.platform in ("emscripten", "wasi"):
            print(" ===================================== ")

            async with app.run_test(headless=True, size=(100, 32)) as pilot:
                while not loop.is_closed():
                    await asyncio.sleep(0.016)
        else:
            await app.run_async()

    except asyncio.exceptions.CancelledError:
        print("Cancelled")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        pass
    print("ended")


asyncio.run(main())
