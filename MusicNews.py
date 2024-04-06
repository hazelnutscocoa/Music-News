"""
KIT101 3.2PP Latest Music News
"""

__author__ = "Roshani Ghimire"
import math

def main():
    
    band: str # Band name
    track_name: str # Track name
    release_day: str # Day of the week the track was released
    service_a: str #name of the first streaming servie
    play_count_a:int #number of times the track has been played on the first streaming service
    service_b:str #name of the second streaming service
    play_count_b:int #number of times the track has been played on the second streaming service
    city: str#name of the city the band will be performing in next
    total_plays: int #total number of plays across both streaming service
    x=int 
    
 


    print("Welcome to Latest Music News")


    band        = input("Enter the name of the band: ")
    track_name  = input("Enter the name of their latest track: ")
    release_day = input("Enter the day of the week the track was released: ")
    service_a   = input("Enter the first streaming service name: ")
    play_count_a= int(input("Enter the play count on the fist streaming service: "))
    service_b   = input("Enter the second streaming service name: ")
    play_count_b= int(input("Enter the play count on the second streaming service: "))
    city        = input("Enter the name of the city the band will play in: ")
     
     #addition function to add total play counts on two platform  
    total_plays =  play_count_a + play_count_b
    
    
    
    #print statement 
    print(f"{band}'s latest track,{track_name}, has been well received by fans.\nReleased on {release_day}, the track has been played {play_count_a} times on {service_a} and {play_count_b} times on {service_b} for a total of {total_plays} play to date.\n{band} will play the track live for the first time in {city} next month.")
    
    


if __name__ == "__main__":
     main()