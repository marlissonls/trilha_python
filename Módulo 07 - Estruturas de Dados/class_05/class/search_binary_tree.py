class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        break
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        break
                    else:
                        current_node = current_node.right_child

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False

    def delete(self, value):
        node_to_delete = self._find_node(value)
        if node_to_delete is None:
            return False  # O nó a ser excluído não foi encontrado na árvore
        parent_node = self._find_parent_node(value)
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            # O nó a ser excluído não tem filhos
            if parent_node is None:
                # O nó a ser excluído é a raiz da árvore
                self.root = None
            elif parent_node.left_child == node_to_delete:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        elif node_to_delete.left_child is not None and node_to_delete.right_child is not None:
            # O nó a ser excluído tem dois filhos
            successor_node = self._find_min_node(node_to_delete.right_child)
            successor_value = successor_node.value
            self.delete(successor_value)
            node_to_delete.value = successor_value
        else:
            # O nó a ser excluído tem apenas um filho
            child_node = node_to_delete.left_child or node_to_delete.right_child
            if parent_node is None:
                # O nó a ser excluído é a raiz da árvore
                self.root = child_node
            elif parent_node.left_child == node_to_delete:
                parent_node.left_child = child_node
            else:
                parent_node.right_child = child_node
        return True

    def _find_node(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def _find_parent_node(self, value):
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if current_node.value == value:
                return parent_node
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left_child
            else:
                parent_node = current_node
                current_node = current_node.right_child
        return None

    def _find_min_node(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node