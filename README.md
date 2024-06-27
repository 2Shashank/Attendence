# Attendance Management System

This project is an Attendance Management System that consists of a client-server application. The server sends student roll numbers (SRNs) to the client, and the client sends back the attendance data to the server.

## Requirements

- Python 3.x
- Tkinter
- Socket
- Pickle
- CSV

## Files

- `Application.py`: This file contains the client-side application code.
- `server.py`: This file contains the server-side application code.
- `Data.csv`: This file is used to store the SRNs and attendance data.

## Setup

1. Ensure you have Python installed on your system.
2. Ensure the required libraries (`tkinter`, `socket`, `pickle`, `csv`) are available.
3. Create a file named `Data.csv` with the SRNs of the students as the first row. For example:
    ```
    SRN1,SRN2,SRN3,SRN4,SRN5
    ```

## Usage

### Server

1. Run the server using the command:
    ```sh
    python server.py
    ```

2. The server will start and listen for client connections on `127.0.0.1:9999` or `localhost:9999`.

### Client

1. Run the client using the command:
    ```sh
    python Application.py
    ```

2. A GUI window will appear with the SRNs and checkboxes. Select the students who are absent and click the `Submit` button.

3. The client will send the attendance data to the server and close the connection.

## Code Explanation

### `server.py`

- The server reads the SRNs from `Data.csv` and sends them to the client.
- It listens for incoming connections and accepts them.
- Upon receiving attendance data from the client, it writes the data to `Data.csv`.

### `Application.py`

- The client connects to the server and receives the SRNs.
- It displays the SRNs and checkboxes in a GUI window.
- When the user submits the attendance, it sends the data back to the server and closes the connection.

## Example

1. Add SRNs to `Data.csv`:
    ```
    SRN001,SRN002,SRN003,SRN004,SRN005
    ```

2. Start the server:
    ```sh
    python server.py
    ```

3. Start the client:
    ```sh
    python Application.py
    ```

4. In the GUI, select the absent students and click `Submit`.

5. The server will log the attendance data and save it to `Data.csv`.

---
