from collections import defaultdict
def process_file(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Create a dictionary to store vertices and their degrees
    vertices = defaultdict(int)

    # Process each line (edge) in the input file
    edges = []
    vertex_map = {}
    current_vertex = 0
    for line in lines:
        vertex1, vertex2 = map(int, line.split(','))
        if vertex1 not in vertex_map:
            vertex_map[vertex1] = current_vertex
            current_vertex += 1
        if vertex2 not in vertex_map:
            vertex_map[vertex2] = current_vertex
            current_vertex += 1
        vertices[vertex_map[vertex1]] += 1
        vertices[vertex_map[vertex2]] += 1
        edges.append((vertex_map[vertex1], vertex_map[vertex2]))

    # Write the output file
    with open(output_file, 'w') as f:
        # Write the number of different vertices
        f.write(str(len(vertices)) + '\n')

        # Write each vertex and its degree
        for vertex, degree in sorted(vertices.items()):
            f.write(str(vertex) + ' ' + str(degree) + '\n')

        # Write the edges from the input file
        for edge in edges:
            f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')

# Call the function with your input and output files
process_file('/home/ttrang/graph/data/karate_edges.txt','/home/ttrang/graph/data/karate_edges.nde')
