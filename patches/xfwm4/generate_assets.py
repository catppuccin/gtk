from typing import List
from catppuccin import PALETTE
from catppuccin.models import Flavor

import re, os, shutil, subprocess, time
from dataclasses import dataclass

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

INDEX = [
    "close-active",
    "close-inactive",
    "close-prelight",
    "close-pressed",
    "hide-active",
    "hide-inactive",
    "hide-prelight",
    "hide-pressed",
    "maximize-active",
    "maximize-inactive",
    "maximize-prelight",
    "maximize-pressed",
    "maximize-toggled-active",
    "maximize-toggled-inactive",
    "maximize-toggled-prelight",
    "maximize-toggled-pressed",
    "menu-active",
    "menu-inactive",
    "menu-prelight",
    "menu-pressed",
    "shade-active",
    "shade-inactive",
    "shade-prelight",
    "shade-pressed",
    "shade-toggled-active",
    "shade-toggled-inactive",
    "shade-toggled-prelight",
    "shade-toggled-pressed",
    "stick-active",
    "stick-inactive",
    "stick-prelight",
    "stick-pressed",
    "stick-toggled-active",
    "stick-toggled-inactive",
    "stick-toggled-prelight",
    "stick-toggled-pressed",
    "title-1-active",
    "title-1-inactive",
    "title-2-active",
    "title-2-inactive",
    "title-3-active",
    "title-3-inactive",
    "title-4-active",
    "title-4-inactive",
    "title-5-active",
    "title-5-inactive",
    "top-left-active",
    "top-left-inactive",
    "top-right-active",
    "top-right-inactive",
    "left-active",
    "left-inactive",
    "right-active",
    "right-inactive",
    "bottom-active",
    "bottom-inactive",
    "bottom-left-active",
    "bottom-left-inactive",
    "bottom-right-active",
    "bottom-right-inactive",
]


def subst_text(path, _from, to):
    with open(path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(re.sub(_from, to, content))


def generate_for_flavor(flavor: Flavor):
    # Setup the palette
    palette = flavor.colors

    close_color=f'#{palette.red.hex}'
    max_color=f'#{palette.green.hex}'
    min_color=f'#{palette.yellow.hex}'

    # We expand the source assets into the 4 flavors, but need to map between
    # Their definition of dark and ours. This means that latte will get the -light assets
    # and the rest get the -dark assets to work from
    color = "-dark"
    if not flavor.dark:
        color = "-light"

    # Make a directory for our patched SVGs to live in before compilation
    odir = f"{THIS_DIR}/patched"
    os.makedirs(odir, exist_ok=True)

    # Copy the base assets into the output
    shutil.copy(
        f"{THIS_DIR}/assets{color}.svg",
        f"{odir}/assets-catppuccin-{flavor.identifier}.svg",
    )
    shutil.copy(
        f"{THIS_DIR}/assets{color}-normal.svg",
        f"{odir}/assets-catppuccin-{flavor.identifier}-normal.svg",
    )

    # Patch all the SVGs
    path = f"{odir}/assets-catppuccin-{flavor.identifier}-normal.svg"
    subst_text(path, "#fd5f51", close_color)
    subst_text(path, "#38c76a", max_color)
    subst_text(path, "#fdbe04", min_color)

    headerbar = palette.base.hex
    headerbar_backdrop = palette.mantle.hex

    if flavor.dark:
        path = f"{odir}/assets-catppuccin-{flavor.identifier}.svg"
        subst_text(path, "#242424", headerbar)
        subst_text(path, "#2c2c2c", headerbar_backdrop)

        path = f"{odir}/assets-catppuccin-{flavor.identifier}-normal.svg"
        subst_text(path, "#242424", headerbar)
        subst_text(path, "#2c2c2c", headerbar_backdrop)
    else:
        path = f"{odir}/assets-catppuccin-{flavor.identifier}.svg"
        subst_text(path, "#f2f2f2", headerbar)
        subst_text(path, "#fafafa", headerbar_backdrop)

        path = f"{odir}/assets-catppuccin-{flavor.identifier}-normal.svg"
        subst_text(path, "#f2f2f2", headerbar)
        subst_text(path, "#fafafa", headerbar_backdrop)


@dataclass
class WorkerInput:
    output_path: str
    output_dir: str
    input_path: str
    dpi: str
    ident: str


def call_subprocesses(inp: WorkerInput):
    inkscape = "inkscape"
    optipng = "optipng"

    return [
        subprocess.Popen(
            [
                inkscape,
                "--export-id",
                inp.ident,
                "--export-id-only",
                "--export-dpi",
                inp.dpi,
                "--export-filename",
                inp.output_path,
                inp.input_path,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        ),
        subprocess.Popen(
            [optipng, "-o7", "--quiet", inp.output_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        ),
    ]


@dataclass
class RenderState:
    tasks: List[subprocess.Popen]
    input_root: str
    output_root: str


screen_to_dpi = {
    "-hdpi": "144",
    "-xhdpi": "192",
}

def render_for_screen(state: RenderState, flavor: Flavor, screen: str, ident: str):
    # NOTE: We do not generate for the -normal variant currently, that would just be 
    #       a stupid amount of compute and time for little benefit
    src_file = f"{state.input_root}/assets-catppuccin-{flavor.identifier}.svg"

    output_dir = f"{state.output_root}/assets-catppuccin-{flavor.identifier}{screen}"
    output_path = f"{output_dir}/{ident}.png"

    dpi = screen_to_dpi.get(screen, "96")

    os.makedirs(output_dir, exist_ok=True)

    if os.path.exists(output_path):
        print(f"Skipping '{output_path}', already generated")
    else:
        new_tasks = call_subprocesses(
            WorkerInput(
                output_path=output_path,
                output_dir=output_dir,
                input_path=src_file,
                dpi=dpi,
                ident=ident,
            )
        )
        state.tasks.extend(new_tasks)


def render_for_flavor(flavor: Flavor, state: RenderState):
    print(
        f"Starting render tasks for {flavor.identifier}"
    )
    for ident in INDEX:
        render_for_screen(state=state, flavor=flavor, screen="", ident=ident)
        render_for_screen(state=state, flavor=flavor, screen="-hdpi", ident=ident)
        render_for_screen(state=state, flavor=flavor, screen="-xhdpi", ident=ident)


generate_for_flavor(PALETTE.mocha)
generate_for_flavor(PALETTE.latte)
generate_for_flavor(PALETTE.macchiato)
generate_for_flavor(PALETTE.frappe)

state = RenderState(
    tasks=[], input_root=f"{THIS_DIR}/patched", output_root=f"{THIS_DIR}/generated"
)
start_time = time.time()

render_for_flavor(PALETTE.mocha, state)
render_for_flavor(PALETTE.latte, state)
render_for_flavor(PALETTE.macchiato, state)
render_for_flavor(PALETTE.frappe, state)

for task in state.tasks:
    task.wait()

end_time = time.time() - start_time
print(f"Generation complete in {end_time} seconds")
shutil.rmtree(state.input_root)
