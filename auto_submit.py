import requests
from bs4 import BeautifulSoup

class AutoSubCode:
    
    def __init__(self):
        self.QuestionCodesInWebSite = []  
    def CrawQuestionCode(self,page):
        burp0_url = f"https://code.ptit.edu.vn:443/student/question?page={page}"
        burp0_cookies = {"_ga_MRZBEE26NG": "GS1.1.1633912882.1.0.1633912997.0", "ozi": "2000.SSZzejyD2CeYdgEpqWm8sIZ9eUVCGWR1QfMpxT9GHDDyXxopsLOCc7o5lhpRMmdSVeg_yz9O3jfrYhF-D0.1", "_ga": "GA1.1.836918944.1633912882", "__zi": "3000.SSZzejyD2CeYdgEpqWm8sIZ9eUVCGWR1QvMpxTDGHDDzXV7zb1v7qpJ1zVsH4aITDCFoifWHGvi_m_w_D0.1", "_ga_YJ08BVKT4Q": "GS1.1.1689226527.8.1.1689226548.0.0.0", "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "eyJpdiI6Inh6STBqOWFvSkx4d0pjT1NZeEo3cnc9PSIsInZhbHVlIjoiSm5IaUtEWHU0eVNyN24xUDVkVHJyQjBsa1pRWjQ4WjRXQ1czdm50eTYzY0ErR3h6bVptcW9pZkRNTEdKSEwzVGZ4Rk1oWFc5SVRmOTVReEs3eElzRW9QS3l4Y21NNkZXNmNwdjB3YUlybmJWYmUwZXlpV2VxbmdFTks4ekRpOEpYTTFGcVd1MnNSb1BESlQyRm5nbHNJdS9XSVFMOEE4U3V2aWlLZWxXZk5CMWp6R0ZVSmFmOHJSem9TV21WSFhnaW9INEM4NjM5WTRQcHQvVSs3OGdDcklIdHpFQitoZFZhVjFyTkprYzJwTT0iLCJtYWMiOiIyMzI3OGJjMTI0Mjk0MmY5NjkxZmM4Y2EyN2QwNmFjOWY0YTlkMTA1MDBmNzcwZWI0NTc4MDAyZWY4M2E5NWUxIiwidGFnIjoiIn0%3D", "XSRF-TOKEN": "eyJpdiI6IlNVeGZKdndYYmlzd1lucUhTQWk4bGc9PSIsInZhbHVlIjoiM1g2OE9yUDZSREF5NmNhR0p5TjJ2U1VZTDhkK1Bhc2ZKRklvVGtidHRPSFk0UjNkeWlNa2hjMHR0dFlKdzdHbGZma2hyczA2dElDQUw5NFVLK3hYNFZMaGU1RnRhYitMS2xCU3NUSnl0WUh2UnNTSkdqWWlLNm0vS2FFREtUb3oiLCJtYWMiOiIzYzNkN2RkZjBiMjQ1ZWE5OGI5ODVmMzFhMWE4MzcxN2Q2ZmEwOGU0NThlMmY3NmFkODE4YmU0OWUxMWNhOTViIiwidGFnIjoiIn0%3D", "ptit_code_session": "eyJpdiI6IlFCL1QvSTVGc21DNlZSd1A1VUJ5VUE9PSIsInZhbHVlIjoiNmFvUXg1WjQyRWFEZVFTVGlaQVVlUm90aTZKZC9jelRLZHA0UXo3N1MwQnFKdFJOMFgrczNJbTVPMVBGL01YbEdDdGNNRkN2Uy9NcithN3lGN2pPZTE4c0hJcGZaaENVR1k1Vi9vdWsweWJjQnlMSStIK0Rqanh1M1d4blhNY00iLCJtYWMiOiI5MjY5NDY4MDc4YjU3MDY5ZDk4MmY0MzA5OGFkZjk0NzY3ZDM4YjJiNjllYzgxYWQzM2NmZDE4NzIzNDkwOTc5IiwidGFnIjoiIn0%3D"}
        burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://code.ptit.edu.vn/student/question", "Accept-Encoding": "gzip, deflate", "Accept-Language": "vi,en-US;q=0.9,en;q=0.8"}
        res = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        soup = BeautifulSoup(res.content, 'html.parser')
        tbody = soup.find('tbody')  # Lựa chọn theo class của div
        rows = tbody.find_all('tr')
        for row in rows:
            td = row.find_all('td')
            QuestionCode = td[2].find('a').text.strip() 
            QuestionName = td[3].find('a').text.strip()
            self.QuestionCodesInWebSite.append({"QuestionName" : QuestionName,"QuestionCode" : QuestionCode})
    def SubCode(self):
        burp0_url = "https://code.ptit.edu.vn:443/student/solution"
        burp0_cookies = {"_ga_MRZBEE26NG": "GS1.1.1633912882.1.0.1633912997.0", "ozi": "2000.SSZzejyD2CeYdgEpqWm8sIZ9eUVCGWR1QfMpxT9GHDDyXxopsLOCc7o5lhpRMmdSVeg_yz9O3jfrYhF-D0.1", "_ga": "GA1.1.836918944.1633912882", "__zi": "3000.SSZzejyD2CeYdgEpqWm8sIZ9eUVCGWR1QvMpxTDGHDDzXV7zb1v7qpJ1zVsH4aITDCFoifWHGvi_m_w_D0.1", "_ga_YJ08BVKT4Q": "GS1.1.1689226527.8.1.1689226548.0.0.0", "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "eyJpdiI6Inh6STBqOWFvSkx4d0pjT1NZeEo3cnc9PSIsInZhbHVlIjoiSm5IaUtEWHU0eVNyN24xUDVkVHJyQjBsa1pRWjQ4WjRXQ1czdm50eTYzY0ErR3h6bVptcW9pZkRNTEdKSEwzVGZ4Rk1oWFc5SVRmOTVReEs3eElzRW9QS3l4Y21NNkZXNmNwdjB3YUlybmJWYmUwZXlpV2VxbmdFTks4ekRpOEpYTTFGcVd1MnNSb1BESlQyRm5nbHNJdS9XSVFMOEE4U3V2aWlLZWxXZk5CMWp6R0ZVSmFmOHJSem9TV21WSFhnaW9INEM4NjM5WTRQcHQvVSs3OGdDcklIdHpFQitoZFZhVjFyTkprYzJwTT0iLCJtYWMiOiIyMzI3OGJjMTI0Mjk0MmY5NjkxZmM4Y2EyN2QwNmFjOWY0YTlkMTA1MDBmNzcwZWI0NTc4MDAyZWY4M2E5NWUxIiwidGFnIjoiIn0%3D", "XSRF-TOKEN": "eyJpdiI6IjdkV2V0eERnUFZYRjBmY2ExcDZncnc9PSIsInZhbHVlIjoibTlZV1dPVVZoN2VHcU1BRnhiQzd1ZTcwOVdmVWo0WGpnVEc4eGM3R1RoZWt6OG9JSUMveUxKM1RMdmp1STkxdkh1eE41SjFLREZmZmkzS2pzSzVtY0RCdk1OWVhzL0JiYkF2cXRpMjA5N2J2NldwdzU3MFBYSStGcll4NWg2aHMiLCJtYWMiOiIwMDRkNWRhMzcyNGQ0ODY1MTc1OTUxNzBjMWM1MzliMzk1NjY0Mjg0YjdjYTkxMDYwOTU4MGRkYzBkOGNiY2U0IiwidGFnIjoiIn0%3D", "ptit_code_session": "eyJpdiI6IjRQc2FnZGI2NVRna0JzczYwNFo2WUE9PSIsInZhbHVlIjoiY1B4dlljcjd0THV4U0lSdDhiRHhSSVpkQURaMDExRUNFb08rdExBR081MmtiY0RXdTFxcEVGMU9tMUlPQUZsWHFUVWNsendPcFFldCtHajRoU0NaenYrZlZ4Tzd3VXhzYmRHWGpabUhJR2RKR1JPNTNyMWVTaVpYSCtvQUJ1dGQiLCJtYWMiOiIyODJhNjg0OGJiYzY3Y2I3OGM0NzRjYjg4YzQ3Yzc4M2VmNjdjYWM1OWM4YWU1MDBiNWUzY2UxZWFiMTIwY2VlIiwidGFnIjoiIn0%3D"}
        burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "https://code.ptit.edu.vn", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLGvHAbobP2ASX60x", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://code.ptit.edu.vn/student/question/1181", "Accept-Encoding": "gzip, deflate", "Accept-Language": "vi,en-US;q=0.9,en;q=0.8"}

        for file in self.QuestionCodesInWebSite:
            QuestionName = file["QuestionName"]+".cpp"
            QuestionCode = file["QuestionCode"]
            FileContent = self.GetContentFile("./code/"+QuestionName)
            if FileContent is not None:
                FileContent = FileContent.replace("#pragma GCC optimize(\"O2\")",'')
                print(f"{QuestionName}\n{QuestionCode}\n{FileContent}\n\n")
                QuestionName = "what_ever_name.cpp"
                burp0_data = "------WebKitFormBoundaryLGvHAbobP2ASX60x\r\nContent-Disposition: form-data; name=\"_token\"\r\n\r\nTcFsMQyslt6m1Mxz4xHEJHA3suG4RnMIJ8dImDqG\r\n------WebKitFormBoundaryLGvHAbobP2ASX60x\r\nContent-Disposition: form-data; name=\"question\"\r\n\r\n"+QuestionCode+"\r\n------WebKitFormBoundaryLGvHAbobP2ASX60x\r\nContent-Disposition: form-data; name=\"compiler\"\r\n\r\n2\r\n------WebKitFormBoundaryLGvHAbobP2ASX60x\r\nContent-Disposition: form-data; name=\"code_file\"; filename="+QuestionName+"\r\nContent-Type: application/octet-stream\r\n\r\n"+FileContent+"\r\n------WebKitFormBoundaryLGvHAbobP2ASX60x--\r\n"
                try:
                    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
                except UnicodeEncodeError as e:
                    pass  
    def GetContentFile(self,path):
        try:
            with open(path) as f:
                try:
                    line = f.readlines()
                    return "".join(line)
                except UnicodeDecodeError:
                    pass
                f.close()
        except FileNotFoundError as e:
            pass
if __name__ == '__main__':
    app = AutoSubCode()
    for page in range(1,5):
        app.QuestionCodesInWebSite =[]
        app.CrawQuestionCode(page)
        app.SubCode()