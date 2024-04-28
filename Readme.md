**Installation**
To run the backend server locally, follow these steps:

Clone this repository to your local machine:
git clone https://github.com/MNJUYDV/rock-paper-scissor-backend.git

Navigate to the project directory:
cd rock-paper-scissor-backend

Install dependencies using pip:
pip3 install -r requirements.txt

Start the Flask server:
python3 run.py
The server should now be running locally at http://localhost:5000.

Docker
Alternatively, you can run the backend server using Docker. Make sure you have Docker installed on your system.

**Build the Docker image:**

docker build -t rock-paper-scissor-backend .
Run the Docker container:
docker run -p 5000:5000 rock-paper-scissor-backend

**The backend server exposes the following APIs:**

GET /api/v1/players-stats: Retrieves the leaderboard players statistics.
POST /api/v1/leaderboard: Creates a new entry in the leaderboard.
POST /api/v1/start-game: Starts a new game.
GET /api/v1/game-players: Retrieves game players join information.