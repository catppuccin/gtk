import os, zipfile, argparse, logging, io
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
            "all",
        ],
        help="Accent of the theme.",
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
    release = "v1.0.0-alpha"
    zip_name = f"catppuccin-{ctx.flavor}-{ctx.accent}-standard+default.zip"

    return f"{repo_root}/{release}/{zip_name}"


def install(ctx: InstallContext):
    url = build_release_url(ctx)
    build_info = f"""Installation info:
    flavor:     {ctx.flavor}
    accent:     {ctx.accent}
    dest:       {ctx.dest.absolute()}
    link:       {ctx.link}
    
    remote_url: {url}"""
    logger.info(build_info)
    httprequest = Request(url)

    zip_file = None
    logger.info("Starting download...")
    with urlopen(httprequest) as response:
        logger.info(f"Response status: {response.status}")
        zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
    logger.info("Download finished, zip is valid")

    logger.info("Verifying download..")
    first_bad_file = zip_file.testzip()
    if first_bad_file is not None:
        logger.error(f'Zip appears to be corrupt, first bad file is "{first_bad_file}"')
        return
    logger.info("Download verified")

    logger.info("Extracting...")
    zip_file.extractall(ctx.dest)
    logger.info("Extraction complete")

    if ctx.link:
        dir_name = (ctx.dest / f"catppuccin-{ctx.flavor}-{ctx.accent}-standard+default" / 'gtk-4.0').absolute()
        gtk4_dir = (Path(os.path.expanduser('~')) / '.config' / 'gtk-4.0').absolute()
        os.makedirs(gtk4_dir, exist_ok=True)

        logger.info("Adding symlinks for libadwaita")
        logger.info(f'Root:   {dir_name}')
        logger.info(f'Target: {gtk4_dir}')
        os.symlink(dir_name / 'assets', gtk4_dir / 'assets')
        os.symlink(dir_name / 'gtk.css', gtk4_dir / 'gtk.css')
        os.symlink(dir_name / 'gtk-Dark.css', gtk4_dir / 'gtk-dark.css')


def main():
    args = parse_args()
    dest = Path(os.path.expanduser("~")) / ".local" / "share" / "themes"
    os.makedirs(dest, exist_ok=True)

    if args.dest:
        dest = Path(args.dest)

    ctx = InstallContext(
        flavor=args.flavor, accent=args.accent, dest=dest, link=args.link
    )

    install(ctx)

    logger.info('Theme installation complete!')


try:
    main()
except Exception as e:
    logger.error("Something went wrong when installing the theme:", exc_info=e)
