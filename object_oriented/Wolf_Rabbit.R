
#Wolf Chase Rabbit Coding Club 
#Original Code comes from https://allthiswasfield.blogspot.com/2018/05/simulating-animal-movements-and-habitat.html


library (raster)  
library (dismo)  

tc <- raster(nrows=100, ncols=100, xmn=0, xmx=100, ymn=0,ymx=100)  
tc[] <- runif(10000, -80, 180)  
tc <- focal(tc, w=matrix(1, 5, 5), mean)  
tc <- focal(tc, w=matrix(1, 5, 5), mean)  
plot(tc) 



species <- setClass("species", slots=c(x="numeric", y="numeric", opt="numeric")) 
Rabbit <- species(x= 30, y =30, opt= 80)  
Wolf <- species(x= 40, y =40, opt= 80)

path <- go (sp, env, n, sigma, theta_x, alpha_x, theta_y, alpha_y)

go <- function (sp, env, n, sigma, theta_x, alpha_x, theta_y, alpha_y) {  
  track <- data.frame()  
  track[1,1] <- sp@x  
  track[1,2] <- sp@y  
  for (step in 2:n) {  
    neig <- adjacent(env,   
                     cellFromXY(env, matrix(c(track[step-1,1],  
                                              track[step-1,2]), 1,2)),   
                     directions=8, pairs=FALSE )  
    options <- data.frame()  
    for (i in 1:length(neig)){  
      options[i,1]<-neig[i]  
      options[i,2]<- sp@opt - env[neig[i]]  
    }  
    option <- c(options[abs(na.omit(options$V2)) == min(abs(na.omit(options$V2))), 1 ],   
                options[abs(na.omit(options$V2)) == min(abs(na.omit(options$V2))), 1 ])  
    new_cell <- sample(option,1)  
    new_coords <- xyFromCell(env,new_cell)  
    lon_candidate<--9999  
    lat_candidate<--9999  
    
    while ( is.na(extract(env, matrix(c(lon_candidate,lat_candidate),1,2)))) {  
      lon_candidate <- new_coords[1]+ (sigma * rnorm(1)) + (alpha_x * ( theta_x - new_coords[1]))  
      lat_candidate <- new_coords[2]+ (sigma * rnorm(1)) + (alpha_y * ( theta_y - new_coords[2]))  
    }  
    track[step,1] <- lon_candidate  
    track[step,2] <- lat_candidate  
  }  
  return(track)  
}  

Rabbit_Sim <- go (Rabbit, tc, 100, 2, 90, 0, 90, 0)  
Wolf_Sim <- go (Wolf, tc, 100, 2, 90, 0, 90, 0)  
plot(tc, main = "Wolf and Rabbit Movement in Habitat", xlab = "Horizontal Distance", ylab = "Vertical Distance")  
lines(Rabbit_Sim, lwd=1.5, col="red")  
points(Rabbit_Sim, cex=0.3, col="red")  
lines(Wolf_Sim, lwd=1.5, col="blue")  
points(Wolf_Sim, cex=0.3, col="blue")  
legend("topleft", legend=c("Rabbit","Wolf"), col=c("red","blue"),  
       lty=c(1,1), lwd=c(2,2)) 


