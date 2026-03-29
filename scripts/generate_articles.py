"""Generate Hugo markdown articles for all spots in all languages."""

import os
import sys
from datetime import datetime, timedelta
from config import SPOTS, LANGUAGES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# Article body templates per language
TEMPLATES = {
    "en": """## Overview

{title} is one of Japan's most remarkable destinations, located in {city}. {description}

Whether you're a first-time visitor to Japan or a seasoned traveler, this spot offers a truly unforgettable experience that captures the essence of Japanese {category_lower}. From the moment you arrive, you'll be struck by the unique atmosphere that has drawn visitors for generations.

The area surrounding {title_short} is rich with history and cultural significance. Locals and tourists alike find themselves returning again and again, each visit revealing new details and perspectives that weren't noticed before.

## How to Get There

**By Train:** The most convenient way to reach {city} is by Shinkansen (bullet train) to the nearest major station. From there, local trains and buses provide easy connections. If you have a JR Pass, most of the journey will be covered.

**By Bus:** Highway buses offer a budget-friendly alternative, with services running from major cities like Tokyo, Osaka, and Kyoto. Book in advance during peak seasons.

**On Foot:** Once you arrive in the area, many of the best experiences can be enjoyed on foot. Comfortable walking shoes are recommended, especially if you plan to explore the surrounding neighborhoods.

## Best Time to Visit

**Spring (March-May):** Cherry blossoms add a magical backdrop. This is one of the most popular times to visit, so expect larger crowds but breathtaking scenery.

**Summer (June-August):** Lush greenery and summer festivals create a vibrant atmosphere. Be prepared for heat and humidity, especially in July and August.

**Autumn (October-November):** Stunning red and golden foliage transforms the landscape. Many consider this the most photogenic season.

**Winter (December-February):** Fewer crowds and a serene atmosphere. Some areas offer beautiful snow-covered views that create an entirely different experience.

## Tips for Visitors

- **Arrive early** to avoid crowds, especially during weekends and holidays
- **Wear comfortable shoes** as there may be significant walking involved
- **Respect the rules** - follow local signage and guidelines at all times
- **Bring cash** - while cards are increasingly accepted, some local shops and restaurants still prefer cash
- **Download offline maps** - cell service can be spotty in some areas
- **Learn a few Japanese phrases** - locals appreciate the effort, even if it's just "arigatou gozaimasu" (thank you)

## Nearby Attractions

While you're in {city}, consider visiting these other popular spots nearby:

- Explore the local shopping streets for unique souvenirs and regional specialties
- Try the local cuisine at nearby restaurants and street food stalls
- Visit other temples, shrines, or cultural sites within walking distance
- Take a scenic walk through the surrounding neighborhood

---

*Presented by Japan Travel Navi*
""",
    "ja": """## 概要

{title}は{city}に位置する、日本を代表する観光名所のひとつです。{description}

初めての日本旅行でも、何度も訪れているリピーターでも、この場所は日本の{category_lower}の真髄を感じられる忘れられない体験を提供してくれます。到着した瞬間から、何世代にもわたって訪問者を魅了してきた独特の雰囲気に包まれるでしょう。

周辺エリアは歴史と文化的な重要性に満ちています。地元の人々も観光客も何度も足を運び、訪れるたびに以前は気づかなかった新しい発見があります。

## アクセス方法

**電車:** 最寄りの主要駅まで新幹線が便利です。そこからは在来線やバスで簡単にアクセスできます。JRパスを持っていれば、移動費のほとんどがカバーされます。

**バス:** 高速バスは東京、大阪、京都などの主要都市から運行しており、予算を抑えたい方におすすめ。ピークシーズンは事前予約を。

**徒歩:** 現地に到着したら、多くの見どころは徒歩で楽しめます。特に周辺の散策を予定している場合は、歩きやすい靴がおすすめです。

## ベストシーズン

**春（3月〜5月）:** 桜が美しい背景を作り出します。最も人気のある時期のひとつで混雑しますが、息をのむような景色が広がります。

**夏（6月〜8月）:** 緑豊かな景色と夏祭りが活気ある雰囲気を演出。7月・8月は暑さと湿気に備えましょう。

**秋（10月〜11月）:** 赤や金色の紅葉が景色を一変させます。写真映えする季節として多くの人に愛されています。

**冬（12月〜2月）:** 観光客が少なく、静寂な雰囲気を楽しめます。雪景色が別世界のような美しさを見せることも。

## 訪問のコツ

- **早朝に到着**して混雑を避けましょう（特に週末や祝日）
- **歩きやすい靴**を履いていきましょう
- **ルールを守り**、現地の案内に従いましょう
- **現金を用意**しましょう（カード対応が増えていますが、まだ現金のみの店もあります）
- **オフラインマップ**をダウンロードしておくと安心です

## 周辺の見どころ

{city}を訪れたら、ぜひ近くの人気スポットも巡ってみてください：

- 地元の商店街でユニークなお土産や名産品を探す
- 近くのレストランや屋台で地元グルメを堪能する
- 徒歩圏内の他の寺社仏閣や文化施設を訪れる
- 周辺の街並みを散策して風情を楽しむ

---

*ジャパントラベルナビ がお届けしました*
""",
    "zh": """## 概述

{title}位于{city}，是日本最具代表性的旅游目的地之一。{description}

无论您是初次来日本的游客还是经验丰富的旅行者，这个景点都能为您带来真正难忘的体验，感受日本{category_lower}的精髓。从您到达的那一刻起，就会被这里独特的氛围所吸引，这种氛围已经吸引了一代又一代的游客。

周边地区充满了历史和文化意义。无论是当地人还是游客，都会一次又一次地回到这里，每次访问都能发现以前没有注意到的新细节和新视角。

## 如何到达

**乘火车：** 最便捷的方式是乘坐新干线到最近的主要车站，然后转乘当地列车和巴士。如果您持有JR通票，大部分行程将被涵盖。

**乘巴士：** 高速巴士提供经济实惠的选择，从东京、大阪和京都等主要城市都有班次。旺季请提前预订。

**步行：** 到达目的地后，许多精彩体验都可以步行享受。建议穿舒适的步行鞋，特别是如果您计划探索周边街区。

## 最佳游览时间

**春季（3月至5月）：** 樱花为景色增添了梦幻般的背景。这是最受欢迎的时期之一，预计人流量较大，但景色令人惊叹。

**夏季（6月至8月）：** 郁郁葱葱的绿色和夏季节日营造出充满活力的氛围。请做好应对高温和潮湿的准备。

**秋季（10月至11月）：** 令人惊叹的红色和金色秋叶改变了整个景观。许多人认为这是最上镜的季节。

**冬季（12月至2月）：** 游客较少，氛围宁静。一些地区还能欣赏到美丽的雪景。

## 游客贴士

- **尽早到达**以避开人群，尤其是周末和节假日
- **穿舒适的鞋子**，因为可能需要大量步行
- **遵守规则**，始终遵循当地标识和指南
- **携带现金**，虽然越来越多的地方接受银行卡，但一些小店仍然只收现金
- **下载离线地图**，某些地区可能信号不佳
- **学习几句日语**，当地人会很感激您的努力

## 周边景点

在{city}游览时，不妨也去看看附近的其他热门景点：

- 在当地商店街寻找独特的纪念品和特产
- 在附近的餐厅和小吃摊品尝当地美食
- 参观步行范围内的其他寺庙、神社或文化遗址
- 在周围街区散步，感受当地氛围

---

*日本旅游导航 为您呈现*
""",
    "ko": """## 개요

{title}은(는) {city}에 위치한 일본을 대표하는 관광 명소 중 하나입니다. {description}

일본 첫 방문이든 여러 번 찾은 리피터이든, 이곳은 일본 {category_lower}의 정수를 느낄 수 있는 잊지 못할 경험을 선사합니다. 도착하는 순간부터 오랜 세월 방문자들을 매료시켜 온 독특한 분위기에 감싸일 것입니다.

주변 에리어는 역사와 문화적 의미로 가득합니다. 현지인과 관광객 모두 여러 번 발걸음을 옮기며, 방문할 때마다 이전에는 눈치채지 못했던 새로운 발견이 있습니다.

## 가는 방법

**전철:** 가장 가까운 주요 역까지 신칸센이 편리합니다. 거기서 재래선이나 버스로 쉽게 접근할 수 있습니다. JR패스가 있으면 대부분의 이동 비용이 커버됩니다.

**버스:** 고속버스는 도쿄, 오사카, 교토 등 주요 도시에서 운행하며, 예산을 절약하고 싶은 분에게 추천합니다. 성수기에는 사전 예약을 권장합니다.

**도보:** 현지에 도착하면 많은 볼거리를 도보로 즐길 수 있습니다. 특히 주변 탐방을 계획하고 있다면 편안한 신발을 추천합니다.

## 추천 방문 시기

**봄 (3월~5월):** 벚꽃이 아름다운 배경을 만들어냅니다. 가장 인기 있는 시기 중 하나로 혼잡하지만, 숨막히는 경치가 펼쳐집니다.

**여름 (6월~8월):** 푸른 녹음과 여름 축제가 활기찬 분위기를 연출합니다. 7~8월의 더위와 습기에 대비하세요.

**가을 (10월~11월):** 빨갛고 금빛의 단풍이 풍경을 완전히 바꿔놓습니다. 많은 사람들이 가장 포토제닉한 계절로 꼽습니다.

**겨울 (12월~2월):** 관광객이 적고 고요한 분위기를 즐길 수 있습니다. 눈 덮인 풍경이 완전히 다른 경험을 선사하기도 합니다.

## 방문 팁

- **이른 아침에 도착**하여 혼잡을 피하세요 (특히 주말과 공휴일)
- **편안한 신발**을 신고 가세요
- **규칙을 지키고** 현지 안내에 따르세요
- **현금을 준비**하세요 (카드 사용이 늘고 있지만 현금만 받는 가게도 있습니다)
- **오프라인 지도**를 다운로드해 두면 안심입니다

## 주변 볼거리

{city}를 방문했다면 근처의 다른 인기 스팟도 둘러보세요:

- 현지 상점가에서 독특한 기념품과 특산품 찾기
- 근처 레스토랑과 포장마차에서 현지 음식 맛보기
- 도보 거리의 다른 사찰, 신사 또는 문화시설 방문
- 주변 거리를 산책하며 분위기 즐기기

---

*일본여행나비가 전해드렸습니다*
""",
    "es": """## Descripción General

{title} es uno de los destinos más notables de Japón, ubicado en {city}. {description}

Ya seas un visitante primerizo en Japón o un viajero experimentado, este lugar ofrece una experiencia verdaderamente inolvidable que captura la esencia de {category_lower} japonesa. Desde el momento en que llegas, te sorprenderá la atmósfera única que ha atraído a visitantes durante generaciones.

El área que rodea este lugar es rica en historia y significado cultural. Tanto los locales como los turistas se encuentran regresando una y otra vez, cada visita revelando nuevos detalles y perspectivas que no se habían notado antes.

## Cómo Llegar

**En tren:** La forma más conveniente de llegar a {city} es en Shinkansen (tren bala) hasta la estación principal más cercana. Desde allí, trenes locales y autobuses proporcionan conexiones fáciles. Si tienes un JR Pass, la mayor parte del viaje estará cubierto.

**En autobús:** Los autobuses de larga distancia ofrecen una alternativa económica, con servicios desde las principales ciudades como Tokio, Osaka y Kioto. Reserva con anticipación durante las temporadas altas.

**A pie:** Una vez que llegues a la zona, muchas de las mejores experiencias se pueden disfrutar caminando. Se recomiendan zapatos cómodos, especialmente si planeas explorar los barrios circundantes.

## Mejor Época para Visitar

**Primavera (marzo-mayo):** Los cerezos en flor añaden un telón de fondo mágico. Es una de las épocas más populares, así que espera más gente pero paisajes impresionantes.

**Verano (junio-agosto):** La vegetación exuberante y los festivales de verano crean una atmósfera vibrante. Prepárate para el calor y la humedad.

**Otoño (octubre-noviembre):** El impresionante follaje rojo y dorado transforma el paisaje. Muchos consideran esta la temporada más fotogénica.

**Invierno (diciembre-febrero):** Menos multitudes y una atmósfera serena. Algunas áreas ofrecen hermosas vistas cubiertas de nieve.

## Consejos para Visitantes

- **Llega temprano** para evitar multitudes, especialmente durante fines de semana y festivos
- **Usa zapatos cómodos** ya que puede haber bastante caminata
- **Respeta las reglas** - sigue las señales y pautas locales en todo momento
- **Lleva efectivo** - aunque las tarjetas son cada vez más aceptadas, algunas tiendas locales aún prefieren efectivo
- **Descarga mapas offline** - la señal puede ser débil en algunas áreas
- **Aprende algunas frases en japonés** - los locales aprecian el esfuerzo

## Atracciones Cercanas

Mientras estés en {city}, considera visitar estos otros lugares populares cercanos:

- Explora las calles comerciales locales en busca de souvenirs únicos y especialidades regionales
- Prueba la cocina local en restaurantes cercanos y puestos de comida callejera
- Visita otros templos, santuarios o sitios culturales a poca distancia
- Da un paseo escénico por el vecindario circundante

---

*Presentado por Japón Travel Navi*
""",
}


