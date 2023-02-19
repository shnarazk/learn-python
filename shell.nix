# shell.nix
{ pkgs ? import <nixpkgs> {} }:
let
  my-python-packages = p: with p; [
    pandas
    matplotlib
    numpy
    pillow
    python-lsp-server
    scipy
    scikit-learn
    tkinter
    # other python packages
  ];
  my-python = pkgs.python310.withPackages my-python-packages;
in my-python.env
