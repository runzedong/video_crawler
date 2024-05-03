import requests

def downloader(url, i):
    file_name = 'main_' + str(i) + '.ts'
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)
    r.close()
    print('finish downloading %s' % (file_name))

def main():
    for i in range(1500):
        url = 'https://v-vod-k.xiaoeknow.com/e43b434705d7499c94f8d73a610597e2/appcafhwq5q8671/video/b_u_chq7l2m1l0ctcb85tlag/lt7246if0m7y/main_' + str(i) + '.ts?t=66351968&us=GSlqgylEjw&time=1714712744622&uuid=u_6633a0f8b3f63_hFronLKc9Q&sign=0f47cd8b43e84b80f9c4aabede14fa8e'
        downloader(url, i)

if __name__ == '__main__':
    main()
