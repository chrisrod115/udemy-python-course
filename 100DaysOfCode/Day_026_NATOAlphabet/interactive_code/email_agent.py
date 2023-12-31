import tkinter as tk
from tkinter import simpledialog


def send_rental_inquiry():
    """
    Creates a popup window for the user to enter various details for generating an inquiry email,
    and then saves the email content to a .txt file.

    """
    # Creating the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Popup dialog to enter the agent's name
    agent_name = simpledialog.askstring("Input", "Enter the real estate agent's name:", parent=root)

    # Popup dialog to enter the agent's email
    agent_email = simpledialog.askstring("Input", "Enter the real estate agent's email address:", parent=root)

    # Popup dialog to enter the property address
    property_address = simpledialog.askstring("Input", "Enter the address of the property you are interested in:",
                                              parent=root)

    # Popup dialog to enter your name
    your_name = simpledialog.askstring("Input", "Enter your name:", parent=root)

    # Check if all inputs were given
    if agent_email and property_address and agent_name and your_name:
        # Email subject
        email_subject = f"Inquiry about Rental Property at {property_address} with Union Station PSH Program"

        # Email body
        email_body = f"""
        Dear {agent_name},

        I hope this message finds you well. I am writing to express my interest in renting the property located at {property_address}, which I found through your listing.

        I would like to inform you that I am pre-approved for the Union Station Permanent Supportive Housing (PSH) program, with an available amount of $3,200. This program is designed to assist individuals in securing stable housing, and I believe it would be an excellent fit for my needs.

        Could you please let me know if this property is available for rent under the Union Station PSH program? I am very enthusiastic about the opportunity to rent this property and would be grateful for your assistance in this matter.

        Thank you for considering my inquiry. I look forward to the possibility of renting this property and appreciate your time and assistance.

        Best regards,

        {your_name}
        """

        # Saving the email content to a file
        with open("rental_inquiry.txt", "w") as file:
            file.write(f"Email Subject: {email_subject}\n")
            file.write("Email Body:\n")
            file.write(email_body)

        return "Email content saved to rental_inquiry.txt"
    else:
        return "No input provided."


# Call the function and display the result
result = send_rental_inquiry()
print(result)

