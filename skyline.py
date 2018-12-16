'''
218. The Skyline Problem
'''


'''
Solution:
1) Take buildings input and for each element which is format [start, end, height].
   Split it into below format and create building objects
   [start, is_start, height]
   [end,   is_start, end]
   is_start = true when its the 0th index
   eg: [1, 3, 4], then after split,
       [1, true, 4]    // [start, is_start, height]
       [3, false, 4]   // [end, is_start, height]
2) The reason we create seperate objects with start and end for each element is to
   make sure we sort it and also keep non-overlapping values
3) We sort the building objects based on following cases:
   1) Compare and return with lower height first
   2) If start points are same then we select one with higher height
   3) If end points are same then we select one with lower height
   4) If start and end points are same then we select one with start height first
4) After the sort, create a Queue with default value as 0 and max_height=0
5) Then traverse the sorted building objects to build the result set
6) To check if it can make to the result list, we look at following things,
   a) If its a start point,
        if the height is not present in queue:
           - add it. If the previous saved max_height is not equal to max(queue) then, we add [start, height] in result
        else:
           don't add to the result
   b) If its an end point,
        if the height is present in queue:
           - remove it. Then check if it saved max_height != max(queue) i.e., max_height has changed,
             then add [end, max(queue)] in the result
'''

class BuildingPoint(object):
    def __init__(self, point, is_start, height):
        self.point = point
        self.is_start = is_start
        self.height = height

    def __repr__(self):
        return "BuildingPoint({}, {}, {})".format(self.point, self.is_start, self.height)

    def __str__(self):
        return "point:{} | is_start:{} | height:{}".format(
            self.point,
            self.is_start,
            self.height
        )

    def __lt__(self, other):
        """
        Used to compare objects when sorted is called. We override in-built sort
        to apply custom sort
        1) If points are un-equal, return smaller one
        2) if points are same,
             - then we convert self.is_start to negative and compare to satisf the following conditions
                   1) If start points are same then we select one with higher height
                   2) If end points are same then we select one with lower height
                   3) If start and end points are same then we select one with start height first
        """
        if self.point != other.point:
            return self.point < other.point
        else:
            if self.is_start:
                h1 = -self.height
            else:
                h1 = self.height

            if other.is_start:
                h2 = -other.height
            else:
                h2 = other.height

            return h1 < h2


def get_skyline(buildings):
    building_points = []
    for building in buildings:
        building_points.append(BuildingPoint(building[0], True, building[2]))
        building_points.append(BuildingPoint(building[1], False, building[2]))

    building_points = sorted(building_points)

    # we use hash_map instead of priority queue to enhance remove and performance
    height_dict = {}
    height_dict[0] = 1
    max_height = 0
    result = []

    for bp in building_points:
        if bp.is_start:
            height_dict[bp.height] =  height_dict[bp.height] + 1 if bp.height in height_dict else 1
        else:
            if height_dict[bp.height] == 1:
                height_dict.pop(bp.height)
            else:
                height_dict[bp.height] = height_dict[bp.height] - 1

        current_max_height = max(height_dict.keys())
        if max_height != current_max_height:
            # If there is any difference in the max_height and current_max_height
            # it becomes part of the result
            if bp.is_start:
                result.append([bp.point, bp.height])
            else:
                result.append([bp.point, current_max_height])

            max_height = current_max_height


    return result


if __name__ == '__main__':
    buildings = [[1, 3, 4], [3, 4, 4], [2, 6, 2], [8, 11, 4], [7, 9, 3], [10, 11, 2]]
    expected_result = [[1, 4], [4, 2], [6, 0], [7, 3], [8, 4], [11, 0]]
    actual_result = get_skyline(buildings)
    assert expected_result == actual_result

    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
    expected_result = [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]
    actual_result = get_skyline(buildings)
    assert expected_result == actual_result