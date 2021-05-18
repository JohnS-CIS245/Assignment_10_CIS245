'''
John Savarese
Week 10
Assignment 10.1
CIS245-T302-T801
May 17, 2021


This week we will create a program that performs file processing activities.  
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.  
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.  
The program should then prompt the user for their name, address, and phone number.  
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 
Submit a link to your Github repository.
'''
import json #Import json
import os #Import os

def get_user_information(): #Function to take user information

    name = input ("\nPlease enter your full name (example : Jane Doe) : ")
    address = input ("\nPlease enter your address (example : 123 Barber Street) : ")
    city = input ("\nPlease enter your city name (example : Greentown) : ")
    state = input ("\nPlease enter your state (example : Idaho) : ")
    zipcode = input ("\nPlease enter your zip code (example : 74502) : ")
    phonenumber = input ("\nPlease enter your phone number (example : 555-555-5555) : ")

    personalinformation = [name, address, city, state, zipcode, phonenumber]
    return personalinformation #Return personalinformation csl

def get_directory_name(): #Function to take user input of directory and create it or check if it exists

    directoryinput = input ("\nPlease enter the directory that you would like to save your file to (example : C:\MyInformation) : ")
    try : #Try makes new folder if the folder does not exist
        os.mkdir(directoryinput)
        print (f"\nDirectory : {directoryinput} created...")
    except : #Except checks to see if folder exists
        print (f"\nOk, that directory already exists, let us continue...")
    return directoryinput #Return file directory

def get_file_name(directoryinput): #Function to take user input of file name and complete file path

    filename = input ("\nPlease enter a file name to save your information to (example : filename) : ")
    path_file = directoryinput + '/' + filename + ".json" #Create a full folder and file path to file

    try : #Try checks to see if file already exists
        with open (path_file) as f:
            filename = input ("\nThat file already exists, please enter a new file name to save your information to (example : filename) : ")
            path_file = directoryinput + '/' + filename + ".json"
    except FileNotFoundError: #Except continues if file does not already exist
        print (f"\nOk, your information will be saved as : {path_file}, let us continue...")
    
    return path_file #Returns full folder and file name

def write_file(personalinfo,path_file): #Function writes information to file

    with open (path_file, 'w') as f :
        json.dump(personalinfo, f)

def open_file(path_file): #Function opens file and returns information from file

    with open (path_file) as f :
        information = json.load(f)
        return information

def print_information_from_file (information,path_file): #Function prints output

    print ("\nThe information you provided to be saved is as follows : ")

    for info in information : #Print each item in list from file for user to see
        print (info.title())

    print (f"\nYour information has been stored in : {path_file}\n") #Lets the user know where it was stored

def main (): #Main function does all the calling and work

    directoryinput = get_directory_name() #Call get_directory_name and return directoryinput string
    path_file = get_file_name(directoryinput) #Call get_file_name, passing directoryinput and return path_file string
    personalinfo = get_user_information() #Call get_user_information and return personalinfo list
    write_file(personalinfo,path_file) #Call write_file, passing personalinfo and path_file, writes file
    information = open_file(path_file) #Call open_file, passing path_file and return information, opens file
    print_information_from_file(information,path_file) #Call print_information_from_file, passing information & path_file, prints output

main() #Call main for program to function as it was meant to







