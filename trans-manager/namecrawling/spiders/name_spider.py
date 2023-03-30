import scrapy


class MovieSpider(scrapy.Spider):
    name = "names"

    def __init__(self, sex=None, *args, **kwargs):
        super(MovieSpider, self).__init__(*args, **kwargs)
        self.sex = sex

    def start_requests(self):
        urls = [
            f'https://namegen.jp/?country=japan&sex={self.sex}&middlename=&middlename_cond=fukumu&middlename_rarity=&middlename_rarity_cond=ika&lastname=&lastname_cond=fukumu&lastname_rarity=&lastname_rarity_cond=ika&lastname_type=name&firstname=&firstname_cond=fukumu&firstname_rarity=&firstname_rarity_cond=ika&firstname_type=name',

            f'https://namegen.jp/?country=japan&sex={self.sex}&middlename=&middlename_cond=fukumu&middlename_rarity=&middlename_rarity_cond=ika&lastname=&lastname_cond=fukumu&lastname_rarity=&lastname_rarity_cond=ika&lastname_type=name&firstname=&firstname_cond=fukumu&firstname_rarity=&firstname_rarity_cond=ika&firstname_type=name'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        names = response.css("table > tr")
        for name in names:
            last_name = name.css("td.name > a:nth-child(1)::text").get()
            first_name = name.css("td.name > a:nth-child(2)::text").get()
            furigana = name.css("td.pron::text").get()
            sex = self.sex

            scraped_name = {           
            'last_name' : last_name,
            'first_name' : first_name,
            'furigana' : furigana,
            'sex' : sex
            }

            yield scraped_name           
