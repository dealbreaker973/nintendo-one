# NOTES
## How Nintendo manage switch games
Nintendo manage switch games in different region separately. 
Different countries are divided into 3 regions:
- Nintendo of America (NoA)
- Nintendo of Europe (NoE)
- Nintendo of Japan (NoJ)
For different regions, the way they manage games are different. 
For example, in NoA, they use [algoliasearch](https://www.algolia.com/) to allow search and filter of games in their website. 

It is worth noticing that the search api key are exposed if you check their website source code:

```html
<script type="text/javascript">
    var NIN = NIN || {};
    var locale = "en_us";
    NIN.algoliaConfig = {
        appId: "U3B6GR4UA3",
        searchApiKey: "c4da8be7fd29f0f5bfa42920b0a99dc7",
        appIndices: {
            all: 'ncom_all_' + locale,
            game: 'ncom_game_' + locale,
            amiibo: 'ncom_amiibo_' + locale,
            article: 'ncom_article_' + locale
        }
    };
</script>
```

## Official data sources
### General API
**All games in Hong Kong**
https://www.nintendo.com.hk/data/json/switch_software.json

**All games in Japan**
https://www.nintendo.co.jp/data/software/xml/switch.xml

**Games on sale**
https://ec.nintendo.com/api/{country}/{lang}/search/sales?count=30&offset=0

i.e. https://ec.nintendo.com/api/JP/ja/search/sales?count=30&offset=0#all games on sale in Japan

** country list [here](TODO)

**Latest Released Game List:**
https://ec.nintendo.com/api/{country}/{lang}/search/new?count=30&offset=0

**Downloading Game Ranking:**
https://ec.nintendo.com/api/{country}/{lang}/search/ranking?count=30&offset=0

**Game price**
https://api.ec.nintendo.com/v1/price?country={country}&ids={game_id}&lang={lang}

i.e. https://api.ec.nintendo.com/v1/price?country=JP&ids=70010000009922&lang=jp

** game in different region has different id. This id can be obtained from games on sale api and from game link.

### Nintendo of America (NoA)
In NoA, they use [algoliasearch](https://www.algolia.com/) to allow search and filter of games in their website. 

An example use of this API in python can be found [here](https://github.com/fedecalendino/nintendeals/blob/ca3fb87e171c6cadb9a5fd82738397878bd58ec4/nintendeals/noa/api/algolia.py)

### Nintendo of Europe (NoE)
There is another search api on NoE:
http://search.nintendo-europe.com/en/select?fq=type:GAME AND system_type:nintendoswitch* AND nsuid_txt:{id}&q=*&sort=sorting_title asc&start={start}
http://search.nintendo-europe.com/en/select?fq=type:GAME AND system_type:nintendoswitch* AND product_code_txt:*&q=*&sort=sorting_title asc&start=0

http://search.nintendo-europe.com/en/select?fq=type:GAME%20AND%20system_type:nintendoswitch*%20AND%20nsuid_txt:70010000000023&q=*&sort=sorting_title%20asc&start=0
http://search.nintendo-europe.com/en/select?fq=type:GAME%20AND%20system_type:nintendoswitch*%20AND%20product_code_txt:*&q=*&sort=sorting_title%20asc&start=4640

It will return at most 10 results.

### Nintendo of Japan (Noj)
TODO