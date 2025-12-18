# DataBloom/__init__.py

from .plots import styled_line
from .plots import styled_bar
from .plots import styled_scatter
from .plots import styled_bubble
from .plots import styled_stacked

# (Optionnel) Définit ce qui est importé si quelqu'un fait "from maviz import *"
__all__ = [
    "styled_line",
    "styled_bar",
    "styled_scatter",
    "styled_bubble",
    "styled_stacked",
]