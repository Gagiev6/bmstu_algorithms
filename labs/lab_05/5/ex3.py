import hashlib
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()  # Вычисляем хеш блока

    def compute_hash(self):
        block_string = f"{self.index}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()  # Хешируем строку и возвращаем результат

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Начинаем цепочку с генезис-блока

    def create_genesis_block(self):
        return Block(0, "Block", "0")  # Создаем первый блок с индексом 0

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)  # Создаем новый блок
        self.chain.append(new_block)  # Добавляем блок в цепочку

# Пример использования блокчейна
if __name__ == "__main__":
    # Создаем экземпляр блокчейна
    my_blockchain = Blockchain()

    # Добавляем несколько блоков в блокчейн
    my_blockchain.add_block("Второй блок")
    my_blockchain.add_block("Третий блок")
    my_blockchain.add_block("Четвертый блок")

    # Выводим информацию о каждом блоке в цепочке
    for block in my_blockchain.chain:
        print(f"Блок #{block.index} | Хеш: {block.hash} | Данные: {block.data} | Предыдущий хеш: {block.previous_hash}")