from dataclasses import dataclass
from typing import Any, Literal, List
from catppuccin.models import Flavor, Color
from .utils import find_and_replace, Subsitution


@dataclass
class Tweaks:
    tweaks: List[str]

    def has(self, tweak: str) -> bool:
        return tweak in self.tweaks

    def id(self) -> str:
        return ",".join(self.tweaks)


@dataclass
class Suffix:
    true_value: str
    test: Any
    false_value: str = ""


@dataclass
class BuildContext:
    # The src dir of the Colloid copy to operate on
    colloid_src_dir: str

    # The root of the project
    git_root: str

    # The root of the output dir (as specified by --dest if given)
    output_root: str

    output_format: Literal["zip"] | Literal["dir"]

    theme_name: str
    flavor: Flavor
    accent: Color
    size: Literal["standard"] | Literal["compact"]
    tweaks: Tweaks

    def output_dir(self) -> str:
        return f"{self.output_root}/{self.build_id()}"

    def build_id(self) -> str:
        return f"{self.theme_name}-{self.flavor.identifier}-{self.accent.identifier}-{self.size}+{self.tweaks.id() or 'default'}"

    def apply_suffix(self, suffix: Suffix) -> str:
        if suffix.test(self):
            return suffix.true_value
        else:
            return suffix.false_value

    def apply_tweak(self, key, default, value):
        find_and_replace(
            f"{self.colloid_src_dir}/sass/_tweaks-temp.scss",
            Subsitution(find=f"\\${key}: {default}", replace=f"${key}: {value}"),
        )

IS_DARK = Suffix(true_value="-Dark", test=lambda ctx: ctx.flavor.dark)
IS_LIGHT = Suffix(true_value="-Light", test=lambda ctx: not ctx.flavor.dark)
IS_WINDOW_NORMAL = Suffix(
    true_value="-Normal", test=lambda ctx: ctx.tweaks.has("normal")
)
DARK_LIGHT = Suffix(
    true_value="-Dark", false_value="-Light", test=lambda ctx: ctx.flavor.dark
)