def generate_article(spot, lang, date_str):
    """Generate a single article for a given spot and language."""
    info = spot[lang]
    tags = spot.get(f"tags_{lang}", spot.get("tags_en", []))
    image = spot.get("image", "")

    # Build front matter
    front_matter = f"""---
title: "{info['title']}"
date: {date_str}T10:00:00+09:00
tags: {tags}
categories: ["{info['category']}"]
draft: false
description: "{info['description']}"
cover:
  image: "{image}"
  alt: "{info['title']}"
  hidden: false
slug: "{spot['slug']}"
---
"""

    # Build body from template
    title_short = info["title"].split(" - ")[0] if " - " in info["title"] else info["title"]
    category_lower = info["category"].lower()

    body = TEMPLATES[lang].format(
        title=info["title"],
        title_short=title_short,
        city=info["city"],
        description=info["description"],
        category_lower=category_lower,
    )

    return front_matter + "\n" + body


def generate_all():
    """Generate all articles for all spots in all languages."""
    base_date = datetime(2026, 3, 1)
    count = 0

    for i, spot in enumerate(SPOTS):
        date = base_date + timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")

        for lang in LANGUAGES:
            if lang not in spot:
                continue

            # Create directory
            lang_dir = os.path.join(CONTENT_DIR, lang, "posts")
            os.makedirs(lang_dir, exist_ok=True)

            # Generate and write article
            article = generate_article(spot, lang, date_str)
            filepath = os.path.join(lang_dir, f"{spot['slug']}.md")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(article)

            count += 1

    return count


def generate_search_pages():
    """Generate search pages for each language."""
    search_content = {
        "en": '---\ntitle: "Search"\nlayout: "search"\nplaceholder: "Search Japan Travel Navi..."\n---\n',
        "ja": '---\ntitle: "検索"\nlayout: "search"\nplaceholder: "ジャパントラベルナビを検索..."\n---\n',
        "zh": '---\ntitle: "搜索"\nlayout: "search"\nplaceholder: "搜索日本旅游导航..."\n---\n',
        "ko": '---\ntitle: "검색"\nlayout: "search"\nplaceholder: "일본여행나비 검색..."\n---\n',
        "es": '---\ntitle: "Buscar"\nlayout: "search"\nplaceholder: "Buscar en Japón Travel Navi..."\n---\n',
    }
    for lang, content in search_content.items():
        lang_dir = os.path.join(CONTENT_DIR, lang)
        os.makedirs(lang_dir, exist_ok=True)
        filepath = os.path.join(lang_dir, "search.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    print("Generating articles...")
    count = generate_all()
    print(f"Generated {count} articles.")

    print("Generating search pages...")
    generate_search_pages()
    print("Done!")
