# News and Dictionary Information Emailer README

## Overview

This Python project, developed as part of the Turing College curriculum, is designed to fetch news or dictionary definitions based on user input and send the information via email. The project incorporates external APIs for news and dictionary data and demonstrates the use of SMTP for sending emails, handling command-line arguments, and validating email addresses.

## Project Structure

- `/src` contains the main Python script (`project.py`) that orchestrates the fetching of information and sending emails.
- `/test_project` includes unit tests that ensure the functionality of the project components works as expected.

## Features

- **Email Validation**: Checks if the provided email address is valid before attempting to send an email.
- **News API Integration**: Fetches news related to a specified topic using the News API and formats it into an HTML table for email content.
- **Dictionary API Integration**: Retrieves definitions, phonetics, and examples for a given word from a dictionary API and formats the information into HTML content.
- **SMTP Email Sending**: Sends the formatted HTML content as an email to the specified recipient using SMTP.

## Prerequisites

To run this project, you will need:

- Python 3.x installed on your system.
- A valid API key from [NewsAPI](https://newsapi.org/).
- An SMTP server setup for sending emails (the project is configured to use Gmail's SMTP server).

## Setup

1. **Clone the repository** to your local machine.

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory** where `project.py` is located.

    ```bash
    cd /src
    ```

3. **Set up environment variables** for sensitive information such as your SMTP email password. For Gmail, you can set `TEST_GMAIL_PASS` to your app-specific password.

4. **Install required Python packages**:

    ```bash
    pip install requests email-validator newsapi-python
    ```

## Usage

To use the script, navigate to the `/src` directory and run `project.py` with command-line arguments specifying the recipient's email address and the desired API ('news' or 'dict').

```bash
python project.py <recipient-email> <news|dict>
```
### For News:

You will be prompted to enter a topic. The script will then fetch top headlines related to this topic and send them as an email.

### For Dictionary Definitions:

You will be prompted to enter a word. The script will fetch the definition, phonetics, and example usage, and send this information as an email.

For help on usage, run:

```bash
python project.py -h
```
This command will display a help message explaining how to use the script correctly, including the syntax for specifying the recipient's email address and choosing between the 'news' or 'dict' APIs.

### For Dictionary Definitions

You will be prompted to enter a word. The script will then fetch the definition, phonetics, and example usage, and send this information as an email.

To get help on how to use the script, including the required command-line arguments, you can run the script with the `-h` option:

```bash
python project.py -h
```
This command will display a help message explaining how to use the script correctly, including the syntax for specifying the recipient's email address and choosing between the 'news' or 'dict' APIs.

## Contributing

Given the educational nature of this project, developed as part of the Turing College curriculum, formal contributions are not solicited. The primary objective is to facilitate an immersive learning experience, whereby participants are encouraged to explore and manipulate the codebase independently, thus fostering a deeper understanding of the underlying concepts and technologies employed within the project. Individuals seeking to extend their learning beyond the initial scope of the project are encouraged to fork the repository. This approach allows for personal experimentation and modification, potentially leading to innovative uses or enhancements of the original project framework. Such endeavors are viewed as valuable extensions of the learning process, encouraging independent problem-solving and creative thinking.

## License

This project is disseminated under the auspices of the MIT License, a permissive licensing agreement designed to encourage the broad use and distribution of the software while minimizing restrictions on freedom of use. Under the terms of the MIT License, users are granted the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the condition that the above copyright notice and this permission notice are included in all copies or substantial portions of the software. It is imperative to acknowledge that the software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other
