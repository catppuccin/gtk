#!/usr/bin/env python3

import os
import zipfile
import argparse
import logging
import io

from typing import Optional
from pathlib import Path
from dataclasses import dataclass
from urllib.request import urlopen, Request

logger = logging.getLogger("catppuccin-gtk")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("[%(name)s] [%(levelname)s] - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


@dataclass
class InstallContext:
    flavor: str
    accent: str
    dest: Path
    link: bool

    def build_info(self, include_url=True) -> str:
        url = build_release_url(self)
        info = f"""Installation info:
        flavor:     {self.flavor}
        accent:     {self.accent}
        dest:       {self.dest.absolute()}
        link:       {self.link}"""
        if include_url:
            info += f"\nremote_url: {url}"
        return info


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "flavor",
        type=str,
        choices=["mocha", "frappe", "macchiato", "latte"],
        help="Flavor of the theme to apply.",
    )

    parser.add_argument(
        "accent",
        type=str,
        default="mauve",
        choices=[
            "rosewater",
            "flamingo",
            "pink",
            "mauve",
            "red",
            "maroon",
            "peach",
            "yellow",
            "green",
            "teal",
            "sky",
            "sapphire",
            "blue",
            "lavender",
        ],
        help="Accent of the theme.",
    )

    parser.add_argument(
        "--from-artifact",
        type=Path,
        dest="from_artifact",
        help="Install from an artifact instead of a mainline release, pass the artifact path (e.g 7bff2448a81e36bf3b0e03bfbd649bebe6973ec7-artifacts.zip)",
    )

    parser.add_argument(
        "--dest",
        "-d",
        type=str,
        dest="dest",
        help="Destination of the files.",
    )

    parser.add_argument(
        "--link",
        help="Whether to add symlinks for libadwaita",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    return parser.parse_args()


def build_release_url(ctx: InstallContext) -> str:
    repo_root = "https://github.com/catppuccin/gtk/releases/download"
    release = "v1.0.4" # x-release-please-version
    zip_name = f"catppuccin-{ctx.flavor}-{ctx.accent}-standard+default.zip"

    return f"{repo_root}/{release}/{zip_name}"


def fetch_zip(url: str) -> Optional[zipfile.ZipFile]:
    req = Request(url)

    zip_file = None
    logger.info("Starting download...")
    with urlopen(req) as response:
        logger.info(f"Response status: {response.status}")
        zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
    logger.info("Download finished, zip is valid")

    logger.info("Verifying download..")
    first_bad_file = zip_file.testzip()
    if first_bad_file is not None:
        logger.error(f'Zip appears to be corrupt, first bad file is "{first_bad_file}"')
        return None
    logger.info("Download verified")
    return zip_file


def add_libadwaita_links(ctx: InstallContext, rewrite: bool = False):
    suffix = "light"
    if ctx.flavor != "latte":
        suffix = "dark"
    dir_name = (
        ctx.dest / f"catppuccin-{ctx.flavor}-{ctx.accent}-standard+default-{suffix}" / "gtk-4.0"
    ).absolute()
    gtk4_dir = (Path(os.path.expanduser("~")) / ".config" / "gtk-4.0").absolute()
    os.makedirs(gtk4_dir, exist_ok=True)

    logger.info("Adding symlinks for libadwaita")
    logger.info(f"Root:   {dir_name}")
    logger.info(f"Target: {gtk4_dir}")
    try:
        if rewrite:
            os.remove(gtk4_dir / "assets")
            os.remove(gtk4_dir / "gtk.css")
            os.remove(gtk4_dir / "gtk-dark.css")
    except FileNotFoundError:
        logger.debug("Ignoring FileNotFound in symlink rewrite")

    os.symlink(dir_name / "assets", gtk4_dir / "assets")
    os.symlink(dir_name / "gtk.css", gtk4_dir / "gtk.css")
    os.symlink(dir_name / "gtk-dark.css", gtk4_dir / "gtk-dark.css")


def install(ctx: InstallContext):
    url = build_release_url(ctx)
    logger.info(ctx.build_info())

    zip_file = fetch_zip(url)
    if zip_file is None:
        return

    logger.info("Extracting...")
    zip_file.extractall(ctx.dest)
    logger.info("Extraction complete")

    if ctx.link:
        add_libadwaita_links(ctx)


def install_from_artifact(ctx: InstallContext, artifact_path: Path):
    # Working from a pull request, special case it
    logger.info(f"Extracting artifact from '{artifact_path}'")
    artifacts = zipfile.ZipFile(artifact_path)

    logger.info("Verifying artifact...")
    first_bad_file = artifacts.testzip()
    if first_bad_file is not None:
        logger.error(f'Zip appears to be corrupt, first bad file is "{first_bad_file}"')
        return None
    logger.info("Artifact verified")

    logger.info(ctx.build_info(False))

    # The zip, inside the artifacts, that we want to pull out
    zip_name = f"catppuccin-{ctx.flavor}-{ctx.accent}-standard+default.zip"
    logger.info(f"Pulling '{zip_name}' from the artifacts")
    info = artifacts.getinfo(zip_name)

    logger.info("Extracting the artifact...")
    artifact = zipfile.ZipFile(io.BytesIO(artifacts.read(info)))
    artifact.extractall(ctx.dest)
    logger.info("Extraction complete")

    if ctx.link:
        logger.info("Adding links (with rewrite)")
        add_libadwaita_links(ctx, True)
        logger.info("Links added")


def main():
    args = parse_args()

    dest = Path(os.path.expanduser("~")) / ".local" / "share" / "themes"
    os.makedirs(dest, exist_ok=True)

    if args.dest:
        dest = Path(args.dest)

    ctx = InstallContext(
        flavor=args.flavor, accent=args.accent, dest=dest, link=args.link
    )

    if args.from_artifact:
        install_from_artifact(ctx, args.from_artifact)
        return

    install(ctx)
    logger.info("Theme installation complete!")


try:
    main()
except Exception as e:
    logger.error("Something went wrong when installing the theme:", exc_info=e)
