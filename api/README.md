# setup app

1. Create virtual environment

```bash
python3 -m venv venv
```

For ubuntu

```bash
source venv/bin/activate
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
python app.py
```

# for Migration

1. Create migration

```bash
flask db migrate
```

2. Apply migration

```bash
flask db upgrade
```
