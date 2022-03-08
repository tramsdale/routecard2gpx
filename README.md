# routecard2gpx

This is a command line utility which turns a list of OS grid references into a gpx file
suitable for loading into OSmaps online or (probably!) other route mapping tools.

The utility also generates a list of distances and bearings.

NOTE - this is NOT a tool you should actually use to plan routes with - it takes no
account of the underlying map or ground features. It is at best good for checking,
but I use it to load up a route plan so I can then go into 'detail mode' on what
I'm expecting to see!

usage: rc2gpx.py [-h] [-o OUTFILE] [-v] [--map MAP] [--name NAME] [--desc DESCRIPTION] [-q] [--speed SPEED] [GR [GR ...]]

Process a route-card into a gpx file

positional arguments:
  GR                  Grid references in 6-digit OS Map format

optional arguments:
  -h, --help          show this help message and exit
  -o OUTFILE          Output file name
  -v                  Select verbose mode
  --map MAP           map square, such as TL, SV, NX etc
  --name NAME         Name to use in gpx file
  --desc DESCRIPTION  Name to use in gpx file
  -q
  --speed SPEED
  
  
  Example:
  
%  python rc2gpx.py 421701 437723 393749 369727 336707 330703 321710 318713 314713 --name="Exped day 1"

Using map square: TL
Writing gpx to file: output.gpx
Processing coordinate TL 421701 ...lat:52.311, lon:0.083  delta = 0.00, 0.00,  ... 0.00km, 0.0deg
Processing coordinate TL 437723 ...lat:52.330, lon:0.107  delta = 1600.00, 2200.00,  ... 2.72km, 36.0deg
Processing coordinate TL 393749 ...lat:52.354, lon:0.044  delta = -4400.00, 2600.00,  ... 5.11km, 300.6deg
Processing coordinate TL 369727 ...lat:52.335, lon:0.008  delta = -2400.00, -2200.00,  ... 3.26km, 227.5deg
Processing coordinate TL 336707 ...lat:52.318, lon:-0.041  delta = -3300.00, -2000.00,  ... 3.86km, 238.8deg
Processing coordinate TL 330703 ...lat:52.315, lon:-0.050  delta = -600.00, -400.00,  ... 0.72km, 236.3deg
Processing coordinate TL 321710 ...lat:52.321, lon:-0.063  delta = -900.00, 700.00,  ... 1.14km, 307.9deg
Processing coordinate TL 318713 ...lat:52.324, lon:-0.068  delta = -300.00, 300.00,  ... 0.42km, 315.0deg
Processing coordinate TL 314713 ...lat:52.324, lon:-0.073  delta = -400.00, 0.00,  ... 0.40km, 270.0deg
╒════════╤════════════╤═══════════╤═══════════════╤════════════════╤══════════════╕
│ Type   │ Grid ref   │ Bearing   │ Distance/km   │ Est leg time   │ Total time   │
╞════════╪════════════╪═══════════╪═══════════════╪════════════════╪══════════════╡
│ START  │ TL 421701  │ 036       │ 2.7           │ 54m            │ 54m          │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY1   │ TL 437723  │ 301       │ 5.1           │ 1h42           │ 2h37         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY2   │ TL 393749  │ 227       │ 3.3           │ 1h05           │ 3h42         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY3   │ TL 369727  │ 239       │ 3.9           │ 1h17           │ 4h59         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY4   │ TL 336707  │ 236       │ 0.7           │ 14m            │ 5h13         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY5   │ TL 330703  │ 308       │ 1.1           │ 23m            │ 5h36         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY6   │ TL 321710  │ 315       │ 0.4           │ 08m            │ 5h45         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ WAY7   │ TL 318713  │ 270       │ 0.4           │ 08m            │ 5h53         │
├────────┼────────────┼───────────┼───────────────┼────────────────┼──────────────┤
│ FINISH │ TL 314713  │           │               │                │              │
╘════════╧════════════╧═══════════╧═══════════════╧════════════════╧══════════════╛
