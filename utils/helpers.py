def determine_table_name(filename):
    """Determines the table name and headers based on the filename."""
    # Implement logic to map filenames to table names
    #print(filename)
    if filename.startswith("departments"):
        table_name = "departments"
        headers = ['id', 'department']
    elif filename.startswith("hired_employees"):
        table_name = "hired_employees"
        headers = ['id', 'name', 'datetime', 'department_id', 'job_id']
    elif filename.startswith("jobs"):
        table_name = "jobs"
        headers = ['id', 'job']
    else:
        raise ValueError(f"Invalid filename: {filename}")
    
    return table_name, headers
