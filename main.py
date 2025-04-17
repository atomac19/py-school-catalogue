class School:
  # Define properties of School class: name, level and number of students
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    if level in ['primary', 'middle', 'high']:
      self.level = level
    else:
      raise ValueError("Level of School must be: primary, middle or high")
    if isinstance(numberOfStudents, int) and numberOfStudents > 0:
      self.numberOfStudents = numberOfStudents
    else:
      raise ValueError("Number of students must be a positive integer")
  # Create getters for all properties
  def get_name(self):
      print(self.name)
  def get_level(self):
      print(self.level)
  def get_numberOfStudents(self):
      print(self.numberOfStudents)
  # Create setters for numberOfStudents
  def set_numberOfStudents(self, number):
      self.numberOfStudents = number
  # Create methods that display info about the school
  def __repr__(self):
      return "{} is {} level school with {} students.".format(self.name, self.level, self.numberOfStudents)

# Class representing primary schools, inheriting from School class
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " Note: The pickup policy is {pickupPolicy}.".format(pickupPolicy = self.pickupPolicy)
# Create class for Middle Schools
class Middle(School):
   def __init__(self, name, numberOfStudents):
    super().__init__(name, 'middle', numberOfStudents)
# Create class for High Schools
class High(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

    # getter for sportsTeams array. return the list of the sports teams
  def getSportsTeams(self):
      return self.sportsTeams
    # override the repr method to display info about sportsTeams
  def __repr__(self):
      parentRepr = super().__repr__()
      return parentRepr + " {} have sports teams in: {}.".format(self.name, self.sportsTeams)

