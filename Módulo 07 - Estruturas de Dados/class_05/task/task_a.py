class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root
    
    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root
    
    def insert(self, value):
        def _insert_node(node, value):
            if node is None:
                return Node(value)
            
            if value < node.value:
                node.left = _insert_node(node.left, value)
            else:
                node.right = _insert_node(node.right, value)
            
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            
            balance = self.balance_factor(node)
            if balance > 1 and value < node.left.value:
                return self.right_rotate(node)
            
            if balance < -1 and value > node.right.value:
                return self.left_rotate(node)
            
            if balance > 1 and value > node.left.value:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            
            if balance < -1 and value < node.right.value:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
            return node
        
        self.root = _insert_node(self.root, value)
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self, value):
        def _delete_node(node, value):
            if node is None:
                return node
            
            if value < node.value:
                node.left = _delete_node(node.left, value)
            elif value > node.value:
                node.right = _delete_node(node.right, value)
            else:
                # Nó com apenas um filho ou nenhum filho
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                
                # Nó com dois filhos
                temp = self.min_value_node(node.right)
                node.value = temp.value
                node.right = _delete_node(node.right, temp.value)
            
            # Se a árvore tiver apenas um nó, não é necessário balanceamento
            if node is None:
                return node
            
            # Atualiza a altura do nó atual
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            
            # Verifica o fator de balanceamento e faz as rotações necessá

            balance = self.balance_factor(node)
            
            # Caso de rotação à esquerda
            if balance > 1 and self.balance_factor(node.left) >= 0:
                return self.right_rotate(node)
            
            # Caso de rotação à direita
            if balance < -1 and self.balance_factor(node.right) <= 0:
                return self.left_rotate(node)
            
            # Caso de rotação dupla à esquerda
            if balance > 1 and self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            
            # Caso de rotação dupla à direita
            if balance < -1 and self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
            return node
        
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        if node is not None:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)