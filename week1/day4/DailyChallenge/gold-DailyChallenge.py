import random

class Gene:
    def __init__(self,gene):
        self.gene = gene
    def mutate(self):
        if self.gene == 0:
            self.gene = 1
        else:
            self.gene = 0

    def __str__(self):
        return str(self.gene)
    
class Chromosome:
    def __init__(self):
        self.genes = [Gene(random.randint(0, 1)) for _ in range(2)]
    
    def mutate (self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def __str__(self):
        return "".join([str(gene) for gene in self.genes])
            
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome()]
    
    def mutate (self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_perfect(self):
        # Exemple de logique pour la vérification
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.gene != 1:
                    return False
        return True

    def __str__(self):
        return "\n".join([str(chromosome) for chromosome in self.chromosomes])


class Organism:
    def __init__(self,DNA_instance,probability):
        self.dna = DNA_instance
        self.probability = probability
        self.generation = 0

    def update(self):
        while not self.dna.is_perfect():
            if random.random() < self.probability:
                self.dna.mutate()
            self.generation += 1

            if self.generation % 1000 == 0:
                print(f"Génération {self.generation}...")

        return self.generation
    

    
   
    

# Test 
mon_adn = DNA()
print("--- AVANT MUTATION ---")
print(mon_adn)

mon_adn.mutate()

print("\n--- APRÈS MUTATION ---")
print(mon_adn)

organism = Organism(mon_adn,0.05)

print(f"le nombre de génération est {organism.update()}")
