from Polygon import Polygon


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        # self._polygons = [Polygon(i, R) for i in range(3, m + 1)]
        print("after init")

    def __len__(self):
        return self._m + 1

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    #
    # def __getitem__(self, s):
    #     return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self.PolygonIterator(self),
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

    def __iter__(self):
        print("Calling polygons instance __iter__")
        return self.PolygonIterator(self)

    class PolygonIterator:
        def __init__(self, polygons):
            print("Calling PolygonIterator __init__")
            self._polygons = polygons
            self._index = 3

        def __iter__(self):
            print("Calling PolygonIterator instance __iter__")
            return self

        def __next__(self):
            print("Calling PolygonIterator __next__")
            if self._index >= len(self._polygons):
                raise StopIteration
            else:
                item = Polygon(self._index, self._polygons._R)
                self._index += 1
                return item
