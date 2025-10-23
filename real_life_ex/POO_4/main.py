# Music festival and ticketing system

# Scenario:

# You are building a management system for a local music festival with concerts, tickets, food stalls, and merchandise.

# Requirements / Tasks:

# User Registration

# Store users in dictionary {email: {name, tickets_bought, spending}}.

# Concerts

# Store concerts in dictionary {concert_name: {available_seats, price}}.

# Users can book tickets (reduce seats).

# Food & Merch

# Menu stored in dictionary {item: price}.

# Users can order multiple items.

# Discounts

# Festival pass = 20% off all purchases.

# Reports

# Most popular concert.

# Top 5 spenders.

# Total food/merch sales.

# Advanced

# Use sets to track unique attendees per concert.

# Recommend concerts: “People who attended X also attended Y”.

# Prevent double-booking of the same user for the same concert.

class Registration:
    def __init__(self, name, email, tickets_bought=False, spending=0):
        self.name = name
        self.email = email
        self.tickets_bought = tickets_bought
        self.spending = spending

    def user_registration(self):
        if not self.tickets_bought:
            self.tickets_bought = True
            user_info = {
                'name': self.name,
                'email': self.email,
                'spending': self.spending,
                'tickets_bought': self.tickets_bought
            }
            return user_info
        else:
            print(f"{self.name} has already been registered.")
