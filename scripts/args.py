import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "flavor",
        type=str,
        choices=["mocha", "frappe", "macchiato", "latte"],
        help="Flavor of the theme to apply.",
    )

    parser.add_argument(
        "--name",
        "-n",
        type=str,
        default="catppuccin",
        dest="name",
        help="Name of the theme to apply.",
    )

    parser.add_argument(
        "--dest",
        "-d",
        type=str,
        required=True,
        dest="dest",
        help="Destination of the files.",
    )

    parser.add_argument(
        "--accent",
        "-a",
        type=str,
        default="mauve",
        nargs="+",
        dest="accents",
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
        "--all-accents",
        help="Whether to build all accents",
        dest="all_accents",
        action="store_true",
    )

    parser.add_argument(
        "--size",
        "-s",
        type=str,
        default="standard",
        dest="size",
        choices=["standard", "compact"],
        help="Size variant of the theme.",
    )

    parser.add_argument(
        "--tweaks",
        type=str,
        default=[],
        nargs="+",
        dest="tweaks",
        choices=["black", "rimless", "normal", "float"],
        help="Tweaks to apply to the build.",
    )

    parser.add_argument(
        "--zip",
        help="Whether to bundle the theme into a zip",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    parser.add_argument(
        "--patch",
        help="Whether to patch the colloid submodule",
        type=bool,
        default=True,
        action=argparse.BooleanOptionalAction,
    )

    return parser.parse_args()
