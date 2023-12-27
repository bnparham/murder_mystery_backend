# Murder Mystery

Welcome to the Murder Mystery project! This README guide will help you get started with setting up and running the project on your local machine.

## Getting Started

Follow these steps to set up the project:

### 1. Setting Up a Virtual Environment

Before you begin, it's a good practice to create a virtual environment to isolate your project's dependencies. If you haven't installed `virtualenv`, follow these steps to set it up:

```bash
# Install virtualenv globally (if not already installed)
pip install virtualenv

# Create a virtual environment named 'env' (you can choose a different name)
virtualenv env

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS and Linux
source env/bin/activate
```

### 2. Installing Project Dependencies

With your virtual environment activated, navigate to the project directory and install the required dependencies listed in the `requirements.txt` file:

```bash
# Navigate to the project directory
cd murder_mystery

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Project
```bash
#Navigate to the project directory:
cd murder_mystery

#Apply database migrations:
python manage.py migrate

#Start the Django development server:
python manage.py runserver
```

## Frontend Repository
Find the Murder Mystery Frontend repository on GitHub: [Murder Mystery Frontend](https://github.com/bnparham/murder_mystery_frontend)


## API Endpoints

The backend exposes the following API endpoints:

- `api/person/`: Information about individuals involved in the mystery.
- `api/phone-calls/`: Details of phone calls related to the investigation.
- `api/location/`: Data on different locations relevant to the case.
- `api/street/`: Street-related information.
- `api/bank-account/`: Bank account details.
- `api/atm/`: Information related to ATMs.
- `api/security-log/`: Security log records.
- `api/crime-scene/`: Details about the crime scene.
- `api/item/`: Items associated with the investigation.
- `api/clue/`: Clues that might help solve the mystery.
- `api/airports/`: Airport details.
- `api/flights/`: Information about flights.
- `api/passengers/`: Passenger details.
- `api/interviews/`: Records of interviews conducted during the investigation.

Additionally, there is a special endpoint for playing Tic-Tac-Toe with AI:


### Tic-Tac-Toe Endpoints

#### `GET /tictoc/list`
View logs of player status on the Tic-Tac-Toe board.

#### `POST /tictoc/startnewgame`
Start a new Tic-Tac-Toe game (send empty json body)

Initial State Response:
```json
{
    "id": ?,
    "player": "X",
    "action": null,
    "board": "000000000",
    "winner": null,
    "terminal": false,
    "time": "?"
}
```
#### `POST /tictoc/moveapi`
Make a move on the Tic-Tac-Toe board.
we should send data to this endpoint like :
```json
{
	"letter":"X",
	"action":"01"
}
```
letter: The player's turn, which can be "X" or "O".

action: The player's choice of section on the board, where the first digit represents the row index, and the second digit represents the column index.

### Note: If letter and the player key in the API are the same (e.g., both "X"), the player goes first; otherwise, the AI goes first.



## XO app : Logic of board Value
The board value in the Tic-Tac-Toe responses is a compressed representation of the game board. The compression is achieved using the following Python function:
```python
def compressBoard(board: list):
    res = ''
    for row in range(len(board)):
        for col in range(len(board)):
            match board[row][col]:
                case None: res += '0'  # Empty cell
                case 'X': res += '1'   # Cell occupied by 'X'
                case 'O': res += '2'   # Cell occupied by 'O'
    return res

```
he function iterates through each cell in the board, representing empty cells as '0', cells with 'X' as '1', and cells with 'O' as '2'. The resulting string provides a concise representation of the game board, indicating the state of each cell and facilitating analysis to determine the winner or the presence of an empty cell.

## XO app : Logic of Action

The action value in the Tic-Tac-Toe move represents the player's choice of section on the board. The format of the action is a two-digit string, where the first digit represents the row index, and the second digit represents the column index.

For example:

action: "01" corresponds to the cell in the first row and second column.
action: "22" corresponds to the cell in the third row and third column.

## XO app : Game Termination and Winner Determination
If the terminal field is True, the game is finished.

If the winner field is null, the game is a draw (equal).

If the winner field is equal to 'X', then 'X' wins.

If the winner field is equal to 'O', then 'O' wins.
