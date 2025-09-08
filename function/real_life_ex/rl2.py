# smart fitness a gym tracker
# Scenario:

# You are building a gym membership and workout tracking system. Members can register, book classes, log workouts, and track progress.

# Requirements / Tasks:

# User Registration

# Each user has: name, age, membership_type, workouts_logged.

# Store in a dictionary {email: user_data}.

# Workout Logging

# Users can log workouts (stored in a list of tuples: (date, workout_name, duration)).

# Class Booking

# Gym classes stored in a dictionary {class_name: {slots, time}}.

# Prevent double-booking for the same user.

# Progress Tracking

# Show most active users (by number of workouts).

# Show top 3 most popular classes.

# Loyalty Points

# Users earn 1 point for each workout over 30 mins.

# Advanced Logic

# Users with more than 100 workouts get a “Pro Badge”.

# Use sets to track unique users attending a class.

# Save/load gym data from JSON files.