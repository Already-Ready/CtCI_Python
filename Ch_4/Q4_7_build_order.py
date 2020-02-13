import unittest

class Node():
    def __init__(self,data):
        self.data = data
        self.edge = []
        # 나를 가르키는 노드가 얼마나 되는가?
        self.dependency_num = 0

    def add_egde_node(self,node):
        self.edge.append(node)
        node.dependency_num += 1

class Queue():
    def __init__(self):
        self.queue = []

    def add(self,data):
        self.queue.append(data)

    def remove(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise Exception("Queue is Empty")

    def is_not_empty(self):
        return len(self.queue) > 0

def build_order(projects, dependencies):
    nodes = {}
    for project in projects:
        nodes[project] = Node(project)
    for dependecy in dependencies:
        nodes[dependecy[0]].add_egde_node(nodes[dependecy[1]])
    queue = Queue()
    for project in projects:
        if not nodes[project].dependency_num:
            queue.add(nodes[project])
    # 초기에 모든 project에 대해 dependecy_num 이 0인 노드가 없다?
    # --> queue가 비었다 --> 사이클이 존재한다.
    if not queue.queue:
        return Exception("Graph have Cycle")
    order = []
    while queue.is_not_empty():
        node = queue.remove()
        order.append(node.data)
        if node.edge:
            for edge_node in node.edge:
                edge_node.dependency_num -= 1
                if edge_node.dependency_num == 0:
                    queue.add(edge_node)
                    
    if len(order) < len(projects):
        return Exception("Graph have Cycle")
    return order

class Test(unittest.TestCase):
  def test_build_order(self):
    projects = ["A", "B", "C", "D", "E", "F", "G"]
    dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]
    self.assertEqual(build_order(projects, dependencies1),
        ["D", "F", "G", "B", "C", "A", "E"])
    dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    self.assertEqual(build_order(projects, dependencies2).__class__, Exception)
    dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
        ("B", "F"), ("C", "F"), ("G", "D")]
    self.assertEqual(build_order(projects, dependencies3),
        ["E", "G", "A", "D", "B", "C", "F"])

if __name__ == "__main__":
  unittest.main()