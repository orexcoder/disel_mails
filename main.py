from loguru import logger

from disel import subscribe_disel

def main(massive):

    with open('files/proxies.txt') as f:
        proxies = f.read().splitlines()

    with open('files/mails.txt') as f:
        emails = f.read().splitlines()

    for proxy in proxies:
        if emails is not None:
            mails = emails[:massive]
            emails = emails[massive:]
            if massive > len(emails):
                mails = emails
                emails = None

            for mail in mails:
                subscribe_disel(mail, proxy)


if __name__ == "__main__":
    massive = int(input('Укажите количество запросов с 1 прокси: '))
    try:
        main(massive)
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.error(err)
