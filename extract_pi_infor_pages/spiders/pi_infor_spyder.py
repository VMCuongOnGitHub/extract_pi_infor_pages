import scrapy
from scrapy import Selector
import re
from datetime import datetime


class PIInforSpyder(scrapy.Spider):
    name = 'pi_infor_spyder'
    allowed_domains = ['www.etoro.com']
    popular_investors = ["rallek", "miyoshi", "reinhardtcoetzee", "sharonconnolly", "cphequities", "rubymza", "richardstroud", "ingruc", "pino428", "triangulacapital", "jordenboer", "slow_and_steady", "monabel", "emge2116", "doopiecash", "magic_kaito", "ioatri",
       "balticseal", "daniel4653", "fifty-five", "calintrading", "sgstjc", "greatcompanies", "karlo_s", "lukaszkisicki", "trojaneto", "chiay0327", "carlos_delarosa", "trex8u247", "estebanopatril", "nintingale", "taherkamari", "zofesu",
      "andreamarcon16", "nestorarmstrong", "bhavesh_spx", "theosanders", "dividends_income", "andresvicunat", "tomwintjes", "nicoroumeau", "mjtfernandez", "myhungetoro", "maxdividend", "victorvatin",
      "aguero1010", "ilakha", "beatthemarketz", "acetoandrea", "jacksmann", "renoi974", "tomchapman1979", "axisnet", "imbolex", "thinhleduc", "jianswang", "marianopardo", "wesl3y", "hyjbrighter", "misterg23", "ligkclaw",
      "alexandrucinca", "rubymza", "jaynemesis", "gserdan", "tradefx525", "eddyb123", "returninvest", "matanspalatrin1", "lee88eng", "bamboo108", "liborvasa", "jeppekirkbonde", "liamdavies", "arash007", "canzhao", "knw500",
      "thibautr", "fundmanagerzech", "sashok281", "alnayef", "campervans", "pizarrosaul", "sandra31168", "social-investor", "prototypevr", "harryh1993", "vidovm", "meldow", "robertunger", "sparkliang", "abbroush",
      "abeershahid", "coolcontribution", "chocowin", "vladd35", "aukie2008", "noasnoas", "b--art", "simonneau"]
    # popular_investors = ["chocowin"]
    # popular_investors = ["pizarrosaul"]
    urls = []
    for popular_investor in popular_investors:
        urls.append("file:///C:/Users/vmcuo/PycharmProjects/downloader/offline_webpage/07-24-2022-h18/" + popular_investor.lower() + ".html")

    print(urls)
    start_urls = urls

    def parse(self, response):

        try:
            name = Selector(response).xpath("//h1[@automation-id='user-head-not-nickname']/text()").extract_first().strip()
        except:
            name = Selector(response).xpath("//h1[@automation-id='user-head-nickname']/text()").extract_first().strip()

        try:
            full_name = Selector(response).xpath("//h2[@automation-id='user-head-fullname']/text()").extract_first().strip()
        except:
            full_name = ""


        country = Selector(response).xpath("(//*[contains(@automation-id,'breadcrumbs-name-results')]/span)[1]/text()").extract_first().strip()
        rank = ""
        # rank = re.findall("pi-level-star--(\d*)", Selector(response).xpath("//*[contains(@class,'pi-level-star')]").xpath("@class").extract_first())[0]
        print("rank=============================")
        print(Selector(response).xpath("(//*[contains(@class,'pi-level-star')])[1]"))
        print("rank=============================")
        try:
            rank = re.findall("pi-level-star--(\d*)", Selector(response).xpath("(//*[contains(@class,'pi-level-star')])[1]").xpath("@class").extract_first())[0]
        except:
            rank = Selector(response).xpath("(//*[contains(@class,'sprite-stats')])[1]").xpath("@class").extract_first()
            if rank == "sprite-stats ng-star-inserted":
                rank = "1"

        # print("++++++++++")
        # print(Selector(response).xpath("//div[@automation-id='stats-user-risk-label']"))
        # print("++++++++++")
        try:
            risk = Selector(response).xpath("//*[contains(@class,'risk-default')]").extract_first().strip()
        except:
            risk = re.findall("risk-(\d*)", Selector(response).xpath("//*[contains(@class,'risk-label')]").xpath("@class").extract_first())[1]
            print("risk: " + risk)


        no_copier = Selector(response).xpath("//et-card[@automation-id='stats-user-copy-item-wrapp']//div[@class='info-procents']/text()").extract_first().strip()
        aum = Selector(response).xpath("//et-card[@automation-id='stats-user-copy-item-wrapp']//div[@class='performance-amount']/text()").extract_first().strip()
        total_trade = Selector(response).xpath("//et-card[@automation-id='stats-user-trading-item-wrapp']//div[@class='performance-num']/text()").extract_first().strip()
        profitable_trade = Selector(response).xpath("//span[@class='top-trade-profit-procent']/text()").extract_first().strip()
        trades_per_week = Selector(response).xpath("//span[@automation-id='stats-user-trade-info']/text()").extract_first().strip()
        avg_holding_time = Selector(response).xpath("//span[@automation-id='stats-user-holding-info']/text()").extract_first().strip()
        active_since = Selector(response).xpath("//span[@automation-id='stats-user-copied-info']/text()").extract_first().strip()
        profitable_weeks = Selector(response).xpath("//span[@automation-id='stats-user-profit-info']/text()").extract_first().strip()

        # trading_stocks = Selector(response).xpath("//span[text()='Stocks']/parent::div/div")
        trading_stocks = Selector(response).xpath("//span[text()='Stocks']/parent::div/div/text()").extract_first()
        trading_people = Selector(response).xpath("//span[text()='People']/parent::div/div/text()").extract_first()
        trading_copy_portfolio = Selector(response).xpath("//span[text()='Copy Portfolio']/parent::div/div/text()").extract_first()
        trading_etfs = Selector(response).xpath("//span[text()='ETFs']/parent::div/div/text()").extract_first()
        trading_crypto = Selector(response).xpath("//span[text()='Crypto']/parent::div/div/text()").extract_first()
        trading_indices = Selector(response).xpath("//span[text()='Indices']/parent::div/div/text()").extract_first()
        trading_commodities = Selector(response).xpath("//span[text()='Commodities']/parent::div/div/text()").extract_first()
        trading_currencies = Selector(response).xpath("//span[text()='Currencies']/parent::div/div/text()").extract_first()

        print("==result=============")
        pi = {
            "name": name,
            "full_name": full_name,
            "country": country,
            "rank": rank,
            "risk": risk,
            "no_copier": no_copier,
            "aum": aum,
            "total_trade": total_trade.split("\n", 1)[0],
            "profitable_trade": profitable_trade,
            "trades_per_week": trades_per_week,
            "avg_holding_time": avg_holding_time.split(" ", 1)[0],
            "active_since": active_since,
            "profitable_weeks": profitable_weeks,
            "trading": {},
            "performance": {},
            "performance_total": {},
            "update_at": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        }
        # Selector(response).xpath("//et-card[@automation-id='stats-user-performance-chart']//div[@class='expand-button']").click()

        jan = {}
        feb = {}
        mar = {}
        apr = {}
        may = {}
        jun = {}
        jul = {}
        aug = {}
        sep = {}
        oct = {}
        nov = {}
        dec = {}
        year_label = {}
        performance_total = {}
        print("=performance=========================")

        years = Selector(response).xpath("//div[@automation-id='stats-user-performance-chart-year']")
        for i in range(len(years), 0, -1):
            # print(i)
            year = Selector(response).xpath("(//div[@automation-id='stats-user-performance-see-more']//div[@automation-id='stats-user-performance-chart-year'])[" + str(
                                                i) + "]/text()").extract_first()
            performance_total_year = Selector(response).xpath("(//div[@automation-id='stats-user-performance-see-more']//div[@class='performance-chart-slot amount'])[" + str(
                                                                  i) + "]/text()").extract_first()
            performance_total[year] = performance_total_year.strip()
            for j in range(12, 0, -1):
                performance_month = Selector(response).xpath("((//div[@automation-id='stats-user-performance-see-more'])[" + str(
                                                                 i) + "]//div[@automation-id='stats-user-performance-chart-amount'])[" + str(
                                                                 j) + "]/text()").extract_first()
                year_label[year] = performance_month
                if j == 12:
                    jan[year] = performance_month
                elif j == 11:
                    feb[year] = performance_month
                elif j == 10:
                    mar[year] = performance_month
                elif j == 9:
                    apr[year] = performance_month
                elif j == 8:
                    may[year] = performance_month
                elif j == 7:
                    jun[year] = performance_month
                elif j == 6:
                    jul[year] = performance_month
                elif j == 5:
                    aug[year] = performance_month
                elif j == 4:
                    sep[year] = performance_month
                elif j == 3:
                    oct[year] = performance_month
                elif j == 2:
                    nov[year] = performance_month
                elif j == 1:
                    dec[year] = performance_month
                year_label = {}

        performance = {"jan": jan, "feb": feb, "mar": mar, "apr": apr, "may": may, "jun": jun, "jul": jul, "aug": aug,
                       "sep": sep, "oct": oct, "nov": nov, "dec": dec}
        pi["performance"].update(performance)
        pi["performance_total"].update(performance_total)

        trading = {
            "STOCKS": trading_stocks,
            "PEOPLE": trading_people,
            "COPY_PORTFOLIOS": trading_copy_portfolio,
            "ETFS": trading_etfs,
            "CRYPTO": trading_crypto,
            "INDICES": trading_indices,
            "COMMODITIES": trading_commodities,
            "CURRENCIES": trading_currencies
        }
        pi["trading"].update(trading)
        yield pi