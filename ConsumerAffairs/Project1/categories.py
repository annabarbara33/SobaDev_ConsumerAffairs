from collections import defaultdict
import random
from myapp import  *

def trail():
    categories =  defaultdict(dict)

    categories["Travel"] = {"Destination and Excursions":["African Safari Tour",
                                                    "CHINA TOURS COMPANIES",
                                                    "RIVER CRUISE LINES",
                                                    "AMUSEMENT PARKS",
                                                    "CRUISE LINES"],
                        "Booking a Trip":["HOTEL BRANDS",
                                        "TIMESHARES",
                                        "TRAVEL SITES",
                                        "TICKET WEBSITES",
                                        "TRAVEL AGENCIES"],
                        "Travel Essentials":["LUGGAGE",
                                            "Travel Insurance"],
                        "Transportation":["AIRLINES",
                                        "TRANSPORTATION AND RIDESHARE APPS",
                                        "Rental Cars"],
                        }

    categories["Shopping"] = {"Clothes and accessories":["CLOTHING SUBSCRIPTION BOXES",
                                                    "JEWELRY STORES",
                                                    "JEWELRY INSURANCE",
                                                    "RETAIL STORES AND SHOPPING"],
                            "Beauty products":["ACNE TREATMENT",
                                                "BEAUTY BOX",
                                                "MAKEUP BRANDS",
                                                "ORGANIC SKIN CARE",
                                                "PERSONAL CARE PRODUCTS",
                                                "WIGS"],
                            "Food":["BACON BRANDS",
                                    "CHAIN RESTAURANTS",
                                    "FOOD PRODUCTS",
                                    "GROCERY STORES",
                                    "MEAL DELIVERY SERVICE",
                                    "WATER DELIVERY SERVICES"],
                            "Sports equipment":["GOLF CLUB BRANDS",
                                                "SPORTING GOODS STORES"],
                            "Online stores":["APPLIANCE STORES",
                                            "DEAL WEBSITES",
                                            "FLOWER DELIVERY",
                                            "FURNITURE STORES",
                                            "ONLINE BATHROOM FIXTURES AND PLUMBING",
                                            "ONLINE PHOTO PRINTING",
                                            "ONLINE SHOPPING WEBSITES",
                                            "SHOES ONLINE"]
                            }

    categories["Insurance"] ={"Personal":["DENTAL INSURANCE",
                                    "DISABILITY INSURANCE",
                                    "HEALTH INSURANCE",
                                    "LIFE INSURANCE COMPANIES",
                                    "LONG TERM CARE INSURANCE",
                                    "MEDICARE SUPPLEMENTAL INSURANCE",
                                    "TRAVEL INSURANCE",
                                    "VISION INSURANCE"],
                        "Home":["FLOOD INSURANCE",
                                "HOMEOWNERS INSURANCE",
                                "JEWELRY INSURANCE",
                                "PET INSURANCE",
                                "RENTERS INSURANCE"
                                ],
                        "Vehicle":["BOAT INSURANCE",
                                "CAR INSURANCE",
                                "MOTORCYCLE INSURANCE",
                                "RV INSURANCE"
                                ]
                        }

    categories["Finance"] = {"Banking and Credit":["BANKS AND CREDIT UNIONS",
                                            "CREDIT CARDS",
                                            "CREDIT REPORT SITES",
                                            "MONEY TRANSFER",
                                            "ONLINE BANKS",
                                            "PREPAID DEBIT CARDS",
                                            "SECURED CREDIT CARDS"
                                            ],
                        "Debt":["BILL NEGOTIATION SERVICES",
                                "CREDIT COUNSELING",
                                "CREDIT REPAIR COMPANIES",
                                "DEBT CONSOLIDATION LOAN COMPANIES",
                                "DEBT SETTLEMENT",
                                "PRE-SETTLEMENT FUNDING",
                                "STRUCTURED SETTLEMENT",
                                "STUDENT LOAN REFINANCING",
                                "TAX RELIEF"
                                ],
                        "Investing":["ANNUITIES",
                                    "AUTOMATED INVESTMENT SERVICES",
                                    "BITCOIN IRA",
                                    "CROWDFUNDING SITES",
                                    "GOLD DEALERS",
                                    "GOLD IRA COMPANIES",
                                    "INVESTMENT COMPANIES",
                                    "LIFE INSURANCE COMPANIES",
                                    "MUTUAL FUND COMPANIES",
                                    "ONLINE BROKERS",
                                    "ONLINE FINANCIAL ADVISORS"
                                    ],
                        "Loans":["AUTO LOANS",
                                "BUSINESS LOANS",
                                "LOAN COMPANIES",
                                "LOAN MODIFICATION COMPANIES",
                                "PAYDAY AND TITLE LOANS",
                                "PERSONAL LOANS",
                                "SOLAR FINANCING",
                                "STUDENT LOANS"
                                ],
                        "Mortgages":["FHA LOAN LENDERS",
                                    "HOME EQUITY LOANS",
                                    "JUMBO LOAN LENDERS",
                                    "MORTGAGE LENDERS",
                                    "REVERSE MORTGAGE LENDERS",
                                    "USDA LENDERS",
                                    "VA LOAN LENDERS"
                                    ],
                        "Online services":["BACKGROUND CHECK COMPANIES",
                                            "IDENTITY THEFT PROTECTION",
                                            "TAX SOFTWARE AND SERVICES"
                                            ]
                                    }

    given = ["African Safari Tour","ANNUITIES"]
    print(ls)

    if ls:
        given.extend(ls)

    found = []
    for key,values in categories.items():
        for things,cats in values.items():
                for i in given:
                        if i in cats:
                                found.extend(cats)
    print(type(given))
    for key,values in categories.items():
        for i in given:
                if i in values.keys():
                        found.extend(values[i])
    for i in given:
        if i in categories.keys():
                found.extend(list(categories[i].keys()))

    #[found.remove(i) for i in given if i in found]
    random.shuffle(found)
    x = found
    images  = defaultdict()
    # 0 of the list is the link to the page and 1 is image link
    images = {"African Safari Tour":["https://www.consumeraffairs.com/travel/african-safari-tours",""],
        "CHINA TOURS COMPANIES":["https://www.consumeraffairs.com/travel/china-tours",""],
        "RIVER CRUISE LINES":["https://www.consumeraffairs.com/travel/river-cruises",""],
        "AMUSEMENT PARKS":["https://www.consumeraffairs.com/travel/amusement-parks",""],
        "CRUISE LINES":["https://www.consumeraffairs.com/travel/cruises.html",""],
        "HOTEL BRANDS":["https://www.consumeraffairs.com/travel/hotels.html",""],
        "TIMESHARES":["https://www.consumeraffairs.com/travel/timeshares.html",""],
        "TRAVEL SITES":["https://www.consumeraffairs.com/travel/travel-sites",""],
        "TICKET WEBSITES":["https://www.consumeraffairs.com/entertainment/ticket-websites",""],
        "TRAVEL AGENCIES":["https://www.consumeraffairs.com/travel/agencies.html",""],
        "LUGGAGE":["https://www.consumeraffairs.com/shopping/luggage",""],
        "Travel Insurance":["https://www.consumeraffairs.com/insurance/travel-insurance",""],
        "AIRLINES":["https://www.consumeraffairs.com/travel/airlines.html",""],
        "TRANSPORTATION AND RIDESHARE APPS":["https://www.consumeraffairs.com/travel/bus.html",""],
        "Rental Cars":["https://www.consumeraffairs.com/travel/car_rental.html",""],
        "CLOTHING SUBSCRIPTION BOXES":["https://www.consumeraffairs.com/online/clothing-subscription-box",""],
        "JEWELRY STORES":["https://www.consumeraffairs.com/jewelry",""],
        "JEWELRY INSURANCE":["https://www.consumeraffairs.com/insurance/jewelry-insurance",""],
        "RETAIL STORES AND SHOPPING":["https://www.consumeraffairs.com/retail/national_chains.htm",""],
        "ACNE TREATMENT":["https://www.consumeraffairs.com/health/acne-treatment",""],
        "BEAUTY BOX":["https://www.consumeraffairs.com/online/beauty-box",""],
        "MAKEUP BRANDS":["https://www.consumeraffairs.com/cosmetics/cosmetics.htm",""],
        "ORGANIC SKIN CARE":["https://www.consumeraffairs.com/health/organic-skin-care",""],
        "PERSONAL CARE PRODUCTS":["https://www.consumeraffairs.com/shopping/personal-care-products",""],
        "WIGS":["https://www.consumeraffairs.com/wigs",""],
        "BACON BRANDS":["https://www.consumeraffairs.com/food/bacon",""],
        "CHAIN RESTAURANTS":["https://www.consumeraffairs.com/food/chain-restaurants",""],
        "FOOD PRODUCTS":["https://www.consumeraffairs.com/food",""],
        "GROCERY STORES":["https://www.consumeraffairs.com/supermarkets",""],
        "MEAL DELIVERY SERVICE":["https://www.consumeraffairs.com/food/meal-delivery-service",""],
        "WATER DELIVERY SERVICES":["https://www.consumeraffairs.com/water-delivery-services",""],
        "GOLF CLUB BRANDS":["https://www.consumeraffairs.com/retail/golf-club-brands",""],
        "SPORTING GOODS STORES":["https://www.consumeraffairs.com/sporting-goods",""],
        "DENTAL INSURANCE":["https://www.consumeraffairs.com/insurance/dental-insurance/",""],
        "DISABILITY INSURANCE":["https://www.consumeraffairs.com/insurance/dis.html",""],
        "HEALTH INSURANCE":["https://www.consumeraffairs.com/insurance/health.html","static/img/health.jpg"],
        "LIFE INSURANCE COMPANIES":["https://www.consumeraffairs.com/insurance/life.html","static/img/LIFE_INSURANCE_COMPANIES.png"],
        "LONG TERM CARE INSURANCE":["https://www.consumeraffairs.com/insurance/ltc.html","static/img/long_term_care_insurance.jpg"],
        "MEDICARE SUPPLEMENTAL INSURANCE":["https://www.consumeraffairs.com/insurance/medicare-supplemental-insurance/","static/img/medicare_suplemental_insurance.jpg"],
        "TRAVEL INSURANCE":["https://www.consumeraffairs.com/insurance/travel-insurance/","static/img/Travel Insurance.jpg"],
        "VISION INSURANCE":["https://www.consumeraffairs.com/insurance/vision-insurance/","static/img/vision_insurance.jpg"],
        "FLOOD INSURANCE":["https://www.consumeraffairs.com/insurance/flood-insurance/","static/img/flood_insurance.jpg"],
        "HOMEOWNERS INSURANCE":["https://www.consumeraffairs.com/insurance/home.html","static/img/homeowners_insurance.jpg"],
        "JEWELRY INSURANCE":["https://www.consumeraffairs.com/insurance/jewelry-insurance","static/img/jewelry_insurance.jpg"],
        "PET INSURANCE":["https://www.consumeraffairs.com/pets/pet-insurance","static/img/pet_insurance.jpg"],
        "RENTERS INSURANCE":["https://www.consumeraffairs.com/insurance/renters-insurance","static/img/renters_insurance.jpg"],
        "BOAT INSURANCE":["https://www.consumeraffairs.com/insurance/boat-insurance","static/img/boat_insurance.jpg"],
        "CAR INSURANCE":["https://www.consumeraffairs.com/insurance/car.html","static/img/car_insurance.jpg"],
        "MOTORCYCLE INSURANCE":["https://www.consumeraffairs.com/insurance/motorcycle-insurance","static/img/motorcycle_insurance.jpg"],
        "RV INSURANCE":["https://www.consumeraffairs.com/insurance/rv-insurance","static/img/rv_insurance.jpg"],
        "BANKS AND CREDIT UNIONS":["https://www.consumeraffairs.com/finance/banks.html",""],
        "CREDIT CARDS":["https://www.consumeraffairs.com/credit_cards/credit_cards.html","static/img/credit cards.jpg"],
        "CREDIT REPORT SITES":["https://www.consumeraffairs.com/online/credit-report/","static/img/credit_report_site.png"],
        "MONEY TRANSFER":["https://www.consumeraffairs.com/finance/money-transfer/",""],
        "ONLINE BANKS":["https://www.consumeraffairs.com/finance/online-banks/","static/img/online_banks.jpg"],
        "PREPAID DEBIT CARDS":["https://www.consumeraffairs.com/finance/prepaid-debit-cards/","static/img/PREPAID_DEBIT_CARDS.jpeg"],
        "SECURED CREDIT CARDS":["https://www.consumeraffairs.com/finance/credit-cards/secured/","static/img/SECURED_CREDIT_CARDS.jpeg"],
        "BILL NEGOTIATION SERVICES":["https://www.consumeraffairs.com/finance/bill-negotiation/","static/img/BILL_NEGOTIATION_SERVICES.jpeg"],
        "CREDIT COUNSELING":["https://www.consumeraffairs.com/finance/credit-counseling/","static/img/CREDIT_REPAIR_COMPANIES.jpeg"],
        "CREDIT REPAIR COMPANIES":["https://www.consumeraffairs.com/finance/credit-repair/","static/img/CREDIT_REPAIR_COMPANIES.jpeg"],
        "DEBT CONSOLIDATION LOAN COMPANIES":["https://www.consumeraffairs.com/debt_counsel/","static/img/DEBT_SETTLEMENT.png"],
        "DEBT SETTLEMENT":["https://www.consumeraffairs.com/finance/debt-settlement/","static/img/DEBT_SETTLEMENT.png"],
        "PRE-SETTLEMENT FUNDING":["https://www.consumeraffairs.com/finance/pre-settlement-funding/","static/img/PRE-SETTLEMENT_FUNDING.jpeg"],
        "STRUCTURED SETTLEMENT":["https://www.consumeraffairs.com/finance/structured-settlement/","static/img/STRUCTURED_SETTLEMENT.jpeg"],
        "STUDENT LOAN REFINANCING":["https://www.consumeraffairs.com/finance/student-loan-consolidation/","static/img/STUDENT_LOANS.png"],
        "TAX RELIEF":["https://www.consumeraffairs.com/finance/tax-relief/","static/img/TAX_RELIEF.jpeg"],
        "ANNUITIES":["https://www.consumeraffairs.com/finance/annuities.html","static/img/ANNUITIES.jpeg"],
        "AUTOMATED INVESTMENT SERVICES":["https://www.consumeraffairs.com/automated-investment-services/","static/img/AUTOMATED_INVESTMENT_SERVICES.jpeg"],
        "BITCOIN IRA":["https://www.consumeraffairs.com/finance/bitcoin-ira/","static/img/BITCOIN_IRA.jpeg"],
        "CROWDFUNDING SITES":["https://www.consumeraffairs.com/business/crowdfunding-sites/","static/img/CROWDFUNDING_SITES.png"],
        "GOLD DEALERS":["https://www.consumeraffairs.com/finance/gold-dealers/","static/img/GOLD_DEALERS.jpeg"],
        "GOLD IRA COMPANIES":["https://www.consumeraffairs.com/finance/gold-ira/","static/img/GOLD_IRA_COMPANIES.jpeg"],
        "INVESTMENT COMPANIES":["https://www.consumeraffairs.com/finance/invest.html","static/img/INVESTMENT_COMPANIES.jpeg"],
        "LIFE INSURANCE COMPANIES":["https://www.consumeraffairs.com/insurance/life.html","static/img/LIFE_INSURANCE_COMPANIES.png"],
        "MUTUAL FUND COMPANIES":["https://www.consumeraffairs.com/finance/mutual-fund-companies/","static/img/MUTUAL_FUND_COMPANIES.png"],
        "ONLINE BROKERS":["https://www.consumeraffairs.com/finance/online-brokers/","static/img/ONLINE_BROKERS.jpeg"],
        "ONLINE FINANCIAL ADVISORS":["https://www.consumeraffairs.com/finance/financial-planning/","static/img/ONLINE_FINANCIAL_ADVISORS.jpeg"],
        "AUTO LOANS":["https://www.consumeraffairs.com/finance/auto-loans/","static/img/AUTO_LOAN.png"],
        "BUSINESS LOANS":["https://www.consumeraffairs.com/business-loans-and-financing/","static/img/BUSINESS_LOANS.jpeg"],
        "LOAN COMPANIES":["https://www.consumeraffairs.com/finance/loan_companies.html","static/img/LOAN_COMPANIES.jpeg"],
        "LOAN MODIFICATION COMPANIES":["https://www.consumeraffairs.com/finance/loan-modification/","static/img/LOAN_MODIFICATION_COMPANIES.jpeg"],
        "PAYDAY AND TITLE LOANS":["https://www.consumeraffairs.com/finance/payday.html","static/img/PAYDAY_AND_TITLE_LOANS.jpeg"],
        "PERSONAL LOANS":["https://www.consumeraffairs.com/finance/personal-loans/","static/img/PERSONAL_LOANS.png"],
        "SOLAR FINANCING":["https://www.consumeraffairs.com/finance/solar-financing/","static/img/SOLAR_FINANCING.jpeg"],
        "STUDENT LOANS":["https://www.consumeraffairs.com/finance/student_loans.html","static/img/STUDENT_LOANS.png"],
        "FHA LOAN LENDERS":["https://www.consumeraffairs.com/finance/fha-loans/","static/img/HOME_EQUITY_LOANS.jpeg"],
        "HOME EQUITY LOANS":["https://www.consumeraffairs.com/finance/home-equity-loans/","static/img/HOME_EQUITY_LOANS.jpeg"],
        "JUMBO LOAN LENDERS":["https://www.consumeraffairs.com/finance/jumbo-loans/","static/img/JUMBO_LOAN_LENDERS.jpeg"],
        "MORTGAGE LENDERS":["https://www.consumeraffairs.com/finance/finance__companies.html","static/img/MORTGAGE_LENDERS.jpeg"],
        "REVERSE MORTGAGE LENDERS":["https://www.consumeraffairs.com/reverse-mortgages/","static/img/REVERSE_MORTGAGE_LENDERS.jpeg"],
        "USDA LENDERS":["https://www.consumeraffairs.com/finance/usda-loans/","static/img/USDA_LENDERS.png"],
        "VA LOAN LENDERS":["https://www.consumeraffairs.com/finance/va-loans/","static/img/VA_LOAN_LENDERS.jpeg"],
        "BACKGROUND CHECK COMPANIES":["https://www.consumeraffairs.com/online/background-check/","static/img/BACKGROUND_CHECK_COMPANIES.jpeg"],
        "IDENTITY THEFT PROTECTION":["https://www.consumeraffairs.com/privacy/","static/img/IDENTITY_THEFT_PROTECTION.jpeg"],
        "TAX SOFTWARE AND SERVICES":["https://www.consumeraffairs.com/finance/tax_prep.html","static/img/TAX_SOFTWARE_AND_SERVICES.jpeg"]
        }

    output = []
    for i in x:
        if i in images:
            output.append(images[i])
    y = list(zip(x,output))
    #print(y)
    return (y)
