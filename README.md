[<img src="https://github.com/hemidvsmusayev/Tkinter/blob/master/ww_images/logo.png?raw=true" align="center" width="750">](https://docs.python.org/3/library/tkinter.html)
# About //still in develop
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> is Python's de-facto standard GUI (Graphical User Interface) package.


> If you appreciate the content 📖, support projects visibility, give 👍| ⭐| 👏
# Contents
> Introduction
- [Standard attributes](#Standard-attributes)
- [About ttk Themed widgets](#About-ttk-Themed-widgets)
- [Importing tkinter and ttk](#Importing-tkinter-and-ttk)
- [All tkk widgets list](#All-tkk-widgets-list)
> tkk Widgets set
- [tkk.Button](#Button)
- [tkk.Check button](#Check-button)
- [tkk.Combo box](#Combo-box)
- [tkk.Entry](#Entry)
- [tkk.Frame](#Frame)
- [tkk.Label](#Label)
- [tkk.Label frame](#Label-frame)
- [tkk.Menu button](#Menu-button)
- [tkk.Notebook](#Notebook)
- [tkk.Paned window](#Paned-window)
- [tkk.Progressbar](#Progressbar)
- [tkk.Radio button](#Radio-button)
- [tkk.Scale](#Scale)
- [tkk.Scrollbar](#Scrollbar)
- [tkk.Separator](#Separator)
- [tkk.Sizegrip](#Sizegrip)
- [tkk.Tree view](#Tree-view)
- [Styling tkk widgets](#Styling-tkk-widgets)
- [Methods common to all tkk widgets](#Methods-common-to-all-tkk-widgets)
> other tkinter widgets
- [Canvas](#Canvas)
- [List box](#List-box)
- [Menu](#Menu)
- [Message box](#Message-box)
- [Text widgets](#Text-widgets)
- [Windows](#Windows)
- [Bonus](#Bonus)

## Standard-attributes

Before we look at the widgets, let's take a look at how some of their common attributes-such as sizes, colors and fonts-are specified.

Each widget has a set of options that affect its appearance and behavior-attributes such as `font`, `color`, `size`, `text`, `label`, and such.

You can specify options when calling the widget's constructor using keyword arguments such as 

`Button(window, text='Ok', fg='Blue')`.

After you have created a widget, you can later change any option by using the widget's `.config()` method.

You can retrieve the current setting of any option by using the widget's `.cget()` method.

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

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/coordinate.PNG?raw=true">

### Colors

[Color chooser example](https://github.com/hemidvs/Tkinter/blob/master/Color%20chooser/color_chooser.py)

There are two general ways to specify colors in Tkinter.

- You can use a string specifying the proportion of red, green, and blue in hexadecimal digits:

| Command | Description |
| --- | --- |
| `#rgb` | Four bits per color |
| `#rrggbb` | Eight bits per color |
| `#rrrgggbbb` | Twelve bits per color |

For example, '#fff' is white, '#000000' is black, '#000fff000' is pure green, and '#00ffff' is pure cyan (green plus blue).

- You can also use any locally defined standard color name. The colors 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta' will always be available. Other names may work, depending on your local installation.

You can browse colors [here](https://www.google.com/search?q=color+picker) or Google Material design colors [here](https://material.io/resources/color/#!/?view.left=0&view.right=0).


### Type-fonts

You can browse all fonts [here](https://fonts.google.com).

[Fonts Example](https://github.com/hemidvs/Tkinter/blob/master/Type%20fonts/type_fonts.py)

Depending on your platform, there may be up to three ways to specify type style.

- As a tuple whose first element is the font family, followed by a size (in points if positive, in pixels if negative), optionally followed by a string containing one or more of the style modifiers bold, italic, underline, and overstrike.

  Examples: ('Helvetica', '16') for a 16-point Helvetica regular; ('Times', '24', 'bold italic') for a 24-point Times bold italic. For a 20-pixel Times bold font, use ('Times', -20, 'bold').
  
- You can create a “font object” by importing the tkFont module and using its Font class constructor:
  
  `import tkFont`
  
  `font = tkFont.Font(option, ...)`
  
   where the options include:
  
| Command | Description |
| --- | --- |
| `family` | The font family name as a string. |
| `size` | The font height as an integer in points. To get a font n pixels high, use -n. |
| `weight` | 'bold' for boldface, 'normal' for regular weight. |
| `slant` | 'italic' for italic, 'roman' for unslanted. |
| `underline` | 1 for underlined text, 0 for normal. |
| `overstrike` | 1 for overstruck text, 0 for normal. |

   For example, to get a 36-point bold Helvetica italic face:
   
   `helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')`
    
To get a list of all the families of fonts available on your platform, call this function:
  
  `tkFont.families()`
  
The return value is a list of strings. Note: You must create your root window before calling this function.

These methods are defined on all `Font` objects:

`.actual(option=None)`

If you pass no arguments, you get back a dictionary of the font's actual attributes, which may differ from the ones you requested. To get back the value of an attribute, pass its name as an argument.

`.cget(option)`

Returns the value of the given option.

`.configure(option, ...)`

Use this method to change one or more options on a font. For example, if you have a Font object called titleFont, if you call titleFont.configure(family='times', size=18), that font will change to 18pt Times and any widgets that use that font will change too.

`.copy()`

Returns a copy of a Font object.

`.measure(text)`

Pass this method a string, and it will return the number of pixels of width that string will take in the font. Warning: some slanted characters may extend outside this area.

`.metrics(option)`

If you call this method with no arguments, it returns a dictionary of all the font metrics. You can retrieve the value of just one metric by passing its name as an argument. Metrics include:

| Command | Description |
| --- | --- |
| `ascent` | Number of pixels of height between the baseline and the top of the highest ascender. |
| `descent` | Number of pixels of height between the baseline and the bottom of the lowest ascender. |
| `fixed` | This value is 0 for a variable-width font and 1 for a monospaced font. |
| `linespace` | Number of pixels of height total. This is the leading of type set solid in the given font. |

### Anchors

The Tkinter module defines a number of anchor constants that you can use to control where items are positioned relative to their context. For example, anchors can specify where a widget is located inside a frame when the frame is bigger than the widget.

These constants are given as compass points, where north is up and west is to the left.

The anchor constants are shown in this diagram:

<img src="https://github.com/hemidvs/Tkinter/blob/master/ww_images/anchors.png" align="center" width="150">

For example, if you create a small widget inside a large frame and use the `anchor=tk.SE` option, the widget will be placed in the bottom right corner of the frame. If you used `anchor=tk.N` instead, the widget would be centered along the top edge.

Anchors are also used to define where text is positioned relative to a reference point. For example, if you use `tk.CENTER` as a text anchor, the text will be centered horizontally and vertically around the reference point. Anchor `tk.NW` will position the text so that the reference point coincides with the northwest (top left) corner of the box containing the text. Anchor `tk.W` will center the text vertically around the reference point, with the left edge of the text box passing through that point, and so on.

### Relief-styles

The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget. Here is a screen shot of a row of buttons exhibiting all the possible relief styles:

<img src="https://github.com/hemidvs/Tkinter/blob/master/ww_images/relief.png?raw=true" align="center" width="400">

### Bitmaps

For bitmap options in widgets, these bitmaps are guaranteed to be available:

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/bitmap.PNG?raw=true" width="400">

The graphic above shows Button widgets bearing the standard bitmaps. From left to right, they are
`'error'`, `'gray75'`, `'gray50'`, `'gray25'`, `'gray12'`, `'hourglass'`, `'info'`, `'questhead'`,
`'question'`, and `'warning'`.
You can use your own bitmaps. Any file in .xbm (X bit map) format will work. In place of a standard
bitmap name, use the string '@' followed by the pathname of the .xbm file.

### Cursors

There are quite a number of different mouse cursors available. Their names and graphics are shown here. The exact graphic may vary according to your operating system.

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/cursor.PNG?raw=true" width="400">
<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/cursors.PNG?raw=true" width="400">

### Images

There are three general methods for displaying graphic images in your Tkinter application.

- To display bitmap (two-color) images in the `.xbm` format, refer to The BitmapImage class.

- To display full-color images in the `.gif`, `.pgm`, or .ppm format, refer to The PhotoImage class.

- The Python Imaging Library (PIL) supports images in a much wider variety of formats. Its ImageTk class is specifically designed for displaying images within Tkinter applications.

- **The-BitmapImage-class**

To display a two-color image in the .xbm format, you will need this constructor:

`tk.BitmapImage(file=f[, background=b][, foreground=c])`

where f is the name of the .xbm image file.

Normally, foreground (1) bits in the image will be displayed as black pixels, and background (0) bits in the image will be transparent. To change this behavior, use the optional `background=b` option to
set the background to color b, and the optional `foreground=c` option to set the foreground to color c. For color specification, see Section [Colors](#Colors).

This constructor returns a value that can be used anywhere Tkinter expects an image. For example, to display an image as a label, use a [tkk.Label widget](#Label) and supply the `BitmapImage` object as the value of the `image` option:

`logo = tk.BitmapImage('logo.xbm', foreground='red')
Label(image=logo).grid()`

- **The-PhotoImage-class**

To display a color image in `.gif`, `.pgm`, or `.ppm` format, you will need this constructor:

`tk.PhotoImage(file=f)`

where f is the name of the image file. The constructor returns a value that can be used anywhere Tkinter
expects an image.

### Geometry-strings

A geometry string is a standard way of describing the size and location of a top-level window on a desktop.

A geometry string has this general form: 

`'wxh±x±y'`

where:

- The w and h parts give the window width and height in pixels. They are separated by the character 'x'.

- If the next part has the form +x, it specifies that the left side of the window should be x pixels from the left side of the desktop. If it has the form -x, the right side of the window is x pixels from the right side of the desktop.

- If the next part has the form +y, it specifies that the top of the window should be y pixels below the top of the desktop. If it has the form -y, the bottom of the window will be y pixels above the bottom edge of the desktop.

For example, a window created with `geometry='120x50-0+20'` would be 120 pixels wide by 50 pixels high, and its top right corner will be along the right edge of the desktop and 20 pixels below the top edge.

### Window-names

The term window describes a rectangular area on the desktop.

- A top-level or root window is a window that has an independent existence under the window manager. It is decorated with the window manager's decorations, and can be moved and resized independently. Your application can use any number of top-level windows.

- The term `“window”` also applies to any widget that is part of a top-level window. Tkinter names all these windows using a hierarchical window path name.

- The root window's name is '.'.

- Child windows have names of the form `'.n'`, where n is some integer in string form. For example, a window named `'.135932060'` is a child of the root window `('.')`.

- Child windows within child windows have names of the form `'p.n'` where `p` is the name of the parent window and `n` is some integer. For example, a window named `'.135932060.137304468'` has parent window `'.135932060'`, so it is a grandchild of the root window.

- The relative name of a window is the part past the last '.' in the path name. To continue the previous example, the grandchild window has a relative name '137304468'.

To get the path name for a widget w, use `str(w)`.

See also Section [Methods common to all tkk widgets](#Methods-common-to-all-tkk-widgets) for methods you can use to operate on window names, especially the .winfo_name, .winfo_parent, and .winfo_pathname methods.

### Cap-and-join-styles

For pleasant and effective rendering of diagrams, sometimes it is a good idea to pay attention to cap and join styles.

1. The cap style of a line is the shape of the end of the line. Styles are:
- `tk.BUTT:` The end of the line is cut off square at a line that passes through the endpoint.
- `tk.PROJECTING:` The end of the line is cut off square, but the cut line projects past the endpoint a distance equal to half the line's width.
- `tk.ROUND:` The end describes a semicircle centered on the endpoint.

2. The join style describes the shape where two line segments meet at an angle.
- `tk.ROUND:` The join is a circle centered on the point where the adjacent line segments meet.
- `tk.BEVEL:` A flat facet is drawn at an angle intermediate between the angles of the adjacent lines.
- `tk.MITER:` The edges of the adjacent line segments are continued to meet at a sharp point.

This illustration shows how Tkinter's cap and join options work with a line made of two connected line segments. Small red circles show the location of the points that define this line.

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/capjoin.PNG?raw=true" width="400">

### Dash-patterns

A number of widgets allow you to specify a dashed outline. The dash and dash offset options give you fine control over the exact pattern of the dashes.

`dash`

This option is specified as a tuple of integers. The first integer specifies how many pixels should be drawn. The second integer specifies how many pixels should be skipped before starting to draw again, and so on. When all the integers in the tuple are exhausted, they are reused in the same order until the border is complete.

For example, `dash=(3,5)` produces alternating 3-pixel dashes separated by 5-pixel gaps. A value of `dash=(7,1,1,1)` produces a dash-and-dot pattern, with the dash seven times as long as the dot or the gaps around the dot. A value of `dash=(5,)` produces alternating five-pixel dashes and five-pixel gaps.

`dashoff`

To start the dash pattern in a different point of cycle instead of at the beginning, use an option of `dashoff=n`, where `n` is the number of pixels to skip at the beginning of the pattern.

For example, for options `dash=(5, 1, 2, 1)` and `dashoff=3`, the first pattern produced will be: 2 on, 1 off, 2 on, and 1 off. Subsequent patterns will be 5 on, 1 off, 2 on, and 1 off. Here is a screen shot of a line drawn with this combination of options:

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/dash.PNG?raw=true" width="300">

### Matching-stipple-patterns

This may seem like an incredibly picky style point, but if you draw a graphic that has two objects with stippled patterns, a real professional will make sure that the patterns align along their boundary.

Here is an example. The left-hand screen shot shows two adjacent `100×100` squares stippled with the `“gray12”` pattern, but the right-hand square is offset vertically by one pixel. The short black line in the center of the figure is drawn along the boundary of the two figures.

<img src="https://github.com/hemidvs/Tkinter-en/blob/master/ww_images/stripplepatterns.PNG?raw=true" width="400">

## About-ttk-Themed-widgets

Starting with Tk 8.5, the ttk module became available. This module replaces much (but not all) of the original Tkinter machinery. Use this module to gain these advantages:

- **Platform-specific appearance.** In releases before Tk 8.5, one of the commonest complaints about Tk applications was that they did not conform to the style of the various platforms.

The ttk module allows you to write your application in a generic way, yet your application can look like a Windows application under Windows, like a MacOS app under MacOS, and so on, without any change to your program.

Each possible different appearance is represented by a named `ttk theme`. For example, the `classic` theme gives you the appearance of the original Tkinter widgets described in the previous sections.

- **Simplification and generalization of state-specific widget behavior.** In the basic Tkinter world, there are a lot of widget options that specify how the widget should look or behave depending on various conditions.

For example, the `tk.Button` widget has several different options that control the foreground `(text)` color.

- The `activeforeground` color option applies when the cursor is over the button.
- The `disabledforeground` color is used when the widget is disabled.
- The widget will have the `foreground` color when the other conditions don't apply.

The ttk module collapses a lot of these special cases into a simple two-part system:

- Every widget has a number of different states, and each state can be turned on or off independently of the others. Examples of states are: disabled, active, and focus.

- You can set up a style map that specifies that certain options will be set to certain values depending on some state or some combination of the widget's states.

To use ttk, you will need to know these things.

[Importing tkinter and ttk](#Importing-tkinter-and-ttk): Setting up your program to use ttk.

[All tkk widgets list](#All-tkk-widgets-list): The new and replaced ttk widgets.

[Styling-tkk-widgets](#Styling-tkk-widgets)

## Importing-tkinter-and-ttk

There are different ways to import the ttk module.

- If you prefer that all the widgets and other features of Tkinter and ttk be in your global namespace, use this form of import:

```
from Tkinter import *
from ttk import *
```

It is important to do these two imports in this order, so that all the widget types from ttk replace the equivalent widgets from Tkinter. For example, all your `Button` widgets will come from ttk and not Tkinter.

-  In more complex applications, where you are using more than one imported module, it can greatly improve the readability of your code if you practice safe namespace hygiene: import all your modules using the `import module name` syntax. This requires just a bit more typing, but it has the great advantage that you can look at a reference to something and tell where it came from.

We recommend this form of import:
```
import ttk
```

So after this import, `ttk.Label` is the `Label` widget constructor, `ttk.Button` is a `Button`, and so on.

If you need to refer to items from the Tkinter module, it is available as `ttk.Tkinter`. For example, the anchor code for `northeast` is `ttk.Tkinter.NE`.

You may instead import Tkinter separately in this way:

```
import Tkinter as tk
```

After this form of import, the code for `northeast` is `tk.NE`.

## All-tkk-widgets-list

The ttk module contains different versions of most of the standard Tkinter widgets and a few new ones. 

> These widgets replace the ones from Tkinter of the same name:
- ttk.Button [Read](#Button).
- ttk.Checkbutton” [Read](#Check-button).
- ttk.Entry” [Read](#Entry).
- ttk.Frame” [Read](#Frame).
- ttk.Label” [Read](#Label).
- ttk.LabelFrame” [Read](#Label-frame).
- ttk.Menubutton” [Read](#Menu-button).
- ttk.PanedWindow” [Read](#Paned-window).
- ttk.Radiobutton” [Read](#Radio-button).
- ttk.Scale” [Read](#Scale).
- ttk.Scrollbar” [Read](#Scrollbar).
> These widgets are new, and specific to ttk:
- ttk.Combobox” [Read](#Combo-box).
- ttk.Notebook” [Read](#Notebook).
- ttk.Progressbar” [Read](#Progressbar).
- ttk.Separator” [Read](#Separator).
- ttk.Sizegrip” [Read](#Sizegrip).
- ttk.Tree view” [Read](#Tree-view).

## Button

To create a `ttk.Button` widget:

```
w = ttk.Button(parent, option=value, ...)
```

Here are the options for the ttk.Button widget.

| Command | Description |
| --- | --- |
| `class_` | The widget class name. This may be specified when the widget is created, but cannot be changed later. |
| `command` | A function to be called when the button is pressed |
| `compound` | If you provide both `image` and `text` options, the compound option specifies the position of the image relative to the text. The value may be `tk.TOP` (image above text), `tk.BOTTOM` (image below text), `tk.LEFT` (image to the left of the text), or `tk.RIGHT` (image to the right of the text). When you provide both image and text options but don't specify a compound option, the image will appear and the text will not. |
| `cursor` | The cursor that will appear when the mouse is over the button; go to [Cursors](#Cursors) |
| `image` | An image to appear on the button; go to [Images](#Images) |
| `style` | The style to be used in rendering this button; go to [Styling tkk widgets](#Styling-tkk-widgets) |
| `takefocus` | By default, a `ttk.Button` will be included in focus traversal. To remove the widget from focus traversal, use `takefocus=False`; go to [Focus: routing keyboard input](#coming soon) |
| `text` | The text to appear on the button, as a string. |
| `textvariable` | A variable that controls the text that appears on the button; go to [Control variables: the values behind the widgets](#coming soon) |
| `underline` | If this option has a non negative value n, an underline will appear under the character at position n. |
| `width` | If the label is text, this option specifies the absolute width of the text area on the button, as a number of characters; the actual width is that number multiplied by the average width of a character in the current font. For image labels, this option is ignored. The option may also be configured in a style |

These options of the Tkinter `Button` widget are not supported by the `ttk.Button` constructor:

**Tkinter Button options not in ttk.Button**

| Command | Description |
| --- | --- |
| `activebackground` | Use a style map to control the `background` option; go to, [ttk style maps: dynamic appearance changes](#coming soon ttk element layer) |
| `activeforeground` | Use a style map to control the `foreground` option. |
| `anchor` | Configure this option using a style; go to [Styling tkk widgets](#Styling-tkk-widgets) Use this option to specify the position of the text when the `width` option allocates extra horizontal space. For example, if you specify options `width=20` and `compound=tk.RIGHT` on a button that displays both text and and image, and a style that specifies `anchor=tk.E (east)`, the image will be at the right-hand end of the twenty character space, with the text just to its left. When the button displays an image but no text, this option is ignored. |
| `background or bg` | Configure the background option using a style. The bg abbreviation is not supported. |
| `bitmap` | Not supported. |
| `borderwidth or bd` | Configure the `borderwidth` option using a style. The `bd` abbreviation is not supported. |
| `cursor` | The cursor that will appear when the mouse is over the checkbutton. |
| `default` | Not supported. |
| `disabledforeground` | Use a style map for the `foreground` option. |
| `font` | Configure this option using a style. |
| `foreground or fg` | Configure this option using a style. |
| `height` | Not supported. |
| `highlightbackground` | To control the color of the focus highlight when the button does not have focus, use a style map to control the `highlightcolor` option. |
| `highlightcolor` | You may specify the default focus highlight color by setting this option in a style. You may also control the focus highlight color using a style map. |
| `highlightthickness` | Configure this option using a style. This option may not work in all themes. |
| `justify` | If the text contains newline `('\n')` characters, the text will occupy multiple lines on the button. The `justify` option controls how each line is positioned horizontally. Configure this option using a style; values may be `tk.LEFT`, `tk.CENTER`, or `tk.RIGHT` for lines that are left-aligned, centered, or right aligned, respectively. |
| `overrelief` | Use a style map to control the relief option. |
| `padx` | Not supported. |
| `pady` | Not supported. |
| `relief` | Configure this option using a style. |
| `repeatdelay` | Not supported. |
| `repeatinterval` | Not supported. |
| `state` | In ttk, there is no option with this name. The state mechanism has been generalized. |
| `wraplength` | If you use a style with this option set to some dimensions, the text will be sliced into pieces no longer than that dimension. |

Methods on a `ttk.Button` include all those described in [Methods common to all tkk widgets](#Methods-common-to-all-tkk-widgets), plus:

`.invoke()`

Calls the button's `command` callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback.

The `.flash()` method of `Tkinter.Button` is not supported by the `ttk.Button` widget.

## Check-button

To create a ttk.Checkbutton widget as the child of a given parent widget:

```
w = ttk.Checkbutton(parent, option=value, ...)
```

Here are the options for the ttk.Checkbutton widget.

| Command | Description |
| --- | --- |
| `class_` | The widget class name. This may be specified when the widget is created, but cannot be changed later. |
| `command` | A function to be called whenever the state of this checkbutton changes. |
| `compound` | This option specifies the relative position of the image relative to the text when you specify both. The value maybe `tk.TOP` (image above text), `tk.BOTTOM` (image below text), `tk.LEFT` (image to the left of the text), or `tk.RIGHT` (image to the right of the text). If you provide both image and text options but do not specify a value for compound, only the image will appear. |
| `cursor` | The cursor that will appear when the mouse is over the checkbutton. |
| `image` | An image to appear on the checkbutton |
| `offvalue` | By default, when a checkbutton is in the off (unchecked) state, the value of the associated variable is 0. You can use the `offvalue` option to specify a different value for the off state. |
| `onvalue` | By default,when a checkbutton is in the on (checked) state, the value of the associated variable is 1. You can use the `onvalue` option to specify a different value for the on state. |
| `style` | The style to be used in rendering this checkbutton |
| `takefocus` | By default, a ttk.Checkbutton will be included in focus traversal, To remove the widget from focus traversal, use `takefocus=False`. |
| `text` | The text to appear on the checkbutton, as a string. |
| `textvariable` | A variable that controls the text that appears on the checkbutton. |
| `underline` | If this option has a non negative value n, an underline will appear under the text character at position `n` |
| `variable` | A control variable that tracks the current state of the checkbutton; go to [Control variables](#coming soon). Normally you will use an `IntVar` here, use `.get` method to see value and the off and on values are 0 and 1, respectively. However, you may use a different control variable type, and specify the `offvalue` and `onvalue` options using values of that type. |
| `width` | Use this option to specify a fixed width or a minimum width. The value is specified in characters; a positive value sets a fixed width of that many average characters, while a negative width sets a minimum width. For example, if an average character in the selected font is 10 pixels wide, option `width=8` will make the text label exactly 80 pixels wide; option `width=-8` will use 80 pixels or the length of the text, whichever is larger. You may also specify a width value in an associated style. If values are specified both in the widget constructor call and in the style, the former takes priority. |

These options of the Tkinter `Checkbutton` widget are not supported by the `ttk.Checkbutton` widget constructor:

**Tkinter Checkbutton options not in ttk.Checkbutton**

| Command | Description |
| --- | --- |
| `activebackground` | Use a style map to control the background option. |
| `activeforeground` | Use a style map to control the foreground option. |
| `anchor` | Configure this option using a style. Use this option to specify the position of the text when the width option allocates extra horizontal space. For example, if you specify options `width=20` and `compound=tk.TOP` on a checkbutton that displays both text and and image, and a style that specifies `anchor=tk.E` (east), the image will be at the right-hand end of the twenty character space, with the text just below it. When a checkbutton displays an image but no text, this option is ignored. |
| `background or bg` | Configure the background option using a style. The bg abbreviation is not supported. |
| `bitmap` | Not supported. |
| `borderwidth or bd` | Configure this option using a style. |
| `disabledforeground` | Use a style map for the foreground option. |
| `font` | Configure this option using a style |
| `foreground or fg ` | Configure this option using a style |
| `height` | Not supported |
| `highlightbackground` | To control the color of the focus highlight when the checkbutton does not have focus, use a style map to control the `highlightcolor` option. |
| `highlightcolor` | You may specify the default focus highlight color by setting this option in a style. You may also control the focus highlight color using a style map |
| `highlightthickness` | Configure this option using a style. This option may not work in all themes. |
| `indicatoron` | Not supported. |
| `justify` | Controls how multiple lines are positioned horizontally relative to each other. Configure this option using a style; values may be `tk.LEFT`, `tk.CENTER`, or `tk.RIGHT` for left-aligned, centered, or right-aligned, respectively. |
| `offrelief` | Not supported. |
| `overrelief` | Use a style map to control the relief option. |
| `padx` | Not supported |
| `pady` | Not supported. |
| `relief` | Use a style map to control the `relief` option. |
| `selectcolor` | Not supported. |
| `selectimage` | Not supported. |
| `state` | In ttk, there is no option with this name. The state mechanism has been generalized. |
| `wraplength` | If you use a style that has this option set to some dimension, the text will be sliced into pieces no longer than that dimension. |

Methods on a `ttk.Checkbutton` include all those described in [Methods-common-to-all-tkk-widgets](#Methods-common-to-all-tkk-widgets), plus:

`.invoke()`

This method toggles the state of the checkbutton. If there is a command callback, it calls that callback, and returns whatever value the callback returned.

Not supported are the following methods of the Tkinter Checkbutton widget: `.deselect()`, `.flash()`, `.select()`, and `.toggle()`. To change the state of a checkbutton through program control, use the `.set()` method of the associated control variable.

## Combo-box
This widget is a combination of an Entry and a drop-down menu. In your application, you will see the usual text entry area, with a downward-pointing arrow. When the user clicks on the arrow, a drop-down menu appears. If the user clicks on one, that choice replaces the current contents of the entry. However, the user may still type text directly into the entry (when it has focus), or edit the current text.

To create a ttk. Combobox widget as the child of a given parent widget:
```
w = ttk.Combobox(parent, option=value, ...)
```
| `class_` | The widget class name. This may be specified when the widget is created, but cannot be changed later. For an explanation of widget classes, see Section 27, “Standardizing appearance” (p.105).|
| `cursor` | The cursor that will appear when the mouse is over the checkbutton;  See Sec-tion 5.8, “Cursors” (p.13).|
| `exportselection` | By default, if you select text within an Entry widget, it is automatically exported to the clipboard. To avoid this exportation, use exportselection=0|
| `height` | Use this option to specify a maximum number of rows that will appear in the drop-down menu; the default is  20. If there are more values than this number, thedrop-down menu will automatically include a vertical scrollbar. |
| `justify` | This option specifies how the text will be positioned with in the entry area when it does not completely fill the area.Values may be tk.LEFT to left-justify ; tk.CENTER to center; or tk.RIGHT to right-justify. |
| `postcommand` |You may use this option to supply a callback function that will be invoked when the user click son the down-arrow.This callback may change the values option; if so, the changes will appear in the drop-down menu.|
| `style` |  The style to be used in rendering this checkbutton; see Section 49, “Using and customizing ttk styles” (p.147). |
| `takefocus` | By default, a ttk. Checkbutton will be included in focus traversal; see Sec-tion 53, “Focus:routing keyboard input” (p.155). To remove the widget from focus traversal, use takefocus=Fals  |
| `textvariable` | A variable that controls the text that appears in the entry area; see Section 52, “Control variables: the values behind the widgets” (p.153)
|
| `` |   |
| `` |   |
| `` |   |
## Entry
## Frame
## Label
## Label-frame
## Menu-button
## Notebook
## Paned-window
## Progressbar
## Radio-button
## Scale
## Scrollbar
## Separator
## Sizegrip
## Tree-view
## Styling-tkk-widgets
## Methods-common-to-all-tkk-widgets


## Bonus
### More references
- <a href="https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html">Tkinter 8.5</a> reference
- <a href="https://coderslegacy.com/python/python-gui/">CodersLegacy</a> blogs Python GUI
