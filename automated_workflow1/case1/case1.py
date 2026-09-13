import time
from queue import Queue

# class of request
class Demand:
  def __init__(self, id_demand, description):
      self.id = id_demand
      self.description = description
      self.status = "Waiting...!"

  def treat(self):
      print(f"\nTraitement of the Request {self.id} : {self.description}")
      time.sleep(1) #Simulation of time of treatement
      self.status="___traited"
      print(f"\n*****The request {self.id} is treated successfully...!")

#----Automated Workflow

class WorkflowAuto:
    def __init__(self):
        self.myQueue = Queue()

    def add_demand(self, demand):
        print(f"Added Request {demand.id} to the Queue..")
        self.myQueue.put(demand)

    def exec_demand(self):
        while not self.myQueue.empty():
            demand = self.myQueue.get()
            demand.treat()
            self.notifier(demand)

    def notifier(self, demand):
        print(f"\n******Notification: the Request {demand.id} is now '{demand.status}'***")

#---Example
if __name__ == "__main__":
    workflow = WorkflowAuto()
    #Adding
    workflow.add_demand(Demand(1,"Creating a client account..."))
    workflow.add_demand(Demand(2,"Resseting a client password..."))
    workflow.add_demand(Demand(3,"Updating cordinates..."))

    #Executing
    workflow.exec_demand()
