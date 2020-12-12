# nintendo-one
Nintendo One is a website that keeps you updated with the latest game discount at NS

# Data used:
- Game full list @ HK server: https://www.nintendo.com.hk/data/json/switch_software.json
Data format:
```json
{
    "r_date": 44239,
    "release_date": "2021.2.12",
    "r_date_tw": "",
    "release_date_tw": "",
    "title": "超級瑪利歐 ３Ｄ世界 ＋ 狂怒世界",
    "title_sc": "超级马力欧3D世界 ＋ 狂怒世界",
    "sale_until": "",
    "pickup": 1,
    "only_for": "",
    "media": "package",
    "lang": "CN",
    "maker_publisher": "Nintendo",
    "thumb_img": "super_mario_3d_world.jpg", // https://www.nintendo.com.hk/software/img/bnr/ + <thumb_img>
    "thumb_img_sc": "",
    "thumb_img_tw": "",
    "link": "/topics/article/a_200904_07.html", // https://www.nintendo.com.hk/topics/article/ + <link>
    "link_sc": "",
    "link_tw": "",
    "link_target": "",
    "platform": "Nintendo Switch",
    "rating": 6,
    "adult_hk": "",
    "category": "",
    "category_sc": "",
    "copyright": "©2020 Nintendo",
    "copyright_sc": "",
    "memo1": "",
    "memo2": "",
    "memo1_sc": "",
    "memo2_sc": "",
    "memo1_tw": "",
    "memo2_tw": "",
    "product_code": "",
    "item_code": "",
    "price": ""
},
```

## API list
**Discounting Game List:**
- Japan: https://ec.nintendo.com/api/JP/ja/search/sales?count=30&offset=0
- US: https://ec.nintendo.com/api/US/en/search/sales?count=30&offset=0
- https://ec.nintendo.com/api/GB/en/search/sales?count=10&offset=0
- Canada: https://ec.nintendo.com/api/CA/en/search/sales?count=30&offset=0#Canada
- Australia: https://ec.nintendo.com/api/AU/en/search/sales?count=10&offset=0#Australia
- New Zealand: https://ec.nintendo.com/api/NZ/en/search/sales?count=10&offset=0#NewZealand
- Czech: https://ec.nintendo.com/api/CZ/en/search/sales?count=10&offset=0#Czech
- Denmark: https://ec.nintendo.com/api/DK/en/search/sales?count=10&offset=0#Denmark
- Finland: https://ec.nintendo.com/api/FI/en/search/sales?count=10&offset=0#Finland
- Greece: https://ec.nintendo.com/api/GR/en/search/sales?count=10&offset=0#Greece
- Hungary: https://ec.nintendo.com/api/HU/en/search/sales?count=10&offset=0#Hungary
- Norway: https://ec.nintendo.com/api/NO/en/search/sales?count=10&offset=0#Norway
- https://ec.nintendo.com/api/PL/en/search/sales?count=10&offset=0#Poland
- Poland: https://ec.nintendo.com/api/ZA/en/search/sales?count=10&offset=0#SouthAfrica
- Sweden: https://ec.nintendo.com/api/SE/en/search/sales?count=10&offset=0#Sweden
- Germany: https://ec.nintendo.com/api/DE/de/search/sales?count=10&offset=0#Germany
- Switzerland: https://ec.nintendo.com/api/CH/de/search/sales?count=10&offset=0#Switzerland
- France: https://ec.nintendo.com/api/FR/fr/search/sales?count=10&offset=0#France
- Belgium: https://ec.nintendo.com/api/BE/fr/search/sales?count=10&offset=0#Belgium
- Italia: https://ec.nintendo.com/api/IT/it/search/sales?count=10&offset=0
- Netherlands: https://ec.nintendo.com/api/NL/nl/search/sales?count=10&offset=0
- Belgium: https://ec.nintendo.com/api/BE/nl/search/sales?count=10&offset=0#Belgium
- https://ec.nintendo.com/api/RU/ru/search/sales?count=30&offset=0
- https://ec.nintendo.com/api/ES/es/search/sales?count=30&offset=0
- https://ec.nintendo.com/api/MX/es/search/sales?count=30&offset=0#Mexico
- https://ec.nintendo.com/api/CO/es/search/sales?count=10&offset=0#Columbia
- https://ec.nintendo.com/api/AR/es/search/sales?count=10&offset=0#Argentina
- https://ec.nintendo.com/api/CL/es/search/sales?count=10&offset=0#Chile
- https://ec.nintendo.com/api/PE/es/search/sales?count=10&offset=0#Peru
- https://ec.nintendo.com/api/PT/pt/search/sales?count=30&offset=0#Portugal
- https://ec.nintendo.com/api/BR/pt/search/sales?count=10&offset=0
- Hong Kong: https://ec.nintendo.com/api/HK/zh/search/sales?count=10&offset=0#HongKong
- South Korea: https://ec.nintendo.com/api/KR/ko/search/sales?count=10&offset=0#SouthKorea

**Latest Released Game List:**
- https://ec.nintendo.com/api/JP/ja/search/new?count=30&offset=0

**Downloading Game Ranking:**
- https://ec.nintendo.com/api/JP/ja/search/ranking?count=10&offset=0

**Format**
```
contents: array
    content_type: string
    disclaimer: string
    dominant_colors: string[]
    formal_name: string
    hero_banner_url: string
    id: number
    is_new: boolean
    public_status: string
    release_date_on_eshop: string
    strong_disclaimer: string
    tags: array
    target_titles: array
length: number
offset: number
total: number
```

**Game Price Query**

- https://api.ec.nintendo.com/v1/price?country=JP&ids=70010000009922&lang=jp
```
personalized: boolean
country: string
prices: array
    title_id: number,
    sales_status: string
    regular_price:
        amount: string
        currency: string
        raw_value: string
    discount_price:
        amount: string
        currency: string
        raw_value: string
        start_datetime: date
        end_datetime: date
```

## Third party library used
[django-money](https://github.com/django-money/django-money)
