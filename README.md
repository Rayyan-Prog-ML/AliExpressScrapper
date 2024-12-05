

```markdown
# AliExpress Product Scraper

A Python-based project to scrape product details like names, prices, store names, and links from **AliExpress** using **Selenium**, **BeautifulSoup**, and **Pandas**. This project automates the data collection process and provides clean, structured data in a CSV file.

---

## Features
- 📦 Extracts product details, including:
  - **Product Name**
  - **Price**
  - **Store Name**
  - **Store Link**
- 🧹 Cleans and structures the data into an easy-to-use **CSV format**.
- 🚀 Automates pagination and handles dynamic web pages.

---

## Technologies Used
- **Python** 🐍
- **Selenium**: Automates browser interactions for web scraping.
- **BeautifulSoup**: Parses and extracts data from HTML files.
- **Pandas**: Cleans, processes, and structures the data.
- **CSV**: Exports the final structured data for analysis.

---

## Installation

### 1. Clone this repository:
```bash
git clone https://github.com/yourusername/aliexpress-scraper.git
```

### 2. Install dependencies:
Make sure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run the HTML Collector Script
Use the `Collecting_data.py` script to scrape product HTML files from AliExpress.  
This will save the raw HTML files in the `data/` directory.

```bash
python scripts/Collecting_data.py
```

### 2. Run the Data Processing Script
Use the `Putting_data.py` script to extract product details from the saved HTML files.  
The cleaned and structured data will be saved in the `Aliexpress_Data.csv` file.

```bash
python scripts/Putting_data.py
```

---

## Example Output

Here’s an example of the cleaned data exported to a CSV file:

| Product Name          | Price (USD) | Store Name    | Store Link                        |
|-----------------------|-------------|---------------|-----------------------------------|
| Laptop XYZ           | 500.00      | Store ABC     | https://aliexpress.com/store/123 |
| Gaming Laptop Alpha  | 700.00      | Tech Store    | https://aliexpress.com/store/456 |

---

## Project Workflow

1. **Scraping HTML**:
   - `Aliexpress.py` uses **Selenium** to navigate AliExpress, search for products, and save the HTML files for each product.

2. **Parsing and Cleaning Data**:
   - `collect_Aliexp.py` uses **BeautifulSoup** to parse the saved HTML files.
   - Extracts details such as names, prices, and store information.
   - Cleans the data with **Pandas**, including removing unnecessary characters and converting data types.

3. **CSV Export**:
   - Final processed data is saved into a **CSV file**, ready for analysis or integration into other systems.

---

## File Structure

```
aliexpress-scraper/
├── Aliexpress/                   # Directory for storing raw HTML files
├── outputs/                      # Directory for cleaned CSV files
├── scripts/
│   ├── Collecting_data.py             # Script for scraping HTML files
│   └── Putting_data.py         # Script for parsing and cleaning data
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
```

---

## Requirements

- Python 3.7+
- Google Chrome and ChromeDriver (for Selenium)

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Challenges and Learnings

- 🛠 Learned to handle dynamic web pages and pagination using **Selenium**.
- 📚 Improved HTML parsing skills with **BeautifulSoup**.
- 🧹 Gained experience in data cleaning and processing with **Pandas**.

---

## Future Enhancements

- Add support for scraping additional product details, like ratings and reviews.
- Implement multi-threading for faster data collection.
- Create a web interface for user-friendly data queries.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact

Feel free to connect with me on LinkedIn or explore my other projects on GitHub!
want me to hire to assist in your projects lets connect and discuss your needs
linkdin: [https://www.linkedin.com/in/rayyan-mustafa-0a201520b/]  
Github:  [https://github.com/Rayyan-Prog-ML]
📧 Email: rayyanmustafa2k456@gmail.com
```

---

