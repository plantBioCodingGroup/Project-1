# Jeremy Pardo 03/04/2019
# Make a rabbit move around a field
import numpy as np
import matplotlib.pyplot as plt
import datetime
import argparse

# function to create an empty field
def getField(max_x, max_y):
    field = [[0] * max_y for _ in range(max_x)]
    return (field)

# class rabbit
# rabbits have a starting position and implement methods to get their position and move
class rabbit:
    # rabbit constructor
    def __init__(self, grid_x, grid_y):
        self.x_position = np.random.randint(0, grid_x)
        self.y_position = np.random.randint(0, grid_y)
        self.pos_his = [self.getPosition()]
    # get the rabbit's current position
    def getPosition(self):
        X_pos = self.x_position
        Y_pos = self.y_position
        pos = [X_pos, Y_pos]
        return (pos)
    # move the rabbit around the field. Can only move one square at a time
    def moveRabbit(self, field, tries=0):
        print("The rabbit is at {0}".format(self.getPosition()))
        field[(self.getPosition()[0])][(self.getPosition()[1])] = 0
        check = False
        while (check == False) and (tries < 100):
            newPos_y = np.random.randint(-1, 2)
            newPos_x = np.random.randint(-1, 2)
            if (((self.getPosition()[0] + newPos_x) >= 0) and ((self.getPosition()[0] + newPos_x) < (len(field) ))):
                if (((self.getPosition()[1] + newPos_y) >= 0) and (
                        (self.getPosition()[1] + newPos_y) < (len(field[0])))):
                    field[(self.getPosition()[0] + newPos_x)][(self.getPosition()[1] + newPos_y)] = 1
                    self.x_position = (self.getPosition()[0] + newPos_x)
                    self.y_position = (self.getPosition()[1] + newPos_y)
                    print("The rabbit moved to {0}".format(self.getPosition()))
                    self.pos_his.append(self.getPosition())
                    check = True
                else:
                    check = False
                    tries += 1
            else:
                check = False
                tries += 1

        if check == False:
            print("The rabbit tried to leave the field too many times!"+"\n"+"We suggest training your rabbit better next time."+"\n"+"The program will now exit. Goodbye!")
            exit(1)
        return(field)

# make a rabbit and move it around the field for a defined number of times
def rabbitWander(field_X, field_Y,iter):
    my_field = getField(field_X, field_Y)
    my_rabbit = rabbit(field_X, field_Y)
    my_field[(my_rabbit.getPosition()[0])][(my_rabbit.getPosition()[1])] = 1
    for i in range(iter):
        my_rabbit.moveRabbit(my_field)
    rabbitTrack = my_rabbit.pos_his
    return(np.array(rabbitTrack))
# plot the rabbit's movements
def plotRabbitTrack(field_X,field_Y,iter):
    rabbitTrack = rabbitWander(field_X,field_Y,iter)
    rabbit_X = rabbitTrack[:,0]
    rabbit_Y = rabbitTrack[:,1]
    fig = plt.figure()
    plt.xlim(0,field_X)
    plt.ylim(0,field_Y)
    plt.scatter(rabbit_X[0],rabbit_Y[0],c='green')
    plt.plot(rabbit_X,rabbit_Y,c='orange',linewidth=0.5)
    plt.scatter(rabbit_X,rabbit_Y,c="black",s=0.5)
    plt.scatter(rabbit_X[len(rabbit_X)-1],rabbit_Y[len(rabbit_Y)-1],c='brown')

    fig.savefig("rabbitTrack.pdf",bbox_inches='tight')
# main method
def main():
    start = datetime.datetime.now()
    # command line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-x","--x_cord",help="x coordinate for field",default=30)
    parser.add_argument("-y","--y_cord",help="y coordinate for field",default=30)
    parser.add_argument("-i","--iterations",help="number of iterations",default=500)
    args = parser.parse_args()
    x_cordinate = args.x_cord
    y_cordinate = args.y_cord
    iter = args.iterations

    plotRabbitTrack(x_cordinate,y_cordinate,iter)
    print("Finished in {0} seconds".format(datetime.datetime.now()-start))

# run the rabbit moving program
if __name__ == "__main__":
    main()
