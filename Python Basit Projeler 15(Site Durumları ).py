import requests
import csv

durum_dict = {}

def main():
    with open("Siteler.txt","r") as siteler:
        for satır in siteler:
            site = satır.strip()
            status = requests.get(site).status_code
            if (status == 200):
                durum_dict[site] = "site calışıyor"
            else:
                durum_dict[site] = "site çalışmıyor"

    with open("site_durumları.csv", "w", newline="") as yazılacak_dosya:
        csv_yazıcı = csv.writer(yazılacak_dosya)
        for key in durum_dict.keys():
            csv_yazıcı.writerow([key, durum_dict[key]])


if __name__ == "__main__":
    main()