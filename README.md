# Service Control

GUI tray program to control systemd (systemctl) services

![image](https://cloud.githubusercontent.com/assets/1845813/14977395/45150b08-1135-11e6-979e-e9017c518efd.png)

## Dependencies

In Ubuntu, you need install following package:
```
sudo apt-get update
sudo apt-get install gir1.2-appindicator3-0.1
```

If you get `ImportError: No module named pam` you need install 
manually from [Python.org](https://pypi.python.org/pypi/python-pam) or
`pip install python-pam`

## License

Licensed under the [MIT License](https://opensource.org/licenses/mit-license.php)