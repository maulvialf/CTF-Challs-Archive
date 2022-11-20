#!/usr/bin/env python3
from nslookup import Nslookup
from sys import stdout

import logging
import requests
import paramiko
import re
import json

logging.basicConfig(level=logging.DEBUG)

FINALIST = [
    '%zqIH@#eo#1YT6pCjQwyQCiO0',
    'BigBrainGurls',
    'Brahmastra',
    'No Rush & Relax',
    'NoBrainBois',
    'Panitia',
    'Rahasia',
    'SHOCKER',
    'Sopan Kh Begitu??',
    'Terlantarkan',
    'Walkie O Talkie',
    'ctf terakhir pas smk',
    'gatao aja lah',
    'jeopardized',
    'tim wangy wangy'
]
CTFd_URL = 'https://ctf.joints.id'
API_ENDPOINT = {
    'login': '/login',
    'chall': '/api/v1/challenges',
    'challid': '/api/v1/challenges/{}',
    'solve': '/api/v1/challenges/{}/solves',
    'scoreboard': '/api/v1/scoreboard',
    'teams': '/api/v1/teams',
    'users': '/api/v1/users',
    'me': '/api/v1/teams/me'
}


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas + '\n')
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)


stdout = Unbuffered(stdout)


class Auth(object):
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

        self.create_session()

    def create_session(self):
        self.ses = requests.session()

        try:
            self.login()
        except:
            logging.error(f'Incorrect CTFd credentials for {self.username}')
            stdout.writelines('\n[x] Incorrect username/password')
            exit()

    def get_csrf_token(self, target_url):
        response = self.ses.get(target_url)
        regex = re.compile(r'csrfNonce.*"([a-f0-9]*)"')

        nonce = regex.findall(response.text)[0]

        return nonce

    def login(self):
        target_url = self.url + API_ENDPOINT.get('login')
        csrf_token = self.get_csrf_token(target_url)
    
        auth_data = {
            'name': self.username,
            'password': self.password,
            'nonce': csrf_token
        }

        post_response = self.ses.post(target_url, data=auth_data)

        assert('incorrect' not in post_response.text)

    def get_user_team(self):
        target_url = self.url + API_ENDPOINT.get('me')
        response = self.ses.get(target_url)

        try:
            json_data = response.json().get('data')
            team_name = json_data['name']
            
            if team_name not in FINALIST:
                logging.error(f'{self.username} is not a Finalist')
                raise Exception
        except:
            stdout.writelines("\n[x] You're not registered as finalist")
            exit()
        else:
            return team_name


class Prompt(object):
    def __init__(self, username, password, host, port, team=''):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.team = team

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def start(self):
        try:
            self.connect()
            stdout.writelines(f'[+] Logged in')
            stdout.writelines(f'[v] Machine IP: {self.host}')
            stdout.writelines(f'[v] Team name: {self.team}\n')
        except Exception as e:
            stdout.writelines('\n[x] Failed to connect to remote machine')
            stdout.writelines(f'[?] Reason: {e}')
            exit()

        while True:
            try:
                stdout.write('$ ')
                command = input()
                response = self.recv(command)

                for r in response:
                    if r:
                        stdout.write(r.read().decode())
            
            except KeyboardInterrupt:
                exit()

    def recv(self, command):
        return self.ssh.exec_command(command)[1:]


def get_resolved_host(domain='snapshot'):
    try:
        query = Nslookup()
        response = query.dns_lookup(domain)
        
        return sorted(response.answer)
    
    except:
        logging.error('DNS not resolved')
        exit()

if __name__ == '__main__':
    ssh_user = 'user'
    ssh_pass = 'joints21ulala'
    ssh_port = 2222
    ip_hosts = get_resolved_host()

    mapped_host = dict(zip(FINALIST, ip_hosts))

    stdout.write('CTFd username: ')
    username = input()
    stdout.write('CTFd password: ')
    password = input()

    logging.info(f'Trying login as {username}')

    ssh = Auth(username, password, CTFd_URL)
    team_name = ssh.get_user_team()
    team_host = mapped_host[team_name]

    logging.info(f'Successfully logged in')

    p = Prompt(ssh_user, ssh_pass, team_host, ssh_port, team_name)
    p.start()