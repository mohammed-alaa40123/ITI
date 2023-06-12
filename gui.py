import tkinter as tk
from tkinter import ttk
from tsp import TSPSolver

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TSP Solver")

        self.text_input = tk.Text(self.root, height=10, width=50)
        self.text_input.pack(padx=10, pady=10)

        self.show_graph_button = tk.Button(self.root, text="Show Graph", command=self.show_graph)
        self.show_graph_button.pack(padx=10, pady=5)

        self.selection_method_label = tk.Label(self.root, text="Selection Method:")
        self.selection_method_label.pack(padx=10, pady=5)
        self.selection_method = ttk.Combobox(self.root, values=["Ranking", "Tournament"])
        self.selection_method.current(0)
        self.selection_method.pack(padx=10, pady=5)

        self.population_size_label = tk.Label(self.root, text="Population Size:")
        self.population_size_label.pack(padx=10, pady=5)
        self.population_size = tk.Entry(self.root)
        self.population_size.pack(padx=10, pady=5)

        self.crossover_rate_label = tk.Label(self.root, text="Crossover Rate:")
        self.crossover_rate_label.pack(padx=10, pady=5)
        self.crossover_rate = tk.Entry(self.root)
        self.crossover_rate.pack(padx=10, pady=5)

        self.mutation_rate_label = tk.Label(self.root, text="Mutation Rate:")
        self.mutation_rate_label.pack(padx=10, pady=5)
        self.mutation_rate = tk.Entry(self.root)
        self.mutation_rate.pack(padx=10, pady=5)

        self.elitism_rate_label = tk.Label(self.root, text="Elitism Rate:")
        self.elitism_rate_label.pack(padx=10, pady=5)
        self.elitism_rate = tk.Entry(self.root)
        self.elitism_rate.pack(padx=10, pady=5)

        self.stopping_criteria_label = tk.Label(self.root, text="Stopping Criteria:")
        self.stopping_criteria_label.pack(padx=10, pady=5)
        self.stopping_criteria = ttk.Combobox(self.root, values=["Saturation", "After Generation"])
        self.stopping_criteria.current(0)
        self.stopping_criteria.pack(padx=10, pady=5)

        self.after_generation_label = tk.Label(self.root, text="After Generation:")
        self.after_generation_label.pack(padx=10, pady=5)
        self.after_generation_input = tk.Entry(self.root)
        self.after_generation_input.pack(padx=10, pady=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.run)
        self.run_button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_graph(self):
        solver = TSPSolver(self.root)
        solver.show_graph(self.text_input)

    def run(self):
        solver = TSPSolver(self.root)
        solver.population_size = int(self.population_size.get())
        solver.crossover_rate = float(self.crossover_rate.get())
        solver.mutation_rate = float(self.mutation_rate.get())
        solver.elitism_rate = float(self.elitism_rate.get())
        solver.stopping_criteria.set(self.stopping_criteria.get())
        solver.after_generation_input = self.after_generation_input
        solver.selection_method.set(self.selection_method.get())
        solver.show_result(self.text_input)