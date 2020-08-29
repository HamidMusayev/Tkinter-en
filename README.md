[<img src="https://github.com/hemidvsmusayev/Tkinter/blob/master/ww_images/logo.png?raw=true" align="center" width="750">](https://docs.python.org/3/library/tkinter.html)
# About -- STILL IN DEVELOP
<a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> is Python's de-facto standard GUI (Graphical User Interface) package.


If you appreciate the content 📖, support projects visibility, give 👍| ⭐| 👏
# Contents
- [Standart attributes](#Standart-attributes)
- [Buttons](#Button)
- [Canvas](#Canvas)
- [Check button](#Check-button)
- [Frames](#Frames)
- [List box](#List-box)
- [Menu](#Menu)
- [Message box](#Message-box)
- [Paned window](#Paned-window)
- [Radio button](#Radio-button)
- [Scrolls](#Scrolls)
- [Text widgets](#Text-widgets)
- [Windows](#Windows)
- [Bonus](#Bonus)

## Standart-attributes
Before we look at the widgets, let's take a look at how some of their common attributes-such as sizes, colors and fonts-are specified.

Each widget has a set of options that affect its appearance and behavior-attributes such as fonts, colors, sizes, text labels, and such.

You can specify options when calling the widget's constructor using keyword arguments such as text='HQ!' or height=24.

After you have created a widget, you can later change any option by using the widget's .config() method. You can retrieve the current setting of any option by using the widget's .cget() method. See Section 26, “Universal widget methods” for more on these methods.

- [Dimensions](#Dimensions)
- [The coordinate system](#The-coordinate-system)
- [Colors](#Colors)
- [Type fonts](#Type-fonts)
- [Anchors](#Anchors)
- [Relief styles](#Relief-styles)
- [Bitmaps](#Bitmaps)
- [Cursors](#Cursors)
- [Images](#Images)
- [Geometry strings](#Geometry-strings)
- [Window names](#Window-names)
- [Cap and join styles](#Cap-and-join-styles)
- [Dash patterns](#Dash-patterns)
- [Matching stipple patterns](#Matching-stipple-patterns)

### Dimensions
Various lengths, widths, and other dimensions of widgets can be described in many different units.

If you set a dimension to an integer, it is assumed to be in pixels.

You can specify units by setting a dimension to a string containing a number followed by:

| Command | Description |
| --- | --- |
| `c` | Centimeters |
| `i` | Inches |
| `m` | Millimeters |
| `p` | Printer's points (about 1/72″) |


### The-coordinate-system
As in most contemporary display systems, the origin of each coordinate system is at its upper left corner, with the x coordinate increasing toward the right, and the y coordinate increasing toward the bottom.
The base unit is the pixel, with the top left pixel having coordinates (0,0). Coordinates that you specify as integers are always expressed in pixels, but any coordinate may be specified as a dimensioned quantity.

### Colors
### Type-fonts
### Anchors
### Relief-styles
### Bitmaps
### Cursors
### Images
### Geometry-strings
### Window-names
### Cap-and-join-styles
### Dash-patterns
### Matching-stipplep-atterns

## Button

## Canvas

## Check-button

## Frames

## List-box

## Menu

## Message-box

## Paned-window

## Radio-button

## Scrolls

## Text-widgets

## Windows

## Bonus
### More references
- <a href="https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html">Tkinter 8.5</a> reference
