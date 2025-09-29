"""
Level 2: Intermediate (Using argparse)
Exercise 2.1: Enhanced Greeting
Improve the greeting script with argparse.
Requirements:
•	Use argparse instead of sys.argv
•	Add optional --formal flag for formal greeting
•	Add --times option to repeat greeting
•	Include help messages
Expected usage:
python greet2.py John
# Output: Hello, John!

python greet2.py John --formal
# Output: Good day, Mr./Ms. John!

python greet2.py Alice --times 3
# Output: Hello, Alice!
#         Hello, Alice!
#         Hello, Alice!
Exercise 2.2: File Backup Tool
Create a file backup utility.
Requirements:
•	Required: source file path
•	Optional: --destination (default: adds .backup extension)
•	Optional: --compress flag to zip the backup
•	Optional: --timestamp flag to add timestamp to filename
Expected usage:
python backup.py document.txt
python backup.py document.txt --destination /backups/
python backup.py document.txt --compress --timestamp
Exercise 2.3: Text Processor
Build a text processing tool.
Requirements:
•	Required: input file
•	Optional: --output (default: print to console)
•	Optional: --uppercase, --lowercase flags
•	Optional: --remove-spaces flag
•	Optional: --word-count flag
Expected usage:
python textproc.py input.txt --uppercase --output result.txt
python textproc.py input.txt --word-count
Level 3: Advanced
Exercise 3.1: Log Analyzer
Create a log file analyzer with subcommands.
Requirements:
•	Subcommands: analyze, search, summarize
•	analyze: count error/warning/info messages
•	search: find lines containing specific text
•	summarize: show top error types
•	Each subcommand should have its own options
Expected usage:
python loganalyzer.py analyze server.log --level ERROR
python loganalyzer.py search server.log --pattern "database"
python loganalyzer.py summarize server.log --top 5
Exercise 3.2: Image Processor
Build an image processing CLI tool.
Requirements:
•	Support multiple input files (glob patterns)
•	Subcommands: resize, convert, rotate
•	resize: --width, --height, --maintain-ratio
•	convert: --format (jpg, png, webp)
•	rotate: --degrees
•	Global options: --output-dir, --quality
Expected usage:
python imgproc.py resize *.jpg --width 800 --height 600
python imgproc.py convert image.png --format jpg --quality 90
python imgproc.py rotate photo.jpg --degrees 90 --output-dir rotated/
Exercise 3.3: Data Analysis Tool
Create a CSV data analysis tool.
Requirements:
•	Multiple subcommands: describe, filter, plot, export
•	describe: statistical summary of numeric columns
•	filter: filter rows based on conditions
•	plot: create simple visualizations
•	export: convert to different formats
•	Support column selection, sorting, grouping
Expected usage:
python datatools.py describe sales.csv
python datatools.py filter sales.csv --column amount --greater-than 1000
python datatools.py plot sales.csv --x date --y amount --type line
python datatools.py export sales.csv --format json --output data.json
Level 4: Master Level
Exercise 4.1: Complete CLI Application
Build a personal task manager with full CLI interface.
Requirements:
•	Subcommands: add, list, complete, delete, edit
•	Data persistence (JSON/SQLite)
•	Filtering and sorting options
•	Priority levels, due dates, categories
•	Configuration file support
•	Colored output
•	Interactive mode option
Exercise 4.2: System Monitoring Tool
Create a system monitoring CLI tool.
Requirements:
•	Monitor: CPU, memory, disk, network
•	Historical data storage
•	Alert thresholds
•	Export reports
•	Dashboard mode
•	Configuration via CLI and file
Bonus Challenges
1.	Add input validation to all exercises
2.	Implement configuration file support (YAML/JSON)
3.	Add colored output using libraries like colorama
4.	Create interactive prompts when arguments are missing
5.	Add progress bars for long-running operations
6.	Implement logging with different verbosity levels
7.	Add shell completion support
8.	Create comprehensive help systems with examples
Getting Started Tips
1.	Start with Exercise 1.1 and work your way up
2.	Focus on one exercise at a time
3.	Test edge cases (missing files, invalid inputs)
4.	Always include help messages
5.	Use meaningful variable names
6.	Handle errors gracefully
7.	Test your scripts thoroughly
Resources to Remember
•	sys.argv for simple cases
•	argparse for most applications
•	click or typer for advanced CLI apps
•	Always validate inputs
•	Provide good error messages
•	Include usage examples in help text



"""