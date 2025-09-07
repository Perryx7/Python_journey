# Level 4 – Employees and Projects
# Create a list of dictionaries representing employees.
# Each dictionary contains 'name' and 'projects' (a list of project names).
# Loop through the list and print employees who have at least 2 projects.


employees = [
       {
        "name" : "employe1",
        "projects" : ['pj1', 'pj2', 'pj3']
        
     },

       {
        "name" : "employe2",
        "projects" : ['pj1', 'pj2']
        
     },

       {
        "name" : "employe3",
        "projects" : ['pj1', 'pj2', 'pj3','pj4']
        
     },

       {
        "name" : "employe4",
        "projects" : ['pj1']
        
     },
    
]

for employee_name in employees : 
    if len(employee_name["projects"]) >= 2 :
        print(employee_name["name"])
    else: 
        print('you must have at least 2 projects')
