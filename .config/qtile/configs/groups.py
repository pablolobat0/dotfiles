from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .keys import mod, keys


# Groups icons: nf-cod-globe, nf-dev-terminal, nf-md-docker, nf-fa-folder, nf-fa-youtube

groups = [Group(i) for i in ["󰖟 ", " ", "󰡨 ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        ]
    )
