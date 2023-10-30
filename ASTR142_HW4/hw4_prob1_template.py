>>> from astroquery.simbad import Simbad
>>> import astropy.coordinates as coord
>>> import astropy.units as u
>>> Simbad.add_votable_fields('ra', 'dec')
>>> result_table = Simbad.query_objects(["M2", "M45", "HD 189733", "3C 273", "NGC 1068", "AU Mic", "TRAPPIST-1"]) 
>>> result_table

#    MAIN_ID           RA      ...     DEC_2     SCRIPT_NUMBER_ID
#                   "h:m:s"    ...    "d:m:s"
#     object         str13     ...     str13          int32
#--------------- ------------- ... ------------- ----------------
#          M   2   21 33 27.02 ...   -00 49 23.7                1
#Cl Melotte   22    03 46 24.2 ...     +24 06 50                2
#      HD 189733 20 00 43.7129 ... +22 42 39.073                3
#         3C 273 12 29 06.6998 ... +02 03 08.597                4
#          M  77 02 42 40.7091 ... -00 00 47.859                5
#      HD 197481 20 45 09.5324 ... -31 20 27.237                6
#     TRAPPIST-1 23 06 29.3684 ... -05 02 29.037                7
