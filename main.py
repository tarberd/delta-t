import matplotlib.pyplot as plt

class wallet:
    def __init__(self):
        self.instant = 0
        self.time = [0]
        self.money = [0]
        self.instant_vel = [0]
        self.instant_acc = [0]
    
    def delta_money(self, delta):
        self.time.append(self.time[ self.instant ] + 1)
        self.money.append(self.money[ self.instant ] + delta)
        self.instant_vel.append(delta)
        delta_v = self.instant_vel[ self.instant + 1] - self.instant_vel[ self.instant ]
        self.instant_acc.append( delta_v )
        self.instant = self.instant + 1

    def apply_acc(self, acc):
        self.time.append(self.time[ self.instant ] + 1)
        self.instant_acc.append( acc )
        self.instant_vel.append( self.instant_vel[self.instant] + acc )
        self.money.append( self.money[self.instant] + self.instant_vel[self.instant] + acc)
        self.instant = self.instant + 1

    def apply_acc_no_inertia(self, acc):
        self.time.append(self.time[ self.instant ] + 1)
        self.instant_acc.append( acc )
        self.instant_vel.append( acc )
        self.money.append( self.money[self.instant] + self.instant_vel[self.instant] + acc)
        self.instant = self.instant + 1

    def print_instant(self, instant):
        print("time at " + str(instant) + ": "  + str(self.time[instant]))
        print("money at " + str(instant) + ": "  + str(self.money[instant]))
        print("instant_vel at " + str(instant) + ": "  + str(self.instant_vel[instant]))
        print("instant_acc at " + str(instant) + ": "  + str(self.instant_acc[instant]))
        

w = wallet()

input_size = int(input())
for i in range(input_size):
    w.apply_acc_no_inertia(int(input()))
    w.print_instant(w.instant)

plt.plot(w.time, w.money, label = "money")
 
plt.plot(w.time, w.instant_vel, label = "velocity")

plt.plot(w.time, w.instant_acc, label = "acceleration")

plt.xlabel('time')
# naming the y axis
plt.ylabel('stuff')
# giving a title to my graph
plt.title('My wallet')

plt.legend()

plt.show()
