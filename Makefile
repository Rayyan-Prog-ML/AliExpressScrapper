# Makefile for AliExpress Product Scraper

# Variables
PYTHON = python
SCRIPTS_DIR = scripts
HTML_DIR = Aliexpress
OUTPUT_FILE = AliexpressSsss_Data.csv

# Install dependencies
install:
	pip install -r requirements.txt

# Run the scraper to collect HTML files
scrape:
	$(PYTHON) $(SCRIPTS_DIR)/Aliexpress.py

# Run the cleaning script to process and export data
clean-data:
	$(PYTHON) $(SCRIPTS_DIR)/collect_Aliexp.py

# Remove generated HTML files
clean-html:
	rm -rf $(HTML_DIR)/*.html

# Remove CSV output file
clean-output:
	rm -f $(OUTPUT_FILE)

# Remove all generated files
clean-all: clean-html clean-output

# Run the entire process: scrape and clean data
run-all: scrape clean-data

# Help: Display usage information
help:
	@echo "Makefile for AliExpress Product Scraper"
	@echo "Available commands:"
	@echo "  install        Install required dependencies"
	@echo "  scrape         Run the scraper to collect product HTML files"
	@echo "  clean-data     Run the script to process and clean the data into CSV"
	@echo "  clean-html     Remove all scraped HTML files"
	@echo "  clean-output   Remove the CSV output file"
	@echo "  clean-all      Remove all generated files (HTML and CSV)"
	@echo "  run-all        Run the entire scraping and cleaning process"
