class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.count += 1

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix, limit=10):
        node = self._find_node(prefix)
        if not node:
            return []
        
        results = []
        self._collect(node, prefix, results, limit)
        return results

    def _collect(self, node, prefix, results, limit):
        if len(results) >= limit:
            return
        if node.is_end:
            results.append(prefix)
        
        for char, child in node.children.items():
            self._collect(child, prefix + char, results, limit)

    def count_words_with_prefix(self, prefix):
        node = self._find_node(prefix)
        if not node:
            return 0
        return self._count(node)

    def _count(self, node):
        total = 1 if node.is_end else 0
        for child in node.children.values():
            total += self._count(child)
        return total

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char], word, depth + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            
            return False
        
        return _delete(self.root, word, 0)

if __name__ == "__main__":
    trie = Trie()
    
    for word in ["apple", "app", "application", "apply", "banana", "band"]:
        trie.insert(word)
