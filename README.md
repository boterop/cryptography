Python API to encode and decode

## Setup

Before running the project we need to install the requirements, in console write `pip install -r requirements.txt`

## Run the project

### Windows

`py main.py`

### Linux & Mac

`python3 main.py`

## To create systemctl service

Go to `/etc/systemd/system` and create a file `script.service` and write:

```
[Unit]
Description="Script Description"
After=network.target

[Service]
User=server
WorkingDirectory=/home/server/script/
ExecStart=/home/server/.asdf/shims/python3.10 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

and then `sudo systemctl enable script`

## Endpoints

- <b>POST</b> _/base64_

  #### Body:

  ```json
  {
    "text": "test",
    "method": "encode"
  }
  ```

  #### Response:

  <b>200</b>

  ```json
  {
    "response": "dGVzdA==",
    "status": 200
  }
  ```

---

- <b>POST</b> _/base64_image_

  #### Body:

  ```json
  {
    "image-url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjzC2JyZDZ_RaWf0qp11K0lcvB6b6kYNMoqtZAQ9hiPZ4cTIOB"
  }
  ```

  #### Response:

  <b>200</b>

  ```json
  {
    "response": "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAADjCAMAAADdXVr2AAABPlBMVEX////pQjU0qFNChfT...",
    "status": 200
  }
  ```

---

- <b>GET</b> _/gen-uuid_

  #### Response:

  <b>200</b>

  ```json
  {
    "response": "a5da4cf4-fa90-4b87-b8e6-2c3da7884e81",
    "status": 200
  }
  ```

---

- <b>GET</b> _/health_

  #### Response:

  <b>200</b>

  ```json
  {
    "response": "OK",
    "status": 200
  }
  ```
