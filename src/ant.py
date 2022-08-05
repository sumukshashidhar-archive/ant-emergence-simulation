"""
This is a simple model of what an ant is, and how it behaves.
"""
import utility_functions as uf

class Ant:

    def __init__(self, type, memory = 20):
        """
        Initialize an ant.

        Args:
            type: The type of ant. (0 = worker, 1 = forager, 2 = soldier, 3 = scout, 4 = caretaker)
        """
        self.type = type
        self.memory = [] # The memory of the ant.
        self.memory_threshold = memory # The memory threshold of the ant.
        # the change threshold is the original percentage of all the types of ants
        # if any ant is below the 20% mark in this case, we can change the type of the ant
        self.change_threshold = 0.2 
        self.history = [] # The history of the ant.
    
    def interact_with_ant(self, ant):
        """
        Interact with another ant.

        Args:
            ant: The ant to interact with.
        """
        # just get the ant's type, and add it to the memory
        self.memory.append(ant.get_type())
        # run the adapt function
        self.adapt()
        pass

    def adapt(self):
        """
        The ant looks at it's memory, and determines which of the types it should be.
        """
        # first check if the ant has met enough ants to meet the memory threshold
        if len(self.memory) >= self.memory_threshold:
            # now we can do something
            # first we need to find the counts of each type
            counts = uf.get_counts(self.memory)
            sums = 0
            for key in counts:
                sums += counts[key]
            # now we can find the percentage of each type
            for key in counts:
                if counts[key] / sums > self.change_threshold:
                    # we found the type that we need to change it to
                    self.history.append(
                        (self.type, key) # what type we were, what type we are
                    )
                    self.type = key
            self.memory = [] # blank out the memory
                    
    
    def get_type(self):
        """
        Return the type of ant.

        Returns:
            The type of ant.
        """
        return self.type

    def __str__(self):
        """
        Return a string representation of the ant.

        Returns:
            A string representation of the ant.
        """
        return "Ant: " + str(self.type)
