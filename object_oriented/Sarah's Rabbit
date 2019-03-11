#Modeling Rabbit Movement

#Random Brownian Movement: Brownian motion or pedesis is the random motion of particles suspended in a fluid resulting from their collision with the fast-moving molecules in the fluid.
#Original Code comes from https://allthiswasfield.blogspot.com/2016/11/ewolk-r-function-to-simulate-two.html

eWalk <- function(sigma,lon,lat, generations,alpha_x,theta_x,alpha_y,theta_y, color,levy=FALSE, plot=TRUE) {
  #Making the function that will represent the random motion.
  route=data.frame(1:generations,1:generations)                             # a data.frame to store the route
  names(route)<-c("lon","lat")
  generation= generations                                               # generation counter
  
  while (generation > 0){                                                   # stops the simulation when generation counter is 0
    if (levy == TRUE){                                                      # only if levy=TRUE: Levy Flight!
      rndm=abs(rcauchy(1))                                                  # process to select if I should jump or not
      if (rndm > 15){                                                       # Levy jump probability threshold
        l=15                                                                # length of the jump
        x= lon + (l * (sigma * rnorm(1))) + (alpha_x * ( theta_x - lon))    # Brownian or OU process for longitude
        y= lat + (l * (sigma * rnorm(1))) + (alpha_y * ( theta_y - lat))    # Brownian or OU process for latitude
        loc=cbind(x,y)
        route[generation,]<- loc                                            # store new location
        generation= generation - 1                                        # advance to next generation
        lon<- x                                                        # go to the new position!
        lat<- y
        
      }
      else{                                                                 # if Levy jump is not selected, l=1 i.e. proceed with  
        l=1                                                                 #normal Brownian motion or OU process
        x= lon + (l * (sigma * rnorm(1))) + (alpha_x * ( theta_x - lon))
        y= lat + (l * (sigma * rnorm(1))) + (alpha_y * ( theta_y - lat))
        loc=cbind(x,y)
        route[generation,]<- loc
        generation= generation - 1  
        lon<- x      
        lat<- y
      }
    }
    else{                                                                   # if levy=FALSE, l=1, only Brownian motion or OU
      l=1
      x= lon + (l * (sigma * rnorm(1))) + (alpha_x * ( theta_x - lon))
      y= lat + (l * (sigma * rnorm(1))) + (alpha_y * ( theta_y - lat))
      loc=cbind(x,y)
      route[generation,]<- loc
      generation= generation - 1  
      lon<- x      
      lat<- y
    }
  }
  
  if (plot == TRUE) {                                                       # if plot=TRUE, plto the route!
    lines(route, col= color, lwd=3)  
  }
  return(route)                                                             # print the data.frame with each location during the walk!
  
}

#Original
#par(mfrow=c(2,2))

#a=eWalk(0.15,0,0,1000, 0, 0, 0, 0, color="blue", levy=FALSE, plot=FALSE)
#plot(a,type="n", main="Brownian motion")
#lines(a,lwd=3, col="blue")
#points(a, cex=.3, col="black", pch=21)



#Altered
par(mfrow=c(2,2))  #Just a way to place multiple graphs in the same area.

a=eWalk(0.15,0,0,100, 0, 0, 0, 0, color="blue", levy=FALSE, plot=FALSE)
plot(a,type="n", main="Rabbit Path", xlab = "Horizontal Distance", ylab = "Verticle Distance")
lines(a,lwd=3, col="blue")
