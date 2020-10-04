import numpy as np

class grid_point:
    def __init__(self,x,y):
        super().__init__()
        status='point'
        self.x=x
        self.y=y
        self.mindistance=None
        self.end_dist=0


class grid:
    def __init__(self, sizeX,sizeY, startpoint, endpoint):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.startpointx=startpoint[0]
        
        self.startpointy=startpoint[1]

        self.endpointx=endpoint[0]
        self.endpointy=endpoint[1]

        self.board=np.full((self.dim,self.dim))

    def makeBoard(self):
        for i in range(sizeX):
            for j in range(sizeY):
                self.board[i][j]=grid_point(i,j)

    def distance(self, point1,point2):
        dist=point1.distance
        newdistX=point1[0]-point2[0]
        newdistY=point1[1]-point2[1]
        newdist=np.sqrt(newdistX**2+newdistY**2)
        return newdist


    def check_neighbour(self,point1,point2):
        if point2.status=='point':
            point2.status='rim'
            point2.distance=distance(point1, point2)
        if point2.status=='rim':
            d=distance(point1,point2)
            if d<point2.distance:
                point2.distance=d

    
    def closest_points(self, point):
        for i in range(-1,1):
            for j in range(-1,1):
               if self.board[point[0]+i][point[1]+j] in self.board:
                   if self.board[point[0]+i][point[1]+j]=='point' or 'rim':
                      check_neighbour([point[0],point[1]],[point[0]+i,point[1]+j])

   
    
    
        