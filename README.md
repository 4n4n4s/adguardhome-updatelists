# adguardhome-updatelists
This tool allows you to update adlists on AdGuardHome similar to pihole-updatelists.

## How it works?
It's using the API from AdGuardHome to login and afterwards it compares the list of filters available with those that are pulled by the ADLIST_URL. 

All lists imported get a prefix so we can identify them and when this tool is run again we can update the lists in case some get added or removed.

## Docker
Checkout the docker-compose.yml file and change the environment parameters so they match your configuration.

## Environment Variables 

| Name       | Description                   | Default         | Example    |
| ---------- | ----------------------------- | --------------- | ---------- |
|ADGUARD_URL | URL of AdGuardHome            | https://adguard | https://adguard.local |
|USERNAME    | AdGuardHome Admin Username    | admin           | admin |
|PASSWORD    | AdguardHome Admin Password    |                 | password |
|ADLIST_URL  | List of URLs that contain URLs to block| https://v.firebog.net/hosts/lists.php?type=tick | https://v.firebog.net/hosts/lists.php?type=tick |
|WHITELIST_URL  | Your allowlist(s), comma separated, that you do not want to block. | https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt |
