import time
import openpyxl
from config import URL, USERNAME, PASSWORD, PROJECT
from playwright.sync_api import sync_playwright

class SonarQubeScraper:
    """
    A class to scrape data from SonarQube's web interface.

    Attributes:
        url (str): The URL of the SonarQube instance.
        username (str): Login username.
        password (str): Login password.
        data (list): List to store extracted data.
    """

    def __init__(self, url, username, password):
        """
        Initialize scraper with SonarQube instance details and credentials.
        """
        self.url = url
        self.username = username
        self.password = password
        self.project_name = PROJECT
        self.data = []

    def login(self, page):
        """
        Login to the SonarQube instance using provided credentials.
        """
        page.fill("#login", self.username)
        page.fill("#password", self.password)
        page.click("button >> text=Log in") 

    def select_project(self, page):
        """
        Select a project in the SonarQube dashboard. Placeholder function.
        """
        page.click(f"a >> text={self.project_name}")

    def extract_data(self, page):
        """
        Extract data from list items in the web page.
        """
        file_path = None
        lis = page.query_selector_all(".issues-workspace-list-item")
        for li in lis:
            new_file_path = li.query_selector(".issues-workspace-list-component")
            if new_file_path and file_path != new_file_path.text_content():
                file_path = new_file_path.text_content()

            data_item = {
                "filepath": file_path,
                "issue_desc": li.query_selector(".issue-message .spacer-right").text_content(),
                "line_number": li.query_selector(
                    ".issue-meta >> .issue-meta-label[title='Line Number']"
                ).text_content(),
                "type": li.query_selector(
                    ".issue-actions >> .issue-meta-list >> .issue-meta >> nth=0 >> button"
                ).text_content(),
                "criticality": li.query_selector(
                    ".issue-actions >> .issue-meta-list >> .issue-meta >> nth=1 >> button"
                ).text_content(),
                "efforts": li.query_selector(
                    ".issue-actions >> .issue-meta-list >> .issue-meta >> nth=4 >> span"
                ).text_content(),
            }
            self.data.append(data_item)

    def click_show_more(self, page):
        """
        Scroll to the bottom of the page and click on the 'show more' button recursively until it doesn't show up.
        #"""
        try:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            while page.is_visible("button >> text=Show More"):
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(1000)
                page.click("button >> text=Show More")
        except:
            pass

    def save_to_excel(self, filename="output.xlsx"):
        """
        Save extracted data to an Excel file.
        """
        wb = openpyxl.Workbook()
        ws = wb.active

        headers = [
            "filepath",
            "issue_desc",
            "line_number",
            "type",
            "criticality",
            "efforts",
        ]
        ws.append(headers)

        for item in self.data:
            ws.append([item[header] for header in headers])

        wb.save(filename)

    def run(self):
        """
        Execute the scraping workflow.
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            self.login(page)
            self.select_project(page)
            page.click(".navbar-tabs >> li >> a >> text=Issues")
            time.sleep(2)
            self.click_show_more(page)
            self.extract_data(page)
            self.save_to_excel(f"{self.project_name}.xlsx")
            browser.close()


if __name__ == "__main__":
    scraper = SonarQubeScraper(URL, USERNAME, PASSWORD)
    scraper.run()