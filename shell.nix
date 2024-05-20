{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  name = "dev-shell";
  buildInputs = with pkgs; [
    python311
    python311Packages.catppuccin
    sassc
    inkscape
    optipng
  ];
}
