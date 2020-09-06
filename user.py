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
    @classmethod
    def check_user(cls,first_name, password):
        '''
        Method that check if users name and password matches
        '''
        current_user = ''
        for user in User.user_list:
            if (user.first_name  == first_name and user.password == password):
                current_user == user.first_name
        return current_user
  