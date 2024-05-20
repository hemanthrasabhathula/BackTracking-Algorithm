from data import graph, colors  # importing graph and color variables dataset


def get_next_county(graph, color_map):
    """
    This Function returns the next county 
    by iterating through the graph counties and skips 
    which are colored and returns the first uncolored one.
    
    Parameters :
        - graph     : Dictionary of county mapping
        - color_map : map to store the newly assigned county with color.

    Returns :
        - next_county  : next county from the graph.
    """

    next_county = None
    for county in graph:
        if county not in color_map:
            next_county = county
            break
    return next_county


def is_safe_color(county, color, graph, color_map):
    """
    for loop iterates through the neighbours of the county
    checks if the input color is already assigned to any of them

    Parameters :
        - county      : county from graph
        - color     : color to check with the neighbours
        - graph     : Dictionary of county mapping
        - color_map : map to store the newly assigned county with color.

    Returns :
        - True  : if the color is not present in the neighbour counties
        - False : if the color is matches with the neighbour county.
    """

    for neighbor in graph[county]:
        if color_map.get(neighbor) == color:
            return False
    return True


def color_utilility(county, colors, graph, color_map):
    """
    This function iterates through colors and checks if is is safe to assign
    if it finds False. Recursively calls itself with next color

    Once the county got assigned. It recursively calls to the next county with updated color_map.

    Parameters :
        - county    : current county from graph
        - colors    : list of available colors
        - graph     : Dictionary of county mapping
        - color_map : map to store the newly assigned county with color.

    Returns :
        - True  : if Solution exists.
        - False : if No Solution exists. 
    """

    for color in colors:
        if is_safe_color(county, color, graph, color_map):  # checks if the color is safe to assign to the county
            print(f"coloring county :: {county} with color {color}")
            color_map[county] = color  # assigning the color to the county
            next_county = get_next_county(graph, color_map)  # fetching the next county from the graph
            if next_county is None or color_utilility(next_county, colors, graph,
                                                      color_map):  # checking if the next county can be colored
                return True  # by recursively calling the color_utility to color next county
            print(f"No possible colors for county [{next_county}]. Hence backtracking to county [{county}]")
            del color_map[county]  # removing the previous county from the color map if the
            # current county is not having any color to choose from. So Backtracking
    return False  # returns False to Further backtrack and iterate with another color.


def missouri_map_coloring(graph, colors):
    """
    Main Class which triggers the utility function 
    by providing graph and colors.

    Parameters :   
        graph  : Dictionary with List of counties and thier neighbours
        colors : List of colors to choose.

    Output : 
        prints out the list of counties and their assigned colors
    """

    color_map = {}  # initializing the color_map with empty
    if not color_utilility(next(iter(graph)), colors, graph,
                           color_map):  # calling the color utility with first element in
        # graph and if the return value is False
        print(
            f"No solution exists with the given colors :: {colors}")  # then there is No Solution with the given colors
        return

    print(f"Solution exists by using the given colors :: {colors}")
    print("Here is the Missouri County map with assigned colors:")  # else we have a Found a solution. Printing it
    print(f"{'Sno'.ljust(3)}  {'Counties'.ljust(20)}  {'Colors'.ljust(5)}")
    sum = 1
    for county, color in color_map.items():  # iterating through the map
        print(f"{sum:3}. {county.ljust(20)}: {color.ljust(5)}")  # and printing the county and its corresponding color
        sum += 1


missouri_map_coloring(graph, colors)  # calling the main function with arguments.
