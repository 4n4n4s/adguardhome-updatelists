"""Main"""
import click
from adguardhome import AdGuadHome
from adlist import AdList
@click.command()
@click.option('--adguard_url', default='https://adguard', prompt='AdGuardHome URL', help='Your AdGuardHome URL')
@click.option('--username', default='admin', prompt='AdguardHome Username', help='Your AdGuardHome Username')
@click.option('--password', prompt='AdGuardHome Password', hide_input=True, help='Your AdGuardHome Password')
@click.option('--adlist_url', default="https://v.firebog.net/hosts/lists.php?type=tick", help='Your AdGuardHome Password')

def main(adguard_url, username, password, adlist_url):
    adguardhome = AdGuadHome(adguard_url, username, password)
    adlist = AdList(adlist_url)

    adguardhome.do_login()
    current_filters = adguardhome.get_current_filters()
    new_filters = adlist.get_new_filters()
    for current_filter in current_filters:
        if adguardhome.name_prefix in current_filter["name"] and not current_filter["url"] in new_filters:
            # remove filters that got removed from list
            print("remove", current_filter["url"])
            adguardhome.remove_url(current_filter["url"])
        if current_filter["url"] in new_filters:
            # filter lists that are already present
            #print("already included", current_filter["url"])
            new_filters.remove(current_filter["url"])

    print("adding", len(new_filters), "new filters")
    for new_filter in new_filters:
        if new_filter:
            adguardhome.add_url(new_filter)

if __name__ == '__main__':
    main()
