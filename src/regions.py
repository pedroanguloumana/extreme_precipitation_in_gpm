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

def wmp_region():
    x = Region(name='WMP', long_name='Warm Pool', lat_south=-40, lat_north=20, lon_west=140, lon_east=178)
    return x

def cio_region():
    x = Region(name='CIO', long_name='Central Indian Oceaan', lat_south=-40, lat_north=40, lon_west=61, lon_east=145)
    return x

def afc_region():
    x = Region(name='AFC', long_name='Africa', lat_south=-40, lat_north=40, lon_west=-30, lon_east=60)
    return x