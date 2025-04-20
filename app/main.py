"""Main"""
import click
from adguardhome import AdGuadHome
from adlist import AdList
@click.command()
@click.option('--adguard_url', default='https://adguard', prompt='AdGuardHome URL', help='Your AdGuardHome URL')
@click.option('--username', default='admin', prompt='AdguardHome Username', help='Your AdGuardHome Username')
@click.option('--password', prompt='AdGuardHome Password', hide_input=True, help='Your AdGuardHome Password')
@click.option('--adlist_url', default="https://v.firebog.net/hosts/lists.php?type=tick", help='Your Adlists that you want to block')
@click.option('--whitelist_url', default="https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt", help='Your allowlist(s), comma separated, that you do not want to block')

def main(adguard_url, username, password, adlist_url, whitelist_url):
    adguardhome = AdGuadHome(adguard_url, username, password)
    adlist = AdList(adlist_url)

    adguardhome.do_login()

    current_filters = adguardhome.get_current_filters()
    new_filters = adlist.get_new_filters()
    add_and_clenup_filter(adguardhome, current_filters, new_filters, False)

    current_filters = adguardhome.get_current_whitelist_filters()
    new_filters = whitelist_url.split(",")
    print("got", len(new_filters), "whitelists")
    add_and_clenup_filter(adguardhome, current_filters, new_filters, True)

def add_and_clenup_filter(adguardhome: AdGuadHome, current_filters: dict, new_filters: [], whitelist: bool):
    filter_type = "whitelist filters" if whitelist else "filters"
    print("processing", filter_type, "started")
    for current_filter in current_filters:
        if adguardhome.name_prefix in current_filter["name"] and not current_filter["url"] in new_filters:
            # remove filters that got removed from list
            print("remove", current_filter["url"], "from", filter_type)
            adguardhome.remove_url(current_filter["url"], whitelist)
        if current_filter["url"] in new_filters:
            # filter lists that are already present
            #print("already included", current_filter["url"])
            new_filters.remove(current_filter["url"])

    print("adding", len(new_filters), "new", filter_type)
    for new_filter in new_filters:
        if new_filter:
            adguardhome.add_url(new_filter, whitelist)
    print("processing", filter_type, "done")


if __name__ == '__main__':
    main()
