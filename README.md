<div align="center">
    <img src="img/ranger-reloaded-logo-outlined.png" alt="ranger reloaded logo" width="350"/>

Ranger Reloaded is a Python script that can be used to scan alive hosts on your network and check for vulnerable open
ports.

<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.10-teal.svg"></a>
</div>

![Demo Pic 1](img/rr_demo.png?raw=true)

## Installation

1. Clone the project.

```bash
git clone https://github.com/joeyagreco/ranger-reloaded.git
```

2. Change your working directory.

```bash
cd ranger-reloaded
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

4. Run the script.

```bash
py app.py
```

## Configuration

To change the ports that are being scanned, simply update the `ports` list in the `app.properties` file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Credits

Inspiration for this script came from [rang3r](https://github.com/floriankunushevci/rang3r).
