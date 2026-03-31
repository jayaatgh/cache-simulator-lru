class LRUCacheSimulator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.hits = 0
        self.misses = 0

    def access(self, block):
        if block in self.cache:
            self.hits += 1
            self.cache.remove(block)
            self.cache.append(block)
        else:
            self.misses += 1
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(block)

    def simulate(self, sequence):
        for block in sequence:
            self.access(block)

    def results(self):
        total = self.hits + self.misses
        hit_rate = self.hits / total if total else 0
        miss_rate = self.misses / total if total else 0

        return {
            "Total Accesses": total,
            "Hits": self.hits,
            "Misses": self.misses,
            "Hit Rate": round(hit_rate, 2),
            "Miss Rate": round(miss_rate, 2)
        }

if __name__ == "__main__":
    cache_size = 3
    access_sequence = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3]

    simulator = LRUCacheSimulator(cache_size)
    simulator.simulate(access_sequence)

    result = simulator.results()

    print("Cache Simulation Results:")
    for key, value in result.items():
        print(f"{key}: {value}")
