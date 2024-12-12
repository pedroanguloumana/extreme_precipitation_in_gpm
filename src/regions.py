class Region:
    def __init__(self, name, long_name, lat_south, lat_north, lon_west, lon_east):
        self._name = name
        self._long_name = long_name
        self._lat_south = lat_south
        self._lat_north = lat_north
        self._lon_west = lon_west
        self._lon_east = lon_east

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def long_name(self):
        return self._long_name

    @long_name.setter
    def long_name(self, value):
        self._long_name = value

    @property
    def lat_south(self):
        return self._lat_south

    @lat_south.setter
    def lat_south(self, value):
        self._lat_south = value

    @property
    def lat_north(self):
        return self._lat_north

    @lat_north.setter
    def lat_north(self, value):
        self._lat_north = value

    @property
    def lon_west(self):
        return self._lon_west

    @lon_west.setter
    def lon_west(self, value):
        self._lon_west = value

    @property
    def lon_east(self):
        return self._lon_east

    @lon_east.setter
    def lon_east(self, value):
        self._lon_east = value

    def get_slices(self):
        """Returns a dictionary with latitude and longitude slices."""
        return {
            'lat': slice(self.lat_south, self.lat_north),
            'lon': slice(self.lon_west, self.lon_east)
        }
def afc_region():
    x = Region(
        name='AFC',
        long_name='Africa',
        lat_south=-40,
        lat_north=40,
        lon_west=-30, # trimmed to match with SAM region better
        lon_east=60
    )
    return x

def aka_region():
    x = Region(
        name='AKA',
        long_name='Alaska',
        lat_south=35,
        lat_north=67,
        lon_west=-178,
        lon_east=-115
    )
    return x

def cio_region():
    x = Region(
        name='CIO',
        long_name='Central Indian Ocean',
        lat_south=-40,
        lat_north=10, 
        lon_west=60,  # 55 originally, trminned for AFC (60)
        lon_east=110
    )
    return x

def epo_region():
    x = Region(
        name='EPO',
        long_name='Eastern Pacific Ocean',
        lat_south=-67,
        lat_north=45,
        lon_west=-178,
        lon_east=-130
    )
    return x

def eur_region():
    x = Region(
        name='EUR',
        long_name='Europe',
        lat_south=35,
        lat_north=67,
        lon_west=-20,
        lon_east=45
    )
    return x

def h01_region():
    x = Region(
        name='H01',
        long_name='Pacific West of South America (Hole1)',
        lat_south=-67,
        lat_north=25,
        lon_west=-130, # -140 original, trimmed for EPO region (-130)
        lon_east=-85  
    )
    return x

def h02_region():
    x = Region(
        name='H02',
        long_name='North Atlantic (Hole2)',
        lat_south=15,
        lat_north=67,
        lon_west=-65,
        lon_east=-10
    )
    return x

def h03_region():
    x = Region(
        name='H03',
        long_name='South of Africa (Hole3)',
        lat_south=-67,
        lat_north=-35,
        lon_west=-30,
        lon_east=75
    )
    return x

def h04_region():
    x = Region(
        name='H04',
        long_name='South Indian Ocean (Hole4)',
        lat_south=-67,
        lat_north=-35,
        lon_west=70,
        lon_east=178
    )
    return x

def h05_region():
    x = Region(
        name='H05',
        long_name='Western Pacific (Hole5)',
        lat_south=10, # 5 originally, trimmed for WMP (10)
        lat_north=40,
        lon_west=130,  # 125 original, trimmed for SAS (130)
        lon_east=178
    )
    return x

def nam_region():
    x = Region(
        name='NAM',
        long_name='North America',
        lat_south=15,
        lat_north=67,
        lon_west=-140,
        lon_east=-55
    )
    return x

def nas_region():
    x = Region(
        name='NAS',
        long_name='North Asia',
        lat_south=35,
        lat_north=67,
        lon_west=40,
        lon_east=178
    )
    return x

def sam_region():
    x = Region(
        name='SAM',
        long_name='South America',
        lat_south=-67,
        lat_north=20,
        lon_west=-85, #  -95 originally, trimmed for H01 (-85)
        lon_east= -30  
    )
    return x

def sas_region():
    x = Region(
        name='SAS',
        long_name='South Asia',
        lat_south=10, # 5 originally, trimmed for CIO (10)
        lat_north=40,
        lon_west=60,  # 55 original, trimmed for AFC (60)
        lon_east=130
    )
    return x

def wmp_region():
    x = Region(
        name='WMP',
        long_name='Warm Pool',
        lat_south=-40,
        lat_north=10, 
        lon_west=110,  # 105 original, trimmed for CIO (110)
        lon_east=178
    )
    return x
