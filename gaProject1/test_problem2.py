import problem2

output1_p2 = {
    'A':[{1: [1, 1, 1, 1],
          2: [0, 2, 2, 2],
          3: [1, 0, 3, 3],
          4: [0, 1, 0, 4],
          5: [1, 2, 1, 0]
          }],
    'B':[{12.1:[0.1, 0.1, 0.1, 2.1],
          14.2: [0.2, 2.2, 2.2, 4.2],
          20.3: [0.3, 2.3, 0.3, 0.3],
          25.4: [1.4, 1.4, 1.4, 0.4]
          }],
    'C':[{10: [0, 1, 2, 0],
          25.5: [1.5, 1.5, 1.5, 0.5],
          50.9: [0.9, 2.9, 2.9, 0.9],
          101: [1, 2, 1, 1]
          }]
}

def test1_problem2():
    assert problem2.modify_dict(problem2.test_dict, problem2.optional_remainder ) == output1_p2


output2_p2 = {
    'A':[{1: [1],
          2: [0],
          3: [1],
          4: [0],
          5: [1]
          }],
    'B':[{12.1:[0.1],
          14.2: [0.2],
          20.3: [0.3],
          25.4: [1.4]
          }],
    'C':[{10: [0],
          25.5: [1.5],
          50.9: [0.9],
          101: [1]
          }]
}
def test2_problem2():
    assert problem2.modify_dict(problem2.test_dict, [2]) == output2_p2