# PyIPLookup
This simple Python script query and return geolocation information for an IP address. It uses IP2Location.io API service to lookup for the information. Free sign up is available through here: https://www.ip2location.io/.

## Usage
Just download the script your choice of directory, and run the script as:
```bash
ip2locationio.py -k your_api_key -p ip_address
```

Or make the script executable before run by using ```chmod +x```:

```bash
chmod +x ip2locationio.py
./ip2locationio.py -k your_api_key -p ip_address
```

You can also extract the specific column from the result using ```jq``` command. For example,

```bash
ip2locationio.py -k your_api_key -p ip_address | jq -r ".country"
```
