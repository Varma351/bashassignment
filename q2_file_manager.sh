#!/bin/bash

#using loop statements to run this infinitely until manually terminated 
while true
do
    echo "-----------FILE MANAGEMENT SYSTEM----------------"
    echo "1. Create a file"
    echo "2. Display file content"
    echo "3. Copy a file"
    echo "4. Move a file"
    echo "5. Delete a file"
    echo "6. Exit"
    echo "---------------------------------------------------"

    
    read -p "Enter your choice: " choice
    #this line is used to take the user input based on this choice a associated task is run 

    case $choice in

        1)
            # files are created using touch command 
            read -p "Enter file name to create: " file

            # Check if file already exists
            if [ -e "$file" ]; then
                echo "File already exists."
            else
                touch "$file"
                echo "File created successfully."
            fi
            ;;

        2)
            # cat is used to display the contents of file 
            read -p "Enter file name to display: " file

            if [ -e "$file" ]; then
                echo "----- File Content -----"
                cat "$file"
                echo "------------------------"
            else
                echo "File not found."
            fi
            ;;

        3)
            # files are copied using cp command
            read -p "Enter source file: " src
            read -p "Enter destination file: " dest

            if [ -e "$src" ]; then
                cp "$src" "$dest"
                echo "File copied successfully."
            else
                echo "Source file not found."
            fi
            ;;

        4)
            # Move/rename file are done mv command
            read -p "Enter file to move: " src
            read -p "Enter destination path/new name: " dest

            if [ -e "$src" ]; then
                mv "$src" "$dest"
                echo "File moved successfully."
            else
                echo "File not found."
            fi
            ;;

        5)
            # rm command is used to delete the files 
            read -p "Enter file to delete: " file

            if [ -e "$file" ]; then
                rm -i "$file"   # -i is used inorder to confirm the deletion of file for safety concerns 
                echo "Delete operation finished."
            else
                echo "File not found."
            fi
            ;;

        6)
            echo "Exiting File Management System..."
            break
            ;;

        *)
            echo "Invalid choice. Try again."
            ;;
    esac
done