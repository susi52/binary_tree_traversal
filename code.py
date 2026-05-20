from collections import deque

# Класс узла бинарного дерева
class TreeNode:
    # Каждый узел хранит значение, ссылку на левого и правого потомка
    def __init__(self, value):
        self.value = value  # значение узла
        self.left = None  # левый потомок
        self.right = None  # правый потомок

# Рекурсивные обходы (DFS)
def preorder(root, result=None):
    # Если список ещё не создан (первый вызов), создаём новый
    if result is None:
        result = []
    # Если узел существует, выполняем прямой обход: корень -> левый -> правый
    if root:
        result.append(root.value)  # посещаем корень
        preorder(root.left, result)  # рекурсивно обходим левое поддерево
        preorder(root.right, result)  # рекурсивно обходим правое поддерево
    return result

# Симметричный обход: левое поддерево -> корень -> правое поддерево
def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)  # левое поддерево
        result.append(root.value)  # корень
        inorder(root.right, result)  # правое поддерево
    return result

# Обратный обход: левое поддерево -> правое поддерево -> корень
def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)  # левое поддерево
        postorder(root.right, result)  # правое поддерево
        result.append(root.value)  # корень
    return result

# Обход в ширину (BFS) – по уровням
def level_order(root):
    # Если дерево пустое, возвращаем пустой список
    if not root:
        return []
    result = []  # здесь будет список уровней (каждый уровень – список значений)
    queue = deque([root])  # очередь, начинаем с корня
    # Пока очередь не пуста, обрабатываем уровень за уровнем
    while queue:
        # Сколько узлов на текущем уровне (именно столько мы должны извлечь)
        level_size = len(queue)
        current_level = []  # список для значений текущего уровня

        # Извлекаем ровно level_size узлов, добавляем их потомков в очередь
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            # Добавляем левого потомка, если он есть
            if node.left:
                queue.append(node.left)
            # Добавляем правого потомка, если он есть
            if node.right:
                queue.append(node.right)
        # Все узлы текущего уровня обработаны – сохраняем их значения
        result.append(current_level)
    return result

# Сумма значений на каждом уровне
def level_sums(root):
    # Если дерево пустое – возвращаем пустой список
    if not root:
        return []

    sums = []  # здесь будут суммы по уровням
    queue = deque([root])  # очередь, начинаем с корня
    while queue:
        level_size = len(queue)  # сколько узлов на текущем уровне
        level_total = 0  # сумма для этого уровня, пока ноль

        for _ in range(level_size):
            node = queue.popleft()
            level_total += node.value  # добавляем значение узла к сумме уровня

            # Добавляем детей в очередь для следующего уровня
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        sums.append(level_total)  # сохранили сумму текущего уровня
    return sums

# Вспомогательные функции для создания тестовых деревьев
def build_sample_tree():
    # Строит дерево формы:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def build_symmetric_tree():
    # Симметричное дерево:
    #         10
    #        /  \
    #       5    15
    #      / \   / \
    #     2   7 12 20
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    return root

def build_left_skewed_tree():
    # Вырожденное дерево (левая цепочка):
    #         1
    #        /
    #       2
    #      /
    #     3
    #    /
    #   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root

# Демонстрация
if __name__ == "__main__":
    # Дерево 1: sample_tree
    tree1 = build_sample_tree()
    print("Дерево 1 (обычное):")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\   \\")
    print("    4   5   6\n")
    print("DFS обходы:")
    print(f"  preorder (прямой): {preorder(tree1)}")
    print(f"  inorder (симметричный): {inorder(tree1)}")
    print(f"  postorder (обратный): {postorder(tree1)}")
    levels1 = level_order(tree1)
    print("\nBFS обход (по уровням):")
    for i, level in enumerate(levels1, 1):
        print(f"  Уровень {i}: {level}")
    print("\nСуммы по уровням:", level_sums(tree1))

    # Дерево 2: symmetric_tree
    tree2 = build_symmetric_tree()
    print("\nДерево 2 (симметричное):")
    print("         10")
    print("        /  \\")
    print("       5    15")
    print("      / \\   / \\")
    print("     2   7 12 20\n")
    print("DFS обходы:")
    print(f"  preorder (прямой): {preorder(tree2)}")
    print(f"  inorder (симметричный): {inorder(tree2)}")
    print(f"  postorder (обратный): {postorder(tree2)}")
    levels2 = level_order(tree2)
    print("\nBFS обход (по уровням):")
    for i, level in enumerate(levels2, 1):
        print(f"  Уровень {i}: {level}")
    print("\nСуммы по уровням:", level_sums(tree2))

    # Дерево 3: left_skewed_tree
    tree3 = build_left_skewed_tree()
    print("\nДерево 3 (левая цепочка / вырожденное):")
    print("         1")
    print("        /")
    print("       2")
    print("      /")
    print("     3")
    print("    /")
    print("   4\n")
    print("DFS обходы:")
    print(f"  preorder (прямой): {preorder(tree3)}")
    print(f"  inorder (симметричный): {inorder(tree3)}")
    print(f"  postorder (обратный): {postorder(tree3)}")
    levels3 = level_order(tree3)
    print("\nBFS обход (по уровням):")
    for i, level in enumerate(levels3, 1):
        print(f"  Уровень {i}: {level}")
    print("\nСуммы по уровням:", level_sums(tree3))
    
