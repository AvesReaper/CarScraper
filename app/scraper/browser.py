from playwright.sync_api import sync_playwright
import time
import json
from app.kafka.producer import publish

def get_text(locator):
    try:
        if locator.count() == 0:
            return None
        return locator.inner_text().strip()
    except Exception:
        return None


def get_specs(page):
    specs = {}

    rows = page.locator("li")

    for i in range(rows.count()):
        row = rows.nth(i)

        if row.locator(".label").count() == 0:
            continue

        try:
            label = row.locator(".label").inner_text().strip()
            value = row.locator(".value-text").inner_text().strip()

            specs[label] = value
        except:
            pass

    return specs

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context()


    cookie_value = json.dumps({
        "choices": {},
        "formData": {
            "cityName": "Chennai",
            "cityId": "280",
            "latitude": "",
            "longitude": "",
            "Address": "",
            "Pincode": "",
            "pincodeCity": ""
        }
    })

    context.add_cookies([
        {
            "name": "__leadForm",
            "value": cookie_value,
            "domain": "www.cardekho.com",
            "path": "/",
            "httpOnly": False,
            "secure": True,
            "sameSite": "Lax"
        }
    ])

    page = context.new_page()
    page.goto("https://www.cardekho.com/used-bmw+cars+in+chennai")


    print(page.title())

    previous = 0

    while True:
        page.mouse.wheel(0, 5000)
        page.wait_for_timeout(1500)

        current = page.locator("#SrpCarsSection h3 a").count()

        if current == previous:
            break

        previous = current


    car_links = page.locator("#SrpCarsSection h3 a")

    count = car_links.count()

    print(f"====={count} cars found=====")

    links = car_links.evaluate_all("(els) => els.map(e => e.href)")
    print(len(links))
    temp = []
    
    for url in links:
        car_page = context.new_page()
        car_page.goto(url, wait_until="domcontentloaded")
        specs = get_specs(car_page)

        # print(specs)

        pay = {
            "brand": "BMW",
            "model": get_text(car_page.locator(".vehicleName h1")),
            "year": specs.get("Year of Manufacture") or specs.get("Registration Year"),
            "price": get_text(car_page.locator(".vehiclePrice span")),
            "fuel_type": specs.get("Fuel") or specs.get("Fuel Type"),
            "transmission": specs.get("Transmission") or specs.get("Transmission Type"),
            "kilometers": specs.get("Kms Driven"),
            "insurance": specs.get("Insurance") or specs.get("Insurance Type"),
            "ownership": specs.get("Ownership") or specs.get("Owner"),
            "displacement": specs.get("Engine") or specs.get("Engine Displacement"),
            "power": specs.get("Power"),
            "drive_type": specs.get("Drive Type") or specs.get("Drivetrain"),
            "url": url,
        }

        # print(pay)
        publish(pay)
        temp.append(json.dumps(pay))
        car_page.close()

    print(temp)

    page.close()

# ==========================OLD attempts
# def get_detail(page, label):
#     return page.locator(
#         f"li:has(.label:text-is('{label}')) .value-text"
#     ).inner_text()


# def get_detail(page, label):
#     try:
#         item = page.locator(
#             "li",
#             has=page.locator(".label", has_text=label)
#         )

#         if item.count() == 0:
#             return None

#         return item.locator(".value-text").inner_text().strip()
#     except Exception:
#         return None


# {"brand": "BMW", 
# "model": "2023 Mercedes-Benz GLE\\n300d BSVI", 
# "year": "2023", 
# "price": "\\u20b975 Lakh", 
# "fuel_type": null, 
# "transmission": null, 
# "kilometers": "26,000 Kms", 
# "insurance": "Comprehensive", 
# "ownership": "Second Owner", 
# "displacement": null, "power": "241.38 bhp", 
# "drive_type": "AWD", 
# "url": "https://www.cardekho.com/used-car-details/used-Mercedes-benz-gle-300d-bsvi-cars-Chennai_7312150d-5aee-446c-bd7a-d3bebb1fc5d4.htm?adId=27841&adType=41"}

        # pay = {
        #     "brand": "BMW",
        #     "model": get_text(car_page.locator(".vehicleName h1")),
        #     "year": get_detail(car_page, "Year of Manufacture"),
        #     "price": get_text(car_page.locator(".vehiclePrice span")),
        #     "fuel_type": get_detail(car_page, "Fuel"),
        #     "transmission": get_detail(car_page, "Transmission"),
        #     "kilometers": get_detail(car_page, "Kms Driven"),
        #     "insurance": get_detail(car_page, "Insurance"),
        #     "ownership": get_detail(car_page, "Ownership"),
        #     "displacement": get_detail(car_page, "Engine"),
        #     "power": get_detail(car_page, "Power"),
        #     "drive_type": get_detail(car_page, "Drive Type"),
        #     "url": url
        # }