class Environment:
    def __init__(self):
        self.grid = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        self.check = [
            ['safe', 'safe', 'fire'],
            ['safe', 'fire', 'safe'],
            ['safe', 'safe', 'fire']
        ]
        
    def display(self):
        print("Grid:")
        for row in self.grid:
            print(row)
        print("\nCheck:")
        for row in self.check:
            print(row)


class Agent(Environment):
    def __init__(self):
        pass
    
    def update(self, env1, env2):
        for i in range(len(env1)):
            for j in range(len(env1[i])):
                if env2[i][j] == 'fire':
                    env2[i][j] = 'safe'
                env1[i][j] = 'x'


env = Environment()
agent = Agent()

print("Initial State:")
env.display()

agent.update(env.grid, env.check)

print("\nUpdated State:")
env.display()
