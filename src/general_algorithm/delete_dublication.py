class delete_dublication:
    elements = []
    epsilon = 10**-4
    def add_element(self,element):
        no_dublicate = True
        for i in range(len(self.elements)):
            if(abs(element-self.elements[i]) < self.epsilon):
                no_dublicate = False
                break
        if no_dublicate:
            self.elements.append(element)
    def get_elements(self):
        return self.elements
    def set_epsilon(self,epsilon):
        self.epsilon = epsilon