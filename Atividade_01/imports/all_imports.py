from tkinter import (
    Label, Entry, Button, Frame, messagebox, StringVar, 
    OptionMenu, Radiobutton
)

import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle, Polygon
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

from PIL import Image, ImageTk

import sys
import math