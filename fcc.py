import re
import requests
import json
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

FAKE_HEADERS = {'User-Agent': 'Mozilla/5.0'}

def scrape_freecodecamp(student_name, url):
  REQUIRED_LESSONS = [
    "Comment Your JavaScript Code",
    "Declare JavaScript Variables",
    "Storing Values with the Assignment Operator",
    "Initializing Variables with the Assignment Operator",
    "Understanding Uninitialized Variables",
    "Understanding Case Sensitivity in Variables",
    "Add Two Numbers with JavaScript",
    "Subtract One Number from Another with JavaScript",
    "Multiply Two Numbers with JavaScript",
    "Divide One Number by Another with JavaScript",
    "Increment a Number with JavaScript",
    "Decrement a Number with JavaScript",
    "Create Decimal Numbers with JavaScript",
    "Multiply Two Decimals with JavaScript",
    "Divide One Decimal by Another with JavaScript",
    "Finding a Remainder in JavaScript",
    "Compound Assignment With Augmented Addition",
    "Compound Assignment With Augmented Subtraction",
    "Compound Assignment With Augmented Multiplication",
    "Compound Assignment With Augmented Division",
    "Declare String Variables",
    "Escaping Literal Quotes in Strings",
    "Quoting Strings with Single Quotes",
    "Escape Sequences in Strings",
    "Concatenating Strings with Plus Operator",
    "Concatenating Strings with the Plus Equals Operator",
    "Constructing Strings with Variables",
    "Appending Variables to Strings",
    "Find the Length of a String",
    "Use Bracket Notation to Find the First Character in a String",
    "Understand String Immutability",
    "Use Bracket Notation to Find the Nth Character in a String",
    "Use Bracket Notation to Find the Last Character in a String",
    "Use Bracket Notation to Find the Nth-to-Last Character in a String",
    "Word Blanks",
    "Store Multiple Values in one Variable using JavaScript Arrays",
    "Nest one Array within Another Array",
    "Access Array Data with Indexes",
    "Modify Array Data With Indexes",
    "Access Multi-Dimensional Arrays With Indexes",
    "Manipulate Arrays With pop()",
    "Manipulate Arrays With push()",
    "Manipulate Arrays With shift()",
    "Manipulate Arrays With unshift()",
    "Shopping List",
    "Write Reusable JavaScript with Functions",
    "Passing Values to Functions with Arguments",
    "Global Scope and Functions",
    "Local Scope and Functions",
    "Global vs. Local Scope in Functions",
    "Return a Value from a Function with Return",
    "Understanding Undefined Value returned from a Function",
    "Assignment with a Returned Value",
    "Stand in Line",
    "Understanding Boolean Values",
    "Use Conditional Logic with If Statements",
    "Comparison with the Equality Operator",
    "Comparison with the Strict Equality Operator",
    "Practice comparing different values",
    "Comparison with the Inequality Operator",
    "Comparison with the Strict Inequality Operator",
    "Comparison with the Greater Than Operator",
    "Comparison with the Greater Than Or Equal To Operator",
    "Comparison with the Less Than Operator",
    "Comparison with the Less Than Or Equal To Operator",
    "Comparisons with the Logical And Operator",
    "Comparisons with the Logical Or Operator",
    "Introducing Else Statements",
    "Introducing Else If Statements",
    "Logical Order in If Else Statements",
    "Chaining If Else Statements",
    "Golf Code",
    "Selecting from Many Options with Switch Statements",
    "Adding a Default Option in Switch Statements",
    "Multiple Identical Options in Switch Statements",
    "Replacing If Else Chains with Switch",
    "Returning Boolean Values from Functions",
    "Return Early Pattern for Functions",
    "Counting Cards",
    "Build JavaScript Objects",
    "Accessing Object Properties with Dot Notation",
    "Accessing Object Properties with Bracket Notation",
    "Accessing Object Properties with Variables",
    "Updating Object Properties",
    "Add New Properties to a JavaScript Object",
    "Delete Properties from a JavaScript Object",
    "Using Objects for Lookups",
    "Testing Objects for Properties",
    "Manipulating Complex Objects",
    "Accessing Nested Objects",
    "Accessing Nested Arrays",
    "Record Collection",
    "Iterate with JavaScript While Loops",
    "Iterate with JavaScript For Loops",
    "Iterate Odd Numbers With a For Loop",
    "Count Backwards With a For Loop",
    "Iterate Through an Array with a For Loop",
    "Nesting For Loops",
    "Iterate with JavaScript Do...While Loops",
    "Replace Loops using Recursion",
    "Profile Lookup",
    "Generate Random Fractions with JavaScript",
    "Generate Random Whole Numbers with JavaScript",
    "Generate Random Whole Numbers within a Range",
    "Use the parseInt Function",
    "Use the parseInt Function with a Radix",
    "Use the Conditional (Ternary) Operator",
    "Use Multiple Conditional (Ternary) Operators",
    "Use Recursion to Create a Countdown",
    "Use Recursion to Create a Range of Numbers",
  ]

  if url:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")

    with webdriver.Chrome(options=chrome_options) as driver:
      driver.get(url)
      driver.implicitly_wait(1)
      next_button = driver.find_elements_by_css_selector(
          'button[aria-label="Go to Next page"]')

      lessons = []
      while len(next_button) > 0:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        lessons_on_page = soup.find_all('tr', class_='timeline-row')
        lessons.extend(lessons_on_page)

        if not next_button[0].get_property('disabled'):
          next_button[0].click()
        else:
          break

      lessons = [lesson.find('a').contents[0] for lesson in lessons]

      finished_lessons = 0
      for name in REQUIRED_LESSONS:
        if name in lessons:
          finished_lessons += 1

      percentage = int(finished_lessons / len(REQUIRED_LESSONS) * 100)
      return percentage
