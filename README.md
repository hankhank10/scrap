# scrap
 
scrap() is an easy way of working out what is going on within your python scripts even if you don't have access to the terminal where they are running - say there's a GUI which takes the full screen or you are on a remote headless server

It can direct output - either manually or automatically - to a "scrap" which you can create at https://scrap.rest/

All that is needed to run this is putting scrap.py (lightweight and open source) in your project folder.  No pips, no dependencies, nothing to install, distribute right with your projects.

## Installation

Copy scrap.py to your project folder.

Initialise in each file you plan to use it in with: ```import scrap```

Set up the scrap (one time) using ```scrap.setup("your-scrap-name")```

## Manual usage

Scrap can report things manually using the following syntax:

```scrap.write ("Your text)```

See example-code.py for a full example.

## Automatic usage

It can also be set to automatically output all future screen output or error output to your scrap:

```scrap.auto_scrap_on_print()```

```scrap.auto_scrap_on_error()```

See example-code-automatic.py for a full example.
