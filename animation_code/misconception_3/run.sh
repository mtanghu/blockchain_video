docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim manim main.py MisconceptionScene3 -qm