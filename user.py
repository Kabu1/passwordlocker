class User:
    """
    Class that creates user accounts and their details.
    """
    user_list = [] #empty contact list
    def __init__(self, first_name, last_name, password):
        """
        Defining the properties of our objects
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
        '''
        Function to save a newly created user instance

        '''
        User.user_list.append(self)
