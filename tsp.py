import tkinter as tk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from individual import Individual
class TSPSolver:
    def __init__(self, gui):
        self.gui = gui
        self.population_size = 100
        self.crossover_rate = 0.8
        self.mutation_rate = 0.1
        self.elitism_rate = 0.1
        self.stopping_criteria = tk.StringVar(value="saturation")
        self.after_generation_input = None
        self.selection_method = tk.StringVar(value="ranking")
        self.points = []
    
    def show_graph(self,text_input):
        edges = []
        weights = []
        input_str = text_input.get("1.0", "end-1c")  # Access the text_input attribute of the gui instance
        lines = input_str.split("\n")
        for line in lines:
            if line:
                x, y, w = line.split(",")
                edges.append((int(x), int(y)))
                weights.append(int(w))
        G = nx.Graph()
        G.add_weighted_edges_from([(edges[i][0], edges[i][1], weights[i]) for i in range(len(edges))])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def init_map(self,text_input):
        input_str = text_input.get("1.0", "end-1c")
        lines = input_str.split("\n")
        for line in lines:
            if line:
                x, y, w = line.split(",")
                self.points.append((int(x), int(y)))

    def init_pop(self):
        self.population = [Individual(self.points) for i in range(self.population_size)]

    def selection(self):
        if self.selection_method.get() == "ranking":
            self.population.sort(key=lambda x: x.score())
            ranks = np.arange(self.population_size) + 1
            probabilities = ranks / np.sum(ranks)
            return np.random.choice(self.population, size=2, replace=False, p=probabilities)
        elif self.selection_method.get() == "tournament":
            tournament_size = 3
            tournament = np.random.choice(self.population, size=tournament_size, replace=False)
            return tournament[np.argmin([t.score() for t in tournament])]

    def crossover(self, parent1, parent2):
        if np.random.rand() > self.crossover_rate:
            return parent1
        crossover_point = np.random.randint(1, len(parent1))
        child = parent1[:crossover_point]
        for i in range(len(parent2)):
            if parent2[i] not in child:
                child.append(parent2[i])
        return Individual(self.points, order=child)

    def mutation(self, child):
        if np.random.rand() > self.mutation_rate:
            return child
        mutation_point1, mutation_point2 = np.random.randint(0, len(child), 2)
        child.order[mutation_point1], child.order[mutation_point2] = child.order[mutation_point2], child.order[mutation_point1]
        return child

    def evolve(self):
        elite_size = int(self.elitism_rate * self.population_size)
        new_population = []
        if elite_size > 0:
            new_population.extend(sorted(self.population, key=lambda x: x.score())[:elite_size])
        while len(new_population) < self.population_size:
            parent1 = self.selection()
            parent2 = self.selection()
            child = self.crossover(parent1, parent2)
            child = self.mutation(child)
            new_population.append(child)
        self.population = new_population

    def show_result(self,text_input):
        self.init_map(text_input)
        self.init_pop()

        num_generations = 100
        if self.stopping_criteria.get() == "Saturation":
            best_score = float("inf")
            for generation in range(num_generations):
                self.evolve()
                score = self.population[0].score()
                if score < best_score:
                    best_score = score
                    best_order = self.population[0].order
            self.plot_result(best_order)
        elif self.stopping_criteria.get() == "After Generation":
            for generation in range(int(self.after_generation_input.get())):
                self.evolve()
            self.plot_result(self.population[0].order)

    def plot_result(self, order):
        x = [self.points[i][0] for i in order]
        y = [self.points[i][1] for i in order]
        plt.plot(x, y, 'ro-')
        plt.show()