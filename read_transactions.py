with open("cash_app_report.csv") as f:
    bulk_read = f.readlines()
    transactions = [i.split(",") for i in bulk_read]
    for transaction in transactions:
        print(transaction)

        
