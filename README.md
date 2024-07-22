## Tutorial

1) Build the project:
```bash
make build
```

2) Run server:
```bash
make run 
```

3) Open status [page](http://localhost:8000/status)

4) Now you can send requests to proxy:
```bash
curl -X POST "http://localhost:8000/proxy" -H "Content-Type: application/json" -d '{"user": "username", "date": "2024-07-21"}'
```

5) Run tests:
```bash
make test
```