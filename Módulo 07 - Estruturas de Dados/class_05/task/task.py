class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, current_node, new_node):
        if new_node.key < current_node.key:
            if not current_node.left:
                current_node.left = new_node
            else:
                self._insert_node(current_node.left, new_node)
        else:
            if not current_node.right:
                current_node.right = new_node
            else:
                self._insert_node(current_node.right, new_node)

    def search(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, current_node, key):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node.value
        elif key < current_node.key:
            return self._search_node(current_node.left, key)
        else:
            return self._search_node(current_node.right, key)

    def delete(self, key):
        self._delete_node(None, self.root, key)

    def _delete_node(self, parent_node, current_node, key):
        if not current_node:
            return False
        elif key == current_node.key:
            if not current_node.left and not current_node.right:
                if current_node == self.root:
                    self.root = None
                elif parent_node.left == current_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            elif current_node.left and not current_node.right:
                if current_node == self.root:
                    self.root = current_node.left
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left
                else:
                    parent_node.right = current_node.left
            elif not current_node.left and current_node.right:
                if current_node == self.root:
                    self.root = current_node.right
                elif parent_node.left == current_node:
                    parent_node.left = current_node.right
