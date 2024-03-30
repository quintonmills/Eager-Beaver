import os 
import requests

def scrape_linkedin_profile(linkedin_profile_url)
    """scrape information from linkedin profiles,
    manually scrape the information from the linkedin profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    response = requests.get(
        api_endpoint, params = {"url": linkedin_profile_url}, headers = header_dic
    )
    data = response.json()

    return data
