"""
    PROJECT    : Outer billiards visualization project.
    FILE       : billiard.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main billiard interface class implementation module.
    LAST UPDATE: 18.05.2021.
"""

from polygon import *
from seg_ray import *


'''
    Outer billiard interface representation class.
    
    Fields:
        plg (polygon): The generative polygon.
        _bound_iter (int): Current boundary iteration.
        bound (array[]): The boundary elements array (rays and segments).
        
    Methods:
        __init__(plg): The constructor.
        transform(p, left): Transform the point by the billiard.
        
        draw_polygon(rnd, color): Draw the generative polygon.
        
        build_bound(n): Build the billiard boundary after the n-th iteration.
        draw_bound(rnd , color): Draw the evaluated boundary.
'''
class billiard:
    '''
        The billiard class constructor.
        Arguments:
            plg (polygon): The polygon for the billiard.
    '''
    def __init__(self, plg):
        self.plg = plg
        self.bound = []
        self._bound_iter = 0
    # End of '__init__' function

    '''
        Pack the split segment auxiliary function.
        Arguments:
            seg (segment): The segment to split.
            v (segment): The ray to split with.
            left (bool): Flag to perform left billiard.
        Returns:
            (array[]): The transformed object.
    '''
    def pack_split(self, seg, v, left):
        split_pnt = seg.intersect(v)
        if split_pnt is None:  # Just in case
            raise Exception("OH NO, WHAT A DISASTER!!!")

        res = []
        first = self.transform(segment(seg.p1, split_pnt), left)
        second = self.transform(segment(split_pnt, seg.p2), left)
        if type(first) == segment:
            res.append(first)
        elif type(first) == list:
            res += first
        if type(second) == segment:
            res.append(second)
        elif type(second) == list:
            res += second
        return res
    # End of 'pack_split' function

    '''
        Transform the point by the billiard.
        Arguments:
            p (point or ray or segment): The object to transform.
            left (bool): Flag to perform left billiard (False by default).
        Returns:
            (point or ray or segment or array[]) The transformed object or several objects. 
    '''
    def transform(self, p, left=False):
        if type(p) == point:
            return p.reflect_about(rightest(p, self.plg.points, left))
        elif type(p) == segment:
            v1 = rightest(p.p1, self.plg.points, left)
            v2 = rightest(p.p2, self.plg.points, left)

            # Both edges are not on the boundaries
            if type(v1) is point and type(v2) is point:
                # Split...
                if v1 is not v2:
                    rig = rightest(point(0, 0), [v1, v2], not left)  # Very bugged for the square; seems unfixable
                    v = segment(rig, self.plg.points[(self.plg.points.index(rig) + int(not left))
                                                     % len(self.plg.points)])
                    return self.pack_split(p, v, left)
                # No split...
                return segment(p.p1.reflect_about(v1), p.p2.reflect_about(v1))

            # Both edges are on the boundaries
            if type(v1) is segment and type(v2) is segment:
                # The whole segment is on boundary line (no transformation)
                if v1 is v2:
                    return None
                # No split...
                if v1.p1 is v2.p1 or v1.p1 is v2.p2 or v1.p2 is v2.p1 or v1.p2 is v2.p2:
                    v = v1.p1 if (v1.p1 == v2.p1 or v1.p1 == v2.p2) else v1.p2
                    return segment(p.p1.reflect_about(v), p.p2.reflect_about(v))
                # Split...
                rig = rightest(point(0, 0), [v1.p1, v1.p2, v2.p1, v2.p2], not left)
                v = segment(rig, self.plg.points[(self.plg.points.index(rig) + int(not left))
                                                 % len(self.plg.points)])
                return self.pack_split(p, v, left)

            # Exactly one edge is on the boundary
            if type(v1) is segment or type(v2) is segment:
                v_ = v1 if type(v1) is segment else v2
                v__ = v1 if v_ is v2 else v2
                # No split...
                if v__ is v_.p1 or v__ is v_.p2:
                    return segment(p.p1.reflect_about(v__), p.p2.reflect_about(v__))
                # Split...
                targ = p.p1 if v_ is v1 else p.p2
                rig = v_.p1 if (v_.p1 - targ).len2() < (v_.p2 - targ).len2() else v_.p2
                v = segment(rig, self.plg.points[(self.plg.points.index(rig) + int(not left))
                                                 % len(self.plg.points)])
                return self.pack_split(p, v, left)

            # Magic happened
            raise Exception("???????????????????????")
        else:  # Ray assumed
            pass
    # End of 'transform' function

    '''
        Draw the generative polygon.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw_polygon(self, rnd, color=(0, 0, 0)):
        self.plg.draw(rnd, color)
    # End of 'draw_polygon' function

    '''
        Build the billiard boundary after the n-th iteration.
        Arguments:
            n (int): Number of iterations to build boundary for.
        Returns: None.
    '''
    def build_bound(self, n, rnd):
        if self._bound_iter >= n:
            return
        self._bound_iter = n
        for i in range(len(self.plg.points)):
            self.bound.append(ray(self.plg.points[i], self.plg.points[(i + 1) % len(self.plg.points)]))
    # End of 'build_bound' function

    '''
        Draw the evaluated boundary.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw_bound(self, rnd, color=(0, 0, 0)):
        for elem in self.bound:
            elem.draw(rnd, color)
    # End of 'draw_bound' function
# End of 'billiard' class

# END OF 'billiard.py' FILE
