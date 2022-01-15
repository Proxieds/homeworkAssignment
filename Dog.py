from Cat import Cat


class Dog(Cat):
    """
    Dog object definition
    """

    def __init__(self, *args, **kwargs):
        # Calls parent class __init__ method
        super(Dog, self).__init__(*args, **kwargs)

    def speak(self, optionalMessage=None):
        """
        Overrides the default speak implementation from parent class, prints "woof" as default message if no optional one is supplied  
            Prints optional message or "woof" to stdout if it does not exist, also increments age by 1 after speaking five times
        """
        print(optionalMessage if optionalMessage else "woof")
        self.setNumberOfSpeaks(self.getNumberOfSpeaks() + 1)
        # Increments age by 1 every time the number of speaks is divisible evenly by 5
        if self.getNumberOfSpeaks() % 5 is 0:
            self.setAge(self.getAge() + 1)
