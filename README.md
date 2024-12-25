# Chatify - Real-Time Chat Room-Application

Chatify is a real-time chat application built with Flask, allowing users to create rooms, send messages, and interact in a smooth, live chat environment. This project is built using Python (Flask) on the backend and provides a simple, user-friendly interface for web-based communication.

## Features

- **Real-Time Messaging**: Users can send and receive messages instantly.
- **Room Creation**: Users can create and join public/private rooms.
- **User Authentication**: Users can sign up, log in, and manage their sessions.
- **Message History**: View previous messages when you join a room.
- **Responsive UI**: The UI adjusts to different screen sizes, ensuring a seamless experience on mobile and desktop.

## Requirements

- Python 3.x
- Flask
- Virtual Environment (`.venv`)
- JavaScript (for front-end)
- MongoDB (for storing chat data)

## Setup and Installation

### 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/your-username/Chatify.git
cd Chatify
```

### 2. Create a Virtual Environment

Create a Python virtual environment to isolate your dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment:

- **Windows (PowerShell):**
  ```bash
  .\.venv\Scripts\Activate
  ```
- **Windows (CMD):**
  ```bash
  .venv\Scripts\activate.bat
  ```
- **Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

Install the necessary Python dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure you have a `requirements.txt` file with the required libraries, including:

- Flask
- Flask-SocketIO (for real-time communication)
- Flask-WTF (for forms)
- pymongo (for MongoDB)
- gunicorn (for production server)

You can create the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

### 4. Setup MongoDB

1. Sign up on MongoDB Atlas (if you don’t have an account) and create a new database cluster.
2. Get the connection string from your MongoDB Atlas dashboard.
3. Replace the placeholder connection string in your project with your own in the `app.py` file or in a separate configuration file.

### 5. Run the Application

Once the environment is set up, run the Flask application:

```bash
python main.py
```

This should start the application on `http://127.0.0.1:5000`.

### 6. Access the Application

Open your web browser and visit:

```arduino
http://127.0.0.1:5000
```

You should see the home page of the chat application, where you can create a room, join existing ones, and start chatting in real-time.

## Project Structure

Here’s an overview of the project's file structure:

```php
Chatify/
│
├── .venv/                  # Virtual environment
├── app.py                  # Main Flask app
├── templates/              # HTML templates for the front-end
│   ├── index.html
│   ├── chat_room.html
│   └── ...
├── static/                 # Static files (CSS, JavaScript, Images)
│   ├── styles.css
│   └── script.js
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── config.py               # Configuration file (e.g., MongoDB URI)
```

## Contribution Guidelines

If you would like to contribute to the project, please fork the repository and submit a pull request. Here's how you can do it:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push the changes (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions, feel free to reach out to me via [your-email@example.com].
