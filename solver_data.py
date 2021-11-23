movedata = {
    "R": ["R", "B", "L", "F"],
    "R'": ["R'", "B'", "L'", "F'"],
    "U": ["U", "U", "U", "U"],
    "U'": ["U'", "U'", "U'", "U'"],
    "L": ["L", "F", "R", "B"],
    "L'": ["L'", "F'", "R'", "B'"],
    "D": ["D", "D", "D", "D"],
    "D'": ["D'", "D'", "D'", "D'"],
    "F": ["F", "R", "B", "L"],
    "F'": ["F'", "R'", "B'", "L'"],
    "B": ["B", "L", "F", "R"],
    "B'": ["B'", "L'", "F'", "R'"]
}

positionTransformData = [
    # target (0 - 3 only)
    [
        # sides
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(4, 0, 0), (4, 0, 1), (4, 0, 2)], [(4, 1, 0), (4, 1, 1), (4, 1, 2)], [(4, 2, 0), (4, 2, 1), (4, 2, 2)]],
        [[(5, 0, 0), (5, 0, 1), (5, 0, 2)], [(5, 1, 0), (5, 1, 1), (5, 1, 2)], [(5, 2, 0), (5, 2, 1), (5, 2, 2)]]
    ],
    [
        [[(1, 0, 0), (1, 0, 1), (0, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (1, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (2, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (3, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(4, 0, 2), (4, 1, 2), (4, 2, 2)], [(4, 0, 1), (4, 1, 1), (4, 2, 1)], [(4, 0, 0), (4, 1, 0), (4, 2, 0)]],
        [[(5, 2, 0), (5, 1, 0), (5, 0, 0)], [(5, 2, 1), (5, 1, 1), (5, 0, 1)], [(5, 2, 2), (5, 1, 2), (5, 0, 2)]]
    ],
    [
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(4, 2, 2), (4, 2, 1), (4, 2, 0)], [(4, 1, 2), (4, 1, 1), (4, 1, 0)], [(4, 0, 2), (4, 0, 1), (4, 0, 0)]],
        [[(5, 2, 2), (5, 2, 1), (5, 2, 0)], [(5, 1, 2), (5, 1, 1), (5, 1, 0)], [(5, 0, 2), (5, 0, 1), (5, 0, 0)]]
    ],
    [
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(4, 2, 0), (4, 1, 0), (4, 0, 0)], [(4, 2, 1), (4, 1, 1), (4, 0, 1)], [(4, 2, 2), (4, 1, 2), (4, 0, 2)]],
        [[(5, 0, 2), (5, 1, 2), (5, 2, 2)], [(5, 0, 1), (5, 1, 1), (5, 2, 1)], [(5, 0, 0), (5, 1, 0), (5, 2, 0)]]
    ]
]

whiteEdgePairs = {
    (0, 0, 1): (5, 2, 1),
    (0, 1, 2): (1, 1, 0),
    (0, 2, 1): (4, 0, 1),
    (0, 1, 0): (3, 1, 2),
    (5, 0, 1): (2, 0, 1),
    (5, 1, 2): (1, 0, 1),
    (5, 2, 1): (0, 0, 1),
    (5, 1, 0): (3, 0, 1)
}

whiteEdgeDirectMoves = {
    (0, 0, 1): ["FDR'D'", "FR'F'", "DF'LFD'", "F'LF"],
    (0, 1, 2): ["DR'D'", "R'", "D'R'D", "F2LF2"],
    (0, 2, 1): ["F'DR'D'", "F'R'", "FD'R'D", "FL"],
    (0, 1, 0): ["D'LD", "F2R'F2", "DLD'", "L"],
    (5, 0, 1): ["U2F2", "UR2", "B2", "U'L2"],
    (5, 1, 2): ["UF2", "R2", "U'B2", "U2L2"],
    (5, 2, 1): ["F2", "U'R2", "U2B2", "UL2"],
    (5, 1, 0): ["U'F2", "U2R2", "UB2", "L2"]
}